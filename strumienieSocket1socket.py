import socket

_BIN = b'b'
_TEKST = b't'

class StrumienWyjsciowy:
    def __init__(self, port=0, serwer='localhost'):
        self.__s = socket.socket()
        self.__s.bind((serwer, port))
        self.__serwer = serwer
        self._readonly = False
    def wyslij(self, wiadomosc):
        if self._readonly:
            raise TypeError('Nie można wysłać do tego typu strumienia')
        if type(wiadomosc) == str:
            wiadomosc = _TEKST + wiadomosc.encode()
        else:
            wiadomosc = _BIN + wiadomosc
        dane = b''
        koniec = memoryview(wiadomosc)
        while koniec:
            poczatek = koniec[:255]
            koniec = koniec[255:]
            dane += b'\1' + poczatek
        dane += b'\0'
        self.__s.send(dane)
    def __repr__(self):
        return f'StrumienWyjsciowy({repr(self.__s.getsockname()[1])}, {repr(self.__serwer)})'
    def zamknij(self):
        self.__s.close()
    def wejsciowy(self):
        s = StrumienWejsciowy(self.__s.getsockname()[1], self.__serwer)
        s._readonly = self._readonly
        return s
    def eksport(self):
        return [self.__s.getsockname()[1], self.__serwer]

class StrumienWejsciowy:
    def __init__(self, port, serwer):
        self.__s = socket.socket()
        self.__serwer = serwer
        self.__port = port
        self.__polaczano = False
        self._readonly = None
    def odczytaj(self):
        if not self.__polaczono:
            while True:
                try:
                    self.__s.connect((serwer, port))
                except ConnectionRefusedError:
                    pass
                else:
                    break
            self.__polaczano = True
        dane = b''
        try:
            while self.__s.recv(1)[0]:
                dane += self.__s.recv(255)
        except KeyboardInterrupt:
            raise
        if dane[0] == _TEKST:
            dane = dane.decode()
        return dane
    def dostepny(self):
        raise NotImplementedError('Nie zaimplementowano') # dokończyć
    def wyjsciowy(self):
        s = StrumienWyjsciowy(self.__port, self.__serwer)
        s._readonly = True
