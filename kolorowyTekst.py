import sys as _sys
from colorama import init as _init, Fore as _Fore
from builtins import print as _print
import moje as _moje

CZERWONY = 'czerwony'
NIEBIESKI = 'niebieski'
ZIELONY = 'zielony'
POMARANCZOWY = 'pomaranczowy'
FIOLETOWY = 'fioletowy'
CZARNY = 'czarny'
STANDARD = 'standard'

_IDLE = 'IDLE'
_TERM = 'TERM'

try:
    _kolor = _sys.stdout.shell
    _zmiany = {CZERWONY:'COMMENT', NIEBIESKI:'DEFINITION',
               ZIELONY:'STRING', POMARANCZOWY:'KEYWORD',
               FIOLETOWY:'BUILTIN', CZARNY:'sync'}
    _tryb = _IDLE
except AttributeError:
    _init(autoreset=True, convert=True)
    _zmiany = {CZERWONY:_Fore.RED, NIEBIESKI:_Fore.BLUE,
               ZIELONY:_Fore.GREEN, POMARANCZOWY:None,
               FIOLETOWY:_Fore.MAGENTA, CZARNY:_Fore.BLACK}
    _tryb = _TERM

class _ReprArg:
    def __init__(self, r):
        self._r = r
    def __repr__(self):
        return self._r
    def __eq__(self, inne):
        try:
            return self._r == inne._r
        except AttributeError:
            return False

def print(*args, sep=' ', end='\n', file=_ReprArg('sys.stdout'), flush=False, kolor=STANDARD):
    if file == _ReprArg('sys.stdout'):
        file = _sys.stdout
    if kolor == STANDARD:
        _print(*args, sep=sep, end=end, file=file, flush=flush)
        return
    if file == _sys.stdout:
        if _tryb == _IDLE:
            _kolor.write(_moje.printFormat(*args, sep=sep, end=end), _zmiany[kolor])
        elif tryb == _TERM:
            if _zmiany[kolor] == None:
                print(*args, sep=sep, end=end, flush=flush)
            else:
                _print(_zmiany[kolor] + args[0], *args[1:], sep=sep, end=end, flush=flush)
    else:
        _print(*args, sep=sep, end=end, file=file, flush=flush)
