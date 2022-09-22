from tkinter import Tk as _Tk, Canvas as _Canvas
from moje import Liczkat as _Liczkat
from PIL import Image as _Image, ImageTk as _ImageTk

_tk = _Tk()
_plotno = _Canvas(_tk, width=800, height=600)
_plotno.grid()
_liczkat = _Liczkat()

class Pen:
    def __init__(self):
        self._pos = (400, 300)
        self._kierunek = 0
        self._up = False
        self._img = _Image.open('turtle.png')
        self._imgid = None
        self._wyswietl()
    def up(self):
        self._up = True
    def down(self):
        self._up = False
    def fd(self, ile):
        _liczkat.reset()
        _liczkat.setpos(self._pos)
        _liczkat.kierunek(self._kierunek)
        _liczkat.przesun(ile)
        if not self._up:
            pos = self._pos
        self._pos = _liczkat.getpos()
        if not self._up:
            _plotno
        self._wyswietl()
    def bk(self, ile):
        self.fd(-ile)
    def lt(self, ile):
        self._kierunek = (self.kierunek - ile) % 360
        self._wyswietl()
    def rt(self, ile):
        self.lt(-ile)
    def _wyswietl(self):
        if self._imgid != None:
            _plotno.delete(self._imgid)
        img = self._img.rotate(-self.kierunek, expand=True)
        img = _ImageTk.PhotoImage(img)
        self._imgid = _plotno.create_image(image=img, anchor='e')
        _plotno.update()
