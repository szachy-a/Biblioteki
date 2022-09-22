from tkinter import (
    Tk as _Tk, Frame as _Frame,
    StringVar as _StringVar, IntVar as _IntVar,
    ttk as _ttk
)
from functools import partial as _partial

_tk = _Tk()
_tk.withdraw()
_tk.protocol('WM_DELETE_WINDOW', lambda: None)

def wyborOpcji(opcje, pytanie='Wybierz opcję', *, font=None, tk=None, addComs=lambda tk: None):
    s = _ttk.Style()
    if font is not None:
        if isinstance(font, str):
            font = (font, 0)
        s.configure('.', font=font)
    start = tk
    if tk == None:
        tk = _tk
        _tk.deiconify()
    addComs(tk)
    fr = _Frame(_tk)
    wybor = _StringVar(fr)
    l = _ttk.Label(fr, text=pytanie)
    l.grid()
    for i, opcja in enumerate(opcje):
        box = _ttk.Button(fr, text=opcja, command=_partial(lambda x: wybor.set(x), opcja))
        box.grid(row=i % 5 + 1, column=i // 5, sticky='w')
    fr.grid()
    fr.wait_variable(wybor)
    wybor = wybor.get()
    fr.destroy()
    if start == None:
        _tk.withdraw()
    return wybor
        
def wieloWybor(opcje, pytanie='Wybierz opcję', *, font=None, tk=None, addComs=lambda tk: None):
    s = _ttk.Style()
    if font is not None:
        if isinstance(font, str):
            font = (font, 0)
        s.configure('.', font=font)
    spam = []
    start = tk
    if tk == None:
        _tk.deiconify()
        tk = _tk
    addComs(tk)
    fr = _Frame(tk)
    koniec = _IntVar(fr)
    wybory = {}
    for opcja in opcje:
        wybory[opcja] = _IntVar(fr, 0)
    l = _ttk.Label(fr, text=pytanie)
    l.grid()
    for opcja in opcje:
        startVar = _IntVar(fr, 0)
        spam.append(startVar)
        box = _ttk.Checkbutton(fr, text=opcja, variable=startVar, command=_partial(lambda x: wybory[x].set(int(not wybory[x].get())), opcja))
        box.grid()
    b = _ttk.Button(fr, text='Koniec', command=lambda: koniec.set(1))
    b.grid()
    fr.grid()
    fr.wait_variable(koniec)
    fr.destroy()
    if start == None:
        _tk.withdraw()
    return list(map(lambda x: x[0], filter(lambda x: x[1].get(), wybory.items())))
