import pygame

import moje
import abc
import numbers

DOMYSLNE = moje.SpecjalnaStala('DOMYSLNE')
AXIS = moje.SpecjalnaStala('AXIS')
BUTTON = moje.SpecjalnaStala('BUTTON')
HAT = moje.SpecjalnaStala('HAT')

@moje.oneTimeGen
def _joys():
    i = 0
    while True:
        yield i
        i += 1

class Kontroler:
    pass

class PgJoystick(Kontroler):
    def __init__(self, drazki, przyciski, stopniowane, daneJoystickow={}):
        global j
        j = pygame.joystick.Joystick(next(_joys))
        self.drazki = []
        for i, (t, dInfo) in enumerate(drazki):
            if t == DOMYSLNE:
                try:
                    info = daneJoystickow[j.get_name()]
                except KeyError as e:
                    try:
                        info = daneJoystickow[DOMYSLNE]
                    except KeyError:
                        raise e
                if info['drazki'][i][0] not in [AXIS, BUTTON, HAT]:
                    raise ValueError(f'Niepoprawny typ drążka')
                t = info['drazki'][i][0]
                if info['drazki'][i][1] is not None:
                    dInfo = info['drazki'][i][1]
                
            if t == AXIS:
                self.drazki.append(DrazekZAxis(j, *dInfo))
            elif t == BUTTON:
                self.drazki.append(DrazekZButton(j, *dInfo))
            elif t == HAT:
                self.drazki.append(DrazekZHat(j, dInfo))

        self.przyciski = []
        for i, (t, bInfo) in enumerate(przyciski):
            if t == DOMYSLNE:
                try:
                    info = daneJoystickow[j.get_name()]
                except KeyError as e:
                    try:
                        info = daneJoystickow[DOMYSLNE]
                    except KeyError:
                        raise e
                if info['przyciski'][i][0] not in [AXIS, BUTTON]:
                    raise ValueError(f'Niepoprawny typ przycisku')
                t = info['przyciski'][i][0]
                if info['przyciski'][i][1] is not None:
                    bInfo = info['przyciski'][i][1]

            if t == AXIS:
                self.przyciski.append(PrzyciskZAxis(j, bInfo))
            elif t == BUTTON:
                self.przyciski.append(PrzyciskZButton(j, bInfo))

        self.stopniowane = []
        for i, (t, sInfo) in enumerate(stopniowane):
            if t == DOMYSLNE:
                try:
                    info = daneJoystickow[j.get_name()]
                except KeyError as e:
                    try:
                        info = daneJoystickow[DOMYSLNE]
                    except KeyError:
                        raise e
                if info['stopniowane'][i][0] not in [AXIS, BUTTON]:
                    raise ValueError(f'Niepoprawny typ stopniowanego')
                t = info['stopniowane'][i][0]
                if info['stopniowane'][i][1] is not None:
                    sInfo = info['stopniowane'][i][1]

            if t == AXIS:
                self.przyciski.append(StopniowaneZAxis(j, sInfo))
            elif t == BUTTON:
                self.przyciski.append(StopniowaneZButton(j, sInfo))

class PgKeyboard(Kontroler):
    def __init__(self, drazki, przyciski, stopniowane):
        raise NotImplementedError('Nie zaimplementowano')

class Drazek(abc.ABC):
    @property
    @abc.abstractmethod
    def x(self) -> numbers.Real:
        pass
    @property 
    @abc.abstractmethod
    def y(self) -> numbers.Real:
        pass
    @property
    @abc.abstractmethod
    def side(self) -> tuple[int, int]:
        pass

class DrazekZAxis(Drazek):
    def __init__(self, j, a1, a2):
        self.__j = j
        self.__a1 = a1
        self.__a2 = a2
    @property
    def x(self):
        return self.__j.get_axis(self.__a1)
    @property
    def y(self):
        return self.__j.get_axis(self.__a2)
    @property
    def side(self):
        return (int(self.x * 1.5), int(self.y * 1.5))

class DrazekZButton(Drazek):
    def __init__(self, j, u, d, l, r):
        self.__j = j
        self.__u = u
        self.__d = d
        self.__l = l
        self.__r = r
    @property
    def x(self):
        return int(self.__j.get_button(self.__r)) - int(self.__j.get_button(self.__l))
    @property
    def y(self):
        return int(self.__j.get_button(self.__d)) - int(self.__j.get_button(self.__u))
    @property
    def side(self):
        return (self.x, self.y)

class DrazekZHat(Drazek):
    def __init__(self, j, h):
        self.__j = j
        self.__h = h
    @property
    def x(self):
        return self.__j.get_hat(self.__h)[0]
    @property
    def y(self):
        return -(self.__j.get_hat(self.__h)[1])
    @property
    def side(self):
        return (self.x, self.y)

class Przycisk(abc.ABC):
    @property
    @abc.abstractmethod
    def pressed(self) -> bool:
        pass

class PrzyciskZAxis(Przycisk):
    def __init__(self, j, a):
        self.__j = j
        self.__a = a
    @property
    def pressed(self):
        return self.__j.get_axis(self.__a) > 0.7

class PrzyciskZButton(Przycisk):
    def __init__(self, j, b):
        self.__j = j
        self.__b = b
    @property
    def pressed(self):
        return self.__j.get_button(self.__b)

class Stopniowane(abc.ABC):
    @property
    @abc.abstractmethod
    def value(self) -> float:
        pass

class StopniowaneZAxis(Stopniowane):
    def __init__(self, j, a):
        self.__j = j
        self.__a = a
    @property
    def value(self):
        return self.__j.get_axis(self.__a)

class StopniowaneZButton(Stopniowane):
    def __init__(self, j, b):
        self.__j = j
        self.__b = b
    @property
    def value(self):
        return float(self.__j.get_button(self.__b))
