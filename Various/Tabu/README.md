# Tabu-Kartengenerator

## Aufbau

Dieses System generiert randomisierte Tabu-Kartendateien mit folgenden Komponenten:

### Dateien

- **tabu_words.txt** — Alle Tabu-Wörter organisiert nach Kategorien
  - Format: `Wort | Tabu-Wörter` pro Zeile
  - Kategorien werden mit `category: Kategoriename` gekennzeichnet

- **tabu_config.txt** — Toggles für aktivierte Kategorien
  - Format: `Kategorie: true/false`
  - true = Kategorie ist aktiv
  - false = Kategorie wird ignoriert

- **Tabu_template.tex** — LaTeX-Template mit Header, Ablauf und Regeln (integriert in main.tex)
- **generate_tabu.py** — Python-Skript zur Generierung der Tabu.tex Datei

## Verwendung

### Wörter hinzufügen/ändern

Bearbeite `tabu_words.txt` und füge Wörter nach Kategorien hinzu:

```
category: Informatik
Python | Programmierung, Code, Schlange
Turtle | Grafik, Zeichnen, Schildkröte
```

### Kategorien aktivieren/deaktivieren

Passe `tabu_config.txt` an:

```
Informatik: true
Jugendwörter: false
Sport: true
```

### Datei generieren und kompilieren

**Schritt 1: Tabu-Kartendatei generieren**
```bash
cd /Users/cyrilwendl/LeeTeX/Various/Tabu
python3 generate_tabu.py
```
Dies generiert eine neue `Tabu.tex` mit:
- Randomisierten Wörtern (jedes Mal andere Reihenfolge)
- Nur aktivierten Kategorien
- Tabu-Kartenseiten im 21:9 Landscape-Format (42cm × 18cm)

**Schritt 2: LaTeX kompilieren**
```bash
cd /Users/cyrilwendl/LeeTeX
lualatex -output-directory=build main.tex
```

Dies generiert `build/main.pdf` mit:
- Alle regulären Inhalte von main.tex (A4 Hochformat)
- Tabu-Kartenseiten integriert im 21:9 Querformat

## Features

- ✓ Wörter zufällig sortiert (jedes Mal andere Reihenfolge)
- ✓ Selektive Kategorien (kannst einzelne Kategorien deaktivieren)
- ✓ Template-basiert (Layout bleibt konsistent)
- ✓ 21:9 Querformat — optimiert für große Displays/Beamer (42cm × 18cm)
- ✓ Schöne tcolorbox-Design mit Wort außerhalb der Box
- ✓ Ein einziges Python-Skript (`generate_tabu.py`)
- ✓ Einfache Verwaltung (nur .txt-Dateien bearbeiten)
