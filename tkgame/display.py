from kontrolaImportu import tkgame as _tkgame
import tkinter as _tkinter
from PIL import ImageTk as _ImageTk

_tk = _tkinter.Tk()
_tk.title('Tkgame window')
_tk.withdraw()
_l = _tkinter.Label(_tk)
_screen = None
_img = None

def quit():
    _tk.destroy()

def set_mode(size, flags=0):
    global _screen
    _tk.deiconify()
    _tk.geometry(f'{size[0]}x{size[1]}')
    _screen = _tkgame.Surface(size)
    return _screen

def flip():
    global _l
    global _img
    _img = _ImageTk.PhotoImage(_screen._img)
    _l.destroy()
    _l = _tkinter.Label(_tk, image=_img)
    _l.grid()
    _tk.update()
