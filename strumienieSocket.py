import socket

_BIN = b'\0'
_TEKST = b'\1'
_ZAMKNIJ = b'\2'

class StrumienWyjsciowy:
    def __init__(self, _=None, port=21331): # argument _ jest dla kompatybilności wstecznej
        self.__port = port
    def wyslij(self, wiadomosc, _raw=False):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((socket.gethostname(), self.__port))
        s.listen()
        if _raw:
            typ = ''
        elif type(wiadomosc) == str:
            wiadomosc = wiadomosc.encode()
            typ = _TEKST
        elif type(wiadomosc) == bytes:
            typ = _BIN
        elif wiadomosc == None:
            typ = _ZAMKNIJ
            wiadomosc = b''
        powtorz = True
        while powtorz:
            clientsocket, address = s.accept()
            clientsocket.send(typ + wiadomosc)
            wynik = clientsocket.recv(1)
            if wynik == b'T':
                powtorz = True
                nast = lambda: None
            elif wynik == b'W':
                nast = lambda: self.wyslij(clientsocket.recv(1024), True)
                powtorz = True
            elif wynik == b'F':
                nast = lambda: None
            nast()
            clientsocket.close()
    def __repr__(self):
        return f'StrumienWyjsciowy(None, {self.__port})'
    def zamknij(self):
        self.wyslij(None)
    def wejsciowy(self):
        return StrumienWejsciowy(socket.gethostbyname(socket.gethostname()), self.port)
    def eksport(self):
        return [socket.gethostbyname(socket.gethostname()), self.__port] # None dla kompatybilności wstecznej

class StrumienWejsciowy:
    def __init__(self, ip, port=21331):
        self.__ip = ip
        self.__port = port
    def odczytaj(self):
        if not self.dostepny():
            raise FileNotFoundError # Dla kompatybilności wstecznej
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.__ip, self.__port))
        dane = s.recv(1024)
        s.send(b'F')
        s.close()
        if dane[0] == _TEKST:
            dane = dane[1:].decode()
        elif dane[0] == _BIN:
            dane = dane[1:]
        elif dane[0] == _ZAMKNIJ:
            raise FileNotFoundError # Dla kompatybilności wstecznej
        return dane
    def dostepny(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((self.__ip, self.__port))
            dane = s.recv(1024)
            if dane[0] == _ZAMKNIJ:
                ret = False
            else:
                ret = True
            s.send(b'T')
        except socket.error:
            ret = False
        s.close()
        return ret
    def wyjsciowy(self):
        return _WirtWy(self.__ip, self.__port)
    def eksport(self):
        return [self.__ip, self.__port]

class _WirtWy:
    def __init__(self, ip, port):
        self.__ip = ip
        self.__port = port
    def wyslij(self, wiadomosc):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.__ip, self.__port))
        dane = s.recv(1024)
        if type(wiadomosc) == str:
            wiadomosc = wiadomosc.encode()
            typ = _TEKST
        elif type(wiadomosc) == bytes:
            typ = _BIN
        elif wiadomosc == None:
            typ = _ZAMKNIJ
            wiadomosc = b''
        s.send(b'W' + typ + wiadomosc)
    def __repr__(self):
        return f'_WirtWy({self.__ip}, {self.__port})'
    def zamknij(self):
        self.wyslij(None)
    def wejsciowy(self):
        return StrumienWejsciowy(self.__ip, self.__port)
    def eksport(self):
        return [self.__ip, self.__port]
