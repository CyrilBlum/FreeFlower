#!/usr/bin/env python3
"""Rebuild the PDF list in docs/compiled-files.md from files.in-form-atik.ch.

Crawls the directory listing of the file server, collects all compiled PDFs and
replaces everything between the BEGIN/END generated markers of the page, grouped
by subject and topic. CSS, text and JavaScript of the page stay untouched.
Run from the repository root:

    python3 docs/_scripts/update_compiled_files.py
"""

import datetime
import html
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

BASE_URL = "https://files.in-form-atik.ch/"
PAGE = Path(__file__).resolve().parents[1] / "compiled-files.md"

BEGIN = "<!-- BEGIN generated: docs/_scripts/update_compiled_files.py -->"
END = "<!-- END generated -->"

# Top-level folders in display order; unknown ones follow alphabetically
SUBJECTS = {
    "Grundlagen_Info": "Grundlagenfach Informatik",
    "EF": "Ergänzungsfach Informatik",
    "FF": "Freifach",
    "Geografie": "Geografie",
    "Interessenwochen": "Interessenwochen",
    "Various": "Diverses",
}
ARTICLES = "Weitere Dokumente"

# Folder segments whose display name cannot be derived mechanically
DISPLAY_FIXES = {
    "Various": "Diverses",
    "La_Te_X": "LaTeX",
    "LaTeX": "LaTeX",
    "Freifach-Git_Hub": "Freifach-GitHub",
}
# Words of folder names that need a manual fix: umlauts transliterated by
# compile_tex.sh, and acronyms the camel-case split would break
WORD_FIXES = {
    "ASCIIund": "ASCII und",
    "Datenintegritaet": "Datenintegrität",
    "Komplexitaet": "Komplexität",
    "Ergaenzungsfach": "Ergänzungsfach",
}

# Slide deck names derived from folder names that read badly as titles
DECK_LABELS = {
    "Was Ist Informatik": "Was ist Informatik?",
    "Basisgroessen und Stellenwert": "Basisgrössen und Stellenwert",
    "Binaer Rechnen und Bits": "Binär rechnen und Bits",
    "ASCII und UTF8": "ASCII und UTF-8",
    "Abstraktion Durch Graphen Kapitel01": "Abstraktion durch Graphen, Kapitel 1",
    "Abstraktion Durch Graphen Kapitel02": "Abstraktion durch Graphen, Kapitel 2",
    "correlation causation": "Korrelation und Kausalität",
    "linear regression": "Lineare Regression",
    "markov chains": "Markov-Ketten",
    "markov appendix": "Markov-Ketten, Anhang",
    "Max Bal": "Kodierung der maximalen Balance",
    "Arithm": "Arithmetische Kodierung",
    "Slides Kryptologie Gf": "Kryptologie (Grundlagenfach)",
    "Kryptologie L01prog": "Kryptologie L01 Programmieren",
    "L02f Bin OTP": "L02f Binäres One-Time-Pad",
    "L03a Drei Wege Schluesseltausch": "L03a Drei-Wege-Schlüsseltausch",
    "L03b Diffie Hellman Merkle": "L03b Diffie-Hellman-Merkle",
    "Chat Sockets": "Chat mit Sockets",
    "K01K02Intro": "K01/K02 Einführung",
    "K04Zeit Tabellen": "K04 Zeittabellen",
    "K05a If Elif Else": "K05a if, elif, else",
    "K05d Break While": "K05d break und while",
    "K06d Listen Teil2": "K06d Listen, Teil 2",
    "K07Klassen": "K07 Klassen",
    "Semesterplanung Slides": "Semesterplanung",
    "complexity": "Complexity",
}


def list_dir(url):
    """Return the hrefs of an nginx/Apache-style directory listing."""
    with urllib.request.urlopen(url, timeout=30) as response:
        text = response.read().decode("utf-8", "replace")
    hrefs = re.findall(r'href="([^"]+)"', text)
    return [h for h in hrefs if not h.startswith(("../", "?", "/", "http"))]


def crawl(url=BASE_URL):
    """Yield the server-relative paths of all PDFs below url."""
    for href in list_dir(url):
        if href.endswith("/"):
            yield from crawl(url + href)
        elif href.endswith(".pdf"):
            yield urllib.parse.unquote(url[len(BASE_URL):] + href)


def split_camel(text):
    """'WasIstInformatik' -> 'Was Ist Informatik' (keeps acronyms like ASCII, FDU)."""
    text = re.sub(r"(?<=[a-z])(?=[A-Z])", " ", text)
    return re.sub(r"(?<=[A-Z])(?=[A-Z][a-z])", " ", text)


