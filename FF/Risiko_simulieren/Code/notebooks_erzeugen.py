"""Erzeugt die Kurs-Notebooks (Schülerversion und Lösung) aus einer gemeinsamen Quelle.

In Code-Zellen steht die Lösung zwischen «#L» und «#E». Die Schülerversion ersetzt sie durch
Platzhalter. Aufruf: python notebooks_erzeugen.py [--test]
--test führt alle Lösungen aus und prüft die Selbstkontrollen.
"""
import json
import re
import sys
from pathlib import Path

ZIEL = Path(__file__).resolve().parent.parent / "Notebooks"

KOPF = """import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(2027)


def pruefe(name, wert, soll, toleranz):
    \"\"\"Selbstkontrolle: vergleicht Ihren Wert mit dem erwarteten Bereich.\"\"\"
    if wert is None:
        print(f"{name}: noch nicht bearbeitet")
    elif abs(wert - soll) <= toleranz:
        print(f"{name}: passt ({wert:.4g})")
    else:
        print(f"{name}: prüfen Sie Ihren Code, erwartet wird etwa {soll:.4g}, Sie haben {wert:.4g}")
"""

NB = {}


def nb(name, titel, frage, *zellen):
    NB[name] = (titel, frage, zellen)


m = lambda t: ("m", t)
c = lambda t: ("c", t)

nb("01_Zufall", "Zufall simulieren",
   "Ein Casino verliert an rund jedem dritten Abend gegen eine Person, die stur auf Rot setzt. Weshalb gehört es trotzdem nie dem Pech?",
   m("## Aufgabe 1: Roulette an einem Abend\nEine Person setzt 100-mal je 1 CHF auf Rot (18 von 37 Feldern). Simulieren Sie 200'000 Abende. Speichern Sie in `gewinn` den Gewinn jedes Abends.\n\n*Hilfestellung:* `rng.binomial(100, p, size=n)` liefert die Anzahl Treffer. Gewinn = Treffer minus Fehlschläge."),
   c("n = 200_000\ngewinn = None\n#L\ngewinn = 2 * rng.binomial(100, 18 / 37, size=n) - 100\n#E\nanteil_plus = None if gewinn is None else np.mean(gewinn > 0)\npruefe('Anteil Abende im Plus', anteil_plus, 0.355, 0.01)"),
   m("## Aufgabe 2: Verteilung ansehen\nZeichnen Sie ein Histogramm von `gewinn` und markieren Sie den Durchschnitt mit `plt.axvline`."),
   c("#L\nplt.hist(gewinn, bins=40)\nplt.axvline(gewinn.mean(), color='red')\nplt.xlabel('Gewinn in CHF')\nplt.show()\n#E"),
   m("## Aufgabe 3: Das Casino zieht Bilanz\nAn einem Abend spielen 500 Personen dieses Programm. Simulieren Sie 10'000 Abende und bestimmen Sie den Anteil Abende, an denen das Casino insgesamt Geld verliert.\n\n*Hilfestellung:* Summe von 500 Abenden = 50'000 Spiele. Sie können direkt `rng.binomial(50_000, p, size=...)` verwenden."),
   c("verlust_casino = None\n#L\nverlust_casino = np.mean(2 * rng.binomial(50_000, 18 / 37, size=10_000) - 50_000 > 0)\n#E\npruefe('Anteil Verlustabende Casino', verlust_casino, 0.0, 0.005)"),
   m("## Challenge: Wie viele Simulationen braucht es?\nWie viele Würfelwürfe brauchen Sie, damit der Durchschnitt mit 95 % Sicherheit höchstens 0.01 von 3.5 abweicht?\n\n*Hilfestellung:* Der Standardfehler ist $\\sigma/\\sqrt{n}$, die 95-%-Grenze liegt bei 1.96 Standardfehlern. Für einen Würfel gilt $\\sigma^2 = 35/12$."),
   c("n_noetig = None\n#L\nn_noetig = (1.96 * np.sqrt(35 / 12) / 0.01) ** 2\n#E\npruefe('Anzahl Würfe', n_noetig, 112_047, 500)"))

