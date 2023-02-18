import sys
import win32.win32gui as win32gui
import win32.win32api as win32api
import win32.lib.win32con as win32con

sys.modules['win32gui'] = win32gui
sys.modules['win32con'] = win32con
sys.modules['win32api'] = win32api

del sys
del win32gui
del win32con
