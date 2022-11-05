import forbiddenfruit
import functools

import __main__

class _ModuleMeta(type):
    

_orgSetattr = type(__main__).__setattr__
@functools.wraps(_orgSetattr)
def _newSetattr(obj, name, v):
    if name.isupper():
        raise TypeError('Can\'t set const')
    return _orgSetattr(obj, name, v)
#forbiddenfruit.curse(type(__main__), '__setattr__', _newSetattr)
type(__main__).__setattr__ = _newSetattr
