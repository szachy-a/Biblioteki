from wirtreg import wirtReg as w

_64 = w.Bit64()

_32l = _32 = w.Bit32(_64, w.MNIEJ_WAZNY)
_32h = w.Bit32(_64, w.WAZNIEJSZY)

_16l = _16 = w.Bit16(_32, w.MNIEJ_WAZNY)
_16h = w.Bit16(_32, w.WAZNIEJSZY)

_8l = w.Bit8(_16, w.MNIEJ_WAZNY)
_8h = w.Bit8(_16, w.WAZNIEJSZY)

def from64to32(v):
    _64.set(v)
    return {'l':_32l.get(), 'h':_32h.get()}

def from32to64(*, l, h):
    _32l.set(l)
    _32h.set(h)
    return _64.get()

def from32to16(v):
    _32.set(v)
    return {'l':_16l.get(), 'h':_16h.get()}

def from16to32(*, l, h):
    _16l.set(l)
    _16h.set(h)
    return _32.get()

def from16to8(v):
    _16.set(v)
    return {'l':_8l.get(), 'h':_8h.get()}

def from8to16(*, l, h):
    _8l.set(l)
    _8h.set(h)
    return _16.get()

def littleOrder(v):
    return (v['l'], v['h'])

def bigOrder(v):
    return (v['h'], v['l'])
