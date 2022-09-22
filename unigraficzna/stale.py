from pygame.locals import *

def _num():
    n = 0
    while True:
        yield n
        n += 1
_num = _num()

class _Stala:
    def __init__(self, r=None):
        if r == None:
            self.__r = f'<Stała numer {next(_num)}>'
        else:
            self.__r = r
    def __repr__(self):
        return self.__r

BINDOWANE = _Stala('BINDOWANE')
SAMODZIELNA_KOLEJKA = _Stala('SAMODZIELNA_KOLEJKA')
