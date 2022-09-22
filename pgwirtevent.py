import pickle
import socket

ms = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss = None

def config(serwer:bool):
    global ss
    if serwer:
        ms.bind((socket.gethostname(), 28775))
        ms.listen()
        ss, _ = server.accept()
    else:
        pass
