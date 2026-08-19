class Auto:
    anzahl_autos = 0  # Klassenattribut

    def __init__(self, marke, modell, baujahr):
        self.marke = marke
        self.modell = modell
        self.baujahr = baujahr
        Auto.anzahl_autos += 1

    def info(self):
        print(f"{self.marke} {self.modell} ({self.baujahr})")


# Autos erstellen
auto_1 = Auto("VW", "Golf", 2018)
auto_2 = Auto("Tesla", "Model 3", 2021)
auto_3 = Auto("BMW", "X5", 2019)

# Infos ausgeben
auto_1.info()
auto_2.info()
auto_3.info()
print(f"Anzahl Autos insgesamt: {Auto.anzahl_autos}")
