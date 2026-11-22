import random
import pygame as pg

pg.init()
WIDTH = 800
HEIGHT = 600
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Muenzen sammeln, Hindernissen ausweichen")
clock = pg.time.Clock()

STRAFPUNKTE = 3  # Abzug pro getroffenes Hindernis


class Spieler(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
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
        self.image = pg.Surface((24, 24), pg.SRCALPHA)
        pg.draw.circle(self.image, (255, 215, 0), (12, 12), 12)
        self.rect = self.image.get_rect(center=(x, y))


class Hindernis(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((30, 30))
        self.image.fill((220, 40, 40))
        self.rect = self.image.get_rect()
        self.neu_platzieren()

    def neu_platzieren(self):
        # zufaellige Position oberhalb des Fensters, zufaellige Geschwindigkeit
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.bottom = random.randint(-300, 0)
        self.speed = random.randint(2, 5)

    def update(self):
        # nach unten fallen, unten angekommen wieder oben starten
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.neu_platzieren()


# Sprite-Gruppen erstellen
spieler = Spieler()
spieler_gruppe = pg.sprite.GroupSingle(spieler)

muenzen_gruppe = pg.sprite.Group()
for _ in range(15):
    x = random.randint(30, WIDTH - 30)
    y = random.randint(30, HEIGHT - 30)
    muenzen_gruppe.add(Muenze(x, y))

hindernis_gruppe = pg.sprite.Group()
for _ in range(5):
    hindernis_gruppe.add(Hindernis())

font = pg.font.Font(None, 36)
score = 0
running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # 1. Update: Spieler und Hindernisse bewegen
    if len(muenzen_gruppe) > 0:
        spieler_gruppe.update()
        hindernis_gruppe.update()

    # 2. Kollisionspruefung
    getroffene_muenzen = pg.sprite.spritecollide(spieler, muenzen_gruppe, True)
    score += len(getroffene_muenzen)

    # Hindernisse ziehen Punkte ab und starten danach wieder oben
    getroffene_hindernisse = pg.sprite.spritecollide(spieler, hindernis_gruppe, False)
    for hindernis in getroffene_hindernisse:
        score -= STRAFPUNKTE
        hindernis.neu_platzieren()

    # 3. Render (Zeichnen)
    screen.fill((30, 30, 40))
    muenzen_gruppe.draw(screen)
    hindernis_gruppe.draw(screen)
    spieler_gruppe.draw(screen)

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Spielende, sobald alle Muenzen eingesammelt sind
    if len(muenzen_gruppe) == 0:
        ende_text = font.render("Alle Muenzen gesammelt!", True, (255, 215, 0))
        screen.blit(ende_text, ende_text.get_rect(center=(WIDTH // 2, HEIGHT // 2)))

    pg.display.flip()
    clock.tick(60)

pg.quit()
