import pygame as pg


class Player:
    """Spielfigur, die mit den Pfeiltasten bewegt wird."""

    def __init__(self, x, y):
        self.rect = pg.Rect(x, y, 50, 50)
        self.speed = 5

    def update(self, keys):
        """Bewegt die Figur gemaess den gedrueckten Tasten."""
        if keys[pg.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pg.K_RIGHT]:
            self.rect.x += self.speed

    def draw(self, screen):
        pg.draw.rect(screen, (0, 150, 255), self.rect)
