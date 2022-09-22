import sys

_uzyte = [sys.modules[x] for x in sys.modules.keys() if x.startswith('emulowanySprzet.kartaGraficzna')]
_ile = 0
for _n in _uzyte:
    if '_' not in _n:
        _ile += 1
        if _ile > 1:
            raise Exception('Za dużo emulowanych kart graficznych')
