from PIL import Image as _Image
import tkinter as _tkinter
from PIL import ImageTk as _ImageTk
import queue as _queue
from functools import partial as _partial
import time as _time
import locals
from locals import *


def init():
    pass

def quit():
    display.quit()

class Surface:
    def __init__(self, size):
        self._img = _Image.new('RGBA', size, (0, 0, 0))
    def fill(self, kolor):
        self._img.paste(kolor, (0, 0) + self._img.size)
    def blit(self, surf, rect):
        if type(rect) == Rect:
            self._img.paste(surf._img, rect.topleft)
        else:
            self._img.paste(surf._img, rect)
    def get_rect(self, topleft=(0, 0)):
        return Rect(topleft[0], topleft[1], topleft[0] + self._img.size[0], topleft[1] + self._img.size[1])

class Rect:
    def __init__(self, lewo, gora, prawo, dol):
        self.topleft = (lewo, gora)
        self.bottomright = (prawo, dol)

_tk = _tkinter.Tk()
_tk.title('Tkgame window')
_tk.withdraw()
_l = _tkinter.Label(_tk)
_screen = None
_img = None
class display:
    def quit():
        _tk.destroy()

    def set_mode(size, flags=0):
        global _screen
        _tk.deiconify()
        _tk.geometry(f'{size[0]}x{size[1]}')
        _screen = Surface(size)
        return _screen

    def flip():
        global _l
        global _img
        _img = _ImageTk.PhotoImage(_screen._img)
        _l.destroy()
        _l = _tkinter.Label(_tk, image=_img)
        _l.grid()
        _tk.update()

class event:
    class Event:
        def __init__(self, type, **kwargs):
            self.type = type
            for k, w in zip(kwargs.keys(), kwargs.values()):
                exec(f'self.{k} = w')
            self._dict = kwargs
    def get():
        while not _eventy.empty():
            yield _eventy.get()
    def __repr__(self):
        return f'<Event {self._dict}>'
_eventy = _queue.Queue()
_tk.protocol('WM_DELETE_WINDOW', lambda: _eventy.put(event.Event(locals.QUIT)))
for i in filter(lambda x: x.startswith('K_'), dir(locals)):
    if len(i) == 3:
        klawisz = i.split('K_')[1]
    elif i in ['K_UP', 'K_DOWN', 'K_LEFT', 'K_RIGHT']:
        klawisz = i.split('K_')[1].lower() + 'arrow'
    elif i == 'K_SPACE':
        klawisz = 'space'
    else:
        dane = i.split('K_')[1].lower()
        klawisz = dane[0].upper() + dane[1:]
    _tk.bind_all(f'<KeyPress-{klawisz}>', _partial(lambda x, y: _eventy.put(event.Event(locals.KEYDOWN, key=eval(f'locals.{x}'))), i))
del i

class time:
    def set_timer(event, czas):
        pass
