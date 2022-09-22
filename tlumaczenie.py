import builtins # do zamiany help
import weakref # do zamiany help
import json

class BladTlumaczenia(LookupError):
    '''Błąd tłumaczenia'''

class Tlumaczenie:
    '''Wczytuje tłumaczenie wyjścia dla użytkownika z pliku json o budowie {"oryginalny tekst 1":"tłumaczenie 1", "oryginalny tekst 2":"tłumaczenie 2", ...}'''
    def __init__(self, plikLubSlownik):
        if isinstance(plikLubSlownik, dict):
            self.__tlumaczenie = plikLubSlownik.copy()
        else:
            f = open(plikLubSlownik, encoding='utf-8')
            self.__tlumaczenie = json.load(f)
            f.close()
    def tlumacz(self, wyrazenie):
        try:
            return self.__tlumaczenie[wyrazenie]
        except KeyError:
            raise BladTlumaczenia(f'Nie znaleziono tłumaczenia dla podanego wyrażenia {wyrazenie!r}') from None
    def __repr__(self):
        return f'{self.__class__.__name__}({self.__tlumaczenie!r})'
