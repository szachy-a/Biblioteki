from collections import abc
import numbers
import moje

NUMERY = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
KOLORY = ('♠', '♣', '♥', '♦')

@moje.zakazDziedziczenia
class Karta:
    def __init__(self, numer, kolor):
        if numer not in NUMERY:
            raise ValueError(f'Numer nie może być {numer!r}')
        if kolor not in KOLORY:
            raise ValueError(f'Kolor nie może być {kolor!r}')
        self.__numer = numer
        self.__kolor = kolor
    @property
    def numer(self):
        return self.__numer
    @property
    def kolor(self):
        return self.__kolor
    def __repr__(self):
        return f'Karta({self.numer!r}, {self.kolor!r})'
    def __str__(self):
        return self.numer + self.kolor
    def __eq__(self, other):
        if not isinstance(other, Karta):
            return NotImplemented
        return self.numer == other.numer and self.kolor == other.kolor
    def __lt__(self, other):
        if not isinstance(other, Karta):
            return NotImplemented
        if self.numer < other.numer:
            return True
        if self.kolor < other.kolor:
            return True
        return False

PELNY_STOS = tuple(Karta(numer, kolor) for kolor in KOLORY for numer in NUMERY)

@moje.zakazDziedziczenia
class Talia(abc.MutableSequence):
    def __init__(self, karty=PELNY_STOS):
        self.__karty = []
        self[:] = karty
    def __getitem__(self, index):
        if isinstance(index, int):
            return self.__karty[index]
        elif isinstance(index, slice):
            return Talia(self.__karty[index])
        else:
            raise TypeError(f'Talia indices must be integers or slices, not {index.__class__.__name__}')
    def __setitem__(self, index, value):
        if isinstance(index, int):
            if isinstance(value, Karta):
                self.__karty[index] = value
            else:
                raise TypeError(f'{value.__class__.__name__} object cannot be interpreted as a Karta')
        elif isinstance(index, slice):
            for v in value:
                if not isinstance(v, Karta):
                    raise TypeError(f'{v.__class__.__name__} object cannot be interpreted as a Karta')
            self.__karty[index] = value
        else:
            raise TypeError(f'Talia indices must be integers or slices, not {index.__class__.__name__}')
    def __delitem__(self, index):
        if isinstance(index, int):
            del self.__karty[index]
        elif isinstance(index, slice):
            del self.__karty[index]
        else:
            raise TypeError(f'Talia indices must be integers or slices, not {index.__class__.__name__}')
    def __len__(self):
        return len(self.__karty)
    def insert(self, index, value):
        if isinstance(index, int):
            if isinstance(value, Karta):
                self.__karty.insert(index, value)
            else:
                raise TypeError(f'{value.__class__.__name__} object cannot be interpreted as a Karta')
        else:
            raise TypeError(f'{index.__class__.__name__} object cannot be interpreted as an integer')
    def append(self, value):
        if isinstance(value, Karta):
            self.__karty.append(value)
        else:
            raise TypeError(f'{value.__class__.__name__} object cannot be interpreted as a Karta')
    def __repr__(self):
        return f'Talia({self.__karty!r})'
