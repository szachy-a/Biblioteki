import kolory

from colorama import Fore as _Fore, Back as _Back, Style as _Style, init as _init

import platform as _platform

_init(convert=_platform.system() == 'Windows')

def kolorowanyTekst(tekst, /, kolorTekstu=kolory.BRAK, kolorTla=kolory.BRAK):
    return kolory._kolorNaColorama(kolorTekstu, kolory.FORE) + kolory._kolorNaColorama(kolorTla, kolory.BACK) + tekst + _Style.RESET_ALL

def zDodatkami(tekst, dodatek=kolory.BRAK, /):
    return kolory._dodatekNaColorama(dodatek) + tekst + _Style.RESET_ALL