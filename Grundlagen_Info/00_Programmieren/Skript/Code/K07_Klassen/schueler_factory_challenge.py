class Schueler:
    anzahl_schueler = 0  # Klassenattribut

    def __init__(self, name, alter):
        self.name = name
        self.alter = alter
        Schueler.anzahl_schueler += 1

    # Alternative Konstruktor-Methode: Erstellt Schueler aus Geburtsjahr
    @classmethod
    def aus_geburtsjahr(cls, name, geburtsjahr):
        alter = 2026 - geburtsjahr
        return cls(name, alter)

    # Alternative Konstruktor-Methode: Erstellt Schueler aus CSV-Zeile "Name;Alter"
    @classmethod
    def aus_csv_zeile(cls, csv_zeile):
        name, alter_str = csv_zeile.split(";")
        return cls(name, int(alter_str))

    def info(self):
        print(f"Schüler/in {self.name}, {self.alter} Jahre alt")


# Normaler Aufruf über __init__
s1 = Schueler("Anna", 16)

# Erzeugung via Alternative Konstruktoren (@classmethod)
s2 = Schueler.aus_geburtsjahr("Ben", 2009)
s3 = Schueler.aus_csv_zeile("Clara;17")

s1.info()
s2.info()
s3.info()
print(f"Total erstellte Schüler: {Schueler.anzahl_schueler}")
