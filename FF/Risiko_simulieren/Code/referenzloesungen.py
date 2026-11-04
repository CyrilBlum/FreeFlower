"""Referenzlösungen zu den anspruchsvolleren Aufgaben und Projekten im Kurs «Risiko simulieren».

Alle Parameter sind Modellannahmen für den Unterricht. Die Ausgabe belegt die Zahlen im Skript.
Aufruf: python referenzloesungen.py
"""
from math import comb, erf, exp, log, sqrt

import numpy as np

rng = np.random.default_rng(2027)


def titel(t):
    print(f"\n## {t}")


def roulette():
    titel("Roulette")
    p = 18 / 37
    print("P(Abend im Plus, 100 Spiele)", sum(comb(100, k) * p**k * (1 - p)**(100 - k) for k in range(51, 101)))
    print("Würfel: n für +-0.01 (95 %)", (1.96 * sqrt(35 / 12) / 0.01) ** 2)


def mittel_median():
    titel("Mittelwert und Median Aktienfonds")
    x = 1000 * np.exp(rng.normal(0.06, 0.16, size=(1_000_000, 30)).sum(axis=1))
    print("Sim Ø", x.mean(), "Formel", 1000 * exp(30 * (0.06 + 0.16**2 / 2)), "Median", np.median(x), 1000 * exp(1.8))
    print("Anteil unter Ø", np.mean(x < x.mean()))


def sparplan():
    titel("Sparplan gegen Einmalanlage, 12000 CHF über 10 Jahre")
    n = 200_000
    r = rng.normal(0.06 / 12, 0.16 / sqrt(12), size=(n, 120))
    einmal = 12000 * np.exp(r.sum(axis=1))
    faktor = np.exp(np.cumsum(r[:, ::-1], axis=1))[:, ::-1]
    plan = 100 * faktor.sum(axis=1)
    for name, w in (("Einmal", einmal), ("Plan", plan)):
        print(name, "Median", np.median(w), "P5", np.percentile(w, 5), "P(Verlust)", np.mean(w < 12000))
    print("P(Einmal > Plan)", np.mean(einmal > plan))


def kelly_muenze():
    titel("Optimaler Einsatz im Münzspiel")
    f = np.linspace(0, 1, 100_001)
    g = 0.5 * np.log(1 + 0.5 * f) + 0.5 * np.log(1 - 0.4 * f)
    print("f*", f[g.argmax()], "Wachstum pro Runde", exp(g.max()) - 1)
    print("Nullwachstum bei f", f[1:][np.argmax(g[1:] < 0)])


def minvar():
    titel("Minimum-Varianz")
    s1, s2, rho = 0.16, 0.04, 0.1
    w = (s2**2 - rho * s1 * s2) / (s1**2 + s2**2 - 2 * rho * s1 * s2)
    v = sqrt(w**2 * s1**2 + (1 - w)**2 * s2**2 + 2 * w * (1 - w) * rho * s1 * s2)
    print("Gewicht Aktien", w, "Vola", v, "Rendite bei 6/2", w * 0.06 + (1 - w) * 0.02)
    z = rng.normal(size=(1_000_000, 2))
    a = s1 * z[:, 0]
    b = s2 * (rho * z[:, 0] + sqrt(1 - rho**2) * z[:, 1])
    print("Simulation", (w * a + (1 - w) * b).std())


def versicherer():
    titel("Versicherungspool")
    for n in (100, 1000, 10000, 100000):
        s = rng.binomial(n, 0.01, size=2_000_000) * 100_000
        q = np.percentile(s, 99)
        print(n, "Prämie für 99 %", q / n, "Zuschlag", q / n - 1000, "Näherung", 2.326 * 100000 * sqrt(0.0099 / n))


