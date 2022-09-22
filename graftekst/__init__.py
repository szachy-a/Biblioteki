class _Brakujacy:
    def __getattr__(self, attr):
        raise ModuleNotFoundError('Nie ma takiej opcji')

try:
    from . import tekst
except ModuleNotFoundError:
    tekst = _Brakujacy()
try:
    from . import grafika
except ModuleNotFoundError:
    grafika = _Brakujacy()
