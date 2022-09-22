import pygame as _pygame
_pygame.init()

class _Repr:
    def __init__(self, s):
        self._s = s
    def __repr__(self):
        return self._s
    def __eq__(self, r2):
        if type(self) == type(r2) and self._s == r2._s:
            return True
        else:
            return False

_font = _pygame.font.SysFont('Courier New', 16)

_SZEROKOSCZNAKU, _WYSOKOSCZNAKU = _font.render(' ', False, (0, 0, 0)).get_size()

_NOERR = 0x1
_ZOSTAWZAWARTOSC = 0x2
UKRYJMYSZ = 0x4

LEWO = '\0'
PRAWO = '\1'
GORA = '\2'
DOL = '\3'

_screen = None

class Screen:
    def __init__(self, szerokosc, wysokosc, pelnyEkran, *, komendy=0):
        global _screen
        self._screen = _pygame.display.set_mode((szerokosc * _SZEROKOSCZNAKU, wysokosc * _WYSOKOSCZNAKU), _pygame.FULLSCREEN if pelnyEkran else 0)
        if szerokosc == 0:
            szerokosc = self._screen.get_width() // _SZEROKOSCZNAKU
        if wysokosc == 0:
            wysokosc = self._screen.get_height() // _WYSOKOSCZNAKU
        self._screen.fill((0, 0, 0))
        _pygame.display.flip()
        if _screen == None:
            _screen = self
        else:
            if not (komendy & _NOERR):
                raise Exception('Tworzysz drugiego screena!')
        self.szerokosc = szerokosc
        self.wysokosc = wysokosc
        self.pelnyEkran = pelnyEkran
        if not (komendy & _ZOSTAWZAWARTOSC):
            self.pos = (0, 0)
            self.tlo = (0, 0, 0)
            self._plansza = []
            for y in range(wysokosc):
                self._plansza.append([])
                for x in range(szerokosc):
                    self._plansza[-1].append((' ', (0, 0, 0), (0, 0, 0)))
        if komendy & UKRYJMYSZ:
            _pygame.mouse.set_visible(False)
    def _reset(self):
        self.__init__(self.szerokosc, self.wysokosc, self.pelnyEkran, komendy=_NOERR | _ZOSTAWZAWARTOSC)
    def ustawPole(self, wsp, znak, fg=(255, 255, 255), bg=_Repr('TŁO')):
        self._plansza[wsp[1]][wsp[0]] = (znak, fg, bg)
    def cputs(self, tekst, pozycja=None, fg=(255, 255, 255), bg=_Repr('TŁO'), zawijanie=False):
        if pozycja == None:
            pozycja = self.pos
        linia = pozycja[1]
        kolumna = pozycja[0]
        for c in tekst:
            if c == '\n':
                linia += 1
                kolumna = 0
            elif c == LEWO:
                kolumna -= 1
            elif c == PRAWO:
                kolumna += 1
            elif c == GORA:
                linia -= 1
            elif c == DOL:
                linia += 1
            else:
                try:
                    self.ustawPole((kolumna, linia), c, fg, bg)
                except IndexError:
                    if zawijanie:
                        kolumna = 0
                        linia += 1
                        self.ustawPole((kolumna, linia), c, fg, bg)
                kolumna += 1
        self.pos = (kolumna, linia)
    def flip(self, antialias=True):
        self._screen.fill(self.tlo)
        for y, rzad in zip(range(len(self._plansza)), self._plansza):
            for x, pole in zip(range(len(rzad)), rzad):
                if pole[2] == _Repr('TŁO'):
                    self._screen.blit(_font.render(pole[0], antialias, pole[1]), (x * _SZEROKOSCZNAKU, y * _WYSOKOSCZNAKU))
                else:
                    self._screen.blit(_font.render(pole[0], antialias, pole[1], pole[2]), (x * _SZEROKOSCZNAKU, y * _WYSOKOSCZNAKU))
        _pygame.display.flip()
    def reset(self):
        self.__init__(self.szerokosc, self.wysokosc, self.pelnyEkran, komendy=_NOERR)

def zmienFonta(nazwa='Courier New', rozmiar=16):
    global _font
    global _SZEROKOSCZNAKU
    global _WYSOKOSCZNAKU
    global _screen
    _font = _pygame.font.SysFont(nazwa, rozmiar)
    _SZEROKOSCZNAKU, _WYSOKOSCZNAKU = _font.render(' ', False, (0, 0, 0)).get_size()
    if _screen != None:
        _screen._reset()

def zamknij():
    _pygame.quit()

def eventy():
    '''zwraca eventy pygameowe'''
    return _pygame.event.get()
