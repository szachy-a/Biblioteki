import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen()

def wyborOpcji(opcje, pytanie='Wybierz opcję'):
    s2, _ = s.accept()
    html = '\n'.join(['HTTP/1.1 200 OK', 'Content-Type: text/html; charset=UTF-8',
                       'Content-Encoding: UTF-8', 'Accept-Ranges: bytes',
                       'Connection: keep-alive']) + '\n\n'
    html += f'''<html>
<head>
    <meta charset="utf-8">
    <title>{pytanie}</title>
</head>
<body>
{pytanie}<br>
'''
    for opcja in opcje:
        html += f'<button onclick="location.href=\'{opcja}\'">{opcja}</button><br>\n'
    html += '''</body>
</html>'''
    s2.send(html.encode())
    s2.close()
    s2, _ = s.accept()
    tekst = s2.recv(1024)[5:].split(' ', 2)[0]
    s2.close()
    return tekst
