import random
import pygame as pg

pg.init()
WIDTH = 800
HEIGHT = 600
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Sprites und Sprite-Gruppen")
clock = pg.time.Clock()


class Spieler(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Grafik fuer den Spieler (Rechteck/Surface)
        self.image = pg.Surface((40, 40))
        self.image.fill((0, 150, 255))
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.speed = 5

    def update(self):
        # Steuerung ueber Pfeiltasten
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pg.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pg.K_UP]:
            self.rect.y -= self.speed
        if keys[pg.K_DOWN]:
            self.rect.y += self.speed
        # Im Fenster halten
        self.rect.clamp_ip(screen.get_rect())


class Muenze(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # Grafik fuer die Muenze
        self.image = pg.Surface((24, 24), pg.SRCALPHA)
        pg.draw.circle(self.image, (255, 215, 0), (12, 12), 12)
        self.rect = self.image.get_rect(center=(x, y))


# Sprite-Gruppen erstellen
spieler = Spieler()
spieler_gruppe = pg.sprite.GroupSingle(spieler)

muenzen_gruppe = pg.sprite.Group()
for _ in range(15):
    x = random.randint(30, WIDTH - 30)
    y = random.randint(30, HEIGHT - 30)
    muenzen_gruppe.add(Muenze(x, y))

font = pg.font.Font(None, 36)
score = 0
running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # 1. Update: Alle Sprites in Gruppen aktualisieren
    spieler_gruppe.update()

    # 2. Kollisionspruefung:
    # dokill=True entfernt getroffene Muenzen automatisch aus muenzen_gruppe
    getroffene_muenzen = pg.sprite.spritecollide(spieler, muenzen_gruppe, True)
    if getroffene_muenzen:
        score += len(getroffene_muenzen)

    # 3. Render (Zeichnen)
    screen.fill((30, 30, 40))

    # Alle Sprites der Gruppen mit nur einem Befehl zeichnen
    muenzen_gruppe.draw(screen)
    spieler_gruppe.draw(screen)

    # Score anzeigen
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pg.display.flip()
    clock.tick(60)

pg.quit()