def expected_shortfall():
    titel("Expected Shortfall und Hebel")
    vola, df = 0.01, 3
    n = 20_000_000
    x = {"normal": rng.normal(0, vola, n), "t3": rng.standard_t(df, n) * vola / sqrt(3)}
    for k, r in x.items():
        v = np.percentile(r, 1)
        print(k, "VaR", v, "ES", r[r <= v].mean(), "ES 99.9 %", r[r <= np.percentile(r, 0.1)].mean())
    tage, laeufe = 252, 200_000
    v2 = 0.005
    for name, r in (("normal", rng.normal(0.0004, v2, (laeufe, tage))),
                    ("t3", 0.0004 + rng.standard_t(df, (laeufe, tage)) * v2 / sqrt(3))):
        for h in (1, 5, 10, 25):
            ruin = np.any(np.cumsum(np.log1p(np.maximum(h * r, -0.999999)), axis=1) <= log(0.2), axis=1)
            print(name, "Hebel", h, "P(-80 % im Jahr)", ruin.mean())


def altersvorsorge():
    titel("P1 Altersvorsorge: 6000 CHF pro Jahr, 40 Jahre, Sparphase")
    n = 200_000
    for q in (0, 0.25, 0.5, 0.75, 1):
        r = q * rng.normal(0.06, 0.16, (n, 40)) + (1 - q) * rng.normal(0.02, 0.04, (n, 40))
        w = 6000 * np.exp(np.cumsum(r[:, ::-1], axis=1)).sum(axis=1)
        print(q, "Median", np.median(w), "P5", np.percentile(w, 5), "P95", np.percentile(w, 95))


def kelly():
    titel("P2 Kelly: p=0.6, Quote 1:1, 1000 Runden")
    n = 200_000
    s = rng.random((n, 1000)) < 0.6
    for f in (0.05, 0.1, 0.2, 0.3, 0.4, 0.5):
        lw = (s * log(1 + f) + (~s) * log(1 - f)).cumsum(axis=1)
        print(f, "Median", exp(np.median(lw[:, -1])), "P(unter Start)", np.mean(lw[:, -1] < 0),
              "P(zwischendurch -50 %)", np.mean(lw.min(axis=1) < log(.5)))


def ruin():
    titel("P3 Ruin des Spielers: Start a, Ziel 2a, Einsatz 1")
    for p in (18 / 37, 0.5):
        for a in (10, 50, 100):
            q = (1 - p) / p
            e = 0.5 if p == 0.5 else (1 - q**a) / (1 - q**(2 * a))
            print(round(p, 4), a, "P(Ziel)", e)
    p, a = 18 / 37, 50
    pos = np.full(20000, a)
    dauer = np.zeros(20000)
    aktiv = np.ones(20000, bool)
    while aktiv.any():
        pos[aktiv] += 2 * (rng.random(aktiv.sum()) < p) - 1
        dauer[aktiv] += 1
        aktiv = (pos > 0) & (pos < 2 * a)
    print("Sim P(Ziel)", np.mean(pos == 2 * a), "Ø Spiele", dauer.mean())


def bank_run():
    titel("P4 Bank Run: Schwellenmodell, 1000 Kundinnen, Reserve 20 %")
    n, laeufe = 1000, 400
    for streuung in (0.15, 0.2, 0.25):
        for schock in (0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4):
            ende = []
            for _ in range(laeufe):
                sw = rng.normal(0.4, streuung, n)
                anteil = schock
                while True:
                    neu = max(schock, np.mean(sw <= anteil))
                    if neu <= anteil:
                        break
                    anteil = neu
                ende.append(anteil)
            print(streuung, schock, "Ø Endabzug", round(float(np.mean(ende)), 3))


def gebaeude():
    titel("P5/P6 Gebäudeversicherung: 100000 Gebäude, Poisson-Pareto")
    jahre, schaeden = 200_000, 200
    for name, h in (("heute", 1.0), ("Häufigkeit +50 %", 1.5)):
        anzahl = rng.poisson(schaeden * h, jahre)
        s = (rng.pareto(1.5, anzahl.sum()) + 1) * 20_000
        idx = np.repeat(np.arange(jahre), anzahl)
        tot = np.bincount(idx, weights=s, minlength=jahre)
        print(name, "Ø Jahr Mio", tot.mean() / 1e6, "99.5 % Mio", np.percentile(tot, 99.5) / 1e6,
              "Prämie pro Gebäude", tot.mean() / 100000, "Reserve Mio", (np.percentile(tot, 99.5) - tot.mean()) / 1e6)


