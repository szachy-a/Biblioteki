import socket as _socket
import urllib.request as _urllib2
import urllib.error as _error
import os as _os
import subprocess as _subprocess
import moje as _moje
import strumienie as _strumienie

IP = _socket.gethostbyname(_socket.gethostname())
IP6 = '[' + _socket.getaddrinfo(_socket.gethostname(), None, _socket.AF_INET6)[0][4][0] + ']'
PORT = 21332

class _SpRepr:
    def __init__(self, nazwa):
        self.nazwa = nazwa
    def __repr__(self):
        return self.nazwa
    def __eq__(self, co):
        return self.nazwa == co
    def zawartosc(self):
        return self.nazwa

class StrumienWyjsciowy:
    def __init__(self, port=_SpRepr('PORT')):
        if port == 'PORT':
            port = PORT
        self._tekst = f'C:/Dodatkowe/HostFlaskDane/{port}.snd'
        self._port = port
        f = open(self._tekst, 'w')
        f.write('')
        f.close()
        s = _strumienie.StrumienWyjsciowy(f'C:/Dodatkowe/HostFlaskDane/{self._port}.0', f'C:/Dodatkowe/HostFlaskDane/{self._port}.1')
        _os.system(f'start C:/Dodatkowe/hostFlask.exe {IP} {port} wiadomosc >nul')
    def wyslij(self, wiadomosc):
        f = open(self._tekst, 'wb')
        f.write(wiadomosc)
        f.close()
    def wejsciowy(self):
        return StrumienWejsciowy(IP)
    def eksport(self):
        return self._port

class StrumienWejsciowy:
    def __init__(self, ip, port=_SpRepr('PORT')):
        self._ip = ip
        if port == 'PORT':
            self._port = PORT
        else:
            self._port = port
    def odczytaj(self):
        url = f'http://{self._ip}:{self._port}/wiadomosc'
        f = _urllib2.urlopen(url)
        dane = f.read()
        return dane
    def __repr__(self):
        return f'StrumienWejsciowy({repr(self._ip)})'
