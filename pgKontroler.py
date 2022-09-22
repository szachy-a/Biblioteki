import pygame as pg # nie będę tutaj importował przez "from" więc skracam nazwę

import os
import subprocess
import winshell
import moje

#################################### Blok stałych i hacków #################################################
class _Meta(type):
    def __repr__(self):
        return '(Dowolne z BUTTON, AXIS, ONEWAY)'

class _TypCzesci(metaclass=_Meta):
    __name__ = __qualname__ = '(Dowolne z BUTTON, AXIS, ONEWAY)'
    def __init__(self, r):
        self.__r = r
    def __repr__(self):
        return self.__r

BUTTON = _TypCzesci('BUTTON')
AXIS = _TypCzesci('AXIS')
ONEWAY = _TypCzesci('ONEWAY')
_TypCzesci._opcje = (BUTTON, AXIS, ONEWAY)
def _fakeInit(self, r):
    '''raise NotImplementedError('Nie można tworzyć instancji tej klasy')'''
    raise NotImplementedError('Nie można tworzyć instancji tej klasy')
_TypCzesci.__init__ = _fakeInit
_TypCzesci.__doc__ = _fakeInit.__doc__

del _Meta
del _fakeInit
####################################     Koniec bloku     #################################################

def zapytajOKonfiguracje(doKonfiguracji : dict[str, _TypCzesci]):
    lnk = winshell.shortcut('C:/Dodatkowe/konfigurator kontrolera.lnk')
    sciezka = lnk.path
    nam = moje.tmpnam()
    f = open(nam, 'w')
    f.close()
    subprocess.run(f'py "{sciezka}" łóżko button >"{nam}" 2>NUL <NUL', shell=True)
    f = open(nam, encoding='1250') # MOŻE BY KTOŚ WYŁĄCZYŁ STRONY KODOWE!!!
    dane = eval(f.read())
    f.close()
    os.remove(nam)
