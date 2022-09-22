from tkinter import (
    Frame as _Frame, Scrollbar as _Scrollbar,
    VERTICAL as _VERTICAL, HORIZONTAL as _HORIZONTAL,
    ttk
)

class ScrolledFrame(_Frame):
    def __init__(self, master, **kw):
        if 'width' not in kw:
            kw['width'] = 800
        if 'height' not in kw:
            kw['height'] = 600
        super(ScrolledFrame, self).__init__(master, **kw)
        self.__pion = _Scrollbar(self, orient=_VERTICAL)
        self.__poziom = _Scrollbar(self, orient=_HORIZONTAL)
        self.__pion.grid(row=0, column=1, sticky='news')
        self.__poziom.grid(row=1, column=0, sticky='news')
        master.update()
        self.__fr = _Frame(self, width=kw['width'] - self.__pion.winfo_width(), height=kw['height'] - self.__poziom.winfo_height())
        self.__fr.grid(row=0, column=0, sticky='news')