def lawine():
    titel("P7 Lawinenrisiko: p=1/10000 pro Tour")
    p = 1e-4
    for t in (10, 100, 500, 1000):
        print(t, 1 - (1 - p)**t)
    print("mit 10 Touren/Jahr und 50 Jahren:", 1 - (1 - p)**500, "mit 3x Risiko an 20 % der Tage:",
          1 - (1 - 3 * p)**100 * (1 - p)**400)


def startup():
    titel("P8 Startups: 30 Investments, Pareto-Vielfache, 65 % Totalverlust")
    n, k = 200_000, 30
    tot = rng.random((n, k)) < 0.65
    m = rng.pareto(1.3, (n, k)) + 1
    x = np.where(tot, 0, m)
    s = np.sort(x, axis=1)[:, ::-1]
    print("Ø Vielfaches Portfolio", x.mean(axis=1).mean(), "Median", np.median(x.mean(axis=1)))
    ok = s.sum(axis=1) > 0
    print("Median-Anteil bester Treffer", np.median(s[ok, 0] / s[ok].sum(axis=1)), "bester+2", np.median(s[ok, :3].sum(axis=1) / s[ok].sum(axis=1)))
    print("P(Portfolio verliert Geld)", np.mean(x.mean(axis=1) < 1))


def wetten():
    titel("P9 Sportwetten")
    q = np.array([2.10, 3.40, 3.60])
    u = 1 / q
    print("Summe", u.sum(), "Marge", u.sum() - 1, "faire p", u / u.sum(), "Auszahlungsquote", 1 / u.sum())
    p = u / u.sum()
    print("E Gewinn je 1 CHF", p * q - 1)
    n = 100_000
    tipps = rng.random((n, 200)) < p[0]
    gewinn = (tipps * (q[0] - 1) - (~tipps)).sum(axis=1)
    print("200 Wetten: Ø", gewinn.mean(), "P(Plus)", np.mean(gewinn > 0))


def bootstrap():
    titel("P11 Bootstrapping: zwei Marktphasen, Autokorrelation der quadrierten Renditen")
    n = 6000
    zustand = np.zeros(n, dtype=int)
    u = rng.random(n)
    for i in range(1, n):
        zustand[i] = zustand[i - 1] if u[i] < 0.97 else 1 - zustand[i - 1]
    x = 0.006 + np.array([0.03, 0.09])[zustand] * rng.normal(size=n)
    einzeln = x[rng.integers(0, n, n)]
    b = 24
    block = np.concatenate([x[s:s + b] for s in rng.integers(0, n - b, n // b)])
    ak = lambda r: np.corrcoef(r[:-1]**2, r[1:]**2)[0, 1]
    for name, r in (("Original", x), ("einzeln", einzeln), ("Block", block)):
        print(name, "Ø", round(r.mean(), 4), "Std", round(r.std(), 4), "AK Quadrate", round(ak(r), 3))


def option():
    titel("P12 Europäische Call-Option")
    S, K, r, s, T = 100, 100, 0.01, 0.2, 1
    Phi = lambda x: 0.5 * (1 + erf(x / sqrt(2)))
    d1 = (log(S / K) + (r + s**2 / 2) * T) / (s * sqrt(T))
    d2 = d1 - s * sqrt(T)
    bs = S * Phi(d1) - K * exp(-r * T) * Phi(d2)
    for n in (1000, 100_000, 10_000_000):
        z = rng.normal(size=n)
        st = S * np.exp((r - s**2 / 2) * T + s * sqrt(T) * z)
        y = np.exp(-r * T) * np.maximum(st - K, 0)
        print(n, "MC", y.mean(), "+-", 1.96 * y.std() / sqrt(n))
    print("Black-Scholes", bs)


if __name__ == "__main__":
    roulette()
    mittel_median()
    sparplan()
    kelly_muenze()
    minvar()
    versicherer()
    expected_shortfall()
    altersvorsorge()
    kelly()
    ruin()
    bank_run()
    gebaeude()
    lawine()
    startup()
    wetten()
    bootstrap()
    option()
