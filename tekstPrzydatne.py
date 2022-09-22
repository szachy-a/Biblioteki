from itertools import zip_longest
import sys
import colorama
colorama.init(convert=True)
import msvcrt
import textwrap

_SETPOS = '\x1b[%d;%dH'
_GETPOS = '\x1b[6n'

class EmptyListDict(dict):
    def __missing__(self, k):
        return []
    def __repr__(self):
        return self.__class__.__name__ + '(' + super().__repr__() + ')'

def _getInt(f):
    s = ''
    while (c := f.read(1)).isdigit():
        s += c
    f.seek(-1, 1) # cofnij się o 1 znak
    return int(s)

##def _getPos():
##    print(_GETPOS, end='')
##    tekst = ''
##    sys.stdin.read(2)
##    x = _getInt(sys.stdin)
##    sys.stdin.read(1)
##    y = _getInt(sys.stdin)
##    sys.stdin.read(1)
##    return (x, y)
def _getPos():
    return (1, 1)

class PoleTekstowe:
    '''x1 - lewy bok pola (1 - ∞) (włącznie)
y1 - górny bok pola (1 - ∞) (włącznie)
x2 - prawy bok pola (1 - ∞) (włącznie)
y2 - dolny bok pola (1 - ∞) (włącznie)'''
    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.__sze = self.__x2 - self.__x1 + 1
        self.__wartosc = ''
        self.update()
        rejestrujCallback('keyPress', lambda x: self.ustawWartosc(self.__wartosc + x))
    def ustawWartosc(self, wartosc):
        self.__wartosc = wartosc
        self.update()
    def update(self):
        startPos = _getPos()
        for y, linia in zip_longest(range(self.__y1, self.__y2 + 1), textwrap.wrap(self.__wartosc, self.__sze), fillvalue=''):
            print(_SETPOS % (self.__x1, y) + linia.ljust(self.__sze))

_callbacki = EmptyListDict()
_config = {'echo':True}
def rejestrujCallback(event, callback):
    '''Eventy:
• 'keyPress' - wciśnięcie klawisza'''
    _callbacki[event].append(callback)

def konfiguruj(co, wartosc):
    '''Co:
• 'echo' - czy wyświetlać echo znaków'''
    _config[co] = wartosc

def obsluzEventy():
    while True:
        if msvcrt.kbhit():
            if _config['echo']:
                c = msvcrt.getche()
            else:
                c = msvcrt.getch()
            if c == '\r':
                c = '\n'
            for f in _callbacki['keyPress']:
                f(c)
        else:
            break
