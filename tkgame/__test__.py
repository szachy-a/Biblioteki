import tkgame
from tkgame.locals import (
    KEYDOWN,
    K_a
)
tkgame.init()

screen = tkgame.display.set_mode((800, 600))

running = True
while running:
    for event in tkgame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_a:
                running = False
    screen.fill((255, 255, 255))
    tkgame.display.flip()
tkgame.quit()
