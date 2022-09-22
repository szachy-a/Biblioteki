class _____Nic_____:
    def __init__(self):
        self._____modul_____ = 'Drzewa binarne'
        self._____isNic_____ = True

class _Goto(Exception):
    pass

class Drzewo:
    def __init__(self, zawartosc, lewo=_____Nic_____(), prawo=_____Nic_____(), wyzej=_____Nic_____()):
        self.zawartosc = zawartosc
        self.lewo = lewo
        self.prawo = prawo
        self.wyzej = wyzej

    def wartosc(self, zawartosc=_____Nic_____(), lewo=_____Nic_____(), prawo=_____Nic_____(), wyzej=_____Nic_____()):
        ret = {}
        try:
            try:
                if lewo._____modul_____ == 'Drzewa binarne' and lewo._____isNic_____:
                    ret['lewo'] = self.lewo
                    raise _Goto
            except AttributeError:
                pass
            self.lewo = lewo
            raise _Goto
        except _Goto:
            pass
        
        try:
            try:
                if prawo._____modul_____ == 'Drzewa binarne' and prawo._____isNic_____:
                    ret['prawo'] = self.prawo
                    raise _Goto
            except AttributeError:
                pass
            self.prawo = prawo
            raise _Goto
        except _Goto:
            pass
        
        try:
            try:
                if zawartosc._____modul_____ == 'Drzewa binarne' and zawartosc._____isNic_____:
                    ret['zawartosc'] = self.zawartosc
                    raise _Goto
            except AttributeError:
                pass
            self.zawartosc = zawartosc
            raise _Goto
        except _Goto:
            pass

        try:
            try:
                if zawartosc._____modul_____ == 'Drzewa binarne' and zawartosc._____isNic_____:
                    ret['wyzej'] = self.wyzej
                    raise _Goto
            except AttributeError:
                pass
            self.wyzej = wyzej
            raise _Goto
        except _Goto:
            pass
        
        if len(ret) == 4:
            return ret
