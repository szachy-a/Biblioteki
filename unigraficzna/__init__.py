import pygame as _pygame
_pygame.init()

import copy

import stale
import event

class Error(Exception):
    '''Błąd biblioteki "unigraficzna"'''

class Event:
    def __init__(self, zawartosc=None, /, **kwargs):
        zawBool = zawartosc != None
        kwBool = kwargs != {}
        if zawBool:
            if kwBool:
                raise Error('Nie wiadomo skąd wziąć dane')
        elif kwBool:
            zawartosc = kwargs
        for k, v in zawartosc.items():
            exec(f'self.{k} = v')
        self.dict = copy.copy(zawartosc)
    def __repr__(self):
        return f'unigraficzna.Event({repr(self.dict)})'

def otworzOkienko(sze, wys, /, fullscreen=False):
    flagi = 0
    if fullscreen:
        flagi |= FULLSCREEN
    return _pygame.display.set_mode((sze, wys), flagi)

def zamknij():
    _pygame.quit()
