#!/usr/bin/env python3
"""Rebuild the PDF tree in docs/compiled-files.md from files.in-form-atik.ch.

Crawls the directory listing of the file server, collects all compiled PDFs and
replaces the statistics bar, the filter buttons and the tree between
``<div id="pdf-tree-root">`` and the closing container. CSS and JavaScript of the
page stay untouched. Run from the repository root:

    python3 docs/_scripts/update_compiled_files.py
"""

import html
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

BASE_URL = "https://files.in-form-atik.ch/"
PAGE = Path(__file__).resolve().parents[1] / "compiled-files.md"

# Folder segments whose display name cannot be derived mechanically
DISPLAY_FIXES = {
    "article": "Artikel",
    "Skript_mit_loesungen": "Skript mit Lösungen",
    "Skript_ohne_loesungen": "Skript ohne Lösungen",
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


def file_entry(path):
    """Return (data-type, label) for a PDF path."""
    parts = path.split("/")
    folder = parts[-2]
    if "/Slides/" in path:
        match = re.match(r"(\d{2})_(.*)", folder)
        if match:
            return "folien", f"Folien {match.group(1)}: {display_name(match.group(2))}"
        return "folien", f"Folien: {display_name(folder)}"
    if folder.startswith("Skript_"):
        return "skript", f"{display_name(folder)}: {display_name(parts[-3])}"
    return "artikel", f"Artikel: {display_name(folder)}"


def build_tree(paths):
    tree = {}
    for path in paths:
        node = tree
        for segment in path.split("/")[:-1]:
            node = node.setdefault(segment, {})
        node.setdefault(None, []).append(path)
    return tree


def count(node):
    return len(node.get(None, [])) + sum(count(v) for k, v in node.items() if k is not None)


def render(node, level, indent):
    pad = " " * indent
    out = []
    for segment in sorted(k for k in node if k is not None):
        child = node[segment]
        out.append(f'{pad}<details class="pdf-tree-node" data-level="{level}">')
        out.append(f'{pad}  <summary class="pdf-tree-summary"><span class="pdf-tree-folder">'
                   f'{html.escape(display_name(segment))}</span> <span class="pdf-tree-count">'
                   f'({count(child)} PDFs)</span></summary>')
        out.append(f'{pad}  <div class="pdf-tree-children">')
        out.extend(render(child, level + 1, indent + 4))
        out.append(f'{pad}  </div>')
        out.append(f'{pad}</details>')
    files = sorted(node.get(None, []))
    if files:
        out.append(f'{pad}<ul class="pdf-tree-files">')
        for path in files:
            doc_type, label = file_entry(path)
            pdf_url = BASE_URL + urllib.parse.quote(path)
            log_url = pdf_url[:-4] + ".log"
            out.append(f'{pad}  <li class="pdf-tree-file" data-type="{doc_type}">')
            out.append(f'{pad}    <a href="{pdf_url}" target="_blank" rel="noopener" class="pdf-file-link">'
                       f'📄 {html.escape(label)}</a> <a href="{log_url}" target="_blank" rel="noopener" '
                       f'class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>')
            out.append(f'{pad}  </li>')
        out.append(f'{pad}</ul>')
    return out


def main():
    paths = sorted(crawl())
    if not paths:
        sys.exit("No PDFs found on the server, page left unchanged.")
    tree = build_tree(paths)
    types = [file_entry(p)[0] for p in paths]
    total = len(paths)

    page = PAGE.read_text(encoding="utf-8")

    badges = "".join(f'<span class="pdf-badge">{html.escape(display_name(k))}: {count(tree[k])}</span>'
                     for k in sorted(tree) if k is not None)
    page = re.sub(r'(<div class="pdf-stats-title">.*?Stand: <strong>)\d+ PDFs',
                  rf"\g<1>{total} PDFs", page)
    page = re.sub(r'(<div class="pdf-stats-badges">\s*).*?(\s*</div>)',
                  lambda m: m.group(1) + badges + m.group(2), page, count=1, flags=re.S)
    for key, count_value in (("all", total), ("skript", types.count("skript")),
                             ("folien", types.count("folien")), ("artikel", types.count("artikel"))):
        page = re.sub(rf'(data-filter="{key}" type="button">[^<(]*\()\d+\)',
                      rf"\g<1>{count_value})", page)

    start = page.index('<div id="pdf-tree-root">') + len('<div id="pdf-tree-root">')
    end = page.index("\n<script>")
    tree_html = "\n".join(render(tree, 0, 0))
    page = page[:start] + "\n" + tree_html + "\n  </div>\n</div>\n" + page[end:]

    PAGE.write_text(page, encoding="utf-8")
    print(f"{total} PDFs: {types.count('skript')} Skripte, {types.count('folien')} Folien, "
          f"{types.count('artikel')} Artikel")


if __name__ == "__main__":
    main()
