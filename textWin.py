import tkinter

import threading
import time

class _TextWin:
    def __init__(self, sze, wys, tytul):
        self.__args = (sze, wys, tytul)
        self._started = False
    def __getitem__(self, indeks):
        if type(indeks) is int:
            return _TextWinRzad(self.__arr[indeks], self._labelToList, self._listEdit)
        elif type(indeks) is tuple:
            if len(indeks) == 2:
                return self._labelToList(self.__arr[indeks[0]][indeks[1]])
        raise TypeError(f'Niedozwolony indeks typu {type(indeks)!r} o wartości {indeks!r}')
    def __setitem__(self, indeks, wartosc):
        if type(indeks) is tuple:
            if len(indeks) == 2:
                self._listEdit(self.__arr[indeks[0]][indeks[1]], wartosc)
        raise TypeError(f'Niedozwolony indeks typu {type(indeks)!r} o wartości {indeks!r}')
    @classmethod
    def _labelToList(cls, l):
        return _TextWinPole([l['text'], l['fg'], l['bg']], cls._listEdit, l)
    @staticmethod
    def _listEdit(la, li):
        la.config(text=li[0], fg=li[1], bg=li[2])
    def _mainloop(self):
        sze, wys, tytul = self.__args
        self.__tk = tkinter.Tk()
        self.__tk.title(tytul)
        self.__arr = []
        for y in range(wys):
            self.__arr.append([])
            for x in range(sze):
                self.__arr[-1].append(tkinter.Label(self.__tk, bg='black', fg='white', font=('Courier', 0), text=' '))
                self.__arr[-1][-1].grid(row=y, column=x)
        print('Gotowy')
        self._started = True
        self.__tk.mainloop()

class _TextWinRzad:
    def __init__(self, l, ltol, le):
        self.__v = l
        self.__ltol = ltol
        self.__le = le
    def __getitem__(self, indeks):
        return _TextWinPole(self.__ltol(self.__v[indeks]), self.__le, self.__v[indeks])
    def __setitem__(self, indeks, wartosc):
        self.__le(self.__v[indeks], wartosc)

class _TextWinPole:
    def __init__(self, li, le, la):
        self.__li = li
        self.__le = le
        self.__la = la
    def __getitem__(self, indeks):
        return self.__li[indeks]
    def __setitem__(self, indeks, wartosc):
        self.__li[indeks] = wartosc
        self.__le(self.__la, self.__li)

_winOpen = False

def textWin(sze, wys, tytul='TextWin'):
    global _winOpen
    if _winOpen:
        raise RuntimeError('Nie można mieć wielu okienek tekstowych')
    else:
        _winOpen = True
        win = _TextWin(sze, wys, tytul)
        t = threading.Thread(None, win._mainloop)
        print('Wątek gotowy')
        t.start()
        print('Wystartowano')
        while not win._started:
            time.sleep(0)
        return win
