from tkinter import Tk, PhotoImage, Button, Entry, Label, Frame, StringVar, messagebox

from functools import partial

_tk = Tk()
_tk.withdraw()

BLAD = PhotoImage(file='Blad.png')
INFO = PhotoImage(file='Info.png')
OSTRZEZENIE = PhotoImage(file='Ostrzezenie.png')
PYTANIE = PhotoImage(file='Pytanie.png')

SYSTEMTYPY = {BLAD:'error', INFO:'info', OSTRZEZENIE:'warning', PYTANIE:'question'}
TYPY = set(SYSTEMTYPY.keys())
TYPY.add(None)

OK = 'OK'
ANULUJ = 'Anuluj'
TAK = 'Tak'
NIE = 'Nie'
PONOW = 'Ponów próbę'

PRZYCISKI = {OK, ANULUJ, TAK, NIE, PONOW}
ZWROTY = {(OK,):(None,), (OK, ANULUJ):(True, False), (TAK, NIE):(True, False),
          (TAK, NIE, ANULUJ):(True, False, None), (PONOW, ANULUJ):(True, False)}
KOMBINACJE = set(ZWROTY.keys())

def komunikat(tresc='', tytul='', typ=INFO, przyciski=(OK,)):
    if len(przyciski) != 1:
        raise RuntimeError('Nieodpowiednia ilość przycisków')
    if typ in TYPY and przyciski in KOMBINACJE:
        messagebox.showinfo(tytul, tresc, icon=SYSTEMTYPY[typ])
        return ZWROTY[przyciski][0]
    else:
        return tkDialog(tresc, tytul, typ, przyciski)

def pytanie(tresc='', tytul='', typ=None, przyciski=(TAK, NIE)):
    if len(przyciski) == 1:
        raise RuntimeError('Nieodpowiednia ilość przycisków')
    if typ in TYPY and przyciski in KOMBINACJE:
        if przyciski == (TAK, NIE):
            return messagebox.askyesno(tytul, tresc, icon=SYSTEMTYPY[typ] or SYSTEMTYPY[PYTANIE])
        elif przyciski == (OK, ANULUJ):
            return messagebox.askokcancel(tytul, tresc, icon=SYSTEMTYPY[typ] or SYSTEMTYPY[PYTANIE])
        elif przyciski == (TAK, NIE, ANULUJ):
            return messagebox.askyesnocancel(tytul, tresc, icon=SYSTEMTYPY[typ] or SYSTEMTYPY[PYTANIE])
        elif przyciski == (PONOW, ANULUJ):
            return messagebox.askretrycancel(tytul, tresc, icon=SYSTEMTYPY[typ] or SYSTEMTYPY[OSTRZEZENIE])
        else:
            return tkDialog(tresc, tytul, typ, przyciski)

def tkDialog(tresc='', tytul='', typ=INFO, przyciski=(OK,)):
    wybor = StringVar()
    _tk.title(tytul)
    _tk.deiconify()
    fr1 = Frame(_tk)
    l1 = Label(fr1, image=typ)
    l2 = Label(fr1, text=tresc)
    l1.grid(row=0, column=0)
    l2.grid(row=0, column=1)
    fr1.grid()
    fr2 = Frame(_tk)
    for i, prz in enumerate(przyciski):
        b = Button(fr2, text=prz, command=partial(lambda x: wybor.set(x), prz))
        b.grid(row=0, column=i)
    fr2.grid()
    _tk.wait_variable(wybor)
    _tk.withdraw()
    if przyciski in KOMBINACJE:
        return ZWROTY[przyciski][przyciski.index(wybor.get())]
    else:
        return wybor.get()
    
    
