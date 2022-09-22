import wirtreg.wirtReg as w

_abcdKonstruktor = '''%s = w.Bit32(_64, w.%s)

%sh = w.Bit16(%s, w.WAZNIEJSZY)
%sl = w.Bit16(%s, w.MNIEJ_WAZNY)

%shh = w.Bit8(%sh, w.WAZNIEJSZY)
%shl = w.Bit8(%sh, w.MNIEJ_WAZNY)

%slh = w.Bit8(%sl, w.WAZNIEJSZY)
%sll = w.Bit8(%sl, w.MNIEJ_WAZNY)'''

_64 = w.Bit64()
exec(_abcdKonstruktor % (('a', 'MNIEJ_WAZNY') + 12 * ('a',)))
exec(_abcdKonstruktor % (('b', 'WAZNIEJSZY') + 12 * ('b',)))
_64 = w.Bit64()
exec(_abcdKonstruktor % (('c', 'MNIEJ_WAZNY') + 12 * ('c',)))
exec(_abcdKonstruktor % (('d', 'WAZNIEJSZY') + 12 * ('d',)))
del _abcdKonstruktor

_64 = w.Bit64()
_32 = w.Bit32(_64, w.MNIEJ_WAZNY)

_flags = w.Bit16(_32, w.MNIEJ_WAZNY)
del _32
del _64

_flagsKonstruktor = '''%sflags = w.Bit8(_flags, %s)
%s1 = w.Bit1(%sflags, 0)
%s2 = w.Bit1(%sflags, 1)
%s3 = w.Bit1(%sflags, 2)
%s4 = w.Bit1(%sflags, 3)
%s5 = w.Bit1(%sflags, 4)
%s6 = w.Bit1(%sflags, 5)
%s7 = w.Bit1(%sflags, 6)
%s8 = w.Bit1(%sflags, 7)'''

exec(_flagsKonstruktor % (('a', 'w.WAZNIEJSZY') + (16 * ('a',))))
exec(_flagsKonstruktor % (('b', 'w.MNIEJ_WAZNY') + (16 * ('b',))))
del _flagsKonstruktor
del _flags

# wolne rejestry:
# - 16 pod "_32" pozycja "WAZNIEJSZY"
# - 32 pod "_64" pozycja "WAZNIEJSZY"

del w
