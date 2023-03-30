import tkinter as tk
import os
import functools

f = open('C:/Dodatkowe/pyzrodlodanych.sciezka', encoding='utf-8')
_SCIEZKA = os.path.join(f.read(), '__lib__tkinterStyles')
f.close()

def toMinecraft(widget):
    widget.config(font='F77 Minecraft')
    if isinstance(widget, (tk.Text, tk.Entry)):
        widget.config(bg='#123456')
        fr = tk.Frame(widget.master)
