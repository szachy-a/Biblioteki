import pip as _pip
_pip.main(['install', 'forbiddenfruit'])

import sys as _sys
import forbiddenfruit as _ff
from functools import wraps as _wraps
import weakref as _weakref
import builtins as _builtins

class _EmptyRepr:
    def __repr__(self):
        return ''
_EMPTY_REPR = _EmptyRepr()

class _Opakowanie:
    def __init__(self, elem):
        self.elem = elem
    def __repr__(self):
        return f'_Opakowanie({self.elem!r})'
    def __hash__(self):
        try:
            return hash(self.elem)
        except TypeError:
            return 0
    def __eq__(self, other):
        return type(self) is type(other) and self.elem == other.elem

class from_:
    def __init__(self, it):
        self._it = iter(it)

def return_(retVal=None):
    raise StopIteration(retVal)

class _GetArgs0:
    def __get__(self, instance, _):
        if instance is None:
            return self
        else:
            return instance.args[0]

_buf = {}
@_wraps(next)
def next(it, default=_EMPTY_REPR):
    orgIt = it
    try:
        while True:
            new = _buf[_Opakowanie(it)]
            prawieIt = it
            it = new
    except KeyError:
        pass
    try:
        elem = it.__next__()
        if type(elem) is from_:
            _buf[_Opakowanie(it)] = elem._it
            return next(it, default)
        return elem
    except StopIteration:
        if orgIt is not it:
            del _buf[_Opakowanie(prawieIt)]
            try:
                return next(orgIt, default)
            except StopIteration:
                pass
            raise
        if default is _EMPTY_REPR:
            raise
        else:
            return default

if _sys.version_info[:2] < (3, 3):
    _ff.curse(StopIteration, 'value', _GetArgs0)

_builtins.next = next
