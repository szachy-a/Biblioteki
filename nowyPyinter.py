import pygame

if __name__ == '__main__':
    pygame.init()

if __name__ == '__main__':
    _screen = pygame.display.set_mode((800, 600))
_font = pygame.font.SysFont('', 18)

class Widget:
    def place(self, *, x, y):
        self._rect = self._surf.get_rect(topleft=(x, y))
        _widgets.append(self)
    def _onMouseDown(self):
        pass
    def _onMouseUp(self):
        pass
    def _onKeyDown(self, event):
        pass
    def _onKeyUp(self, event):
        pass

class Label(Widget):
    def __init__(self, *, text=''):
        self._surf = _font.render(text, True, (0, 0, 0))

class Button(Widget):
    def __init__(self, *, text='', command=lambda: None):
        self.__text = text
        self._surf = _font.render(self.__text, True, (0, 0, 0), (255, 255, 255))
        self.__command = command
    def _onMouseDown(self):
        self.__command()
        self._surf = _font.render(self.__text, True, (255, 255, 255), (0, 0, 0))
    def _onMouseUp(self):
        self._surf = _font.render(self.__text, True, (0, 0, 0), (255, 255, 255))

class Entry(Widget):
    def __init__(self):
        self.__text = ''
        self._surf = pygame.Surface((200, 40))
        self._surf.fill((255, 255, 255))
        pygame.draw.rect(self._surf, (0, 0, 0), (1, 1, 199, 39), 1)
        self._surf.blit(_font.render(self.__text, True, (0, 0, 0), (255, 255, 255)), (5, 5))
    def _onKeyDown(self, event):
        self.__text += event.unicode
        self._surf.fill((255, 255, 255))
        pygame.draw.rect(self._surf, (0, 0, 0), (1, 1, 199, 39), 1)
        self._surf.blit(_font.render(self.__text, True, (0, 0, 0), (255, 255, 255)), (5, 5))

class _NoWidget(Widget):
    def place(self, *, x, y):
        pass

def onEvent(event):
    global _focus
    if event.type == pygame.MOUSEBUTTONDOWN:
        for widget in _widgets:
            if widget._rect.collidepoint(event.pos):
                _focus = widget
        _focus._onMouseDown()
    elif event.type == pygame.MOUSEBUTTONUP:
        _focus._onMouseUp()
    elif event.type == pygame.KEYDOWN:
        _focus._onKeyDown(event)
    elif event.type == pygame.KEYUP:
        _focus._onKeyUp(event)

def blitWidgets(screen):
    for widget in _widgets:
        screen.blit(widget._surf, widget._rect)

_focus = _NoWidget()
_widgets = []

if __name__ == '__main__':
    e = Entry()
    e.place(x=100, y=100)
    while True:
        for event in pygame.event.get():
            onEvent(event)
        _screen.fill((255, 255, 255))
        blitWidgets(_screen)
        pygame.display.flip()
