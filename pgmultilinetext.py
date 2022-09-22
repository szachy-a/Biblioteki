import pygame
pygame.init()

from itertools import chain
import io

def render(font, text, antialias, color, csze, ssze, swys):
    teksty = map(lambda x: _oddzielPo(x, csze), text.split('\n'))
    linie = tuple(map(lambda x: font.render(x, antialias, color), chain(*teksty)))
    s = pygame.Surface((ssze, sum(map(lambda x: x.get_height(), linie))))
    s.fill((0, 0, 0))
    aktWys = 0
    for linia in linie:
        s.blit(linia, (0, aktWys))
        aktWys += linia.get_height()
    s2 = pygame.Surface((ssze, swys))
    s2.fill((0, 0, 0))
    s2.blit(s, s.get_rect(left=0, bottom=swys))
    return s2

def _oddzielPo(s, dlugosc):
    f = io.StringIO(s)
    while so := f.read(dlugosc):
        yield so
