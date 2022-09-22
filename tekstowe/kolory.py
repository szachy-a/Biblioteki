from colorama import Fore as _Fore, Back as _Back, Style as _Style

FORE, BACK, BRAK, \
BIALY, CZARNY, NIEBIESKI, JASNONIEBIESKI, ZIELONY, FIOLETOWY, CZERWONY, ZOLTY, \
POGRUBIONY, GORA, DOL, LEWO, PRAWO, *reszta = range(100)
del reszta

def _kolorNaColorama(kolor, fb):
    if fb == FORE:
        mod = _Fore
    elif fb == BACK:
        mod = _Back
    else:
        raise ValueError(f'Niepoprawna wartość FORE/BACK {fb}')
    if kolor == BRAK:
        return ''
    if kolor == BIALY:
        return mod.WHITE
    elif kolor == CZARNY:
        return mod.BLACK
    elif kolor == NIEBIESKI:
        return mod.BLUE
    elif kolor == JASNONIEBIESKI:
        return mod.CYAN
    elif kolor == ZIELONY:
        return mod.GREEN
    elif kolor == FIOLETOWY:
        return mod.MAGENTA
    elif kolor == CZERWONY:
        return mod.RED
    elif kolor == ZOLTY:
        return mod.YELLOW
    else:
        raise ValueError(f'Nieznany kolor {kolor}')
    
def _dodatekNaColorama(dodatek):
    if dodatek == POGRUBIONY:
        return _Style.BRIGHT
    elif dodatek == BRAK:
        return ''
    else:
        raise ValueError(f'Nieznany dodatek {dodatek}')
