import os
import subprocess
import pickle

def doSchowka(dane):
    dane = repr(pickle.dumps(dane))
    if ' ' in dane:
        dane = '"' + dane + '"'
    subprocess.run(f'setx MOJSCHOWEK {dane}')
    os.system('mojSchowekGetenv.bat')
    f = open('D:/tempy/mojschoweklib.txt')
    nowe = f.read()[:-1]
    f.close()
    if nowe != dane:
        raise ValueError('Niepoprawne kopiowanie do mojego schowka')

def zSchowka():
    pass
