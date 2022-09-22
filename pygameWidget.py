'''KLIK:
Jest to event pygame oznaczający kliknięcie przycisku.
Atrybuty:
type -> == KLIK
pos -> == pozycja kliknięcia'''
import pygame
if not pygame.get_init():
    pygame.init()

class _Repr:
    def __init__(self, tekst):
        self.tekst = tekst
        self.wartosc = eval(self.tekst)
    def __repr__(self):
        return self.tekst

class _NoneWidzet:
    def __init__(self):
        pass
    def kliknij(self):
        pass
    def pisz(self, znak):
        pass

_widzety = pygame.sprite.Group()
_focus = _NoneWidzet()

KLIK = pygame.MOUSEBUTTONUP

class Button(pygame.sprite.Sprite):
    def __init__(self, pos, *, flagi=0, text='', command=None, rozmiar=None, fg=(0, 0, 0), bg=(240, 240, 240), font=_Repr('pygame.font.SysFont(\'Arial\', 20)')):
        super(Button, self).__init__()
        if type(font) == _Repr:
            font = font.wartosc
        if rozmiar == None:
            tsurf = font.render(text, True, fg)
            rozmiar = tsurf.get_size()
        self.surf = pygame.Surface(rozmiar)
        self.rect = self.surf.get_rect(topleft=pos)
        self.font = font
        self.command = command
        self.fg = fg
        self.bg = bg
        self.text = text
        self.rozmiar = rozmiar
        _widzety.add(self)
    def kliknij(self):
        self.command()
    def pisz(self, znak):
        pass
    def blit(self):
        self.surf.fill(self.bg)
        tsurf = self.font.render(self.text, True, self.fg)
        self.surf.blit(tsurf, tsurf.get_rect(center=(self.rozmiar[0] // 2, self.rozmiar[1] // 2)))

class Entry(pygame.sprite.Sprite):
    def __init__(self, pos, *, flagi=0, text='', command=None, rozmiar=(100, 50), fg=(0, 0, 0), bg=(240, 240, 240), font=_Repr('pygame.font.SysFont(\'Arial\', 20)')):
        super(Entry, self).__init__()
        if type(font) == _Repr:
            font = font.wartosc
        self.surf = pygame.Surface(rozmiar)
        self.rect = self.surf.get_rect(topleft=pos)
        self.font = font
        self.command = command
        self.fg = fg
        self.bg = bg
        self.text = text
        self.rozmiar = rozmiar
        _widzety.add(self)
    def kliknij(self):
        pass
    def pisz(self, znak):
        if znak == '\b':
            self.text = self.text[:-1]
        else:
            self.text += znak
    def blit(self):
        self.surf.fill(self.bg)
        tsurf = self.font.render(self.text, True, self.fg)
        self.surf.blit(tsurf, tsurf.get_rect(right=self.rozmiar[0], centery=self.rozmiar[1] // 2))

def event(event, /):
    global _focus
    if event.type == KLIK:
        for widzet in _widzety:
            if widzet.rect.collidepoint(event.pos):
                _focus = widzet
                widzet.kliknij()
    elif event.type == pygame.KEYDOWN:
        _focus.pisz(event.unicode)

def blit(screen, /):
    for widzet in _widzety:
        widzet.blit()
        screen.blit(widzet.surf, widzet.rect)