nb("02_Anlageformen", "Anlageformen",
   "Was genau besitzen Sie, wenn Ihr Geld «auf der Bank» liegt?",
   m("## Aufgabe 1: Der Steckbrief\nWählen Sie zu zweit eine Anlageform und halten Sie unten fest: Was besitzt man rechtlich? Woher kommt der Ertrag? Wer verliert zuerst, wenn es schiefgeht? Quellen sind das Skript und die Internetseiten der Anbieter."),
   m("*Ihr Steckbrief:*"),
   m("## Aufgabe 2: Zinseszins\nBerechnen Sie, was aus 1000 CHF in 30 Jahren bei 7 % wird."),
   c("endwert = None\n#L\nendwert = 1000 * 1.07 ** 30\n#E\npruefe('Endwert', endwert, 7612, 1)"),
   m("## Aufgabe 3: Rendite und Volatilität aus Daten\nDie Liste enthält Jahresendkurse einer erfundenen Aktie. Berechnen Sie die Jahresrenditen, deren Durchschnitt und Standardabweichung.\n\n*Hilfestellung:* `np.diff(kurs) / kurs[:-1]`"),
   c("kurs = np.array([100, 112, 104, 131, 118, 142, 136, 160])\nrendite = None\n#L\nrendite = np.diff(kurs) / kurs[:-1]\n#E\nmittel = None if rendite is None else rendite.mean()\nvola = None if rendite is None else rendite.std(ddof=1)\npruefe('Mittlere Rendite', mittel, 0.0781, 0.001)\npruefe('Volatilität', vola, 0.1463, 0.002)"),
   m("## Aufgabe 4: Teuerung\nAuf dem Sparkonto gibt es 0.5 %, die Teuerung beträgt 1.5 %. Wie viel Kaufkraft bleibt von 1000 CHF nach 30 Jahren?"),
   c("kaufkraft = None\n#L\nkaufkraft = 1000 * (1.005 / 1.015) ** 30\n#E\npruefe('Kaufkraft', kaufkraft, 742.8, 1)"))

nb("03_30_Jahre", "30 Jahre in die Zukunft",
   "Zwei Personen sparen 40 Jahre lang genau gleich viel in genau denselben Fonds. Im Modell hat die eine am Ende rund zwölfmal so viel wie die andere. War sie klüger?",
   m("## Aufgabe 1: Viele Verläufe\nSimulieren Sie 100'000 Verläufe über 30 Jahre: Wachstum 6 %, Volatilität 16 %, Start 1000 CHF.\n\n*Hilfestellung:* `rng.normal(0.06, 0.16, size=(pfade, jahre))` erzeugt die Renditen. Summieren Sie pro Zeile und wenden Sie `np.exp` an."),
   c("pfade, jahre = 100_000, 30\nvermoegen = None\n#L\nr = rng.normal(0.06, 0.16, size=(pfade, jahre))\nvermoegen = 1000 * np.exp(r.sum(axis=1))\n#E\nmedian = None if vermoegen is None else np.median(vermoegen)\npruefe('Median', median, 6050, 120)"),
   m("## Aufgabe 2: Wie schlecht kann es laufen?\nBestimmen Sie das 5-%-Perzentil und den Anteil Verläufe unter 1000 CHF."),
   c("p5 = verlust = None\n#L\np5 = np.percentile(vermoegen, 5)\nverlust = np.mean(vermoegen < 1000)\n#E\npruefe('5-%-Perzentil', p5, 1430, 60)\npruefe('Verlustanteil', verlust, 0.02, 0.004)"),
   m("## Challenge: Mittelwert gegen Median\nBerechnen Sie den Mittelwert und erklären Sie, weshalb rund zwei Drittel aller Personen unter dem Durchschnitt liegen.\n\n*Hilfestellung:* Für eine Lognormalverteilung gilt $E[X] = e^{\\mu + \\sigma^2/2}$, hier mit $\\mu = 30 \\cdot 0.06$ und $\\sigma^2 = 30 \\cdot 0.16^2$."),
   c("anteil_unter = None\n#L\nanteil_unter = np.mean(vermoegen < vermoegen.mean())\n#E\npruefe('Anteil unter dem Durchschnitt', anteil_unter, 0.669, 0.01)"),
   m("## Challenge: Sparplan oder alles auf einmal?\nSie haben 12'000 CHF. Entweder legen Sie alles sofort an oder monatlich 100 CHF während 10 Jahren. Monatliches Wachstum 0.06/12, Monatsvolatilität $0.16/\\sqrt{12}$. Wie oft gewinnt die Einmalanlage?\n\n*Hilfestellung:* Die Rate im Monat $t$ wächst nur über die verbleibenden Monate. `np.cumsum(r[:, ::-1], axis=1)[:, ::-1]` liefert diese Restsummen."),
   c("sieg_einmal = None\n#L\nr = rng.normal(0.06 / 12, 0.16 / np.sqrt(12), size=(100_000, 120))\neinmal = 12_000 * np.exp(r.sum(axis=1))\nplan = 100 * np.exp(np.cumsum(r[:, ::-1], axis=1)[:, ::-1]).sum(axis=1)\nsieg_einmal = np.mean(einmal > plan)\n#E\npruefe('Einmalanlage gewinnt', sieg_einmal, 0.836, 0.01)"))

