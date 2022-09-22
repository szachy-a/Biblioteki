from flask import Flask, request, redirect

import sys
import time

from strumienie import *

app = Flask(__name__)

@app.route('/')
def stronaGlowna():
    s = StrumienWejsciowy(sys.argv[1], sys.argv[2])
    dane = s.odczytaj()
    return f'''<html>
<body>
{dane}
<form action="wyslij">
  <input type="text" id="wiad" name="wiad">
  <input type="submit" value="Wyślij">
</body>
</html>'''

@app.route('/wyslij')
def wyslij():
    s = StrumienWyjsciowy(sys.argv[3], sys.argv[4])
    s.wyslij(request.args.get('wiad'))
    time.sleep(1)
    return redirect('/')

if sys.argv[1] == '--help':
    print('''Hostuje czat na podanym porcie. Argumenty:
host "kod 1 strumienia z ostatnią częścią rozmowy" "kod 2 strumienia z ostatnią częścią rozmowy" "kod 1 strumienia do wysłania odpowiedzi" "kod 2 strumienia do wysłania odpowiedzi" "port do hostowania"
''')
    raise SystemExit
app.run(port=int(sys.argv[5]))
