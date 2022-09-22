PRAWO = '\0'

class Menu:
    def __init__(self):
        self.nazwa = None
        self.altkey = None
        self.skrot = None
        self.elems = []
    def __repr__(self):
        return f'Menu o nazwie {self.nazwa}, altkey {self.altkey} i skrócie {self.skrot}. Elementy:\n' + '\n'.join(map(repr, self.elems)) + '\nKoniec elementów'

class _HackMenu:
    def __init__(self, l, menus):
        self._l = l # dwa podkreśllenia nie działają
        self._menus = menus # -||-
    def __setattr__(self, nazwa, wartosc):
        if nazwa[0] == '_':
            object.__setattr__(self, nazwa, wartosc)
            return
        del self._menus[-1]
        self._l.append(Menu())
        self._menus.append(self._l[-1])
        setattr(self._l[-1], nazwa, wartosc)
        self._menus.append(self)
            

def odczytaj(tekst):
    tekst = ''.join(tekst.split('\n'))
    it = iter(tekst)
    menus = []
    try:
        while True:
            c = next(it)
            if c == '<': # to jest tag
                tag = '<' + _do('>', it) + '>'
                if tag == '<menu>':
                    menus.append(Menu())
                    addmenus = menus[-1].elems
                elif tag == '<name>':
                    nazwa = _do('</name>', it) # odczytaj całą nazwę
                    itn = iter(nazwa)
                    nazwa = ''
                    try:
                        while True:
                            c = next(itn)
                            if c == '<':
                                tag = '<' + _do('>', itn) + '>'
                                if tag == '<altkey>':
                                    altkey = _do('</altkey>', itn)
                                    menus[-1].altkey = altkey
                                    nazwa += altkey
                                elif tag == '<skrot>':
                                    skrot = _do('</skrot>', itn)
                                    menus[-1].skrot = skrot
                                    nazwa += PRAWO + skrot
                                else:
                                    raise SyntaxError('Nieznany tag')
                    except StopIteration:
                        pass
                    menus[-1].nazwa = nazwa
                elif tag == '<content>':
                    menus.append(_HackMenu(menus[-1].elems, menus))
    except StopIteration:
        pass
    return menus[0]

                                

def _do(tag, it):
    tekst = ''
    while tag not in tekst:
        tekst += next(it)
    return tekst.split(tag)[0] # [1] == ''