nb("04_Durchschnitt", "Der Durchschnitt täuscht",
   "In diesem Spiel wird der Durchschnitt aller Teilnehmenden in jeder Runde reicher. Weshalb sollten Sie trotzdem nicht mitspielen?",
   m("## Aufgabe 1: Das Spiel\nStart 100 CHF, pro Runde +50 % oder −40 %, 20 Runden, 200'000 Personen. Bestimmen Sie Mittelwert, Median und den Anteil der Personen mit Verlust."),
   c("ende = None\n#L\nende = 100 * rng.choice([1.5, 0.6], size=(200_000, 20)).prod(axis=1)\n#E\nmed = None if ende is None else np.median(ende)\nanteil = None if ende is None else np.mean(ende < 100)\npruefe('Median', med, 34.87, 0.01)\npruefe('Verlustanteil', anteil, 0.749, 0.01)"),
   m("## Aufgabe 2: Teil des Vermögens einsetzen\nSie setzen pro Runde nur den Anteil $f$ ein. Berechnen Sie die typische Wachstumsrate $g(f) = \\sqrt{(1+0.5f)(1-0.4f)} - 1$ für viele $f$ und zeichnen Sie die Kurve. Wo liegt das Maximum, und ab welchem $f$ schrumpft das Vermögen?"),
   c("f = np.linspace(0, 1, 10_001)\nbestes_f = None\n#L\ng = np.sqrt((1 + 0.5 * f) * (1 - 0.4 * f)) - 1\nbestes_f = f[g.argmax()]\nplt.plot(f, g)\nplt.axhline(0, color='gray')\nplt.show()\n#E\npruefe('Bestes f', bestes_f, 0.25, 0.001)"),
   m("## Aufgabe 3: Rente aus dem Vermögen\n100'000 CHF, zu Beginn jedes Jahres 12'000 CHF entnehmen. Berechnen Sie das Endvermögen für beide Reihenfolgen. Ein negativer Wert heisst, dass das Geld nicht gereicht hat."),
   c("renditen = [0.20, 0.15, 0.10, 0.10, 0.05, 0.05, 0.0, -0.05, -0.15, -0.25]\n\n\ndef endvermoegen(folge):\n    w = 100_000\n#L\n    for x in folge:\n        w = (w - 12_000) * (1 + x)\n#E\n    return w\n\n\npruefe('Gute Jahre zuerst', endvermoegen(renditen), 21_627, 1)\npruefe('Schlechte Jahre zuerst', endvermoegen(renditen[::-1]), -75_148, 1)"))

