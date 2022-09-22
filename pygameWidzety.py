import pygame
pygame.init()

import abc

_font = pygame.font.SysFont('', 30)

_widzety = []

class _Repr:
    def __init__(self, r):
        self.r = r
    def __repr__(self):
        return self.r

class _ZmianaDoc:
    def __init_subclass__(cls, **kwargs):
        super(_ZmianaDoc).__init_subclass__(**kwargs)
        if cls.__module__ == _ZmianaDoc.__module__:
            cls.__doc__ = 'Klasa widżetu ' + cls.__module__ + '.' + cls.__name__

class Widget(abc.ABC, _ZmianaDoc):
    def __init__(self, master, *args, **kwargs):
        if isinstance(master, pygame.Surface) or isinstance(master, Frame):
            self._master = master
        else:
            raise TypeError(f'Nieprawidłowy typ argumentu master ({master}) gdy oczekiwano pygame.Surface lub pygameWidzety.Frame')
        self.surf = None
        self.rect = None
        _widzety.append(self)
        self.__klikniety = False
    def place(self, x, y):
        self.rect.topleft = (x, y)
    def _event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.__klikniety = True
                self._klik()
        elif event.type == pygame.MOUSEBUTTONUP:
            self.__klikniety = False
            self._pusc()
    @abc.abstractmethod
    def _klik(self):
        '''Widżet został naciśnięty'''
    @abc.abstractmethod
    def _pusc(self):
        '''Widżet został puszczony'''

class Label(Widget):
    def __init__(self, master, *, text=''):
        super().__init__(master)
        self.surf = _font.render(text, True, (0, 0, 0), (255, 255, 255))
        self.rect = self.surf.get_rect()
    def _klik(self):
        pass
    def _pusc(self):
        pass

class Button(Widget):
    def __init__(self, master, *, text='', command=_Repr('lambda: None')):
        super().__init__(master)
        self.surf = _font.render(text, True, (0, 0, 0), (255, 255, 255))
        pygame.draw.rect(self.surf, (0, 0, 0), pygame.Rect((0, 0), (self.surf.get_width(), self.surf.get_height())), width=2)
        self.rect = self.surf.get_rect()
        self.__text = text
        if isinstance(command, _Repr) and command.r == 'lambda: None':
            self.__command = lambda: None
        else:
            self.__command = command
    def _klik(self):
        self.surf = _font.render(self.__text, True, (255, 255, 255), (0, 0, 0))
        pygame.draw.rect(self.surf, (255, 255, 255), pygame.Rect((0, 0), (self.surf.get_width(), self.surf.get_height())), width=2)
        self.rect = self.surf.get_rect()
    def _pusc(self):
        self.surf = _font.render(self.__text, True, (0, 0, 0), (255, 255, 255))
        pygame.draw.rect(self.surf, (0, 0, 0), pygame.Rect((0, 0), (self.surf.get_width(), self.surf.get_height())), width=2)
        self.rect = self.surf.get_rect()
        self.__command()

class Frame(Widget):
    @property
    def _master(self):
        class _Master(type(self.__master)):
            def __init__(self, prawdziwy):
                self.__prawdziwy = prawdziwy
            def blit(self, source, dest, area=None, special_flags=0):
                for widzet in _widzety:
                    if widzet._master in [self, self.__prawdziwy]:
                        self.__prawdziwy.blit(widzet.surf, widzet.rect)
                
        return _Master(self.__master)
    @_master.setter
    def _master(self, wartosc):
        self.__master = wartosc
        
    def __init__(self, master):
        super().__init__(master)
        self.__master = master

    def blit(self, source, dest, area=None, special_flags=0):
        self.surf.blit(sorce, dest, area, special_flags)

############# Małpie łatanie Pygame ###############
def _latanie():
    _orgGet = pygame.event.get
    def _get(eventtype=None, pump=True, exclude=None):
        ret = _orgGet(eventtype, pump, exclude)
        for event in ret:
            for widzet in _widzety:
                widzet._event(event)
        return ret
    pygame.event.get = _get

    _orgPoll = pygame.event.poll
    def _poll():
        ret = _orgPoll()
        for widzet in _widzety:
            widzet._event(ret)
        return ret
    pygame.event.poll = _poll

    _orgWait = pygame.event.wait
    def _wait(timeout=_Repr('')):
        if timeout == _Repr(''):
            ret = _orgWait()
        else:
            ret = _orgWait(timeout)
        for widzet in _widzety:
            widzet._event(ret)
        return ret
    pygame.event.wait = _wait

    _orgUpdate = pygame.display.update
    def _update(rectangle=None, /):
        '''(rectangle_list, /)'''
        if _screen != None:
            for widzet in _widzety:
                _screen.blit(widzet.surf, widzet.rect)
        _orgUpdate(rectangle)
    pygame.display.update = _update

    _orgFlip = pygame.display.flip
    def _flip():
        for widzet in _widzety:
            widzet._master.blit(widzet.surf, widzet.rect)
        _orgFlip()
    pygame.display.flip = _flip

_latanie()
del _latanie
################## Koniec łatania ###################
