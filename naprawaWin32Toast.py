import sys
import win32.win32api

sys.modules['win32api'] = win32.win32api
del sys
del win32
