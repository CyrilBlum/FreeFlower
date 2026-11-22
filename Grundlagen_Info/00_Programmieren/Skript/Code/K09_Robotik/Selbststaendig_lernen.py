from mbrobot import *
from microbit import *

# Roboter Umgebung für den Simulator
# im Realmodus auskommentieren
RobotContext.useBackground("sprites/learntrack1.gif")
RobotContext.setStartPosition(385, 490)


TURNTIME_90 = 550  # muss kalibriert werden


def keepOnTrack():
    if vL == 0 and vR == 0:
        forward()
    elif vL == 0 and vR == 1:
        leftArc(0.1)
    elif vL == 1 and vR == 0:
        rightArc(0.1)


def turnLeft():
    left()
    delay(TURNTIME_90)


def turnRight():
    right()
    delay(TURNTIME_90)


memory = []
setSpeed(30)
# learning: selbststaendig durch Versuch und Irrtum
# beenden mit Taste A
lastTurnTime = running_time()
while not button_a.was_pressed():
    vR = irRight.read_digital()
    vL = irLeft.read_digital()
    keepOnTrack()
    if vL == 1 and vR == 1:
        stop()
        if running_time() - lastTurnTime > 1500:
            # letzte Entscheidung war richtig: neue Kreuzung, links versuchen
            turnLeft()
            memory.append(0)
            forward()
        elif memory != []:
            # Spur zu schnell verlassen: letzte Linksdrehung war falsch
            memory.pop()
            memory.append(1)
            right()
            delay(2 * TURNTIME_90)
            forward()
        print(memory)
        lastTurnTime = running_time()

# Neustart im Simulatormodus
# Im Realmodus ersetzen durch die Zeilen darunter
stop()
print("Mit dem Hand-Symbol den Roboter an den Anfang ziehen")
print("Achten Sie darauf, dass er nach oben schaut")
print("Wenn Sie soweit sind, können Sie mit der Taste B weitermachen")
while not button_b.was_pressed():
    pass


# Neustart im Realmodus:
# Roboter an den Anfang setzen
# wenn bereit, Taste b drücken
# stop()
# while not button_b.was_pressed():
#    pass


n = 0
# running
while True:
    vR = irRight.read_digital()
    vL = irLeft.read_digital()
    keepOnTrack()
    if vL == 1 and vR == 1:
        stop()
        if len(memory) == n:
            break
        if memory[n] == 0:
            turnLeft()
        else:
            turnRight()
        n += 1
stop()