nb("05_Diversifikation", "Diversifikation",
   "Sie besitzen 500 verschiedene Aktien. Weshalb können Sie trotzdem an einem Tag einen grossen Teil verlieren?",
   m("## Aufgabe 1: Formel\nProgrammieren Sie $\\sigma_P = \\sigma\\sqrt{1/n + (n-1)/n \\cdot \\rho}$ und vergleichen Sie $\\rho = 0.2$ mit $\\rho = 0.7$ für $n = 1$ bis $50$ in einem Diagramm."),
   c("def portfolio_vola(n, sigma, rho):\n    wert = None\n#L\n    wert = sigma * np.sqrt(1 / n + (n - 1) / n * rho)\n#E\n    return wert\n\n\npruefe('n=20, rho=0.2', portfolio_vola(20, 0.3, 0.2), 0.147, 0.001)"),
   m("## Aufgabe 2: Simulation mit Marktfaktor\nJede Aktie setzt sich aus einem gemeinsamen Marktanteil und einem eigenen Teil zusammen: $r_i = \\sigma(\\sqrt{\\rho}\\,M + \\sqrt{1-\\rho}\\,E_i)$.\n\n*Hilfestellung:* `M` hat die Form `(jahre, 1)`, `E` die Form `(jahre, n)`. NumPy addiert die beiden automatisch."),
   c("jahre, n, sigma, rho = 200_000, 20, 0.3, 0.2\nsim = None\n#L\nM = rng.normal(size=(jahre, 1))\nE = rng.normal(size=(jahre, n))\nr = sigma * (np.sqrt(rho) * M + np.sqrt(1 - rho) * E)\nsim = r.mean(axis=1).std()\n#E\npruefe('Simulierte Volatilität', sim, 0.147, 0.002)"),
   m("## Challenge: Das risikoärmste Portfolio\nAktien haben $\\sigma_1 = 16$ %, Obligationen $\\sigma_2 = 4$ %, Korrelation 0.1. Suchen Sie das Gewicht $w$ der Aktien mit der kleinsten Volatilität. Weshalb ist es nicht 0?\n\n*Hilfestellung:* Berechnen Sie $\\sigma_P^2 = w^2\\sigma_1^2 + (1-w)^2\\sigma_2^2 + 2w(1-w)\\rho\\sigma_1\\sigma_2$ für viele $w$."),
   c("w = np.linspace(0, 1, 100_001)\nbestes_w = None\n#L\nv = w**2 * 0.16**2 + (1 - w)**2 * 0.04**2 + 2 * w * (1 - w) * 0.1 * 0.16 * 0.04\nbestes_w = w[v.argmin()]\n#E\npruefe('Bestes Gewicht', bestes_w, 0.037, 0.001)"))

nb("06_Franchise", "Versicherung im Alltag",
   "Wer eine hohe Franchise wählt, spart Prämie, weil er voraussichtlich gesund bleibt. Wer zahlt dann die Rechnung der Kranken, und ist das gerecht?",
   m("## Aufgabe 1: Kostenfunktion\nDie Prämie bei Franchise 300 beträgt fiktiv 4200 CHF, jeder Franken mehr Franchise senkt sie um 0.70 CHF. Über der Franchise zahlen Sie 10 %, maximal 700 CHF."),
   c("def jahreskosten(k, f):\n    wert = None\n#L\n    praemie = 4200 - 0.7 * (f - 300)\n    wert = praemie + np.minimum(k, f) + np.minimum(0.1 * np.maximum(k - f, 0), 700)\n#E\n    return wert\n\n\npruefe('Kosten 0, Franchise 300', jahreskosten(0, 300), 4200, 0.1)\npruefe('Kosten 20000, Franchise 2500', jahreskosten(20_000, 2500), 5860, 0.1)"),
   m("## Aufgabe 2: Zwei Personen\nBehandlungskosten: gesund `600 * np.exp(rng.normal(0, 1.4, n))`, chronisch krank `6000 * np.exp(rng.normal(0, 0.8, n))`. Wie oft ist Franchise 2500 günstiger als Franchise 300?"),
   c("n = 1_000_000\nanteil_gesund = anteil_krank = None\n#L\nk1 = 600 * np.exp(rng.normal(0, 1.4, n))\nk2 = 6000 * np.exp(rng.normal(0, 0.8, n))\nanteil_gesund = np.mean(jahreskosten(k1, 2500) < jahreskosten(k1, 300))\nanteil_krank = np.mean(jahreskosten(k2, 2500) < jahreskosten(k2, 300))\n#E\npruefe('Gesund', anteil_gesund, 0.806, 0.005)\npruefe('Chronisch krank', anteil_krank, 0.086, 0.005)"),
   m("## Challenge: Wie gross muss eine Versicherung sein?\n$n$ Versicherte, jede Person hat mit 1 % Wahrscheinlichkeit einen Schaden von 100'000 CHF. Welche Prämie deckt die Schäden in 99 % der Jahre? Vergleichen Sie $n = 100$, $1000$, $10'000$, $100'000$.\n\n*Hilfestellung:* `rng.binomial(n, 0.01, size=1_000_000)` und `np.percentile(..., 99)`."),
   c("praemien = {}\n#L\nfor n in (100, 1000, 10_000, 100_000):\n    praemien[n] = np.percentile(rng.binomial(n, 0.01, size=1_000_000), 99) * 100_000 / n\n#E\npruefe('Prämie bei n=10000', praemien.get(10_000), 1240, 5)\npruefe('Prämie bei n=100', praemien.get(100), 4000, 1)"))

