from functools import partial
import codecs

class _DefaultDictWithKey(dict):
    def __init__(self, f, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__f = f
    def __missing__(self, k):
        self.__f(k)

#################################################################################################        
########################################### JKOD ################################################
#################################################################################################
_JKOD_TO_STR = dict(zip(range(0xff), bytes(range(128)).decode('ascii') +
                        'ąćęłńóśźżüáéíßäö' +
                        'ĄĆĘŁŃÓŚŹŻÜÁÉÍ◈ÄÖ' +
                        '•◘π║☺╝╗╣☻╚╔╠═╩╦╬' +
                        '○◙♥♦♣♠αβγδ▲▼◄►€√' +
                        '' + # pierwszych 16 znaków do prywatnego użytku
                        '§▘▝▀▖▌▞▛▗▚▐▜▄▙▟█' +
                        '„”⌂░▒▓≥≤÷²³™©®∞➤' +
                        '°↑↓↕←↖↙💎→↗↘🔴↔🟢'))
_JKOD_TO_STR[0xff] = None
_STR_TO_JKOD = _DefaultDictWithKey(lambda x: b'\xff' + x.encode('utf-32'),
                                   ((s, j)  for j, s in _JKOD_TO_STR.items()))
del _STR_TO_JKOD[None]

def jkodSearch(encoding):
    if encoding == 'jkod':
        return codecs.CodecInfo(name='jkod', encode=jkodEncode, decode=jkodDecode)

def jkodEncode(s):
    return (bytes(_STR_TO_JKOD[c] for c in s), len(s))

def jkodDecode(b):
    def _decode():
        it = iter(b)
        try:
            while True:
                i = next(it)
                if i == 0xff:
                    try:
                        yield bytes(next(it) for _ in range(4)).decode('utf-32')
                    except StopIteration as e:
                        raise UnicodeDecodeError('Za mało danych aby zdekodować znak Unicode') from e
                else:
                    try:
                        yield _JKOD_TO_STR[i]
                    except KeyError as e:
                        raise UnicodeDecodeError('Nieistniejący punkt kodowy') from e
        except StopIteration:
            pass
    return (''.join(_decode()), len(b))

codecs.register(jkodSearch)
####################################################################################################
####################################################################################################
####################################################################################################
