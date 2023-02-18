from collections import namedtuple

NUMERY = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
KOLORY = ('♠', '♣', '♥', '♦')
PELNY_STOS = tuple(Karta(numer, kolor) for kolor in KOLORY for numer in NUMERY)

Karta = namedtuple('Karta', 'numer kolor')

def rozdaj(talia, gracze):
    def numGen(gracze):
        while True:
            yield from range(gracze)
    karty = [[] for _ in range(gracze)]
    for i in numGen(gracze):
        karty[i].append(talia.pop())
