import random
from pathlib import Path


class Hangman:
    """Ein Hangman-Spiel mit Texteingabe und Turtle- oder ASCII-Galgen."""

    def __init__(self, wort=None, galgen="turtle"):
        """Wort und Darstellung für ein Spiel mit sechs Fehlversuchen festlegen."""
        if wort is None:
            wort = self.waehle_zufaelliges_wort()
        self.wort = wort.strip().upper()
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
        elif station == 1:
            self.stift.penup()
            self.stift.forward(2 * radius)
            self.stift.left(90)
            self.stift.pendown()
            self.stift.circle(radius)
        elif station == 2:
            self.stift.right(90)
            self.stift.forward(torso)
        elif station == 3:
            self.stift.back(torso)
            self.stift.right(25)
            self.stift.forward(arm)
        elif station == 4:
            self.stift.back(arm)
            self.stift.left(50)
            self.stift.forward(arm)
        elif station == 5:
            self.stift.back(arm)
            self.stift.right(25)
            self.stift.forward(torso)
            self.stift.right(25)
            self.stift.forward(bein)
        elif station == 6:
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

        # Anfänglicher ("leeren") Galgen anzeigen (station 0).
        if self.galgen == "turtle":
            self.galgen_turtle(0)
        else:
            self.galgen_ascii(0)

        while (not self.erraten) and (self.falsche < 6):
            buchstabe = input("Bitte gib einen Buchstaben ein:\n").strip().upper()
            if buchstabe in self.geratene_buchstaben:
                print("Den Buchstaben", buchstabe, "hast du schon ausprobiert.")
            elif buchstabe not in self.wort:
                print(buchstabe, "ist nicht im Wort enthalten.")
                self.falsche += 1
                self.geratene_buchstaben += buchstabe

                # Rufe die galgen-Funktion nur nach einem falschen Versuch erneut auf.
                if self.galgen == "turtle":
                    self.galgen_turtle(self.falsche)
                else:
                    self.galgen_ascii(self.falsche)
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
            if self.galgen == "turtle":
                print("Klicke ins Turtle-Fenster, um es zu schliessen.")
                self.stift.getscreen().exitonclick()
                self.stift = None


if __name__ == "__main__":
    spiel = Hangman(galgen="turtle")
    spiel.spielen()
