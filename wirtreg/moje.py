import wirtreg.wirtReg as w

_abcdsKonstruktor = '''%sx = w.Bit32(_64, w.%s)

%sh = w.Bit16(%sx, w.WAZNIEJSZY)
%sl = w.Bit16(%sx, w.MNIEJ_WAZNY)

%shh = w.Bit8(%sh, w.WAZNIEJSZY)
%shl = w.Bit8(%sh, w.MNIEJ_WAZNY)

%slh = w.Bit8(%sl, w.WAZNIEJSZY)
%sll = w.Bit8(%sl, w.MNIEJ_WAZNY)'''

_64 = w.Bit64()
exec(_abcdsKonstruktor % (('a', 'MNIEJ_WAZNY') + 12 * ('a',)))
exec(_abcdsKonstruktor % (('b', 'WAZNIEJSZY') + 12 * ('b',)))
_64 = w.Bit64()
exec(_abcdsKonstruktor % (('c', 'MNIEJ_WAZNY') + 12 * ('c',)))
exec(_abcdsKonstruktor % (('d', 'WAZNIEJSZY') + 12 * ('d',)))
_64 = w.Bit64()
exec(_abcdsKonstruktor % (('s', 'MNIEJ_WAZNY') + 12 * ('s',)))
del _abcdsKonstruktor

_32 = w.Bit32(_64, w.WAZNIEJSZY)

_flags = w.Bit16(_32, w.MNIEJ_WAZNY)
_16 = w.Bit16(_32, w.WAZNIEJSZY)
_8 = w.Bit8(_16, w.MNIEJ_WAZNY)

uf = w.Bit1(_8, 0)

del _8
del _16
del _32
del _64

_flagsKonstruktor = '''%sf = w.Bit8(_flags, %s)
%s0 = w.Bit1(%sf, 0)
%s1 = w.Bit1(%sf, 1)
%s2 = w.Bit1(%sf, 2)
%s3 = w.Bit1(%sf, 3)
%s4 = w.Bit1(%sf, 4)
%s5 = w.Bit1(%sf, 5)
%s6 = w.Bit1(%sf, 6)
%s7 = w.Bit1(%sf, 7)'''

exec(_flagsKonstruktor % (('a', 'w.WAZNIEJSZY') + (16 * ('a',))))
exec(_flagsKonstruktor % (('b', 'w.MNIEJ_WAZNY') + (16 * ('b',))))
del _flagsKonstruktor
del _flags

# wolne rejestry:
# - 1 pod "_8" pozycje 1 - 7
# - 8 pod "_16" pozycja "WAZNIEJSZY"

_64 = w.Bit64()
sp = w.Bit32(_64, w.MNIEJ_WAZNY)
ss = w.Bit32(_64, w.WAZNIEJSZY)

_64 = w.Bit64()
ms = w.Bit32(_64, w.MNIEJ_WAZNY)
ip = w.Bit32(_64, w.WAZNIEJSZY)

del _64

del w
