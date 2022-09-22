import os
import sys
import io

from strumienie import StrumienWyjsciowy as _StrumienWyjsciowy, StrumienWejsciowy as _StrumienWejsciowy

_KODY = [_StrumienWyjsciowy().eksport(), _StrumienWyjsciowy().eksport()]

class _Wejscie(io.StringIO):
    def __init__(self, kody):
        super(_Wejscie, self).__init__()
        self.__kody = kody
        s = _StrumienWejsciowy(*self.__kody)
        s.odczytaj()
        self.__zapas = []
    def write(self, tekst):
        raise Exception
    def read(self, num=-1):
        s = _StrumienWejsciowy(*self.__kody)
        print(s.dostepny(), file=sys.stderr)
        dane = s.odczytaj()
        super(_Wejscie, self).write(dane)
        return super(_Wejscie, self).read(num)

class _Wyjscie(io.StringIO):
    def __init__(self, kody):
        super(_Wyjscie, self).__init__()
        self.__kody = kody
        s = _StrumienWyjsciowy(*self.__kody)
        s.wyslij('')
    def write(self, tekst):
        s = _StrumienWejsciowy(*self.__kody)
        dane = s.odczytaj()
        s = _StrumienWyjsciowy(*self.__kody)
        s.wyslij(dane + '\n' + tekst)
    def read(self, num=-1):
        raise Exception

def przekieruj():
    os.system('start C:/Dodatkowe/host.py ' + ' '.join(_KODY[0] + _KODY[1]) + ' 16980')
    sys.stdin = _Wejscie(_KODY[1])
    sys.stdout = _Wyjscie(_KODY[0])
