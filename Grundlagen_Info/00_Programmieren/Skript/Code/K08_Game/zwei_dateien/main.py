import pygame as pg
from player import Player  # Klasse Player aus der Datei player.py

pg.init()
screen = pg.display.set_mode((800, 600))
clock = pg.time.Clock()
player = Player(375, 500)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    player.update(pg.key.get_pressed())
    screen.fill((255, 255, 255))
    player.draw(screen)
    pg.display.flip()
    clock.tick(60)

pg.quit()
