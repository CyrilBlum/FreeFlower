import math
import turtle as t

# blauer Teil (Dreieck unten links, Diagonale von oben links nach unten rechts)
t.fillcolor((0, 112 / 255, 180 / 255))
t.begin_fill()
t.rt(90)
t.fd(100)
t.lt(90)
t.fd(100)
t.lt(135)
t.fd(math.sqrt(2 * 100**2))
t.end_fill()

# weisser Teil (Rand oben und rechts)
t.rt(135)
t.fd(100)
t.rt(90)
t.fd(100)

# Fertig
t.done()
