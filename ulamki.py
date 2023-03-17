import moje

@moje.zakazDziedziczenia
class UlamekZwykly:
    def __init__(self, licznik, mianownik=1):
        self.__licznik = licznik
        self.__mianownik = mianownik
        if type(self.__licznik) is float:
            while self.__licznik != int(self.__licznik):
                self.__licznik *= 2
                self.__mianownik *= 2
            self.__licznik = int(self.__licznik)
        elif type(self.__licznik) is int:
            pass
        else:
            raise TypeError(f'Licznik nie może być typu {type(self.__licznik)}')
        if type(self.__mianownik) is float:
            while self.__mianownik != int(self.__mianownik):
                self.__licznik *= 2
                self.__mianownik *= 2
            self.__mianownik = int(self.mianownik)
        elif type(self.__mianownik) is int:
            pass
        else:
            raise TypeError(f'Mianownik nie może być typu {type(self.__mianownik)}')
        self._skroc()
    def __repr__(self):
        return f'{self.__class__.__name__}({self.licznik}, {self.mianownik})'
    def __str__(self):
        return f'{self.licznik}/{self.mianownik}'
    def _skroc(self):
        if self.__mianownik < 0:
            self.__licznik = -self.__licznik
            self.__mianownik = -self.__mianownik
        nwd = _nwd(self.__licznik, self.__mianownik)
        self.__licznik //= nwd
        self.__mianownik //= nwd
    @property
    def licznik(self):
        return self.__licznik
    @property
    def mianownik(self):
        return self.__mianownik
    def __add__(self, other):
        if type(other) is not type(self):
            return NotImplemented
        return UlamekZwykly(self.licznik * other.mianownik + other.licznik * self.mianownik, self.mianownik * other.mianownik)
    def __sub__(self, other):
        if type(other) is not type(self):
            return NotImplemented
        return UlamekZwykly(self.licznik * other.mianownik - other.licznik * self.mianownik, self.mianownik * other.mianownik)
    def __mul__(self, other):
        if type(other) is not type(self):
            return NotImplemented
        return UlamekZwykly(self.licznik * other.licznik, self.mianownik * other.mianownik)
    def __truediv__(self, other):
        if type(other) is not type(self):
            return NotImplemented
        return UlamekZwykly(self.licznik * other.mianownik, other.licznik * self.mianownik)
    def __neg__(self):
        return UlamekZwykly(-self.licznik, self.mianownik)
    def __pos__(self):
        return UlamekZwykly(self.licznik, self.mianownik)
    def __eq__(self, other):
        if type(other) is not type(self):
            return NotImplemented
        return self.licznik == other.licznik and self.mianownik == other.mianownik
    def __lt__(self, other):
        if type(other) is not type(self):
            return NotImplemented
        return self.licznik * other.mianownik < other.licznik * self.mianownik
    def __le__(self, other):
        if type(other) is not type(self):
            return NotImplemented
        return self.licznik * other.mianownik <= other.licznik * self.mianownik
    def __float__(self):
        return self.licznik / self.mianownik
    def __int__(self):
        return self.licznik // self.mianownik
    def __hash__(self):
        return hash(self.licznik) ^ hash(self.mianownik)
    def __bool__(self):
        return bool(self.licznik)
    __match_args__ = ('licznik', 'mianownik')

def _nwd(a, b):
    while b:
        a, b = b, a % b
    return a
