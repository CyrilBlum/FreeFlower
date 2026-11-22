import turtle as t


def farb_vieleck(ecken, farbe, breite):
    t.color(farbe)
    t.width(breite)
    for _ in range(ecken):
        t.fd(50)
        t.rt(360 / ecken)


farb_vieleck(3, "red", 1)
farb_vieleck(6, "green", 5)
farb_vieleck(4, "blue", 10)

t.done()
