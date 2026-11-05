
def wort_anzeigen(loesungwort, erratene_buchstaben):
    # baue die Ausgabe Buchstabe für Buchstabe auf
    # beginne mit dem leeren String
    anzeige = ""

    for buchstabe in loesungwort:
        if buchstabe in erratene_buchstaben:
            # dieser Buchstabe wurde schon erraten
            anzeige += buchstabe 
        else:
            # noch nicht erraten: setze Platzhalter
            anzeige += "_"

    print(anzeige)

wort_anzeigen("KROKODIL", "KL")