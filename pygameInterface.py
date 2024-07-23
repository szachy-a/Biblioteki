import pygame

import abc
from collections.abc import Callable

from pygame.event import Event

VALID_X_POINTS = frozenset({'left', 'right', 'centerx'})
VALID_Y_POINTS = frozenset({'top', 'bottom', 'centery'})

_DEFAULT_FONT = pygame.font.SysFont('Calibri', 11)

class Widget(abc.ABC):
    _rect : pygame.Rect
    @property
    def _surf(self) -> pygame.Surface:
        return self.__surf
    @_surf.setter
    def _surf(self, surf : pygame.Surface):
        self.__surf = surf
        self._rePlace()
    def __init__(self, **kwargs):
        self.config(**kwargs)
    @abc.abstractmethod
    def config(self, **kwargs):
        pass
    def processEvent(self, event : pygame.event.Event):
        pass
    def place(self, x, y, xPoint='left', yPoint='top'):
        assert xPoint in VALID_X_POINTS
        assert yPoint in VALID_Y_POINTS
        self._x = x
        self._y = y
        self._xPoint = xPoint
        self._yPoint = yPoint
        self.rePlace()
    def rePlace(self):
        self._rect = self._surf.get_rect(**{self._xPoint:self._x, self._yPoint:self._y})
    def display(self, screen):
        screen.blit(self._surf, self._rect)

class WithFg(Widget):
    def __init__(self, fg=(0, 0, 0), **kwargs):
        super().__init__(self, fg=fg, **kwargs)
    def config(self, fg : tuple[int, int, int]=None, **kwargs):
        super().__init__(self, fg=fg, **kwargs)
        if fg is not None:
            self._fg = fg

class WithBg(Widget):
    def __init__(self, bg=(255, 255, 255), **kwargs):
        super().__init__(self, bg=bg, **kwargs)
    def config(self, bg : tuple[int, int, int]=None, **kwargs):
        super().__init__(self, bg=bg, **kwargs)
        if bg is not None:
            self._bg = bg

class WithFont(Widget):
    def __init__(self, font : pygame.font.Font=_DEFAULT_FONT, **kwargs):
        super().__init__(self, font=font, **kwargs)
    def config(self, font : pygame.font.Font=None, **kwargs):
        super().config(self, font=font, **kwargs)
        if font is not None:
            self._font = font

class Label(WithBg):
    pass

class TextLabel(Label, WithFg, WithFont):
    def config(self, text : str=None, **kwargs):
        super().config(text=text, **kwargs)
        if text is not None:
            self._surf = self._font.render(text, True, self._fg, self._bg)

class ImageLabel(Label):
    def config(self, image : pygame.Surface=None, **kwargs):
        super().config(image=image, **kwargs)
        if image is not None:
            self._surf = image

class Button(Label):
    def config(self, command : Callable=None, **kwargs):
        super().config(self, command=command, **kwargs)
        if command is not None:
            self._command = command
    def processEvent(self, event):
        super().processEvent(event)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self._rect.collidepoint(event.pos):
                self._command()

class TextButton(Button, TextLabel):
    pass

class ImageButton(Button, ImageLabel):
    pass

class TextInput(WithFg, WithBg, WithFont):
    @property
    def content(self):
        return self.__content
    @content.setter
    def content(self, value):
        self.__content = value
        self.reDraw()
    def __init__(self, width : int=_DEFAULT_FONT.render('A' * 20, True, (0, 0, 0)).get_width(), **kwargs):
        super().__init__(self, width=width, **kwargs)
    def config(self, width : int=None, **kwargs):
        if width is not None:
            self._width = width
        super().config(self, width=width, **kwargs)
        self.reDraw()
    def reDraw(self):
        textSurf = self._font.render(self.content, True, self._fg, self._bg)
        surf = pygame.Surface((self._width, textSurf.get_height()))
        surf.blit(textSurf, (0, 0))
        self._surf = surf
    def processEvent(self, event: Event):
        super().processEvent(event)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self._rect.collidepoint(event.pos):
                self.__active = True
            else:
                self.__active = False
        elif event.type == pygame.KEYDOWN and self.__active:
            if event.key == pygame.K_BACKSPACE:
                self.content = self.content[:-1]
            else:
                self.content += event.unicode