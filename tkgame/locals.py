KEYUP = 1
KEYDOWN = 2

RLEACCEL = 3

for i in range(ord('A'), ord('Z') + 1):
    exec(f'''global K_{chr(i)}
K_{chr(i)} = {i}
K_{chr(i).lower()} = {ord(chr(i).lower())}''')
del i

K_UP = 127
K_DOWN = 128
K_LEFT = 129
K_RIGHT = 130
K_ESCAPE = 131
K_SPACE = 132
QUIT = 133
