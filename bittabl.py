import math

class BitTabl:
    _INT_BITS = 64
    _INT_MAX = 2 ** _INT_BITS - 1
    
    def __init__(self, dlugosc):
        self.__tabl = math.ceil(dlugosc / self._INT_BITS) * [0]
        self.__dlugosc = dlugosc
        
    def __getitem__(self, indeks):
        if indeks >= self.__dlugosc or indeks < 0:
            raise IndexError(f'Nieprawidłowy indeks {indeks}')
        nadElem = self.__tabl[indeks // self._INT_BITS]
        return (nadElem >> (indeks % self._INT_BITS)) & 1
    
    def __setitem__(self, indeks, wartosc):
        if wartosc not in [0, 1]:
            raise ValueError(f'Nieprawidłowa wartość {wartosc}')
        if indeks >= self.__dlugosc or indeks < 0:
            raise IndexError(f'Nieprawidłowy indeks {indeks}')
        nadInd = indeks // self._INT_BITS
        podInd = indeks % self._INT_BITS
        maska = self.__bitnot(1 << podInd)
        wynik = (self.__tabl[nadInd] & maska) | wartosc << podInd
        self.__tabl[nadInd] = wynik

    def __len__(self):
        return self.__dlugosc

    def __iter__(self):
        for i in range(len(self)):
            yield self[i]

    @staticmethod
    def __bitnot(v):
        return (~v) & BitTabl._INT_MAX
