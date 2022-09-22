import curses

import sys
import functools

LASTMODE = (-1, -1)
C40 = BW40 = MONO = (40, -1)
C80 = BW80 = (80, -1)

_orgCursesWin = None
_orgConioWin = None
_curConioWin = None
_lastMode = None
_orgBuf = None
_curBuf = None

class ConioError(Exception):
    '''Błąd związany z biblioteką conioInCurses'''

def _conioFunStart():
    if not _orgCursesWin:
        raise ConioError('Nie zainicjalizowano conioInCurses')

def _conioFunEnd():
    _curConioWin.refresh()
    _orgConioWin.refresh()
    _orgCursesWin.refresh()

def _conioFun(f):
    @functools.wraps(f)
    def new(*args, **kwargs):
        _conioFunStart()
        try:
            r = f(*args, **kwargs)
        except curses.error as e:
            raise ConioError(f'Błąd w funkcji {f.__name__}') from e
        _conioFunEnd()
        return r
    return new

def init():
    global _orgCursesWin
    _orgCursesWin = curses.initscr()
    curses.cbreak()
    textmode((_orgCursesWin.getmaxyx()[1] - 1, -1))

def quit():
    global _orgCursesWin
    _orgCursesWin = None
    curses.endwin()

@_conioFun
def clreol():
    _curConioWin.clrtoeol()

@_conioFun
def clrscr():
    _curConioWin.erase()

@_conioFun
def cprint(*args, sep=' ', end='\n'):
    _conioFunStart()
    _curConioWin.addstr(sep.join(map(str, args)) + end)
    _conioFunEnd()

@_conioFun
def delline():
    _curConioWin.deleteln()

@_conioFun
def gettext(left, top, right, bottom):
    _curConioWin
    
@_conioFun
def textmode(newmode):
    global _orgConioWin
    global _curConioWin
    global _orgBuf
    global _curBuf
    if type(newmode) is not tuple or len(newmode) != 2:
        raise ConioError(f'Nie można wywołać textmode z argumentem {newmode!r}')
    if newmode == (-1, -1):
        textmode(_lastMode)
    elif newmode[1] == -1:
        textmode((newmode[0], _orgCursesWin.getmaxyx()[0] - 1))
    else:
        _orgConioWin = _orgCursesWin.subwin(newmode[1], newmode[0], 1, 1)
        _curConioWin = _orgConioWin.subwin(1, 1)
        _orgBuf = [newmode[0] * [('\0', 0x0F)] for _ in range(newmode[1])]
        _curBuf = _orgBuf

if __name__ == '__main__' and sys.__stdout__:
    init()
