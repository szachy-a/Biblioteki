import pygame
pygame.init()

class _Grid:
    def __init__(self):
        self.__budowa = [] # lista rzędów
    def dodaj(self, x, y, elem):
        while True:
            try:
                rzad = self.__budowa[y]
            except IndexError:
                self.__budowa.append([])
            else:
                break
        while True:
            try:
                rzad[x] = elem
            except IndexError:
                rzad.append(_Pusty())
            else:
                break
    @property
    def surf(self):
        sze = sum(max(rzad[x].sze for rzad in self.__budowa if x < len(rzad)) for x in range(max(map(len, self.__budowa))))
        wys = sum(max(elem.wys for elem in rzad) for rzad in self.__budowa)
        
        
