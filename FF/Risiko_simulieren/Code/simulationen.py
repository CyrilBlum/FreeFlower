"""Simulationen zum Kurs «Risiko simulieren».

Erzeugt die Datenreihen in ../Figures und gibt die im Skript zitierten Kennzahlen aus.
Alle Parameter sind Modellannahmen für den Unterricht, keine Prognosen.
Aufruf aus dem Ordner Code: python simulationen.py
"""
from pathlib import Path

import numpy as np

FIG = Path(__file__).resolve().parent.parent / "Figures"
rng = np.random.default_rng(2026)


def schreibe(name, kopf, zeilen):
    """Schreibt eine Tabelle, die pgfplots direkt lesen kann."""
    text = kopf + "\n" + "\n".join(" ".join(f"{w:.4f}" for w in z) for z in zeilen) + "\n"
    (FIG / name).write_text(text, encoding="utf-8")


def anlagen():
    """30 Jahre Vermögensentwicklung für vier Anlageklassen."""
    jahre, pfade, start = 30, 100_000, 1000
    klassen = {
        "Sparkonto": (0.005, 0.0),
        "Obligationen": (0.02, 0.04),
        "Aktienfonds": (0.06, 0.16),
        "Krypto": (0.10, 0.80),
    }
    print("Anlagen nach 30 Jahren (1000 CHF), Median, 5 %, 95 %, P(Verlust)")
    for name, (mu, sigma) in klassen.items():
        r = rng.normal(mu, sigma, size=(pfade, jahre))
        w = start * np.exp(np.cumsum(r, axis=1))
        ende = w[:, -1]
        print(f"  {name:13s} {np.median(ende):10.0f} {np.percentile(ende, 5):10.0f} "
              f"{np.percentile(ende, 95):10.0f} {np.mean(ende < start):7.3f}")
        if name == "Aktienfonds":
            q = np.percentile(w, [5, 50, 95], axis=0)
            schreibe("faecher_aktien.dat", "jahr p05 p50 p95",
                     [(0, start, start, start)] + [(j + 1, *q[:, j]) for j in range(jahre)])


def muenzspiel():
    """+50 % oder -40 % pro Runde: Durchschnitt und typischer Verlauf laufen auseinander."""
    runden, spieler = 20, 200_000
    faktor = rng.choice([1.5, 0.6], size=(spieler, runden))
    w = 100 * np.cumprod(faktor, axis=1)
    mittel, median = w.mean(axis=0), np.median(w, axis=0)
    theorie = 100 * 1.05 ** np.arange(1, runden + 1)
    schreibe("muenzspiel.dat", "runde theorie median",
             [(0, 100, 100)] + [(i + 1, theorie[i], median[i]) for i in range(1, runden, 2)])  # nur gerade Runden, sonst springt der Median
    ende = w[:, -1]
    print(f"Münzspiel: Theorie Ø {theorie[-1]:.1f}, simuliert Ø {mittel[-1]:.1f}, "
          f"Median {median[-1]:.2f}, Anteil < 100: {np.mean(ende < 100):.3f}, "
          f"Anteil der Spieler über dem Ø: {np.mean(ende > theorie[-1]):.3f}, "
          f"exakter Median {100 * (1.5 * 0.6) ** 10:.2f}")


def portfolio_vola(n, sigma, rho):
    return sigma * np.sqrt(1 / n + (n - 1) / n * rho)


def diversifikation():
    """Volatilität gleichgewichteter Portfolios bei normaler und hoher Korrelation."""
    sigma = 0.30
    n_werte = np.arange(1, 51)
    schreibe("diversifikation.dat", "n normal krise",
             [(n, 100 * portfolio_vola(n, sigma, 0.2), 100 * portfolio_vola(n, sigma, 0.7))
              for n in n_werte])
    for rho in (0.2, 0.7):
        n, jahre = 20, 200_000
        markt = rng.normal(size=(jahre, 1))
        eigen = rng.normal(size=(jahre, n))
        r = sigma * (np.sqrt(rho) * markt + np.sqrt(1 - rho) * eigen)
        print(f"Diversifikation rho={rho}: n=20 Formel {portfolio_vola(20, sigma, rho):.4f}, "
              f"Simulation {r.mean(axis=1).std():.4f}, Grenzwert {sigma * np.sqrt(rho):.4f}")


def franchise():
    """Jahreskosten je Franchise, Prämien und Kosten sind fiktiv."""
    franchisen = [300, 500, 1000, 1500, 2000, 2500]
    praemie_300, personen = 4200, 1_000_000
    profile = {"gesund": (600, 1.4), "chronisch": (6000, 0.8)}
    zeilen = []
    print("Franchise: Mittel und 95-%-Perzentil der Jahreskosten")
    kosten = {p: m * np.exp(rng.normal(0, s, personen)) for p, (m, s) in profile.items()}
    gesamt = {}
    for f in franchisen:
        praemie = praemie_300 - 0.7 * (f - 300)
        zeile = [f]
        for p in profile:
            k = kosten[p]
            selbst = np.minimum(k, f) + np.minimum(0.1 * np.maximum(k - f, 0), 700)
            g = praemie + selbst
            gesamt[(p, f)] = g
            zeile += [g.mean(), np.percentile(g, 95)]
            print(f"  {p:9s} F={f:4d} Prämie {praemie:6.0f} Ø {g.mean():7.0f} "
                  f"P95 {np.percentile(g, 95):7.0f}")
        zeilen.append(zeile)
    schreibe("franchise.dat", "franchise gesund gesundp95 chronisch chronischp95", zeilen)
    for p in profile:
        print(f"  {p}: P(F2500 günstiger als F300) = "
              f"{np.mean(gesamt[(p, 2500)] < gesamt[(p, 300)]):.3f}")


def extremereignisse():
    """Gleiche Tagesvolatilität, aber dünne oder dicke Ränder."""
    tage, laeufe, vola, df = 2520, 2000, 0.01, 3
    normal = rng.normal(0, vola, size=(laeufe, tage))
    t = rng.standard_t(df, size=(laeufe, tage)) * vola / np.sqrt(df / (df - 2))
    print("Extremereignisse pro 10 Jahre: Std, Ø Tage <= -3 %, Ø Tage <= -5 %, VaR 99 %, schlimmster Tag (Median)")
    for name, r in (("normal", normal), ("t3", t)):
        print(f"  {name:7s} {r.std():.4f} {np.mean(np.sum(r <= -0.03, axis=1)):7.2f} "
              f"{np.mean(np.sum(r <= -0.05, axis=1)):7.2f} {np.percentile(r, 1):.4f} "
              f"{np.median(r.min(axis=1)):.4f}")


def entnahme():
    """Gleiche Jahresrenditen, andere Reihenfolge: Rentenentnahme während 10 Jahren."""
    r = [0.20, 0.15, 0.10, 0.10, 0.05, 0.05, 0.0, -0.05, -0.15, -0.25]
    for name, folge in (("gute Jahre zuerst", r), ("schlechte Jahre zuerst", r[::-1])):
        w = 100_000.0
        for x in folge:
            w = (w - 12_000) * (1 + x)
        print(f"Entnahme {name}: Endvermögen {w:.0f}")
    print(f"Ohne Entnahme: Faktor {np.prod([1 + x for x in r]):.3f}")


if __name__ == "__main__":
    anlagen()
    muenzspiel()
    diversifikation()
    franchise()
    extremereignisse()
    entnahme()
