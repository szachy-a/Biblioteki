from kontrolaImportu import locals as _locals, display as _display
import queue as _queue
from functools import partial as _partial

class Event:
    def __init__(self, type, **kwargs):
        self.type = type
        for k, w in zip(kwargs.keys(), kwargs.values()):
            exec(f'self.{k} = w')

_eventy = _queue.Queue()
for i in filter(lambda x: x.startswith('K_'), dir(_locals)):
    if len(i) == 3:
        klawisz = i.split('K_')[1]
    elif i in ['K_UP', 'K_DOWN', 'K_LEFT', 'K_RIGHT']:
        klawisz = i.split('K_')[1].lower() + 'arrow'
    elif i == 'K_SPACE':
        klawisz = 'space'
    else:
        dane = i.split('K_')[1].lower()
        klawisz = dane[0].upper() + dane[1:]
    _display._tk.bind_all(f'<KeyPress-{klawisz}>', _partial(lambda x, y: _eventy.put(Event(_locals.KEYDOWN, key=eval(f'_locals.{x}'))), i))
del i

def get():
    while not _eventy.empty():
        yield _eventy.get()
