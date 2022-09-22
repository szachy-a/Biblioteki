import pygame
pygame.init()

import pygameWidzety

screen = pygame.display.set_mode((800, 600))

running = True
b = pygameWidzety.Button(screen, text='Przycisk', command=lambda: print('Klik'))
b.place(0, 0)
l = pygameWidzety.Label(screen, text='Tekst')
l.place(300, 300)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 255, 0))
    pygame.display.flip()
pygame.quit()
