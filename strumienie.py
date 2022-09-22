import os

_ODCZYTANO = 'o'
_ZAPISANOBIN = 'z'
_ZAPISANOTEKST = 'Z'
_NIEZACZETO = '-'

class StrumienWyjsciowy:
    def __init__(self, wiadomosci=None, stan=None):
        if wiadomosci == None:
            if stan == None:
                wiadomosci = _tmpnam()
            else:
                wiadomosci = _tmpnam([stan])
        if stan == None:
            stan =_tmpnam([wiadomosci])
        self._wiadomosci = wiadomosci
        self._stan = stan
        f = open(self._stan, 'w')
        f.write(_NIEZACZETO)
        f.close()
        f = open(self._wiadomosci, 'wb')
        f.write(b'')
        f.close()
    def wyslij(self, wiadomosc):
        while _stan(self._stan) in [_ZAPISANOBIN, _ZAPISANOTEKST]:
            pass
        f = open(self._wiadomosci, 'wb')
        if type(wiadomosc) == str:
            wiadomosc = wiadomosc.encode()
            stan = _ZAPISANOTEKST
        else:
            stan = _ZAPISANOBIN
        f.write(wiadomosc)
        f.close()
        f = open(self._stan, 'w')
        f.write(stan)
        f.close()
    def wyslijDodaj(self, wiadomosc):
        f = open(self._wiadomosci, 'ab')
        if type(wiadomosc) == str:
            wiadomosc = wiadomosc.encode()
            stan = _ZAPISANOTEKST
        else:
            stan = _ZAPISANOBIN
        f.write(wiadomosc)
        f.close()
        f = open(self._stan, 'w')
        f.write(stan)
        f.close()
    def __repr__(self):
        return f'StrumienWyjsciowy({repr(self._wiadomosci)}, {repr(self._stan)})'
    def zamknij(self):
        os.remove(self._wiadomosci)
        os.remove(self._stan)
    def wejsciowy(self):
        return StrumienWejsciowy(self._wiadomosci, self._stan)
    def eksport(self):
        return [self._wiadomosci, self._stan]

class StrumienWejsciowy:
    def __init__(self, wiadomosci, stan):
        self._wiadomosci = wiadomosci
        self._stan = stan
    def odczytaj(self):
        while _stan(self._stan) == _ODCZYTANO:
            pass
        f = open(self._wiadomosci, 'rb')
        dane = f.read()
        f.close()
        if _stan(self._stan) == _ZAPISANOTEKST:
            dane = dane.decode()
        f = open(self._stan, 'w')
        f.write(_ODCZYTANO)
        f.close()
        return dane
    def dostepny(self):
        return _stan(self._stan) in [_ZAPISANOBIN, _ZAPISANOTEKST]
    def wyjsciowy(self):
        return StrumienWyjsciowy(self._wiadomosci, self._stan)
    def eksport(self):
        return [self._wiadomosci, self._stan]

def _tmpnam(istnieja=[]):
    try:
        os.mkdir('D:/tmp')
    except FileExistsError:
        pass
    num = 0
    while os.path.exists(f'D:/tmp/{num}.tmp') or f'D:/tmp/{num}.tmp' in istnieja:
        num += 1
    return f'D:/tmp/{num}.tmp'

def _stan(plik):
    try:
        f = open(plik, 'r')
        stan = f.read()
        f.close()
        return stan
    except FileNotFoundError:
        return None
