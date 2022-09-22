import json

def dumps(obj):
    return json.dumps(toJsonTypes(obj))

def toJsonTypes(obj):
    if type(obj) in [list, tuple, set, frozenset]:
        return [type(obj).__name__, [toJsonTypes(obj) for obj in obj]]
    elif type(obj) is dict:
        return [type(obj).__name__, [[toJsonTypes(k), toJsonTypes(v)] for k, v in obj.items()]]
    elif type(obj) is bytes:
        return [type(obj).__name__, obj.decode('852')]
    elif type(obj) in [int, float, str, bool, type(None)]:
        return [type(obj).__name__, obj]
    elif isinstance(type(obj), type):
        return [type(obj).__name__, [obj.__module__, obj.__qualname__]]
    else:
        return ['object', [toJsonTypes(obj.__dict__)]]
