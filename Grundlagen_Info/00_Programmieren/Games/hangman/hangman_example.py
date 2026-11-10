def wort_anzeigen(loesungswort, erratene_buchstaben):

    # baue die Anzeige Buchstabe für Buchstabe auf, sodass
    # nur die bereits erratenen Buchstaben als solche
    # angezeigt werden (sonst Platzhalter: _)
    anzeige_wort = ""

    for buchstabe in loesungswort:
        if buchstabe in erratene_buchstaben:
            anzeige_wort += buchstabe
        else:
            anzeige_wort += "_"

    return anzeige_wort


def spiel():
    ...
    ...

    # Game-Loop
    while True:
        # Frage den Spieler nach Input

        wort_anzeigen(...)

        break