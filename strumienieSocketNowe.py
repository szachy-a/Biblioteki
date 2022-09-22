import os
import socket

_ODCZYTANO = 'o'
_ZAPISANOBIN = 'z'
_ZAPISANOTEKST = 'Z'
_NIEZACZETO = '-'

class StrumienWyjsciowy:
    def __init__(self):
        pass
    def wyslij(self, wiadomosc):
        print(wiadomosc)
    def zamknij(self):
        pass
    def wejsciowy(self):
        pass
    def eksport(self):
        return [socket.gethostbyname(socket.gethostname())]

class StrumienWejsciowy:
    def __init__(self, wiadomosci, stan):
        pass
    def odczytaj(self):
        return input()
    def dostepny(self):
        return True
    def eksport(self):
        return []
