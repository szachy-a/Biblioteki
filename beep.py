from winsound import PlaySound as _PlaySound, SND_ALIAS as _SND_ALIAS
import os as _os

f = open('C:/Dodatkowe/pyzrodlodanych.sciezka', encoding='utf-8')
_SCIEZKA = _os.path.join(f.read(), '__lib__beep.wav')
f.close()
del f

def sysBeep():
    _PlaySound('SystemExclamation', _SND_ALIAS)

def trzyBeep():
    _PlaySound(_SCIEZKA, 0)

if __name__ == '__main__':
    input('Kliknij enter aby puścić "sysBeep"')
    sysBeep()
    input('Kliknij enter aby puścić "trzyBeep"')
    trzyBeep()
    input('Kliknij enter aby zakończyć')