def display_name(segment):
    if segment in DISPLAY_FIXES:
        return DISPLAY_FIXES[segment]
    words = []
    for word in segment.split("_"):
        words.append(WORD_FIXES[word] if word in WORD_FIXES else split_camel(word))
    return " ".join(w for w in words if w)


def classify(path):
    """Return (subject, topic, kind, name) for a server path.

    Layouts written by compile_tex.sh:
      LEVEL/Topic/Skript_mit_loesungen/output_book_….pdf
      LEVEL/Topic/Slides/NN_Deck/output_beamer_NN_Deck.pdf
      LEVEL/article/Name/output_article_Name.pdf
    """
    parts = path.split("/")
    subject, folder = parts[0], parts[-2]
    if parts[1] == "article":
        return subject, ARTICLES, "artikel", folder
    if "Slides" in parts[2:-1]:
        return subject, parts[1], "folien", folder
    return subject, parts[1], "skript", folder


def link(path, text):
    url = BASE_URL + urllib.parse.quote(path)
    return (f'<a href="{url}">{html.escape(text)}</a>'
            f'<a class="cf-log" href="{url[:-4]}.log">Log</a>')


def render_topic(name, docs):
    skripts = sorted(d for d in docs if d[0] == "skript")
    slides = sorted(d for d in docs if d[0] == "folien")
    articles = sorted(d for d in docs if d[0] == "artikel")

    summary = []
    if skripts:
        summary.append("Skript")
    if slides:
        summary.append(f"{len(slides)} Foliensätze" if len(slides) > 1 else "1 Foliensatz")
    if articles:
        summary.append(f"{len(articles)} Dokumente" if len(articles) > 1 else "1 Dokument")

    out = [f'<details class="cf-topic" data-name="{html.escape(name)}">',
           f'<summary>{html.escape(name)}<span class="cf-count">{", ".join(summary)}</span></summary>',
           '<div class="cf-topic-body">']
    if skripts:
        out.append('<div class="cf-section"><h3>Skript</h3><ul class="cf-list">')
        for _, folder, path in skripts:
            text = "mit Lösungen" if folder.endswith("mit_loesungen") else "ohne Lösungen"
            out.append(f'<li data-type="skript">{link(path, text)}</li>')
        out.append('</ul></div>')
    if slides:
        out.append('<div class="cf-section"><h3>Folien</h3><ul class="cf-list">')
        for _, folder, path in slides:
            match = re.match(r"(\d{2})_(.*)", folder)
            nr, deck = (match.group(1), match.group(2)) if match else ("", folder)
            out.append(f'<li data-type="folien"><span class="cf-nr">{nr}</span>'
                       f'{link(path, DECK_LABELS.get(display_name(deck), display_name(deck)))}</li>')
        out.append('</ul></div>')
    if articles:
        out.append('<div class="cf-section"><ul class="cf-list">')
        for _, folder, path in sorted(articles, key=lambda d: display_name(d[1]).lower()):
            out.append(f'<li data-type="artikel">{link(path, display_name(folder))}</li>')
        out.append('</ul></div>')
    out.append('</div>')
    out.append('</details>')
    return out


def render(paths):
    groups = {}
    for path in paths:
        subject, topic, kind, folder = classify(path)
        groups.setdefault(subject, {}).setdefault(topic, []).append((kind, folder, path))

    order = list(SUBJECTS) + sorted(s for s in groups if s not in SUBJECTS)
    today = datetime.date.today().strftime("%d.%m.%Y")
    out = [f'<p class="cf-count">Stand {today}, {len(paths)} PDFs.</p>']
    for subject in (s for s in order if s in groups):
        topics = groups[subject]
        out.append('<section class="cf-group">')
        out.append(f'<h2>{html.escape(SUBJECTS.get(subject, display_name(subject)))}</h2>')
        # Topics alphabetically, «Diverses» and the article collection at the end
        names = {t: (ARTICLES if t == ARTICLES else display_name(t)) for t in topics}
        tail = {"Diverses": 1, ARTICLES: 2}
        for topic in sorted(topics, key=lambda t: (tail.get(names[t], 0), names[t].lower())):
            out.extend(render_topic(names[topic], topics[topic]))
        out.append('</section>')
    return "\n".join(out)


def main():
    paths = sorted(crawl())
    if not paths:
        sys.exit("No PDFs found on the server, page left unchanged.")

    page = PAGE.read_text(encoding="utf-8")
    start = page.index(BEGIN) + len(BEGIN)
    end = page.index(END)
    page = page[:start] + "\n" + render(paths) + "\n" + page[end:]
    PAGE.write_text(page, encoding="utf-8")

    kinds = [classify(p)[2] for p in paths]
    print(f"{len(paths)} PDFs: {kinds.count('skript')} Skripte, {kinds.count('folien')} Folien, "
          f"{kinds.count('artikel')} weitere")


if __name__ == "__main__":
    main()