nb("07_Modell", "Wenn das Modell versagt",
   "Ein Modell sagt: Ein solcher Tag kommt alle 13'800 Jahre. Dann passiert er zweimal in zehn Jahren. Wer haftet?",
   m("## Aufgabe 1: Dicke Ränder\nErzeugen Sie 2520 Tage mal 2000 Läufe mit Tagesvolatilität 1 %: einmal normalverteilt, einmal t-verteilt mit 3 Freiheitsgraden.\n\n*Hilfestellung:* `rng.standard_t(3, size=...)` hat die Standardabweichung $\\sqrt{3}$. Teilen Sie durch diesen Wert und multiplizieren Sie mit 0.01."),
   c("form = (2000, 2520)\nnormal = dick = None\n#L\nnormal = rng.normal(0, 0.01, size=form)\ndick = rng.standard_t(3, size=form) * 0.01 / np.sqrt(3)\n#E\nt5 = None if dick is None else np.mean(np.sum(dick <= -0.05, axis=1))\nn5 = None if normal is None else np.mean(np.sum(normal <= -0.05, axis=1))\npruefe('Tage bis -5 %, normal', n5, 0.0, 0.01)\npruefe('Tage bis -5 %, dick', t5, 4.0, 0.3)"),
   m("## Aufgabe 2: Value at Risk und Expected Shortfall\nDer VaR 99 % ist das 1-%-Perzentil. Der Expected Shortfall ist der Durchschnitt aller Tage, die noch schlechter sind. Welche Zahl trennt die beiden Modelle besser?"),
   c("es_normal = es_dick = None\n#L\nv1 = np.percentile(normal, 1)\nv2 = np.percentile(dick, 1)\nes_normal = normal[normal <= v1].mean()\nes_dick = dick[dick <= v2].mean()\n#E\npruefe('ES normal', es_normal, -0.0266, 0.0005)\npruefe('ES dick', es_dick, -0.0404, 0.002)"),
   m("## Challenge: Schulden als Verstärker\nEin Fonds hat Tagesvolatilität 0.5 %, Tagesdrift 0.04 % und arbeitet mit Hebel $h$: Die Tagesrendite des Eigenkapitals ist $h \\cdot r$. Wie oft fällt das Eigenkapital innerhalb eines Jahres (252 Tage) um mindestens 80 %? Vergleichen Sie Hebel 5, 10 und 25, normal und dick.\n\n*Hilfestellung:* Rechnen Sie mit `np.log1p(np.maximum(h * r, -0.999999))`, summieren Sie mit `np.cumsum` und vergleichen Sie mit `np.log(0.2)`."),
   c("def ruin(r, h):\n    wert = None\n#L\n    lw = np.cumsum(np.log1p(np.maximum(h * r, -0.999999)), axis=1)\n    wert = np.mean(np.any(lw <= np.log(0.2), axis=1))\n#E\n    return wert\n\n\nr = 0.0004 + rng.standard_t(3, size=(100_000, 252)) * 0.005 / np.sqrt(3)\npruefe('Dick, Hebel 10', ruin(r, 10), 0.0189, 0.003)\npruefe('Dick, Hebel 25', ruin(r, 25), 0.336, 0.01)"))

