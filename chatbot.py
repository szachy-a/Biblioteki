import io
import os
import sys
import contextlib
import threading
import collections
import flask
import logging
import time

import __main__

_f = open('C:/Dodatkowe/botSmall.png', 'rb')
_BOT = _f.read()
_f.close()
_f = open('C:/Dodatkowe/userSmall.png', 'rb')
_USER = _f.read()
_f.close()

_lock = threading.Lock()
_flushed = False
_allLines = []

class In(io.IOBase):
    def __init__(self):
        self._lines = collections.deque()
    def readable(self):
        return True
    def writable(self):
        return False
    def readline(self, num=-1):
        global _flushed
        while not self._lines:
            pass
        with _lock:
            if num == -1:
                return self._lines.popleft()
            else:
                l = self._lines.popleft()
                r = l[:num]
                n = l[num:]
                if n:
                    self._lines.appendleft(n)
                return r
            _flushed = False
    def read(self, num=-1):
        raise io.UnsupportedOperation('read')
    def readlines(self, num=-1):
        raise io.UnsupportedOperation('readlines')
    def seek(self, pos, od):
        raise io.UnsupportedOperation('seek')
    def isatty(self):
        return True

class Out(io.IOBase):
    def __init__(self):
        self._tag = 'p'
    def readable(self):
        return False
    def writable(self):
        return True
    def write(self, s):
        if s == '\n':
            return
        def _ctoh(c):
            if c == '<':
                return '&lt'
            elif c == '>':
                return '&gt'
            elif c == '&':
                return '&amp'
            elif c == '"':
                return '&quot'
            else:
                return c
        ws = f'<{self._tag}>'
        it = iter(s)
        for c in it:
            if c == '\033':
                c = next(it)
                if c == 's':
                    c = next(it)
                    if c == 's':
                        ws += f'</{self._tag}>'
                        ws += '<pre>'
                        self._tag = 'pre'
                    elif c == 'z':
                        ws += f'</{self._tag}>'
                        ws += '<pre>'
                        self._tag = 'pre'
                    else:
                        ws += '\033s' + _ctoh(c)
                else:
                    ws += '\033' + _ctoh(c)
            else:
                ws += _ctoh(c)
        ws += f'</{self._tag}>'
        _allLines.append((_BOT, ws))
        return len(s)
    def flush(self):
        global _flushed
        _flushed = True
    def isatty(self):
        return True

_out = Out()
_in = In()

def _runWebApp(port):
    app = flask.Flask('chatbot')

    @app.route('/')
    def stronaGlowna():
        while not _flushed:
            pass
        html = '''<html>
<head>
    <meta charset="utf-8">
    <title>chatbot</title>
    <style src="style.css"></style>
<body>
'''
        with _lock:
            for elem in _allLines:
                if elem[0] is _BOT:
                    html += '<img src="bot.png">'
                elif elem[0] is _USER:
                    html += '<img src="user.png">'
                html += elem[1]
                html += '<br><br>'
        html += '''<form action="send">
    <input type="text" id="msg" name="msg">
    <input type="submit" value="Wyślij">
</body>
</html>'''
        return html

    @app.route('/send')
    def wyslij():
        msg = flask.request.args.get('msg')
        _in._lines.append(msg)
        _allLines.append((_USER, msg))
        return flask.redirect('/')

    @app.route('/bot.png')
    def botPng():
        return _BOT

    @app.route('/user.png')
    def userPng():
        return _USER

    app.run(port=port)

@contextlib.contextmanager
def withRedirectIO():
    stdout = sys.stdout
    stdin = sys.stdin
    sys.stdout = _out
    sys.stdin = _in
    try:
        yield
    finally:
        sys.stdout = stdout
        sys.stdin = stdin

def start(port):
    stdout = sys.stdout
    sys.stdout = io.StringIO()
    logging.getLogger('werkzeug').setLevel(logging.ERROR)
    threading.Thread(None, _runWebApp, args=(port,)).start()
    time.sleep(1)
    sys.stdout = stdout
