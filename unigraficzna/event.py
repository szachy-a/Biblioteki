import __init__ as _unigraficzna

_POBIERACZ_DANYCH = _unigraficzna.stale._Stala()

_tryb = None
def tryb(tryb=None):
    _zbindowane = {}
    
    def _pobierz():
        for event in _unigraficzna._pygame.event.get():
            yield _unigraficzna.Event(type=event.type, **event.dict)

    def _aktualizuj():
        for event in _pobierz():
            if event in _zbindowane:
                _zbindowane[event.type](event)

    def _binduj(event, funkcja):
        _zbindowane[event] = funkcja

    def _rzucacz(*args, **kwargs):
        raise NameError('Niedostępne w tym trybie')
    
    global pobierz
    global aktualizuj
    global binduj
    global _tryb
    if tryb == _unigraficzna.stale.SAMODZIELNA_KOLEJKA:
        _tryb = tryb
        pobierz = _pobierz
        aktualizuj = _rzucacz
        _binduj = _rzucacz
    elif tryb == _unigraficzna.stale.BINDOWANE:
        _tryb = tryb
        pobierz = _rzucacz
        aktualizuj = _aktualizuj
        binduj = _binduj
    elif tryb == None:
        if tryb != None:
            return _tryb
        else:
            raise _unigraficzna.Error('Nie ustawiono trybu')
    elif tryb == _POBIERACZ_DANYCH:
        return {'pobierz':_pobierz, 'aktualizuj':_aktualizuj, 'binduj':_binduj, 'rzucacz':_rzucacz}
    else:
        raise _unigraficzna.Error(f'Nieprawidłowy tryb {repr(tryb)}')

pobierz = aktualizuj = binduj = tryb(_POBIERACZ_DANYCH)['rzucacz']
del _POBIERACZ_DANYCH