nb("08_Projektvorlage", "Projektvorlage",
   "Welche Entscheidung möchten Sie untersuchen, und wem würde ein Fehler in Ihrem Modell schaden?",
   m("## 1. Entscheidung\nWas genau wird entschieden, von wem, und wie sieht ein gutes Ergebnis aus?"),
   m("## 2. Annahmen\nListen Sie jede Annahme mit Herkunft auf: Quelle, Schätzung oder bewusst gewählt."),
   c("# Parameter des Modells\nn = 100_000"),
   m("## 3. Modell\nProgrammieren Sie eine Funktion, die mit einem Parametersatz die Ergebnisse aller Läufe liefert."),
   c("def simuliere(parameter):\n    pass"),
   m("## 4. Ergebnis\nZeigen Sie Median, schlechten Fall und eine Grafik."),
   m("## 5. Kipppunkt\nVariieren Sie die wichtigste Annahme. Wann ändert sich Ihre Schlussfolgerung?"),
   m("## 6. Grenzen\nWas kann Ihr Modell nicht, und was würde Sie an Ihrem eigenen Ergebnis zweifeln lassen?"))


def code_zelle(text, loesung):
    if loesung:
        return re.sub(r"^#[LE]\n?", "", text, flags=re.M)
    return re.sub(r"^#L\n.*?^#E\n?", "# Ihr Code\n", text, flags=re.M | re.S)


def zelle(typ, text):
    quelle = text.rstrip("\n").splitlines(keepends=True)
    if typ == "m":
        return {"cell_type": "markdown", "metadata": {}, "source": quelle}
    return {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": quelle}


def schreibe():
    (ZIEL / "Loesungen").mkdir(parents=True, exist_ok=True)
    for name, (titel, frage, zellen) in NB.items():
        for loesung in (False, True):
            inhalt = [zelle("m", f"# {titel}\n\n**Einstiegsfrage:** {frage}"), zelle("c", KOPF)]
            inhalt += [zelle(t, code_zelle(x, loesung) if t == "c" else x) for t, x in zellen]
            pfad = (ZIEL / "Loesungen" if loesung else ZIEL) / f"{name}.ipynb"
            pfad.write_text(json.dumps({"cells": inhalt, "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}}, "nbformat": 4, "nbformat_minor": 5}, ensure_ascii=False, indent=1), encoding="utf-8")


def teste():
    import contextlib
    import io

    import matplotlib
    matplotlib.use("Agg")
    fehler = 0
    for name, (_, _, zellen) in NB.items():
        for loesung in (True, False):
            raum, puffer = {}, io.StringIO()
            with contextlib.redirect_stdout(puffer):
                exec(KOPF, raum)
                for t, x in zellen:
                    if t == "c":
                        try:
                            exec(code_zelle(x, loesung), raum)
                        except Exception as e:
                            if loesung:
                                raise
                            print("FEHLER", type(e).__name__, e)
            aus = puffer.getvalue()
            schlecht = aus.count("prüfen Sie") + (aus.count("noch nicht") if loesung else 0)
            if loesung:
                fehler += schlecht
                print(name, "Lösung:", aus.count("passt"), "passt,", schlecht, "Abweichungen")
                if schlecht:
                    print(aus)
            else:
                print(name, "Schülerversion:", aus.count("noch nicht"), "offen,", aus.count("FEHLER"), "Laufzeitfehler")
    sys.exit(1 if fehler else 0)


if __name__ == "__main__":
    schreibe()
    if "--test" in sys.argv:
        teste()
