import tkinter as _tk

from collections import defaultdict as _defaultdict

from pythonlangutil.overload import Overload as _Overload, signature as _signature

class _Repr:
    def __init__(self, r):
        self.__r = r
    def __repr__(self):
        return self.__r

DOMYSLNY = _Repr('guiLib.DOMYSLNY')

class Styl:
    def __init__(self, nazwa):
        self.__nazwa = nazwa
    def __eq__(self, inny):
        if isinstance(inny, Styl):
            return self.__nazwa == inny.__nazwa
        else:
            return NotImplemented
    def __repr__(self):
        return f'guiLib.Styl({self.__nazwa})'

class Okno:
    def __init__(self, tytul='Okno GuiLib', styl=Styl(DOMYSLNY)):
        self._tk = _tk.Tk()
        self._tk.title(tytul)
        self.styl = styl
    def petlaGlowna(self):
        self._tk.mainloop()
    def __repr__(self):
        return f'<obiekt typu {self.__class__.__name__}>'

class Widzet:
    def __init__(self, okno):
        self.__eventBind = {}
        self.styl = okno.styl
        self._okno = okno
        self._widzet = None
        
    def bind(self, event, fun):
        self._widzet.bind(self.__przetworz(event), lambda x: fun())
        
    def _klik(self, przycisk, nacisnieto):
        if nacisnieto:
            nacPusc = 'Nacisnieto'
        else:
            nacPusc = 'Puszczono'
        self.__eventBind[('Mysz', nacPusc, przycisk)]()
        
    @_Overload
    @_signature()
    def umiesc(self):
        self._widzet.grid()
        
    @umiesc.overload
    @_signature('int', 'int')
    def umiesc(self, x, y):
        self._widzet.grid(row=y, column=x)

    @staticmethod
    def __przetworz(event):
        nowy = '<'
        if event[0] == 'Mysz':
            nowy += 'Button'
            if event[1] == 'Nacisnieto':
                nowy += 'Press'
            elif event[1] == 'Puszczono':
                nowy += 'Release'
            else:
                raise Exception('Nieprawidłowe dane eventu')
            if event[2] in [1, 2, 3]:
                nowy += str(event[2])
            else:
                raise Exception('Nieprawidłowe dane eventu')
        else:
            raise Exception('Nieprawidłowe dane eventu')
        nowy += '>'
        
    def __repr__(self):
        return f'<obiekt typu {self.__class__.__name__}>'

class Przycisk(Widzet):
    def __init__(self, okno, *, tekst='', komenda=None):
        super(Przycisk, self).__init__(okno)
        self.__tekst = tekst
        if komenda == None:
            self.__komenda = lambda: None
        else:
            self.__komenda = komenda
        self._widzet = _tk.Button(self._okno._tk, text=self.__tekst, command=self.__komenda)
    def _klik(self, przycisk, nacisnieto):
        super(Przycisk, self)._klik(przycisk, nacisnieto)
        if przycisk == 1:
            self.klatka = self.__klatki[nacisnieto]
            if nacisnieto:
                self.__komenda()
