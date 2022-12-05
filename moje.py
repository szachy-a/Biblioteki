from functools import partial as _partial
from tkinter import Tk as _Tk, Frame as _Frame, Canvas as _Canvas
from turtle import RawTurtle as _RawTurtle, TurtleScreen as _TurtleScreen
import math as _math
import os as _os
import sys as _sys
import io as _io
from collections import abc as _abc

class Struktura:
    def __init__(self, **kwargs):
        self._zawartosc = list(kwargs.keys())
        for i in kwargs:
            exec(f'self.{i} = kwargs["{i}"]')
    def __repr__(self):
        s = '<'
        for i in self._zawartosc:
            s += i + ':' + eval(f'self.{i}').__repr__() + ', '
        s = s[:-2] + '>'
        return s

class _Nic:
    def __init__(self, wartosc):
        self.wartosc = wartosc
    def __repr__(self):
        return self.wartosc

NIC = _Nic('NIC')
PUSTYREPR = _Nic('')

class Referencja:
    def __init__(self, co):
        self.co = co
    def __str__(self):
        return str(self.co)
    def __repr__(self):
        return 'Referencja(' + repr(self.co) + ')'
    def __int__(self):
        return int(self.co)
    def __float__(self):
        return float(self.co)
    def __lt__(self, co):
        return self.co < co
    def __le__(self, co):
        return self.co <= co
    def __eq__(self, co):
        return self.co == co
    def __ne__(self, co):
        return self.co != co
    def __ge__(self, co):
        return self.co >= co
    def __gt__(self, co):
        return self.co > co
    def przypisz(self, co):
        self.co = co
    def zwrot(self):
        return self.co
    def __add__(self, co):
        return self.co + co
    def __sub__(self, co):
        return self.co - co
    def __mul__(self, co):
        return self.co * co
    def __truediv__(self, co):
        return self.co / co
    def __floordiv__(self, co):
        return self.co // co
    def __mod__(self, co):
        return self.co % co
    def __iadd__(self, co):
        self.co += co
        return self
    def __isub__(self, co):
        self.co -= co
        return self
    def __imul__(self, co):
        self.co *= co
        return self
    def __itruediv__(self, co):
        self.co /= co
        return self
    def __ifloordiv__(self, co):
        self.co //= co
        return self
    def __imod__(self, co):
        self.co %= co
        return self

class Struktura:
    def __init__(self, **kwargs):
        self._zawartosc = list(kwargs.keys())
        for i in kwargs:
            exec(f'self.{i} = kwargs["{i}"]')
    def __repr__(self):
        s = '<'
        for i in self._zawartosc:
            s += i + ':' + eval(f'self.{i}').__repr__() + ', '
        s = s[:-2] + '>'
        return s

def ownStruct(name, elems):
    def __init__(self, *args, **kwargs):
        for n, v in zip(self.__slots__, args):
            setattr(self, n, v)
        for n, v in kwargs.items():
            setattr(self, n, v)
    def __repr__(self):
        r = self.__class__.__name__ + '('
        for n in self.__slots__:
            r += n + '=' + repr(getattr(self, n)) + ', '
        return r[:-2] + ')'
    def __eq__(self, o):
        return type(self) is type(o) and all(getattr(self, n) == getattr(o, n) for n in self.__slots__)
    return type(name, (), {'__slots__':tuple(elems), '__init__':__init__, '__repr__':__repr__, '__eq__':__eq__, '__module__':''})

class Wysypisko:
    def __init__(self):
        self.zaw = []
    def dodaj(self, co):
        self.zaw.append(co)
    def dodajret(self, co):
        self.dodaj(co)
        return co
    def reset(self):
        self.zaw = []

def partial(func, /, *args, **kwargs):
    def newfunc(*fargs, **fkwargs):
        return func(*args, **kwargs)
    return newfunc

class Liczkat:
    def __init__(self):
        self._tk = _Tk()
        self._tk.withdraw()
        self._plotno = _Canvas(self._tk, width=1000000, height=1000000)
        self._plotno.grid()
        self._turtle = _RawTurtle(self._plotno)
    def reset(self):
        self._turtle.reset()
    def setpos(self, x, y=None):
        if y == None:
            pos = x
        else:
            pos = (x, y)
        self._turtle.goto(pos)
    def kierunek(self, ile):
        self._turtle.seth(ile)
    def przesun(self, ile):
        self._turtle.fd(ile)
    def getpos(self):
        return self._turtle.pos()

def kierunek(p1, p2):
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]
    dx,dy = x2-x1,y2-y1
    rads = _math.atan2(dx, dy)
    degs = _math.degrees(rads)
    return degs

def tmpnam(roz='.tmp'):
    num = 0
    while _os.path.exists(f'{_os.getenv("TMP")}\\{num}{roz}'):
        num += 1
    return f'{_os.getenv("TMP")}\\{num}{roz}'

def printFormat(*args, sep=' ', end='\n'):
    return sep.join(args) + end

class SpecjalnaStala:
    def __init__(self, nazwa=None):
        self.nazwa = nazwa
        self.spkod = next(_kody)
    def __repr__(self):
        if self.nazwa == None:
            return f'<SpecjalnaStala bez nazwy o numerze {self.spkod}>'
        else:
            return f'<SpecjalnaStala o nazwie {self.nazwa}>'
    def __eq__(self, co):
        if type(self) != type(co):
            return False
        if self.spkod == co.spkod:
            return True
        return False
    def __hash__(self):
        return self.spkod

def _kody():
    i = 0
    while True:
        yield i
        i += 1

_kody = _kody()

class FrozenDict(_abc.Mapping):
    def __init__(self, *args, **kwargs):
        self.__dict = dict(*args, **kwargs)
    def __getitem__(self, key):
        return self.__dict[key]
    def __len__(self):
        return len(self.__dict)
    def __repr__(self):
        return f'FrozenDict({self.__dict})'

def haszowanie(cls):
    '''Dodaje obsługę haszowania opartą na haszach instancji do klasy. Nie działa z atrybutami zmiennymi.'''
    def __hash__(obj):
        wartosc = 0
        for attr in obj.__dict__.items():
            wartosc ^= hash(attr)
        return wartosc
    cls.__hash__ = __hash__
    return cls

def oneTimeGen(f):
    return f()

class IntConsts:
    def __init__(self, *args):
        for i, n in enumerate(args):
            setattr(self, n, i)
    def __setattr__(self, attr, value):
        if hasattr(self, attr):
            raise TypeError('Nie można przypisywać do const')
        else:
            super().__setattr__(attr, value)
