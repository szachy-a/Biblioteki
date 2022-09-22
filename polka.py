import pickle as _pickle

print('Witamy w półce wersji 1.0!')

PRZOD = '<-'
TYL = '->'

class Polka:
    def __init__(self, plik='D:/biblioteki/polka.polka'):
        self._nazwa = plik
    def odloz(self, co, koniec=TYL):
        wszystko = self.wszystko()
        if koniec == TYL:
            wszystko = wszystko + [co]
        elif koniec == PRZOD:
            wszystko = [co] + wszystko
        f = open(self._nazwa, 'wb')
        _pickle.dump(wszystko, f)
        f.close()
    def zabierz(self, koniec):
        wszystko = self.wszystko()
        if koniec == TYL:
            ret = wszystko.pop(-1)
        elif koniec == PRZOD:
            ret = wszystko.pop(0)
        else:
            raise TypeError(f'koniec {koniec} nie jest PRZOD ani TYL')
        f = open(self._nazwa, 'wb')
        _pickle.dump(wszystko, f)
        f.close()
        return ret
    def wszystko(self):
        f = open(self._nazwa, 'rb')
        dane = _pickle.load(f)
        f.close()
        return dane
