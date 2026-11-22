"""
Dieses Programm wandelt Dezimalzahlen in Binärzahlen um.
Die eingegebene Dezimalzahl muss kleiner als 1024 sein.
"""

# Die folgende Dezimalzahl soll umgewandelt werden
zahl = 892

# Beginnen mit der grössten Basisgrösse
# In diesem Programm ist es  2^9 = 512
basisgroesse = 2**9

# Berechnung der 10 Ziffern der Binärzahl
for _ in range(10):
    # Ziffer: Wie häufig passt die Basisgrösse in den Betrag?
    ziffer = zahl // basisgroesse
    print(ziffer, "ist die ", basisgroesse, "er Ziffer")

    #  Welche Zahl muss durch die weiteren Basisgrössen abgedeckt werden?
    zahl -= ziffer * basisgroesse

    # Basisgrösse wird auf die nächst kleinere Basisgrösse gesetzt.
    basisgroesse //= 2
