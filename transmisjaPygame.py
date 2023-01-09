import socket
import pygame

_DEFAULT_WIDTH = 800
_DEFAULT_HEIGHT = 600

def _set_mode(size=(0, 0), flags=0, depth=0, display=0, vsync=0):
    global _screen
    if size[0] == 0:
        size = (_DEFAULT_WIDTH, size[1])
    if size[1] == 0:
        size = (size[0], _DEFAULT_HEIGHT)
    _screen = pygame.Surface(size, 0)
    return _screen

def _get_surface():
    return _screen

_screen = None
pygame.display.set_mode = _set_mode
pygame.display.get_surface = _get_surface
