import pygame

import warnings

# STAŁE GLOBALNE
PRZYCISK = pygame.NUMEVENTS - 1
DRAZEK = pygame.NUMEVENTS - 2

B_L2, B_R2, B_A, B_B, B_C, B_D, D_L, D_R, D_L1, D_R1, D_TOUCHPAD, D_POKRETLO, B_L3, B_R3, B_TOUCHPAD, D_STRZALKI, B_STRZALKI, B_ZATWIERDZ, B_GWIAZDKA, B_PLUS, B_MINUS, B_SHARE, B_OPTIONS, B_TOUCHPAD_DOTKIETY, B_FK, *_ = range(100)
del _
# KONIEC STAŁYCH

_MAPOWANIE_B = {0:B_A, 1:B_B, 2:B_C, 3:B_D, 4:B_SHARE, 5:B_FK, 6:B_OPTIONS, 7:B_L3, 8:B_R3, 9:B_L2, 10:B_R2, 15:B_TOUCHPAD}
_MAPOWANIE_B_TO_D = {11:(D_STRZALKI, 0, -1), 12:(D_STRZALKI, 0, 1), 13:(D_STRZALKI, -1, 0), 14:(D_STRZALKI, 1, 0)}
_MAPOWANIE_D = {0:lambda x: (D_L, x, None), 1:lambda y: (D_L, None, y), 2:lambda x: (D_R, x, None), 3:lambda y: (D_R, None, y), 4:lambda x: (D_L1, x, None), 5: lambda x: (D_R1, x, None)}

_spamJoys = []
pygame.joystick.init()
for i in range(pygame.joystick.get_count()):
    _spamJoys.append(pygame.joystick.Joystick(i))
del i

_daneDr = {D_L:[0, 0], D_R:[0, 0]}
def _setDr(dr, x, y):
    if x != None:
        _daneDr[dr][0] = x
    if y != None:
        _daneDr[dr][1] = y

def _getDr(dr):
    return _daneDr[dr]

_orgPygameEventGet = pygame.event.get
def _pygameEventGet():
    wynik = _orgPygameEventGet()
    ustDr = {}
    for event in wynik:
        if event.type in [pygame.JOYBUTTONUP, pygame.JOYBUTTONDOWN]:
            try:
                nowy = pygame.event.Event(PRZYCISK, przycisk=_MAPOWANIE[event.button], nacisniety=event.type == pygame.JOYBUTTONDOWN)
            except KeyError:
                m = _MAPOWANIE_B_TO_D[event.button]
                nowy = pygame.event.Event(DRAZEK, drazek=m[0], x=m[1], y=m[2])
            wynik.append(nowy)
        elif event.type == pygame.JOYAXISMOTION:
            m = _MAPOWANIE_D[event.axis](event.value)
            _setDr(*m)
            ustDr.add(m[0])
    for i in ustDr:
        m = _getDr(i)
        wynik.append(pygame.event.Event(DRAZEK, drazek=m[0], x=m[1], y=m[2]))
    return wynik
pygame.event.get = _pygameEventGet

class _lampka: # będzie jeden obiekt - pseudomoduł
    def wlacz(self, kolor):
        warnings.warn('Niemożliwa funkcja', FutureWarning)
    def wylacz(self):
        warnings.warn('Niemożliwa funkcja', FutureWarning)
def _lampkaInit():
    raise TypeError('Pseudomoduł')
lampka = _lampka()
_lampka.__init__ = _lampkaInit
del _lampka
