import colorama

_init = colorama.init
def init(autoreset=False, convert=None, strip=None, wrap=True):
    _init(autoreset, None, strip, wrap)
colorama.init = init
del init

for _attr in ['BLACK', 'BLUE', 'CYAN', 'GREEN', 'LIGHTBLACK_EX', 'LIGHTBLUE_EX', 'LIGHTCYAN_EX', 'LIGHTGREEN_EX', 'LIGHTMAGENTA_EX', 'LIGHTRED_EX', 'LIGHTWHITE_EX', 'LIGHTYELLOW_EX', 'MAGENTA', 'RED', 'RESET', 'WHITE', 'YELLOW']:
    if hasattr(colorama.Fore, _attr):
        setattr(colorama.Fore, _attr, '')
    if hasattr(colorama.Back, _attr):
        setattr(colorama.Back, _attr, '')

for _attr in ['BRIGHT', 'DIM', 'NORMAL', 'RESET_ALL']:
    setattr(colorama.Style, _attr, '')

del _attr
