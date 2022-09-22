import socket
import base64

def infSend(s, string):
    s.send(base64.a85encode(string) + b'\0')

def infRecv(s):
    r = b''
    while (b := s.recv(1024))[-1] != b'\0':
        r += b
    return r
