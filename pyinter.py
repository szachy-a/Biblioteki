import pygame
import time
pygame.init()

class _Nad:
    def __init__(self):
        self.surf = None
        self.pod = pygame.sprite.Group()

class Tk(_Nad):
    def __init__(self):
        super(Tk, self).__init__()
        self.surf = pygame.display.set_mode((200, 200))
        self.surf.fill((230, 230, 230))
        pygame.display.flip()
    def update(self):
        pygame.event.get()
        pygame.display.flip()

class _Widzet(pygame.sprite.Sprite):
    def __init__(self, nad):
        super(_Widzet, self).__init__()
        self.surf = None
        self.nad = nad
        self.nad.pod.add(self)
    def place(self, x, y):
        self.nad.surf.blit(self.surf, (x, y))

class Label(_Widzet):
    def __init__(self, nad, *, text):
        super(Label, self).__init__(nad)
        self.font = pygame.font.SysFont(None, 50)
        self.surf = self.font.render(text, False, (0, 0, 0))

class Button(Label):
    def __init__(self, nad, *, text, command=None):
        super(Button, self).__init__(nad, text=text)
        self.font = pygame.font.SysFont('Courier New', 20)
        self.surf = self.font.render(text, False, (0, 0, 0))
