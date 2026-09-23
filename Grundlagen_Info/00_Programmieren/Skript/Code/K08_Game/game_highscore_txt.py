import pygame as pg
import random

pg.init()
WIDTH, HEIGHT = 800, 600
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Pong mit Highscore")
clock = pg.time.Clock()
font = pg.font.Font(None, 36)

# Schläger und Ball
paddle_w, paddle_h = 15, 100
left_paddle = pg.Rect(30, HEIGHT // 2 - paddle_h // 2, paddle_w, paddle_h)
right_paddle = pg.Rect(
    WIDTH - 30 - paddle_w, HEIGHT // 2 - paddle_h // 2, paddle_w, paddle_h
)
ball = pg.Rect(WIDTH // 2 - 10, HEIGHT // 2 - 10, 20, 20)

paddle_speed = 6
ball_speed_x = 5
ball_speed_y = 5

left_score = 0
right_score = 0

# 1. Highscore beim Start aus Datei laden
with open("highscore.txt", "r") as file:
    highscore = int(file.read())

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Schläger steuern
    keys = pg.key.get_pressed()
    if keys[pg.K_w] and left_paddle.top > 0:
        left_paddle.y -= paddle_speed
    if keys[pg.K_s] and left_paddle.bottom < HEIGHT:
        left_paddle.y += paddle_speed
    if keys[pg.K_UP] and right_paddle.top > 0:
        right_paddle.y -= paddle_speed
    if keys[pg.K_DOWN] and right_paddle.bottom < HEIGHT:
        right_paddle.y += paddle_speed

    # Ball bewegen
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Abprallen an oberem/unterem Rand
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    # Abprallen an Schlägern
    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_speed_x *= -1

    # Punkte zählen und Ball zurücksetzen
    if ball.left <= 0:
        right_score += 1
        ball.center = (WIDTH // 2, HEIGHT // 2)
        ball_speed_x = 5
    elif ball.right >= WIDTH:
        left_score += 1
        ball.center = (WIDTH // 2, HEIGHT // 2)
        ball_speed_x = -5

    # 2. Highscore prüfen und bei neuem Rekord direkt in Datei speichern
    current_max = max(left_score, right_score)
    if current_max > highscore:
        highscore = current_max
        with open("highscore.txt", "w") as file:
            file.write(str(highscore))

    # Zeichnen
    screen.fill((30, 30, 40))
    pg.draw.rect(screen, (255, 255, 255), left_paddle)
    pg.draw.rect(screen, (255, 255, 255), right_paddle)
    pg.draw.ellipse(screen, (255, 255, 255), ball)
    pg.draw.aaline(
        screen, (100, 100, 100), (WIDTH // 2, 0), (WIDTH // 2, HEIGHT)
    )

    # 3. Spielstand und Highscore anzeigen
    score_surf = font.render(
        f"{left_score} : {right_score}", True, (255, 255, 255)
    )
    highscore_surf = font.render(
        f"Highscore: {highscore}", True, (200, 200, 100)
    )
    screen.blit(score_surf, (WIDTH // 2 - score_surf.get_width() // 2, 20))
    screen.blit(
        highscore_surf, (WIDTH // 2 - highscore_surf.get_width() // 2, 60)
    )

    pg.display.flip()
    clock.tick(60)

pg.quit()
