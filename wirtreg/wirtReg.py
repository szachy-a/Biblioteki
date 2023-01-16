class _Repr:
    def __init__(self, r):
        self.__r = r
    def __repr__(self):
        return self.__r

WAZNIEJSZY = _Repr('WAZNIEJSZY')
MNIEJ_WAZNY = _Repr('MNIEJ_WAZNY')

LONGLONG_MAX = 0xFFFFFFFFFFFFFFFF
LONG_MAX = 0xFFFFFFFF
SHORT_MAX = 0xFFFF
BYTE_MAX = 0xFF

LONG_BITS = 32
SHORT_BITS = 16
BYTE_BITS = 8

class _Reg:
    def __repr__(self):
        import wirtreg.moje
        for name, value in vars(wirtreg.moje).items():
            if value is self:
                return '<' + name + '>'
        return super().__repr__()

class Bit64(_Reg):
    def __init__(self):
        self.__v = 0
    def get(self):
        return self.__v & LONGLONG_MAX
    def set(self, v):
        self.__v = (v & LONGLONG_MAX)

class Bit32(_Reg):
    def __init__(self, bit64, waznosc):
        self.__bit64 = bit64
        self.waznosc = waznosc
    def get(self):
        if self.waznosc == MNIEJ_WAZNY:
            return self.__bit64.get() & LONG_MAX
        elif self.waznosc == WAZNIEJSZY:
            return (self.__bit64.get() >> LONG_BITS) & LONG_MAX
        else:
            raise Exception('Nieprawidłowa ważność')
    def set(self, v):
        if self.waznosc == MNIEJ_WAZNY:
            orgedit = self.__bit64.get() & (LONG_MAX << LONG_BITS)
            orgedit |= v
            self.__bit64.set(orgedit)
        elif self.waznosc == WAZNIEJSZY:
            orgedit = self.__bit64.get() & LONG_MAX
            orgedit |= (v << LONG_BITS)
            self.__bit64.set(orgedit)
        else:
            raise Exception('Nieprawidłowa ważność')

class Bit16(_Reg):
    def __init__(self, bit32, waznosc):
        self.__bit32 = bit32
        self.waznosc = waznosc
    def get(self):
        if self.waznosc == MNIEJ_WAZNY:
            return self.__bit32.get() & SHORT_MAX
        elif self.waznosc == WAZNIEJSZY:
            return (self.__bit32.get() >> SHORT_BITS) & SHORT_MAX
        else:
            raise Exception('Nieprawidłowa ważność')
    def set(self, v):
        if self.waznosc == MNIEJ_WAZNY:
            orgedit = self.__bit32.get() & (SHORT_MAX << SHORT_BITS)
            orgedit |= v
            self.__bit32.set(orgedit)
        elif self.waznosc == WAZNIEJSZY:
            orgedit = self.__bit32.get() & SHORT_MAX
            orgedit |= (v << SHORT_BITS)
            self.__bit32.set(orgedit)
        else:
            raise Exception('Nieprawidłowa ważność')

class Bit8(_Reg):
    def __init__(self, bit16, waznosc):
        self.__bit16 = bit16
        self.waznosc = waznosc
    def get(self):
        if self.waznosc == MNIEJ_WAZNY:
            return self.__bit16.get() & BYTE_MAX
        elif self.waznosc == WAZNIEJSZY:
            return (self.__bit16.get() >> BYTE_BITS) & BYTE_MAX
        else:
            raise Exception('Nieprawidłowa ważność')
    def set(self, v):
        if self.waznosc == MNIEJ_WAZNY:
            orgedit = self.__bit16.get() & (BYTE_MAX << BYTE_BITS)
            orgedit |= v
            self.__bit16.set(orgedit)
        elif self.waznosc == WAZNIEJSZY:
            orgedit = self.__bit16.get() & BYTE_MAX
            orgedit |= (v << BYTE_BITS)
            self.__bit16.set(orgedit)
        else:
            raise Exception('Nieprawidłowa ważność')

class Bit1(_Reg):
    def __init__(self, bit8, waznosc):
        self.__bit8 = bit8
        self.waznosc = waznosc
    def get(self):
        return (self.__bit8.get() >> self.waznosc) & 1
    def set(self, v):
        self.__bit8.set(self.__bit8.get() & (~(1 << self.waznosc)))
        self.__bit8.set(self.__bit8.get() | (int(bool(v)) << self.waznosc))
