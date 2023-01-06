try:
    import os as _os
    _os.putenv('PYGAME_HIDE_SUPPORT_PROMPT', 'to nie ma znaczenia')
    import contextlib
    with contextlib.redirect_stdout(None):
        import pygame as _pygame
        _pygame.init()
except ModuleNotFoundError:
    pass

class Bitmapa:
    def __init__(self, *, nazwa=None, szerokosc=None, wysokosc=None, tryb='rgba', wypelnienie=None):
        '''Należy podać argument "nazwa" LUB argumenty "szerokosc" I "wysokosc" i do nich ewentualnie argument "wypelnienie" i ewentualnie argument "tryb"'''
        if nazwa and not szerokosc and not wysokosc:
            self._ladujZPliku(nazwa)
        elif not nazwa and szerokosc and wysokosc:
            self._nowa(szerokosc, wysokosc, wypelnienie, tryb)
        else:
            raise TypeError('Zła kombinacja argumentów!')
    def _ladujZPliku(self, nazwa):
        f = open(nazwa, 'rb')
        if ord(f.read(1).decode(encoding='ansi')) & 1:
            alfa = True
            self.tryb = 'rgba'
        else:
            raise ValueError('Nieznany typ bitmapy')
        wym = f.readline()
        wym = wym[:-1].decode(encoding='ascii')
        wym = tuple(map(int, wym.split('x')))
        self.sze, self.wys = wym
        self.zawartosc = []
        for y in range(self.wys):
            self.zawartosc.append([])
            for x in range(self.sze):
                self.zawartosc[-1].append(_rgba(f.read(4)))
    def _nowa(self, sze, wys, wypelnienie, tryb):
        if tryb == 'rgba':
            self.tryb = tryb
        else:
            raise ValueError('Nieznany tryb')
        self.tryb = tryb
        if not wypelnienie:
            if self.tryb == 'rgba':
                wypelnienie = (255, 255, 255, 255)
            else:
                raise Exception('Brakuje tego trybu (prosimy o kontakt pod reklamacje@szachy-a.tk)')
        self.sze = sze
        self.wys = wys
        self.zawartosc = []
        for y in range(self.wys):
            self.zawartosc.append([])
            for x in range(self.sze):
                self.zawartosc[-1].append(wypelnienie)
    try:
        _pygame
        def naSurface(self):
            surf = _pygame.Surface((self.sze, self.wys), flags=_pygame.SRCALPHA)
            surf.lock()
            for rzad, y in zip(self.zawartosc, range(len(self.zawartosc))):
                for pole, x in zip(rzad, range(len(rzad))):
                    surf.set_at((x, y), pole)
            surf.unlock()
            return surf
    except NameError:
        pass

def _rgba(b):
    t = []
    for i in b:
        t.append(i)
    return tuple(t)
