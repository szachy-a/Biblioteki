import pygame
pygame.init()

from collections import abc
import numbers

_screen = None
_czas = pygame.time.Clock()

class Paleta(abc.MutableSequence):
    def __init__(self, rozmiar):
        self.__zawartosc = rozmiar * [(0, 0, 0)]
    def __getitem__(self, i):
        if isinstance(i, numbers.Integral):
            return self.__zawartosc[i]
        else:
            raise TypeError('Paleta indices must be integers')
    def __setitem__(self, i, v):
        if isinstance(i, numbers.Integral):
            if isinstance(v, tuple) and all(isinstance(x, numbers.Integral) for x in v):
                self.__zawartosc[i] = v
            else:
                raise TypeError
        else:
            raise TypeError('Paleta indices must be integers')
    def __delitem__(self, i):
        raise TypeError('Paleta object doesn\'t support item deletion')
    def insert(self, i, v):
        if isinstance(i, numbers.Integral):
            if isinstance(v, tuple) and all(isinstance(x, numbers.Integral) for x in v):
                self.__zawartosc.insert(i, v)
            else:
                raise TypeError
        else:
            raise TypeError('Paleta indices must be integers')
    def __len__(self):
        return len(self.__zawartosc)

def config(rozdzielczosc, pelnyEkran, rMax, gMax, bMax):
    global _screen
    global _max
    _screen = pygame.display.set_mode(rozdzielczosc, pygame.FULLSCREEN if pelnyEkran else 0)
    _max = (rMax, gMax, bMax)

def update(tablica, paleta):
    if not isinstance(paleta, (Paleta, None)):
        raise TypeError('Wymagany obiekt typu Paleta lub None')
    arr = pygame.surfarray.pixels3d(_screen)
    for inRzad, outRzad in zip(tablica, arr):
        for i in range(len(outRzad)):
            if isinstance(paleta, Paleta):
                v = paleta[inRzad[i]]
            elif isinstance(inRzad[i], tuple):
                v = inRzad[i]
            else:
                raise TypeError('Nieprawidłowy typ tablica[y][x]')
            outRzad[i][:] = v
    del outRzad
    del arr
    pygame.display.flip()

def ograniczenieFPS(fps):
    _czas.tick(fps)
