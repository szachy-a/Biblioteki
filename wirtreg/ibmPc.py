import wirtreg.wirtReg as w

_abcdKonstruktor = '''e%sx = w.Bit32(_64, w.%s)

%sx = w.Bit16(e%sx, w.MNIEJ_WAZNY)

%sh = w.Bit8(%sx, w.WAZNIEJSZY)
%sl = w.Bit8(%sx, w.MNIEJ_WAZNY)'''

_64 = w.Bit64()
exec(_abcdKonstruktor % (('a', 'MNIEJ_WAZNY') + 6 * ('a',)))
exec(_abcdKonstruktor % (('b', 'WAZNIEJSZY') + 6 * ('b',)))
_64 = w.Bit64()
exec(_abcdKonstruktor % (('c', 'MNIEJ_WAZNY') + 6 * ('c',)))
exec(_abcdKonstruktor % (('d', 'WAZNIEJSZY') + 6 * ('d',)))
del _abcdKonstruktor

_64 = w.Bit64()
_32 = w.Bit32(_64, w.MNIEJ_WAZNY)

si = w.Bit16(_32, w.WAZNIEJSZY)
di = w.Bit16(_32, w.MNIEJ_WAZNY)

_32 = w.Bit32(_64, w.WAZNIEJSZY)

bp = w.Bit16(_32, w.WAZNIEJSZY)
sp = w.Bit16(_32, w.MNIEJ_WAZNY)

del _32
del _64

del w
