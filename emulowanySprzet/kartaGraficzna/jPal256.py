import _check
import _impl
import threading as _threading

def _run():
    while True:
        update(tablica, paleta)
        ograniczenieFPS(60)

_impl.config((800, 600), False, 255, 255, 255)
tablica = [[0] * 800 for _ in range(600)]
paleta = _impl.Paleta(256)
_threading.Thread(None, _run, ()).start()
