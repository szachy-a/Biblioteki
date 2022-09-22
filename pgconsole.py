from pygame import (
    QUIT,
    KEYDOWN,
    K_BACKSPACE,
    K_RETURN
)

import trybTekstowy as tt

import sys
import io

_KOLORY = {'tekst':{
    30:(0, 0, 0), 31:(255, 0, 0), 32:(0, 255, 0), 33:(255, 255, 0),
    34:(0, 0, 255), 35:(128, 0, 255), 36:(0, 255, 255), 37:(255, 255, 255),
    39:(0, 0, 0)}}
_KOLORY['tlo'] = dict(map(lambda x: (x[0] + 10, x[1]), _KOLORY['tekst'].items()))

_screen = tt.Screen(0, 0, True, komendy=tt.UKRYJMYSZ)

class _Out(io.TextIOBase):
    def __init__(self):
        self.__tekst = ''
        self.__ansi = ''
        self.kolor = [(255, 255, 255), (0, 0, 0)]
    def write(self, tekst):
        for c in tekst:
            if c == '\b':
                _screen.cputs('\b', self.kolor[0], self.kolor[1], True)
            elif c == '\r':
                _screen.pos = [0, _screen.pos[1]]
            elif c == '\033':
                self.__ansi = '\033'
            elif self.__ansi:
                if c == 'm':
                    if c[1] != '[':
                        _reset()
                        raise RuntimeError('Nieznana sekwencja ansi')
                    try:
                        n = int(c[2:])
                    except ValueError:
                        _reset()
                        raise RuntimeError('Nieznana sekwencja ansi')
                    if n in _KOLORY['tekst']:
                        self.kolor[0] = _KOLORY['tekst'][n]
                    elif n in _KOLORY['tlo']:
                        self.kolor[1] = _KOLORY['tlo'][n]
                    elif n == 0:
                        self.kolor = [(255, 255, 255), (0, 0, 0)]
                    else:
                        _reset()
                        raise RuntimeError('Nieznana sekwencja ansi')
                else:
                    self.__ansi += c
            else:
              _screen.cputs(c, self.kolor[0], self.kolor[1], True)
        _upd()
    def read(self, num=-1):
        raise io.UnsupportedOperation
    def readline(self, num=-1):
        raise io.UnsupportedOperation
    def detach(self):
        raise io.UnsupportedOperation
    def _readAll(self):
        return self.__tekst

class _In(io.TextIOBase):
    def __init__(self):
        self.__tekst = ''
    def write(self, tekst):
        raise io.UnsupportedOperation
    def read(self, num=-1):
        if num == -1:
            num = None
        ret = self.__tekst[:num]
        self.__tekst = self.__tekst[num:]
        return ret
    def readline(self, num=-1):
        s = ''
        while (c := self.read(1)) != '\n' and c:
            s += c
        s += '\n'
        return s
    def detach(self):
        raise io.UnsupportedOperation
    def _writeIn(self, tekst):
        self.__tekst += tekst

sys.stdout = _Out()
sys.stdin = _In()

_tekst = ''
def _upd():
    global _tekst
    running = True
    for event in tt.eventy():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_BACKSPACE:
                try:
                    stdin._writeIn(stdin.read()[:-1])
                except IndexError:
                    pass
                sys.stdout.write('\b \b')
            elif event.key == K_RETURN:
                sys.stdin._writeIn(_tekst)
                _tekst = ''
                sys.stdout.write('\n')
            else:
                if event.unicode.isalpha():
                    _tekst += event.unicode
                    sys.stdout.write(event.unicode)
    _screen.flip()
    if not running:
        _reset()
        raise SystemExit

def _reset():
    global _upd
    pygame.quit()
    sys.stdout = sys.__stdout__
    sys.stdin = sys.__stdin__
    _upd = lambda: None
