import tkinter as _tk
from PIL import Image as _Image, ImageTk as _ImageTk

import pygame as _pygame
_pygame.init()

class Screen:
    '''Parametr "bledy" mówi o zachowaniu gdy zostanie wykryty niepoprawny kolor.
Przyjmuje on następujące wartości:
- Typ wyjątku - Rzuć wyjątek tego typu
- 0 - Zamień na kolor tekstu
- 1 - Zamień na kolor tła'''
    def __init__(self, sze, wys, sciezkaDoFonta, bledy=OSError):
        self.__tk = _tk.Tk()
        self.__znaki = {}
        self.__kratki = []
        self.__sciezka = sciezkaDoFonta
        self.__bledy = bledy
        for y in range(wys):
            self.__kratki.append([])
            for x in range(sze):
                self.__kratki[-1].append(_tk.Label(self.__tk, image=self._znak(' ', (0, 0, 0), (0, 0, 0))))
                self.__kratki[-1][-1].grid(row=y, column=x)
    def _znak(self, znak, fg, bg):
        try:
            return self.__znaki[(znak, fg, bg)]
        except KeyError:
            pass
        try:
            surf = _pygame.image.load(self.__sciezka + '/' + znak + '.png')
        except FileNotFoundError:
            try:
                surf = _pygame.image.load(self.__sciezka + '/' + hex(ord(znak)) + '.png')
            except FileNotFoundError:
                surf = _pygame.Surface((1, 1))
                surf.fill((255, 255, 255))
        surf = surf.convert(32)
        arr = _pygame.surfarray.pixels3d(surf)
        for rzad in arr:
            for pole in rzad:
                match tuple(pole):
                    case (0, 0, 0):
                        pole[:] = fg
                    case (255, 255, 255):
                        pole[:] = bg
                    case _:
                        if isinstance(self.__bledy, type) and issubclass(self.__bledy, BaseException):
                            raise self.__bledy('Nieznany kolor ' + str(tuple(pole)))
                        elif self.__bledy == 0:
                            pole[:] = fg
                        elif self.__bledy == 1:
                            pole[:] = bg
                        else:
                            raise TypeError('Nieznane rozpoznawanie błędów ' + repr(self.__bledy))
        del rzad
        del arr
        strImg = _pygame.image.tostring(surf, 'RGB', False)
        pilImg = _Image.frombytes('RGB', surf.get_size(), strImg)
        self.__znaki[(znak, fg, bg)] = (pilImg, _ImageTk.PhotoImage(pilImg, master=self.__tk))
        return self.__znaki[(znak, fg, bg)][1]
    def put(self, pos, tekst, fg, bg):
        for x, c in enumerate(tekst, pos[0]):
            try:
                self.__kratki[pos[1]][x].config(image=self._znak(c, fg, bg))
            except IndexError:
                break
        
