import random
from pathlib import Path


class Hangman:
    """Ein Hangman-Spiel mit Texteingabe und Turtle- oder ASCII-Galgen."""

    def __init__(self, wort=None, max_falsche=6, galgen="turtle"):
        """Darstellung und maximale Anzahl falscher Versuche festlegen."""
        if galgen not in ("turtle", "ascii"):
            raise ValueError('galgen muss "turtle" oder "ascii" sein.')
        if (
            not isinstance(max_falsche, int)
            or isinstance(max_falsche, bool)
            or max_falsche < 1
        ):
            raise ValueError("max_falsche muss eine positive ganze Zahl sein.")
        if wort is None:
            wort = self.waehle_zufaelliges_wort()
        if not isinstance(wort, str) or not wort.strip().isalpha():
            raise ValueError("Das Wort muss aus mindestens einem Buchstaben bestehen.")
        self.wort = wort.strip().upper()
        self.max_falsche = max_falsche
        self.galgen = galgen
        self.erraten = False
        self.falsche = 0
        self.geratene_buchstaben = ""
        self.stift = None

    def waehle_zufaelliges_wort(self):
        # Die Wortliste liegt neben dieser Datei, unabhängig vom Arbeitsverzeichnis.
        pfad = Path(__file__).with_name("helvetismen_ascii.txt")
        with pfad.open(encoding="utf-8") as datei:
            woerter = datei.read().splitlines()
        return random.choice(woerter)

    def wort_anzeigen(self):
        # Bereits geratene Buchstaben anzeigen, die übrigen durch Unterstriche ersetzen.
        angezeigtes_wort = ""
        for buchstabe in self.wort:
            if buchstabe in self.geratene_buchstaben:
                angezeigtes_wort += buchstabe
            else:
                angezeigtes_wort += "_"
        return angezeigtes_wort

    def galgen_ascii(self, station):
        ascii = [
            """
     +---+
     |   |
         |
         |
         |
         |
    =========""",
            """
     +---+
     |   |
     O   |
         |
         |
         |
    =========""",
            """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========""",
            """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========""",
            """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========""",
            """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========""",
            """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========""",
        ]
        print(ascii[station])

    def galgen_turtle(self, station):
        radius = 8
        torso = 35
        arm = 0.85 * torso
        bein = 1.05 * torso

        if station == 0:
            self.stift.hideturtle()
            self.stift.pensize(3)
            # Den 160 Einheiten hohen Galgen vertikal um die Fenstermitte platzieren.
            self.stift.penup()
            self.stift.goto(0, -80)
            self.stift.setheading(0)
            self.stift.pendown()
            self.stift.forward(100)
            self.stift.back(50)
            self.stift.left(90)
            self.stift.forward(160)
            self.stift.left(90)
            self.stift.forward(50)
            self.stift.left(90)
            self.stift.forward(20)
        if station == 1:
            self.stift.penup()
            self.stift.forward(2 * radius)
            self.stift.left(90)
            self.stift.pendown()
            self.stift.circle(radius)
        if station == 2:
            self.stift.right(90)
            self.stift.forward(torso)
        if station == 3:
            self.stift.back(torso)
            self.stift.right(25)
            self.stift.forward(arm)
        if station == 4:
            self.stift.back(arm)
            self.stift.left(50)
            self.stift.forward(arm)
        if station == 5:
            self.stift.back(arm)
            self.stift.right(25)
            self.stift.forward(torso)
            self.stift.right(25)
            self.stift.forward(bein)
        if station == 6:
            self.stift.back(bein)
            self.stift.left(50)
            self.stift.forward(bein)

    def spielen(self):
        # Jeder Aufruf startet eine neue Runde mit dem Wort dieser Instanz.
        self.erraten = False
        self.falsche = 0
        self.geratene_buchstaben = ""
        if self.galgen == "turtle":
            # ASCII funktioniert auch ohne installierte Tk-Grafikunterstützung.
            from turtle import Turtle

            if self.stift is None:
                self.stift = Turtle()
            else:
                self.stift.reset()

        print("Lass uns Hangman spielen!")
        print("Aktuell gefundene Buchstaben:", self.wort_anzeigen())
        if self.galgen == "turtle":
            self.galgen_turtle(0)
        else:
            self.galgen_ascii(0)

        while (not self.erraten) and (self.falsche < self.max_falsche):
            buchstabe = input("Bitte gib einen Buchstaben ein:\n").strip().upper()
            if len(buchstabe) != 1 or not buchstabe.isalpha():
                print("Bitte gib genau einen Buchstaben ein.")
                continue
            if buchstabe in self.geratene_buchstaben:
                print("Den Buchstaben", buchstabe, "hast du schon ausprobiert.")
            elif buchstabe not in self.wort:
                print(buchstabe, "ist nicht im Wort enthalten.")
                # Die sechs Zeichenstufen auf die erlaubten Fehlversuche verteilen.
                vorherige_station = self.falsche * 6 // self.max_falsche
                self.falsche += 1
                self.geratene_buchstaben += buchstabe
                station = self.falsche * 6 // self.max_falsche
                if self.galgen == "turtle":
                    # Turtle muss jede neue Stufe der Reihe nach zeichnen.
                    for neue_station in range(vorherige_station + 1, station + 1):
                        self.galgen_turtle(neue_station)
                else:
                    self.galgen_ascii(station)
            else:
                print("Gut gemacht,", buchstabe, "ist im Wort enthalten.")
                self.geratene_buchstaben += buchstabe

                # Ohne Lücken "_" ist das Wort vollständig erraten.
                if "_" not in self.wort_anzeigen():
                    self.erraten = True

            print(self.wort_anzeigen())

        if self.erraten:
            print("Toll, du hast das Wort erraten!")
        else:
            print(
                "Sorry, du hast alle deine Leben aufgebraucht. Das gesuchte Wort war:",
                self.wort,
            )


if __name__ == "__main__":
    spiel = Hangman(galgen="turtle", max_falsche=6)
    spiel.spielen()