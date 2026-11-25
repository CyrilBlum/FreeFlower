---
layout: default
title: Skripte und Slides
nav_order: 1
---

<style>
/* Liste der kompilierten PDFs; Farben angelehnt an das Theme just-the-docs */
.cf-intro { margin-bottom: 1.5rem; }

.cf-controls {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem 1rem;
  align-items: center;
  margin-bottom: 1.5rem;
}

.cf-search {
  flex: 1 1 16rem;
  padding: 0.4rem 0.6rem;
  border: 1px solid #d0cbd6;
  border-radius: 4px;
  font: inherit;
  font-size: 0.9rem;
}

.cf-search:focus {
  outline: none;
  border-color: #7253ed;
  box-shadow: 0 0 0 2px rgba(114, 83, 237, 0.2);
}

.cf-filter {
  display: inline-flex;
  border: 1px solid #d0cbd6;
  border-radius: 4px;
  overflow: hidden;
}

.cf-filter button, .cf-toggle {
  background: #fff;
  border: 0;
  padding: 0.35rem 0.7rem;
  font: inherit;
  font-size: 0.85rem;
  color: #5c5962;
  cursor: pointer;
}

.cf-filter button + button { border-left: 1px solid #d0cbd6; }
.cf-filter button:hover, .cf-toggle:hover { background: #f5f6fa; }
.cf-filter button.active { background: #7253ed; color: #fff; }

.cf-toggle {
  padding: 0.35rem 0.2rem;
  background: none;
  color: #7253ed;
}

.cf-toggle:hover { background: none; text-decoration: underline; }

.cf-group h2 { margin-top: 2rem; }

.cf-topic { border-bottom: 1px solid #eeebee; }

.cf-topic > summary {
  cursor: pointer;
  padding: 0.5rem 0;
  font-weight: 500;
}

.cf-topic > summary .cf-count {
  font-weight: 400;
  font-size: 0.85rem;
  color: #959396;
  margin-left: 0.4rem;
}

.cf-topic-body { padding: 0 0 0.75rem 1.1rem; }

.cf-topic-body h3 {
  font-size: 0.75rem !important;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: #959396;
  margin: 0.6rem 0 0.2rem;
}

.cf-list {
  list-style: none;
  margin: 0;
  padding: 0;
}

.cf-list li {
  margin: 0.1rem 0;
  padding: 0;
  font-size: 0.95rem;
}

.cf-list li::before { content: none !important; }

.cf-nr {
  display: inline-block;
  min-width: 1.8rem;
  color: #959396;
  font-variant-numeric: tabular-nums;
}

.cf-log {
  font-size: 0.8rem;
  color: #959396 !important;
  margin-left: 0.5rem;
}

.cf-hidden { display: none !important; }

.cf-empty { color: #959396; }
</style>

# Skripte und Slides

<div class="cf-intro" markdown="1">
Alle Skripte, Folien und weiteren Dokumente werden bei jedem Push auf `main` auf dem Server neu kompiliert und auf [files.in-form-atik.ch](https://files.in-form-atik.ch) abgelegt. Die Liste unten bildet diesen Stand ab. Die Skripte gibt es jeweils mit und ohne Lösungen, das Log zeigt die Ausgabe der letzten Kompilation.
</div>

<div class="cf-controls">
  <input type="search" id="cf-search" class="cf-search" placeholder="Suchen, z. B. Hamming oder SQL" aria-label="PDFs durchsuchen">
  <div class="cf-filter" role="group" aria-label="Dokumenttyp">
    <button type="button" class="active" data-filter="all">Alle</button>
    <button type="button" data-filter="skript">Skripte</button>
    <button type="button" data-filter="folien">Folien</button>
    <button type="button" data-filter="artikel">Weitere</button>
  </div>
  <span>
    <button type="button" class="cf-toggle" id="cf-open">Alle aufklappen</button>
    <button type="button" class="cf-toggle" id="cf-close">Alle zuklappen</button>
  </span>
</div>

<!-- BEGIN generated: docs/_scripts/update_compiled_files.py -->
<p class="cf-count">Stand 25.11.2026, 148 PDFs.</p>
<section class="cf-group">
<h2>Grundlagenfach Informatik</h2>
<details class="cf-topic" data-name="Computer und Kodierungen">
<summary>Computer und Kodierungen<span class="cf-count">Skript, 12 Foliensätze</span></summary>
<div class="cf-topic-body">
<div class="cf-section"><h3>Skript</h3><ul class="cf-list">
<li data-type="skript"><a href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Skript_mit_loesungen/output_book_mit_loesungen_Computer_und_Kodierungen.pdf">mit Lösungen</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Skript_mit_loesungen/output_book_mit_loesungen_Computer_und_Kodierungen.log">Log</a></li>
<li data-type="skript"><a href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Skript_ohne_loesungen/output_book_ohne_loesungen_Computer_und_Kodierungen.pdf">ohne Lösungen</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Skript_ohne_loesungen/output_book_ohne_loesungen_Computer_und_Kodierungen.log">Log</a></li>
</ul></div>
<div class="cf-section"><h3>Folien</h3><ul class="cf-list">
<li data-type="folien"><span class="cf-nr">01</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Slides/01_Was_Ist_Informatik/output_beamer_01_Was_Ist_Informatik.pdf">Was ist Informatik?</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Slides/01_Was_Ist_Informatik/output_beamer_01_Was_Ist_Informatik.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">02</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Slides/02_Basisgroessen_und_Stellenwert/output_beamer_02_Basisgroessen_und_Stellenwert.pdf">Basisgrössen und Stellenwert</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Slides/02_Basisgroessen_und_Stellenwert/output_beamer_02_Basisgroessen_und_Stellenwert.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">03</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Slides/03_Umrechnung_und_Hex/output_beamer_03_Umrechnung_und_Hex.pdf">Umrechnung und Hex</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Slides/03_Umrechnung_und_Hex/output_beamer_03_Umrechnung_und_Hex.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">04</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Slides/04_Binaer_Rechnen_und_Bits/output_beamer_04_Binaer_Rechnen_und_Bits.pdf">Binär rechnen und Bits</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Slides/04_Binaer_Rechnen_und_Bits/output_beamer_04_Binaer_Rechnen_und_Bits.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">05</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Slides/05_ASCIIund_UTF8/output_beamer_05_ASCIIund_UTF8.pdf">ASCII und UTF-8</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Slides/05_ASCIIund_UTF8/output_beamer_05_ASCIIund_UTF8.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">06</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Slides/06_Bilder_und_Farben/output_beamer_06_Bilder_und_Farben.pdf">Bilder und Farben</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Slides/06_Bilder_und_Farben/output_beamer_06_Bilder_und_Farben.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">07</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Slides/07_Dateiformate_und_Speicher/output_beamer_07_Dateiformate_und_Speicher.pdf">Dateiformate und Speicher</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Slides/07_Dateiformate_und_Speicher/output_beamer_07_Dateiformate_und_Speicher.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">08</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Slides/08_Logische_Gatter_I/output_beamer_08_Logische_Gatter_I.pdf">Logische Gatter I</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Slides/08_Logische_Gatter_I/output_beamer_08_Logische_Gatter_I.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">09</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Slides/09_Logische_Gatter_II/output_beamer_09_Logische_Gatter_II.pdf">Logische Gatter II</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Slides/09_Logische_Gatter_II/output_beamer_09_Logische_Gatter_II.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">10</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Slides/10_Aufbau_Computer_I/output_beamer_10_Aufbau_Computer_I.pdf">Aufbau Computer I</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Slides/10_Aufbau_Computer_I/output_beamer_10_Aufbau_Computer_I.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">11</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Slides/11_Aufbau_Computer_II/output_beamer_11_Aufbau_Computer_II.pdf">Aufbau Computer II</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Slides/11_Aufbau_Computer_II/output_beamer_11_Aufbau_Computer_II.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">12</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Slides/12_Betriebssystem/output_beamer_12_Betriebssystem.pdf">Betriebssystem</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Slides/12_Betriebssystem/output_beamer_12_Betriebssystem.log">Log</a></li>
</ul></div>
</div>
</details>
<details class="cf-topic" data-name="Datenbanken">
<summary>Datenbanken<span class="cf-count">Skript, 6 Foliensätze</span></summary>
<div class="cf-topic-body">
<div class="cf-section"><h3>Skript</h3><ul class="cf-list">
<li data-type="skript"><a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenbanken/Skript_mit_loesungen/output_book_mit_loesungen_Datenbanken.pdf">mit Lösungen</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Datenbanken/Skript_mit_loesungen/output_book_mit_loesungen_Datenbanken.log">Log</a></li>
<li data-type="skript"><a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenbanken/Skript_ohne_loesungen/output_book_ohne_loesungen_Datenbanken.pdf">ohne Lösungen</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Datenbanken/Skript_ohne_loesungen/output_book_ohne_loesungen_Datenbanken.log">Log</a></li>
</ul></div>
<div class="cf-section"><h3>Folien</h3><ul class="cf-list">
<li data-type="folien"><span class="cf-nr">01</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenbanken/Slides/01_Intro/output_beamer_01_Intro.pdf">Intro</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Datenbanken/Slides/01_Intro/output_beamer_01_Intro.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">02</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenbanken/Slides/02_SELECT/output_beamer_02_SELECT.pdf">SELECT</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Datenbanken/Slides/02_SELECT/output_beamer_02_SELECT.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">03</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenbanken/Slides/03_Subqueries/output_beamer_03_Subqueries.pdf">Subqueries</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Datenbanken/Slides/03_Subqueries/output_beamer_03_Subqueries.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">04</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenbanken/Slides/04_JOIN/output_beamer_04_JOIN.pdf">JOIN</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Datenbanken/Slides/04_JOIN/output_beamer_04_JOIN.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">05</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenbanken/Slides/05_DML/output_beamer_05_DML.pdf">DML</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Datenbanken/Slides/05_DML/output_beamer_05_DML.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">06</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenbanken/Slides/06_Game/output_beamer_06_Game.pdf">Game</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Datenbanken/Slides/06_Game/output_beamer_06_Game.log">Log</a></li>
</ul></div>
</div>
</details>
<details class="cf-topic" data-name="Datenbanken Cheatsheet">
<summary>Datenbanken Cheatsheet<span class="cf-count">Skript</span></summary>
<div class="cf-topic-body">
<div class="cf-section"><h3>Skript</h3><ul class="cf-list">
<li data-type="skript"><a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenbanken_Cheatsheet/Skript_mit_loesungen/output_book_mit_loesungen_Datenbanken_Cheatsheet.pdf">mit Lösungen</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Datenbanken_Cheatsheet/Skript_mit_loesungen/output_book_mit_loesungen_Datenbanken_Cheatsheet.log">Log</a></li>
<li data-type="skript"><a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenbanken_Cheatsheet/Skript_ohne_loesungen/output_book_ohne_loesungen_Datenbanken_Cheatsheet.pdf">ohne Lösungen</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Datenbanken_Cheatsheet/Skript_ohne_loesungen/output_book_ohne_loesungen_Datenbanken_Cheatsheet.log">Log</a></li>
</ul></div>
</div>
</details>
<details class="cf-topic" data-name="Datenintegrität">
<summary>Datenintegrität<span class="cf-count">Skript, 6 Foliensätze</span></summary>
<div class="cf-topic-body">
<div class="cf-section"><h3>Skript</h3><ul class="cf-list">
<li data-type="skript"><a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenintegritaet/Skript_mit_loesungen/output_book_mit_loesungen_Datenintegritaet.pdf">mit Lösungen</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Datenintegritaet/Skript_mit_loesungen/output_book_mit_loesungen_Datenintegritaet.log">Log</a></li>
<li data-type="skript"><a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenintegritaet/Skript_ohne_loesungen/output_book_ohne_loesungen_Datenintegritaet.pdf">ohne Lösungen</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Datenintegritaet/Skript_ohne_loesungen/output_book_ohne_loesungen_Datenintegritaet.log">Log</a></li>
</ul></div>
<div class="cf-section"><h3>Folien</h3><ul class="cf-list">
<li data-type="folien"><span class="cf-nr">01</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenintegritaet/Slides/01_Intro/output_beamer_01_Intro.pdf">Intro</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Datenintegritaet/Slides/01_Intro/output_beamer_01_Intro.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">02</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenintegritaet/Slides/02_Fehlererkennung/output_beamer_02_Fehlererkennung.pdf">Fehlererkennung</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Datenintegritaet/Slides/02_Fehlererkennung/output_beamer_02_Fehlererkennung.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">03</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenintegritaet/Slides/03_Fehlerkorrektur/output_beamer_03_Fehlerkorrektur.pdf">Fehlerkorrektur</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Datenintegritaet/Slides/03_Fehlerkorrektur/output_beamer_03_Fehlerkorrektur.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">04</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenintegritaet/Slides/04_Kartentrick/output_beamer_04_Kartentrick.pdf">Kartentrick</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Datenintegritaet/Slides/04_Kartentrick/output_beamer_04_Kartentrick.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">05</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenintegritaet/Slides/05_Hamming/output_beamer_05_Hamming.pdf">Hamming</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Datenintegritaet/Slides/05_Hamming/output_beamer_05_Hamming.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">06</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenintegritaet/Slides/06_RAID/output_beamer_06_RAID.pdf">RAID</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Datenintegritaet/Slides/06_RAID/output_beamer_06_RAID.log">Log</a></li>
</ul></div>
</div>
</details>
<details class="cf-topic" data-name="Graphen">
<summary>Graphen<span class="cf-count">5 Foliensätze</span></summary>
<div class="cf-topic-body">
<div class="cf-section"><h3>Folien</h3><ul class="cf-list">
<li data-type="folien"><span class="cf-nr">01</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Graphen/Slides/01_Graphen_L01/output_beamer_01_Graphen_L01.pdf">Graphen L01</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Graphen/Slides/01_Graphen_L01/output_beamer_01_Graphen_L01.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">02</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Graphen/Slides/02_Graphen_L02/output_beamer_02_Graphen_L02.pdf">Graphen L02</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Graphen/Slides/02_Graphen_L02/output_beamer_02_Graphen_L02.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">03</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Graphen/Slides/03_Graphen_L03/output_beamer_03_Graphen_L03.pdf">Graphen L03</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Graphen/Slides/03_Graphen_L03/output_beamer_03_Graphen_L03.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">04</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Graphen/Slides/04_Abstraktion_Durch_Graphen_Kapitel01/output_beamer_04_Abstraktion_Durch_Graphen_Kapitel01.pdf">Abstraktion durch Graphen, Kapitel 1</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Graphen/Slides/04_Abstraktion_Durch_Graphen_Kapitel01/output_beamer_04_Abstraktion_Durch_Graphen_Kapitel01.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">05</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Graphen/Slides/05_Abstraktion_Durch_Graphen_Kapitel02/output_beamer_05_Abstraktion_Durch_Graphen_Kapitel02.pdf">Abstraktion durch Graphen, Kapitel 2</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Graphen/Slides/05_Abstraktion_Durch_Graphen_Kapitel02/output_beamer_05_Abstraktion_Durch_Graphen_Kapitel02.log">Log</a></li>
</ul></div>
</div>
</details>
<details class="cf-topic" data-name="KI und Algorithmen">
<summary>KI und Algorithmen<span class="cf-count">Skript, 4 Foliensätze</span></summary>
<div class="cf-topic-body">
<div class="cf-section"><h3>Skript</h3><ul class="cf-list">
<li data-type="skript"><a href="https://files.in-form-atik.ch/Grundlagen_Info/KI_und_Algorithmen/Skript_mit_loesungen/output_book_mit_loesungen_KI_und_Algorithmen.pdf">mit Lösungen</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/KI_und_Algorithmen/Skript_mit_loesungen/output_book_mit_loesungen_KI_und_Algorithmen.log">Log</a></li>
<li data-type="skript"><a href="https://files.in-form-atik.ch/Grundlagen_Info/KI_und_Algorithmen/Skript_ohne_loesungen/output_book_ohne_loesungen_KI_und_Algorithmen.pdf">ohne Lösungen</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/KI_und_Algorithmen/Skript_ohne_loesungen/output_book_ohne_loesungen_KI_und_Algorithmen.log">Log</a></li>
</ul></div>
<div class="cf-section"><h3>Folien</h3><ul class="cf-list">
<li data-type="folien"><span class="cf-nr">01</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/KI_und_Algorithmen/Slides/01_correlation_causation/output_beamer_01_correlation_causation.pdf">Korrelation und Kausalität</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/KI_und_Algorithmen/Slides/01_correlation_causation/output_beamer_01_correlation_causation.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">02</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/KI_und_Algorithmen/Slides/02_linear_regression/output_beamer_02_linear_regression.pdf">Lineare Regression</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/KI_und_Algorithmen/Slides/02_linear_regression/output_beamer_02_linear_regression.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">03</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/KI_und_Algorithmen/Slides/03_markov_chains/output_beamer_03_markov_chains.pdf">Markov-Ketten</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/KI_und_Algorithmen/Slides/03_markov_chains/output_beamer_03_markov_chains.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">04</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/KI_und_Algorithmen/Slides/04_markov_appendix/output_beamer_04_markov_appendix.pdf">Markov-Ketten, Anhang</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/KI_und_Algorithmen/Slides/04_markov_appendix/output_beamer_04_markov_appendix.log">Log</a></li>
</ul></div>
</div>
</details>
<details class="cf-topic" data-name="KI und Prompting">
<summary>KI und Prompting<span class="cf-count">Skript</span></summary>
<div class="cf-topic-body">
<div class="cf-section"><h3>Skript</h3><ul class="cf-list">
<li data-type="skript"><a href="https://files.in-form-atik.ch/Grundlagen_Info/KI_und_Prompting/Skript_mit_loesungen/output_book_mit_loesungen_KI_und_Prompting.pdf">mit Lösungen</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/KI_und_Prompting/Skript_mit_loesungen/output_book_mit_loesungen_KI_und_Prompting.log">Log</a></li>
<li data-type="skript"><a href="https://files.in-form-atik.ch/Grundlagen_Info/KI_und_Prompting/Skript_ohne_loesungen/output_book_ohne_loesungen_KI_und_Prompting.pdf">ohne Lösungen</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/KI_und_Prompting/Skript_ohne_loesungen/output_book_ohne_loesungen_KI_und_Prompting.log">Log</a></li>
</ul></div>
</div>
</details>
<details class="cf-topic" data-name="Kompression">
<summary>Kompression<span class="cf-count">Skript, 4 Foliensätze</span></summary>
<div class="cf-topic-body">
<div class="cf-section"><h3>Skript</h3><ul class="cf-list">
<li data-type="skript"><a href="https://files.in-form-atik.ch/Grundlagen_Info/Kompression/Skript_mit_loesungen/output_book_mit_loesungen_Kompression.pdf">mit Lösungen</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Kompression/Skript_mit_loesungen/output_book_mit_loesungen_Kompression.log">Log</a></li>
<li data-type="skript"><a href="https://files.in-form-atik.ch/Grundlagen_Info/Kompression/Skript_ohne_loesungen/output_book_ohne_loesungen_Kompression.pdf">ohne Lösungen</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Kompression/Skript_ohne_loesungen/output_book_ohne_loesungen_Kompression.log">Log</a></li>
</ul></div>
<div class="cf-section"><h3>Folien</h3><ul class="cf-list">
<li data-type="folien"><span class="cf-nr">01</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Kompression/Slides/01_Intro/output_beamer_01_Intro.pdf">Intro</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Kompression/Slides/01_Intro/output_beamer_01_Intro.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">02</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Kompression/Slides/02_Max_Bal/output_beamer_02_Max_Bal.pdf">Kodierung der maximalen Balance</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Kompression/Slides/02_Max_Bal/output_beamer_02_Max_Bal.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">03</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Kompression/Slides/03_Huffman/output_beamer_03_Huffman.pdf">Huffman</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Kompression/Slides/03_Huffman/output_beamer_03_Huffman.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">04</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Kompression/Slides/04_Arithm/output_beamer_04_Arithm.pdf">Arithmetische Kodierung</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Kompression/Slides/04_Arithm/output_beamer_04_Arithm.log">Log</a></li>
</ul></div>
</div>
</details>
<details class="cf-topic" data-name="Kryptologie">
<summary>Kryptologie<span class="cf-count">Skript, 17 Foliensätze</span></summary>
<div class="cf-topic-body">
<div class="cf-section"><h3>Skript</h3><ul class="cf-list">
<li data-type="skript"><a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Skript_mit_loesungen/output_book_mit_loesungen_Kryptologie.pdf">mit Lösungen</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Skript_mit_loesungen/output_book_mit_loesungen_Kryptologie.log">Log</a></li>
<li data-type="skript"><a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Skript_ohne_loesungen/output_book_ohne_loesungen_Kryptologie.pdf">ohne Lösungen</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Skript_ohne_loesungen/output_book_ohne_loesungen_Kryptologie.log">Log</a></li>
</ul></div>
<div class="cf-section"><h3>Folien</h3><ul class="cf-list">
<li data-type="folien"><span class="cf-nr">01</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/01_Slides_Kryptologie_Gf/output_beamer_01_Slides_Kryptologie_Gf.pdf">Kryptologie (Grundlagenfach)</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/01_Slides_Kryptologie_Gf/output_beamer_01_Slides_Kryptologie_Gf.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">02</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/02_Kryptologie_L01/output_beamer_02_Kryptologie_L01.pdf">Kryptologie L01</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/02_Kryptologie_L01/output_beamer_02_Kryptologie_L01.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">03</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/03_Kryptologie_L01prog/output_beamer_03_Kryptologie_L01prog.pdf">Kryptologie L01 Programmieren</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/03_Kryptologie_L01prog/output_beamer_03_Kryptologie_L01prog.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">04</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/04_L02a_Kryptoanalyse_Caesar/output_beamer_04_L02a_Kryptoanalyse_Caesar.pdf">L02a Kryptoanalyse Caesar</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/04_L02a_Kryptoanalyse_Caesar/output_beamer_04_L02a_Kryptoanalyse_Caesar.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">05</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/05_L02b_Kryptoanalyse_Monoalph/output_beamer_05_L02b_Kryptoanalyse_Monoalph.pdf">L02b Kryptoanalyse Monoalph</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/05_L02b_Kryptoanalyse_Monoalph/output_beamer_05_L02b_Kryptoanalyse_Monoalph.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">06</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/06_L02c_Kryptoanalyse_Vigenere/output_beamer_06_L02c_Kryptoanalyse_Vigenere.pdf">L02c Kryptoanalyse Vigenere</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/06_L02c_Kryptoanalyse_Vigenere/output_beamer_06_L02c_Kryptoanalyse_Vigenere.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">07</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/07_L02d_Kryptoanalyse_Vigenere_Kasiski/output_beamer_07_L02d_Kryptoanalyse_Vigenere_Kasiski.pdf">L02d Kryptoanalyse Vigenere Kasiski</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/07_L02d_Kryptoanalyse_Vigenere_Kasiski/output_beamer_07_L02d_Kryptoanalyse_Vigenere_Kasiski.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">08</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/08_L02e_Kryptoanalyse_Vigenere_Friedman/output_beamer_08_L02e_Kryptoanalyse_Vigenere_Friedman.pdf">L02e Kryptoanalyse Vigenere Friedman</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/08_L02e_Kryptoanalyse_Vigenere_Friedman/output_beamer_08_L02e_Kryptoanalyse_Vigenere_Friedman.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">09</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/09_L02f_Bin_OTP/output_beamer_09_L02f_Bin_OTP.pdf">L02f Binäres One-Time-Pad</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/09_L02f_Bin_OTP/output_beamer_09_L02f_Bin_OTP.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">10</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/10_L03a_Drei_Wege_Schluesseltausch/output_beamer_10_L03a_Drei_Wege_Schluesseltausch.pdf">L03a Drei-Wege-Schlüsseltausch</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/10_L03a_Drei_Wege_Schluesseltausch/output_beamer_10_L03a_Drei_Wege_Schluesseltausch.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">11</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/11_L03b_Diffie_Hellman_Merkle/output_beamer_11_L03b_Diffie_Hellman_Merkle.pdf">L03b Diffie-Hellman-Merkle</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/11_L03b_Diffie_Hellman_Merkle/output_beamer_11_L03b_Diffie_Hellman_Merkle.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">12</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/12_Kryptologie_L04/output_beamer_12_Kryptologie_L04.pdf">Kryptologie L04</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/12_Kryptologie_L04/output_beamer_12_Kryptologie_L04.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">13</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/13_L04a_Asymmetrische_Kryptosysteme_RSA/output_beamer_13_L04a_Asymmetrische_Kryptosysteme_RSA.pdf">L04a Asymmetrische Kryptosysteme RSA</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/13_L04a_Asymmetrische_Kryptosysteme_RSA/output_beamer_13_L04a_Asymmetrische_Kryptosysteme_RSA.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">14</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/14_L04b_Digitale_Signaturen_RSA/output_beamer_14_L04b_Digitale_Signaturen_RSA.pdf">L04b Digitale Signaturen RSA</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/14_L04b_Digitale_Signaturen_RSA/output_beamer_14_L04b_Digitale_Signaturen_RSA.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">15</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/15_Kryptologie_L05/output_beamer_15_Kryptologie_L05.pdf">Kryptologie L05</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/15_Kryptologie_L05/output_beamer_15_Kryptologie_L05.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">16</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/16_L05_Digitale_Zertifikate_PKI/output_beamer_16_L05_Digitale_Zertifikate_PKI.pdf">L05 Digitale Zertifikate PKI</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/16_L05_Digitale_Zertifikate_PKI/output_beamer_16_L05_Digitale_Zertifikate_PKI.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">17</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/17_Appendix/output_beamer_17_Appendix.pdf">Appendix</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/17_Appendix/output_beamer_17_Appendix.log">Log</a></li>
</ul></div>
</div>
</details>
<details class="cf-topic" data-name="Netzwerke">
<summary>Netzwerke<span class="cf-count">Skript, 7 Foliensätze</span></summary>
<div class="cf-topic-body">
<div class="cf-section"><h3>Skript</h3><ul class="cf-list">
<li data-type="skript"><a href="https://files.in-form-atik.ch/Grundlagen_Info/Netzwerke/Skript_mit_loesungen/output_book_mit_loesungen_Netzwerke.pdf">mit Lösungen</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Netzwerke/Skript_mit_loesungen/output_book_mit_loesungen_Netzwerke.log">Log</a></li>
<li data-type="skript"><a href="https://files.in-form-atik.ch/Grundlagen_Info/Netzwerke/Skript_ohne_loesungen/output_book_ohne_loesungen_Netzwerke.pdf">ohne Lösungen</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Netzwerke/Skript_ohne_loesungen/output_book_ohne_loesungen_Netzwerke.log">Log</a></li>
</ul></div>
<div class="cf-section"><h3>Folien</h3><ul class="cf-list">
<li data-type="folien"><span class="cf-nr">00</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Netzwerke/Slides/00_Geschichte/output_beamer_00_Geschichte.pdf">Geschichte</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Netzwerke/Slides/00_Geschichte/output_beamer_00_Geschichte.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">01</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Netzwerke/Slides/01_Schichtenmodell/output_beamer_01_Schichtenmodell.pdf">Schichtenmodell</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Netzwerke/Slides/01_Schichtenmodell/output_beamer_01_Schichtenmodell.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">02</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Netzwerke/Slides/02_Netzzugangsschicht/output_beamer_02_Netzzugangsschicht.pdf">Netzzugangsschicht</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Netzwerke/Slides/02_Netzzugangsschicht/output_beamer_02_Netzzugangsschicht.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">03</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Netzwerke/Slides/03_Vermittlungsschicht/output_beamer_03_Vermittlungsschicht.pdf">Vermittlungsschicht</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Netzwerke/Slides/03_Vermittlungsschicht/output_beamer_03_Vermittlungsschicht.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">04</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Netzwerke/Slides/04_Transportschicht/output_beamer_04_Transportschicht.pdf">Transportschicht</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Netzwerke/Slides/04_Transportschicht/output_beamer_04_Transportschicht.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">05</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Netzwerke/Slides/05_Anwendungsschicht/output_beamer_05_Anwendungsschicht.pdf">Anwendungsschicht</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Netzwerke/Slides/05_Anwendungsschicht/output_beamer_05_Anwendungsschicht.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">06</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Netzwerke/Slides/06_Chat_Sockets/output_beamer_06_Chat_Sockets.pdf">Chat mit Sockets</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Netzwerke/Slides/06_Chat_Sockets/output_beamer_06_Chat_Sockets.log">Log</a></li>
</ul></div>
</div>
</details>
<details class="cf-topic" data-name="Programmieren">
<summary>Programmieren<span class="cf-count">Skript, 21 Foliensätze</span></summary>
<div class="cf-topic-body">
<div class="cf-section"><h3>Skript</h3><ul class="cf-list">
<li data-type="skript"><a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Skript_mit_loesungen/output_book_mit_loesungen_Programmieren.pdf">mit Lösungen</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Skript_mit_loesungen/output_book_mit_loesungen_Programmieren.log">Log</a></li>
<li data-type="skript"><a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Skript_ohne_loesungen/output_book_ohne_loesungen_Programmieren.pdf">ohne Lösungen</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Skript_ohne_loesungen/output_book_ohne_loesungen_Programmieren.log">Log</a></li>
</ul></div>
<div class="cf-section"><h3>Folien</h3><ul class="cf-list">
<li data-type="folien"><span class="cf-nr">01</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/01_K01K02Intro/output_beamer_01_K01K02Intro.pdf">K01/K02 Einführung</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/01_K01K02Intro/output_beamer_01_K01K02Intro.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">02</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/02_K03a_Variablen/output_beamer_02_K03a_Variablen.pdf">K03a Variablen</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/02_K03a_Variablen/output_beamer_02_K03a_Variablen.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">03</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/03_K03b_Input/output_beamer_03_K03b_Input.pdf">K03b Input</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/03_K03b_Input/output_beamer_03_K03b_Input.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">04</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/04_K03c_Modulo/output_beamer_04_K03c_Modulo.pdf">K03c Modulo</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/04_K03c_Modulo/output_beamer_04_K03c_Modulo.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">05</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/05_K04a_Funktionen/output_beamer_05_K04a_Funktionen.pdf">K04a Funktionen</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/05_K04a_Funktionen/output_beamer_05_K04a_Funktionen.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">06</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/06_K04b_Parameter/output_beamer_06_K04b_Parameter.pdf">K04b Parameter</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/06_K04b_Parameter/output_beamer_06_K04b_Parameter.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">07</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/07_K04c_Funktionen_Einzelne/output_beamer_07_K04c_Funktionen_Einzelne.pdf">K04c Funktionen Einzelne</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/07_K04c_Funktionen_Einzelne/output_beamer_07_K04c_Funktionen_Einzelne.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">08</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/08_K04c_Funktionen_Mehrere/output_beamer_08_K04c_Funktionen_Mehrere.pdf">K04c Funktionen Mehrere</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/08_K04c_Funktionen_Mehrere/output_beamer_08_K04c_Funktionen_Mehrere.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">09</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/09_K04Zeit_Tabellen/output_beamer_09_K04Zeit_Tabellen.pdf">K04 Zeittabellen</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/09_K04Zeit_Tabellen/output_beamer_09_K04Zeit_Tabellen.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">10</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/10_K05a_If_Elif_Else/output_beamer_10_K05a_If_Elif_Else.pdf">K05a if, elif, else</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/10_K05a_If_Elif_Else/output_beamer_10_K05a_If_Elif_Else.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">11</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/11_K05b_Logische_Operatoren/output_beamer_11_K05b_Logische_Operatoren.pdf">K05b Logische Operatoren</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/11_K05b_Logische_Operatoren/output_beamer_11_K05b_Logische_Operatoren.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">12</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/12_K05c_Negation/output_beamer_12_K05c_Negation.pdf">K05c Negation</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/12_K05c_Negation/output_beamer_12_K05c_Negation.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">13</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/13_K05d_Break_While/output_beamer_13_K05d_Break_While.pdf">K05d break und while</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/13_K05d_Break_While/output_beamer_13_K05d_Break_While.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">14</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/14_K06a_Listen/output_beamer_14_K06a_Listen.pdf">K06a Listen</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/14_K06a_Listen/output_beamer_14_K06a_Listen.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">15</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/15_K06b_Bubble_Sort/output_beamer_15_K06b_Bubble_Sort.pdf">K06b Bubble Sort</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/15_K06b_Bubble_Sort/output_beamer_15_K06b_Bubble_Sort.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">16</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/16_K06c_Binary_Search/output_beamer_16_K06c_Binary_Search.pdf">K06c Binary Search</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/16_K06c_Binary_Search/output_beamer_16_K06c_Binary_Search.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">17</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/17_K06d_Listen_Teil2/output_beamer_17_K06d_Listen_Teil2.pdf">K06d Listen, Teil 2</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/17_K06d_Listen_Teil2/output_beamer_17_K06d_Listen_Teil2.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">18</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/18_K06e_Dictionaries/output_beamer_18_K06e_Dictionaries.pdf">K06e Dictionaries</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/18_K06e_Dictionaries/output_beamer_18_K06e_Dictionaries.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">19</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/19_K06f_Sets/output_beamer_19_K06f_Sets.pdf">K06f Sets</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/19_K06f_Sets/output_beamer_19_K06f_Sets.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">20</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/20_K07Klassen/output_beamer_20_K07Klassen.pdf">K07 Klassen</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/20_K07Klassen/output_beamer_20_K07Klassen.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">21</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/21_Turtle_Grafik/output_beamer_21_Turtle_Grafik.pdf">Turtle Grafik</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/21_Turtle_Grafik/output_beamer_21_Turtle_Grafik.log">Log</a></li>
</ul></div>
</div>
</details>
<details class="cf-topic" data-name="Randomisierte Algorithmen">
<summary>Randomisierte Algorithmen<span class="cf-count">Skript</span></summary>
<div class="cf-topic-body">
<div class="cf-section"><h3>Skript</h3><ul class="cf-list">
<li data-type="skript"><a href="https://files.in-form-atik.ch/Grundlagen_Info/Randomisierte_Algorithmen/Skript_mit_loesungen/output_book_mit_loesungen_Randomisierte_Algorithmen.pdf">mit Lösungen</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Randomisierte_Algorithmen/Skript_mit_loesungen/output_book_mit_loesungen_Randomisierte_Algorithmen.log">Log</a></li>
<li data-type="skript"><a href="https://files.in-form-atik.ch/Grundlagen_Info/Randomisierte_Algorithmen/Skript_ohne_loesungen/output_book_ohne_loesungen_Randomisierte_Algorithmen.pdf">ohne Lösungen</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Randomisierte_Algorithmen/Skript_ohne_loesungen/output_book_ohne_loesungen_Randomisierte_Algorithmen.log">Log</a></li>
</ul></div>
</div>
</details>
<details class="cf-topic" data-name="Tabellenkalkulation">
<summary>Tabellenkalkulation<span class="cf-count">Skript</span></summary>
<div class="cf-topic-body">
<div class="cf-section"><h3>Skript</h3><ul class="cf-list">
<li data-type="skript"><a href="https://files.in-form-atik.ch/Grundlagen_Info/Tabellenkalkulation/Skript_mit_loesungen/output_book_mit_loesungen_Tabellenkalkulation.pdf">mit Lösungen</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Tabellenkalkulation/Skript_mit_loesungen/output_book_mit_loesungen_Tabellenkalkulation.log">Log</a></li>
<li data-type="skript"><a href="https://files.in-form-atik.ch/Grundlagen_Info/Tabellenkalkulation/Skript_ohne_loesungen/output_book_ohne_loesungen_Tabellenkalkulation.pdf">ohne Lösungen</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Tabellenkalkulation/Skript_ohne_loesungen/output_book_ohne_loesungen_Tabellenkalkulation.log">Log</a></li>
</ul></div>
</div>
</details>
<details class="cf-topic" data-name="Zahlendarstellungen und Kodierungen">
<summary>Zahlendarstellungen und Kodierungen<span class="cf-count">Skript, 5 Foliensätze</span></summary>
<div class="cf-topic-body">
<div class="cf-section"><h3>Skript</h3><ul class="cf-list">
<li data-type="skript"><a href="https://files.in-form-atik.ch/Grundlagen_Info/Zahlendarstellungen_und_Kodierungen/Skript_mit_loesungen/output_book_mit_loesungen_Zahlendarstellungen_und_Kodierungen.pdf">mit Lösungen</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Zahlendarstellungen_und_Kodierungen/Skript_mit_loesungen/output_book_mit_loesungen_Zahlendarstellungen_und_Kodierungen.log">Log</a></li>
<li data-type="skript"><a href="https://files.in-form-atik.ch/Grundlagen_Info/Zahlendarstellungen_und_Kodierungen/Skript_ohne_loesungen/output_book_ohne_loesungen_Zahlendarstellungen_und_Kodierungen.pdf">ohne Lösungen</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Zahlendarstellungen_und_Kodierungen/Skript_ohne_loesungen/output_book_ohne_loesungen_Zahlendarstellungen_und_Kodierungen.log">Log</a></li>
</ul></div>
<div class="cf-section"><h3>Folien</h3><ul class="cf-list">
<li data-type="folien"><span class="cf-nr">01</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Zahlendarstellungen_und_Kodierungen/Slides/01_Zahlensysteme_L01/output_beamer_01_Zahlensysteme_L01.pdf">Zahlensysteme L01</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Zahlendarstellungen_und_Kodierungen/Slides/01_Zahlensysteme_L01/output_beamer_01_Zahlensysteme_L01.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">02</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Zahlendarstellungen_und_Kodierungen/Slides/02_Zahlensysteme_L02/output_beamer_02_Zahlensysteme_L02.pdf">Zahlensysteme L02</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Zahlendarstellungen_und_Kodierungen/Slides/02_Zahlensysteme_L02/output_beamer_02_Zahlensysteme_L02.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">03</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Zahlendarstellungen_und_Kodierungen/Slides/03_Zahlensysteme_L03/output_beamer_03_Zahlensysteme_L03.pdf">Zahlensysteme L03</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Zahlendarstellungen_und_Kodierungen/Slides/03_Zahlensysteme_L03/output_beamer_03_Zahlensysteme_L03.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">04</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Zahlendarstellungen_und_Kodierungen/Slides/04_Zahlensysteme_L04/output_beamer_04_Zahlensysteme_L04.pdf">Zahlensysteme L04</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Zahlendarstellungen_und_Kodierungen/Slides/04_Zahlensysteme_L04/output_beamer_04_Zahlensysteme_L04.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">05</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Zahlendarstellungen_und_Kodierungen/Slides/05_Zahlensysteme_L05/output_beamer_05_Zahlensysteme_L05.pdf">Zahlensysteme L05</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Zahlendarstellungen_und_Kodierungen/Slides/05_Zahlensysteme_L05/output_beamer_05_Zahlensysteme_L05.log">Log</a></li>
</ul></div>
</div>
</details>
<details class="cf-topic" data-name="Diverses">
<summary>Diverses<span class="cf-count">2 Foliensätze</span></summary>
<div class="cf-topic-body">
<div class="cf-section"><h3>Folien</h3><ul class="cf-list">
<li data-type="folien"><span class="cf-nr">01</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Various/Slides/01_Semesterplanung_Slides/output_beamer_01_Semesterplanung_Slides.pdf">Semesterplanung</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Various/Slides/01_Semesterplanung_Slides/output_beamer_01_Semesterplanung_Slides.log">Log</a></li>
<li data-type="folien"><span class="cf-nr">02</span><a href="https://files.in-form-atik.ch/Grundlagen_Info/Various/Slides/02_Intro_FDU/output_beamer_02_Intro_FDU.pdf">Intro FDU</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/Various/Slides/02_Intro_FDU/output_beamer_02_Intro_FDU.log">Log</a></li>
</ul></div>
</div>
</details>
<details class="cf-topic" data-name="Weitere Dokumente">
<summary>Weitere Dokumente<span class="cf-count">7 Dokumente</span></summary>
<div class="cf-topic-body">
<div class="cf-section"><ul class="cf-list">
<li data-type="artikel"><a href="https://files.in-form-atik.ch/Grundlagen_Info/article/Benotung/output_article_Benotung.pdf">Benotung</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/article/Benotung/output_article_Benotung.log">Log</a></li>
<li data-type="artikel"><a href="https://files.in-form-atik.ch/Grundlagen_Info/article/Benotung_FDU/output_article_Benotung_FDU.pdf">Benotung FDU</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/article/Benotung_FDU/output_article_Benotung_FDU.log">Log</a></li>
<li data-type="artikel"><a href="https://files.in-form-atik.ch/Grundlagen_Info/article/Excel-Projekte/output_article_Excel-Projekte.pdf">Excel-Projekte</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/article/Excel-Projekte/output_article_Excel-Projekte.log">Log</a></li>
<li data-type="artikel"><a href="https://files.in-form-atik.ch/Grundlagen_Info/article/Hannah_Fry/output_article_Hannah_Fry.pdf">Hannah Fry</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/article/Hannah_Fry/output_article_Hannah_Fry.log">Log</a></li>
<li data-type="artikel"><a href="https://files.in-form-atik.ch/Grundlagen_Info/article/Semesterplanung/output_article_Semesterplanung.pdf">Semesterplanung</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/article/Semesterplanung/output_article_Semesterplanung.log">Log</a></li>
<li data-type="artikel"><a href="https://files.in-form-atik.ch/Grundlagen_Info/article/Semesterplanung_FDU/output_article_Semesterplanung_FDU.pdf">Semesterplanung FDU</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/article/Semesterplanung_FDU/output_article_Semesterplanung_FDU.log">Log</a></li>
<li data-type="artikel"><a href="https://files.in-form-atik.ch/Grundlagen_Info/article/Vertiefungsthema/output_article_Vertiefungsthema.pdf">Vertiefungsthema</a><a class="cf-log" href="https://files.in-form-atik.ch/Grundlagen_Info/article/Vertiefungsthema/output_article_Vertiefungsthema.log">Log</a></li>
</ul></div>
</div>
</details>
</section>
<section class="cf-group">
<h2>Ergänzungsfach Informatik</h2>
<details class="cf-topic" data-name="Complexity">
<summary>Complexity<span class="cf-count">1 Foliensatz</span></summary>
<div class="cf-topic-body">
<div class="cf-section"><h3>Folien</h3><ul class="cf-list">
<li data-type="folien"><span class="cf-nr">01</span><a href="https://files.in-form-atik.ch/EF/Complexity/Slides/01_complexity/output_beamer_01_complexity.pdf">Complexity</a><a class="cf-log" href="https://files.in-form-atik.ch/EF/Complexity/Slides/01_complexity/output_beamer_01_complexity.log">Log</a></li>
</ul></div>
</div>
</details>
<details class="cf-topic" data-name="Endliche Automaten">
<summary>Endliche Automaten<span class="cf-count">Skript</span></summary>
<div class="cf-topic-body">
<div class="cf-section"><h3>Skript</h3><ul class="cf-list">
<li data-type="skript"><a href="https://files.in-form-atik.ch/EF/Endliche_Automaten/Skript_mit_loesungen/output_book_mit_loesungen_Endliche_Automaten.pdf">mit Lösungen</a><a class="cf-log" href="https://files.in-form-atik.ch/EF/Endliche_Automaten/Skript_mit_loesungen/output_book_mit_loesungen_Endliche_Automaten.log">Log</a></li>
<li data-type="skript"><a href="https://files.in-form-atik.ch/EF/Endliche_Automaten/Skript_ohne_loesungen/output_book_ohne_loesungen_Endliche_Automaten.pdf">ohne Lösungen</a><a class="cf-log" href="https://files.in-form-atik.ch/EF/Endliche_Automaten/Skript_ohne_loesungen/output_book_ohne_loesungen_Endliche_Automaten.log">Log</a></li>
</ul></div>
</div>
</details>
<details class="cf-topic" data-name="Induktion und Rekursion">
<summary>Induktion und Rekursion<span class="cf-count">Skript</span></summary>
<div class="cf-topic-body">
<div class="cf-section"><h3>Skript</h3><ul class="cf-list">
<li data-type="skript"><a href="https://files.in-form-atik.ch/EF/Induktion_und_Rekursion/Skript_mit_loesungen/output_book_mit_loesungen_Induktion_und_Rekursion.pdf">mit Lösungen</a><a class="cf-log" href="https://files.in-form-atik.ch/EF/Induktion_und_Rekursion/Skript_mit_loesungen/output_book_mit_loesungen_Induktion_und_Rekursion.log">Log</a></li>
<li data-type="skript"><a href="https://files.in-form-atik.ch/EF/Induktion_und_Rekursion/Skript_ohne_loesungen/output_book_ohne_loesungen_Induktion_und_Rekursion.pdf">ohne Lösungen</a><a class="cf-log" href="https://files.in-form-atik.ch/EF/Induktion_und_Rekursion/Skript_ohne_loesungen/output_book_ohne_loesungen_Induktion_und_Rekursion.log">Log</a></li>
</ul></div>
</div>
</details>
<details class="cf-topic" data-name="Kolmogorov Komplexität">
<summary>Kolmogorov Komplexität<span class="cf-count">Skript</span></summary>
<div class="cf-topic-body">
<div class="cf-section"><h3>Skript</h3><ul class="cf-list">
<li data-type="skript"><a href="https://files.in-form-atik.ch/EF/Kolmogorov_Komplexitaet/Skript_mit_loesungen/output_book_mit_loesungen_Kolmogorov_Komplexitaet.pdf">mit Lösungen</a><a class="cf-log" href="https://files.in-form-atik.ch/EF/Kolmogorov_Komplexitaet/Skript_mit_loesungen/output_book_mit_loesungen_Kolmogorov_Komplexitaet.log">Log</a></li>
<li data-type="skript"><a href="https://files.in-form-atik.ch/EF/Kolmogorov_Komplexitaet/Skript_ohne_loesungen/output_book_ohne_loesungen_Kolmogorov_Komplexitaet.pdf">ohne Lösungen</a><a class="cf-log" href="https://files.in-form-atik.ch/EF/Kolmogorov_Komplexitaet/Skript_ohne_loesungen/output_book_ohne_loesungen_Kolmogorov_Komplexitaet.log">Log</a></li>
</ul></div>
</div>
</details>
<details class="cf-topic" data-name="LaTeX">
<summary>LaTeX<span class="cf-count">1 Foliensatz</span></summary>
<div class="cf-topic-body">
<div class="cf-section"><h3>Folien</h3><ul class="cf-list">
<li data-type="folien"><span class="cf-nr">01</span><a href="https://files.in-form-atik.ch/EF/La_Te_X/Slides/01_La_Te_X/output_beamer_01_La_Te_X.pdf">LaTeX</a><a class="cf-log" href="https://files.in-form-atik.ch/EF/La_Te_X/Slides/01_La_Te_X/output_beamer_01_La_Te_X.log">Log</a></li>
</ul></div>
</div>
</details>
<details class="cf-topic" data-name="Weitere Dokumente">
<summary>Weitere Dokumente<span class="cf-count">1 Dokument</span></summary>
<div class="cf-topic-body">
<div class="cf-section"><ul class="cf-list">
<li data-type="artikel"><a href="https://files.in-form-atik.ch/EF/article/Ergaenzungsfach_Ausschreibungstext/output_article_Ergaenzungsfach_Ausschreibungstext.pdf">Ergänzungsfach Ausschreibungstext</a><a class="cf-log" href="https://files.in-form-atik.ch/EF/article/Ergaenzungsfach_Ausschreibungstext/output_article_Ergaenzungsfach_Ausschreibungstext.log">Log</a></li>
</ul></div>
</div>
</details>
</section>
<section class="cf-group">
<h2>Freifach</h2>
<details class="cf-topic" data-name="Weitere Dokumente">
<summary>Weitere Dokumente<span class="cf-count">2 Dokumente</span></summary>
<div class="cf-topic-body">
<div class="cf-section"><ul class="cf-list">
<li data-type="artikel"><a href="https://files.in-form-atik.ch/FF/article/Freifach-Auftrag/output_article_Freifach-Auftrag.pdf">Freifach-Auftrag</a><a class="cf-log" href="https://files.in-form-atik.ch/FF/article/Freifach-Auftrag/output_article_Freifach-Auftrag.log">Log</a></li>
<li data-type="artikel"><a href="https://files.in-form-atik.ch/FF/article/Freifach-Git_Hub/output_article_Freifach-Git_Hub.pdf">Freifach-GitHub</a><a class="cf-log" href="https://files.in-form-atik.ch/FF/article/Freifach-Git_Hub/output_article_Freifach-Git_Hub.log">Log</a></li>
</ul></div>
</div>
</details>
</section>
<section class="cf-group">
<h2>Geografie</h2>
<details class="cf-topic" data-name="Geomorphologie">
<summary>Geomorphologie<span class="cf-count">Skript</span></summary>
<div class="cf-topic-body">
<div class="cf-section"><h3>Skript</h3><ul class="cf-list">
<li data-type="skript"><a href="https://files.in-form-atik.ch/Geografie/Geomorphologie/Skript_mit_loesungen/output_book_mit_loesungen_Geomorphologie.pdf">mit Lösungen</a><a class="cf-log" href="https://files.in-form-atik.ch/Geografie/Geomorphologie/Skript_mit_loesungen/output_book_mit_loesungen_Geomorphologie.log">Log</a></li>
<li data-type="skript"><a href="https://files.in-form-atik.ch/Geografie/Geomorphologie/Skript_ohne_loesungen/output_book_ohne_loesungen_Geomorphologie.pdf">ohne Lösungen</a><a class="cf-log" href="https://files.in-form-atik.ch/Geografie/Geomorphologie/Skript_ohne_loesungen/output_book_ohne_loesungen_Geomorphologie.log">Log</a></li>
</ul></div>
</div>
</details>
<details class="cf-topic" data-name="Stadtgeografie">
<summary>Stadtgeografie<span class="cf-count">Skript</span></summary>
<div class="cf-topic-body">
<div class="cf-section"><h3>Skript</h3><ul class="cf-list">
<li data-type="skript"><a href="https://files.in-form-atik.ch/Geografie/Stadtgeografie/Skript_mit_loesungen/output_book_mit_loesungen_Stadtgeografie.pdf">mit Lösungen</a><a class="cf-log" href="https://files.in-form-atik.ch/Geografie/Stadtgeografie/Skript_mit_loesungen/output_book_mit_loesungen_Stadtgeografie.log">Log</a></li>
<li data-type="skript"><a href="https://files.in-form-atik.ch/Geografie/Stadtgeografie/Skript_ohne_loesungen/output_book_ohne_loesungen_Stadtgeografie.pdf">ohne Lösungen</a><a class="cf-log" href="https://files.in-form-atik.ch/Geografie/Stadtgeografie/Skript_ohne_loesungen/output_book_ohne_loesungen_Stadtgeografie.log">Log</a></li>
</ul></div>
</div>
</details>
</section>
<section class="cf-group">
<h2>Interessenwochen</h2>
<details class="cf-topic" data-name="Weitere Dokumente">
<summary>Weitere Dokumente<span class="cf-count">2 Dokumente</span></summary>
<div class="cf-topic-body">
<div class="cf-section"><ul class="cf-list">
<li data-type="artikel"><a href="https://files.in-form-atik.ch/Interessenwochen/article/Interessenwoche_Ablauf/output_article_Interessenwoche_Ablauf.pdf">Interessenwoche Ablauf</a><a class="cf-log" href="https://files.in-form-atik.ch/Interessenwochen/article/Interessenwoche_Ablauf/output_article_Interessenwoche_Ablauf.log">Log</a></li>
<li data-type="artikel"><a href="https://files.in-form-atik.ch/Interessenwochen/article/Interessenwoche_Auftrag/output_article_Interessenwoche_Auftrag.pdf">Interessenwoche Auftrag</a><a class="cf-log" href="https://files.in-form-atik.ch/Interessenwochen/article/Interessenwoche_Auftrag/output_article_Interessenwoche_Auftrag.log">Log</a></li>
</ul></div>
</div>
</details>
</section>
<section class="cf-group">
<h2>Diverses</h2>
<details class="cf-topic" data-name="Wahlpflichtmodul Statistik">
<summary>Wahlpflichtmodul Statistik<span class="cf-count">Skript, 1 Foliensatz</span></summary>
<div class="cf-topic-body">
<div class="cf-section"><h3>Skript</h3><ul class="cf-list">
<li data-type="skript"><a href="https://files.in-form-atik.ch/Various/Wahlpflichtmodul_Statistik/Skript_mit_loesungen/output_book_mit_loesungen_Wahlpflichtmodul_Statistik.pdf">mit Lösungen</a><a class="cf-log" href="https://files.in-form-atik.ch/Various/Wahlpflichtmodul_Statistik/Skript_mit_loesungen/output_book_mit_loesungen_Wahlpflichtmodul_Statistik.log">Log</a></li>
<li data-type="skript"><a href="https://files.in-form-atik.ch/Various/Wahlpflichtmodul_Statistik/Skript_ohne_loesungen/output_book_ohne_loesungen_Wahlpflichtmodul_Statistik.pdf">ohne Lösungen</a><a class="cf-log" href="https://files.in-form-atik.ch/Various/Wahlpflichtmodul_Statistik/Skript_ohne_loesungen/output_book_ohne_loesungen_Wahlpflichtmodul_Statistik.log">Log</a></li>
</ul></div>
<div class="cf-section"><h3>Folien</h3><ul class="cf-list">
<li data-type="folien"><span class="cf-nr">01</span><a href="https://files.in-form-atik.ch/Various/Wahlpflichtmodul_Statistik/Slides/01_Deskriptive_Statistik/output_beamer_01_Deskriptive_Statistik.pdf">Deskriptive Statistik</a><a class="cf-log" href="https://files.in-form-atik.ch/Various/Wahlpflichtmodul_Statistik/Slides/01_Deskriptive_Statistik/output_beamer_01_Deskriptive_Statistik.log">Log</a></li>
</ul></div>
</div>
</details>
<details class="cf-topic" data-name="Weitere Dokumente">
<summary>Weitere Dokumente<span class="cf-count">6 Dokumente</span></summary>
<div class="cf-topic-body">
<div class="cf-section"><ul class="cf-list">
<li data-type="artikel"><a href="https://files.in-form-atik.ch/Various/article/Filme/output_article_Filme.pdf">Filme</a><a class="cf-log" href="https://files.in-form-atik.ch/Various/article/Filme/output_article_Filme.log">Log</a></li>
<li data-type="artikel"><a href="https://files.in-form-atik.ch/Various/article/Fun_Quotes/output_article_Fun_Quotes.pdf">Fun Quotes</a><a class="cf-log" href="https://files.in-form-atik.ch/Various/article/Fun_Quotes/output_article_Fun_Quotes.log">Log</a></li>
<li data-type="artikel"><a href="https://files.in-form-atik.ch/Various/article/MA_Thesis_Guidelines/output_article_MA_Thesis_Guidelines.pdf">MA Thesis Guidelines</a><a class="cf-log" href="https://files.in-form-atik.ch/Various/article/MA_Thesis_Guidelines/output_article_MA_Thesis_Guidelines.log">Log</a></li>
<li data-type="artikel"><a href="https://files.in-form-atik.ch/Various/article/MA_Thesis_Guidelines_de/output_article_MA_Thesis_Guidelines_de.pdf">MA Thesis Guidelines de</a><a class="cf-log" href="https://files.in-form-atik.ch/Various/article/MA_Thesis_Guidelines_de/output_article_MA_Thesis_Guidelines_de.log">Log</a></li>
<li data-type="artikel"><a href="https://files.in-form-atik.ch/Various/article/MA_Thesis_Ideas/output_article_MA_Thesis_Ideas.pdf">MA Thesis Ideas</a><a class="cf-log" href="https://files.in-form-atik.ch/Various/article/MA_Thesis_Ideas/output_article_MA_Thesis_Ideas.log">Log</a></li>
<li data-type="artikel"><a href="https://files.in-form-atik.ch/Various/article/Tabu/output_article_Tabu.pdf">Tabu</a><a class="cf-log" href="https://files.in-form-atik.ch/Various/article/Tabu/output_article_Tabu.log">Log</a></li>
</ul></div>
</div>
</details>
</section>
<!-- END generated -->

<p class="cf-empty cf-hidden" id="cf-none">Keine Dokumente gefunden.</p>

<script>
(function () {
  function init() {
    const search = document.getElementById('cf-search');
    const buttons = document.querySelectorAll('.cf-filter button');
    const items = document.querySelectorAll('.cf-list li');
    const topics = document.querySelectorAll('.cf-topic');
    const none = document.getElementById('cf-none');
    if (!search || !items.length) return;

    let filter = 'all';

    function apply() {
      const query = search.value.toLowerCase().trim();
      const active = query !== '' || filter !== 'all';
      let shown = 0;

      items.forEach(function (li) {
        /* Suche im Eintrag selbst und im Thema, damit «Datenbanken» alle Folien des Themas findet */
        const topic = li.closest('.cf-topic');
        const text = (li.textContent + ' ' + topic.dataset.name).toLowerCase();
        const ok = (filter === 'all' || li.dataset.type === filter) && (!query || text.includes(query));
        li.classList.toggle('cf-hidden', !ok);
        if (ok) shown++;
      });

      /* Zwischentitel, Themen und Fächer ohne sichtbare Einträge ausblenden */
      document.querySelectorAll('.cf-section').forEach(function (sec) {
        sec.classList.toggle('cf-hidden', !sec.querySelector('li:not(.cf-hidden)'));
      });
      topics.forEach(function (t) {
        const visible = !!t.querySelector('li:not(.cf-hidden)');
        t.classList.toggle('cf-hidden', !visible);
        if (active) t.open = visible;
      });
      document.querySelectorAll('.cf-group').forEach(function (g) {
        g.classList.toggle('cf-hidden', !g.querySelector('.cf-topic:not(.cf-hidden)'));
      });
      none.classList.toggle('cf-hidden', shown > 0);
    }

    search.addEventListener('input', apply);
    buttons.forEach(function (btn) {
      btn.addEventListener('click', function () {
        buttons.forEach(function (b) { b.classList.remove('active'); });
        btn.classList.add('active');
        filter = btn.dataset.filter;
        apply();
      });
    });
    document.getElementById('cf-open').addEventListener('click', function () {
      topics.forEach(function (t) { t.open = true; });
    });
    document.getElementById('cf-close').addEventListener('click', function () {
      topics.forEach(function (t) { t.open = false; });
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
</script>
