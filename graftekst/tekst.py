_RAMKI = '╔╗╚╝║═╠╣╦╩╬'
_POTWIERDZENIA = 'XV'

def wyborOpcji(opcje, pytanie='Wybierz opcję'):
    def _pasuje(wybor, maxopcja):
        try:
            if 1 <= int(wybor) <= maxopcja:
                return True
        except ValueError:
            pass
        return False
    
    maxlen = max(map(len, opcje))
    print(_RAMKI[0] + 3 * _RAMKI[5] + _RAMKI[8] + maxlen * _RAMKI[5] + _RAMKI[1])
    for i, opcja in enumerate(opcje, 1):
        print(_RAMKI[4] + '%2d' % i + '.' + _RAMKI[4] + opcja.ljust(maxlen) + _RAMKI[4])
        if i < len(opcje):
            print(_RAMKI[6] + 3 * _RAMKI[5] + _RAMKI[10] + maxlen * _RAMKI[5] + _RAMKI[7])
    print(_RAMKI[2] + 3 * _RAMKI[5] + _RAMKI[9] + maxlen * _RAMKI[5] + _RAMKI[3])
    wybor = input(pytanie + ': ')
    while not _pasuje(wybor, len(opcje)):
        wybor = input(pytanie + ': ')
    return opcje[int(wybor) - 1]

def wieloWybor(opcje, pytanie='Wybierz opcję'):
    def _pasuje(wybor, maxopcja):
        if wybor == 'koniec':
            return True
        try:
            return 1 <= int(wybor) <= maxopcja
        except ValueError:
            return False
    
    maxlen = max(map(len, opcje))
    czy = len(opcje) * [False]
    while True:
        print(_RAMKI[0] + _RAMKI[5] + _RAMKI[8] + 3 * _RAMKI[5] + _RAMKI[8] + maxlen * _RAMKI[5] + _RAMKI[1])
        for i, opcja in enumerate(opcje, 1):
            print(_RAMKI[4] + _POTWIERDZENIA[int(czy[i - 1])] + _RAMKI[4] + '%2d' % (i) + '.' + _RAMKI[4] + opcja.ljust(maxlen) + _RAMKI[4])
            if i < len(opcje):
                print(_RAMKI[6] + _RAMKI[5] + _RAMKI[10] + 3 * _RAMKI[5] + _RAMKI[10] + maxlen * _RAMKI[5] + _RAMKI[7])
        print(_RAMKI[2] + _RAMKI[5] + _RAMKI[9] + 3 * _RAMKI[5] + _RAMKI[9] + maxlen * _RAMKI[5] + _RAMKI[3])
        wybor = input(pytanie + ': ')
        while not _pasuje(wybor, len(opcje)):
            wybor = input(pytanie + ': ')
        if wybor == 'koniec':
            break
        else:
            czy[int(wybor) - 1] = not czy[int(wybor) - 1]
    return list(map(lambda x: x[0], filter(lambda x: x[1], zip(opcje, czy))))
