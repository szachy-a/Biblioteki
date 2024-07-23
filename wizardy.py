import tkinter as tk
from tkinter import ttk

import types

class Wizard:
    def __init__(self, steps: list[types.FunctionType], *, title=None, width=800, height=600):
        self.__tk = tk.Tk()
        self.__tk.resizable(0, 0)
        if title is not None:
            self.__tk.title(title)
        self.__fr = tk.Frame(self.__tk)
        self.__fr.grid()
        self.__bFr = tk.Frame(self.__tk)
        self.__bFr.grid()
        self.__back = ttk.Button(self.__bFr, text='< Back', command=self._back)
        self.__back.grid(row=0, column=0)
        self.__next = ttk.Button(self.__bFr, text='Next >', command=self._next)
        self.__next.grid(row=0, column=1)
        przerwa = tk.Label(self.__bFr, text=5 * ' ')
        przerwa.grid(row=0, column=2)
        self.__cancel = ttk.Button(self.__bFr, text='Cancel', command=self._cancel)
        self.__cancel.grid(row=0, column=3)
        self.__tk.update_idletasks()
        self.__tk.geometry(self.__tk.geometry())
        self.__tk.update_idletasks()
        self.__bFr.place(x=800 - self.__bFr.winfo_width(), y=600)
        self.__steps = tuple(steps)
        self.__current = 0
        self._render()
    @property
    def frame(self):
        return self.__fr
    def _back(self):
        self.__current -= 1
        self._render()
    def _next(self):
        self.__current += 1
        self._render()
    def _cancel(self):
        self.__tk.destroy()
    def _render(self):
        self.__fr.destroy()
        self.__fr = tk.Frame(self.__tk)
        self.__fr.grid()
        if self.__current == 0:
            self.__back.state(['disabled'])
        else:
            self.__back.state(['!disabled'])
        if self.__current + 1 >= len(self.__steps):
            self.__next.state(['disabled'])
        else:
            self.__next.state(['!disabled'])
        self.__steps[self.__current](self)
    def mainloop(self):
        self.__tk.mainloop()

if __name__ == '__main__':
    def f(w):
        l = tk.Label(w.frame, text='Hello world 1')
        l.grid()
    def g(w):
        l = tk.Label(w.frame, text='Hello world 2')
        l.grid()
    w = Wizard([f, g], title='Wizard')
    w.mainloop()
