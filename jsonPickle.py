def toJsonTypes(v):
    if type(v) in [list, tuple, set, frozenset, memoryview]:
        return ['builtins', type(v).__name__, list(map(toJsonTypes, v))]
    elif type(v) == dict:
        return ['builtins', type(v).__name__, [[toJsonTypes(k), toJsonTypes(v)] for k, v in v.items()]]
    elif type(v) in [int, float, bool, type(None), str]:
        return ['builtins', type(v).__name__, v]
    elif type(v) in [bytes, bytearray]:
        return ['builtins', type(v).__name__, bytes(v).decode('cp852')]
    elif type(v) == type:
        return ['builtins', type(v).__name__, [v.__module__, v.__qualname__
    elif isinstance(v, BaseException):
        return ['builtins', type(v).__name__, toJsonTypes(v.__dict__)]
    elif type(v) == type(lambda: None):
        return ['
