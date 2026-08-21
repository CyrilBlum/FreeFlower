---
layout: default
title: Skripte und Slides
nav_order: 1
---

<style>
.compiled-files-container {
  margin-top: 1rem;
}

.pdf-hidden {
  display: none !important;
}

.pdf-stats-bar {
  background: var(--btn-primary-bg, #f3f4f6);
  border: 1px solid var(--border-color, #e5e7eb);
  border-radius: 8px;
  padding: 0.85rem 1.1rem;
  margin-bottom: 1.25rem;
  font-size: 0.93rem;
}

.pdf-stats-title {
  font-weight: 600;
  margin-bottom: 0.4rem;
}

.pdf-stats-badges {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
}

.pdf-badge {
  background: #e2e8f0;
  color: #1e293b;
  padding: 0.2rem 0.55rem;
  border-radius: 9999px;
  font-size: 0.82rem;
  font-weight: 500;
}

.pdf-controls {
  display: flex;
  flex-wrap: wrap;
  gap: 0.6rem;
  align-items: center;
  margin-bottom: 1.25rem;
}

.pdf-search-input {
  flex: 1 1 240px;
  padding: 0.45rem 0.85rem;
  border: 1px solid var(--border-color, #cbd5e1);
  border-radius: 6px;
  font-size: 0.92rem;
  background: var(--bg-color, #ffffff);
  color: var(--text-color, #0f172a);
}

.pdf-search-input:focus {
  outline: none;
  border-color: #3b82f6;
  box-shadow: 0 0 0 2px rgba(59, 130, 246, 0.2);
}

.pdf-filter-btn, .pdf-action-btn {
  background: #ffffff;
  border: 1px solid #cbd5e1;
  color: #334155;
  padding: 0.4rem 0.75rem;
  border-radius: 6px;
  font-size: 0.86rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.15s ease;
}

.pdf-filter-btn:hover, .pdf-action-btn:hover {
  background: #f1f5f9;
  border-color: #94a3b8;
}

.pdf-filter-btn.active {
  background: #2563eb;
  color: #ffffff;
  border-color: #2563eb;
}

.pdf-tree-node {
  margin: 0.35rem 0;
}

.pdf-tree-summary {
  cursor: pointer;
  padding: 0.3rem 0.5rem;
  border-radius: 4px;
  transition: background 0.15s ease;
}

.pdf-tree-summary:hover {
  background: rgba(0, 0, 0, 0.04);
}

.pdf-tree-folder {
  font-weight: 600;
}

.pdf-tree-count {
  opacity: .75;
  font-size: .88em;
  margin-left: 0.2rem;
}

.pdf-tree-children {
  margin-left: 1.15rem;
  padding-left: 0.85rem;
  border-left: 2px solid #e2e8f0;
}

.pdf-tree-files {
  margin: 0.4rem 0 0.6rem 0;
  padding-left: 0.5rem;
  list-style: none;
}

.pdf-tree-file {
  margin: 0.25rem 0;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  flex-wrap: wrap;
}

.pdf-file-link {
  text-decoration: none;
  font-weight: 500;
}

.pdf-file-link:hover {
  text-decoration: underline;
}

.pdf-log-link {
  font-size: 0.78rem;
  padding: 0.1rem 0.4rem;
  border-radius: 4px;
  background: #f1f5f9;
  color: #64748b;
  text-decoration: none;
  border: 1px solid #e2e8f0;
}

.pdf-log-link:hover {
  background: #e2e8f0;
  color: #334155;
}

@media (prefers-color-scheme: dark) {
  .pdf-stats-bar {
    background: #1e293b;
    border-color: #334155;
    color: #f8fafc;
  }
  .pdf-badge {
    background: #334155;
    color: #f1f5f9;
  }
  .pdf-search-input {
    background: #0f172a;
    border-color: #334155;
    color: #f8fafc;
  }
  .pdf-filter-btn, .pdf-action-btn {
    background: #1e293b;
    border-color: #334155;
    color: #cbd5e1;
  }
  .pdf-filter-btn:hover, .pdf-action-btn:hover {
    background: #334155;
    color: #f8fafc;
  }
  .pdf-tree-children {
    border-left-color: #334155;
  }
  .pdf-tree-summary:hover {
    background: rgba(255, 255, 255, 0.06);
  }
  .pdf-log-link {
    background: #1e293b;
    border-color: #334155;
    color: #94a3b8;
  }
  .pdf-log-link:hover {
    background: #334155;
    color: #f1f5f9;
  }
}
</style>

# Zugriff auf kompilierte Skripte und Slides

Diese Seite zeigt alle derzeit verfügbaren finalen PDF-Dateien von [files.in-form-atik.ch](https://files.in-form-atik.ch) als ausklappbare Ordnerstruktur.

<div class="compiled-files-container">
  <div class="pdf-stats-bar">
    <div class="pdf-stats-title">📊 Übersichtsstatistik (Stand: <strong>134 PDFs</strong>)</div>
    <div class="pdf-stats-badges">
      <span class="pdf-badge">EF: 9</span><span class="pdf-badge">FF: 2</span><span class="pdf-badge">Geografie: 4</span><span class="pdf-badge">Grundlagen Info: 108</span><span class="pdf-badge">Interessenwochen: 2</span><span class="pdf-badge">Various: 9</span>
    </div>
  </div>

  <div class="pdf-controls">
    <input type="text" id="pdf-search" class="pdf-search-input" placeholder="🔍 PDF oder Thema suchen..." aria-label="PDFs durchsuchen">
    <div style="display: flex; gap: 0.4rem; flex-wrap: wrap;">
      <button class="pdf-filter-btn active" data-filter="all" type="button">Alle (134)</button>
      <button class="pdf-filter-btn" data-filter="skript" type="button">📘 Skripte (38)</button>
      <button class="pdf-filter-btn" data-filter="folien" type="button">📊 Folien (78)</button>
      <button class="pdf-filter-btn" data-filter="artikel" type="button">📄 Artikel (18)</button>
    </div>
    <div style="display: flex; gap: 0.4rem; margin-left: auto;">
      <button class="pdf-action-btn" id="btn-expand-all" type="button">📂 Alle aufklappen</button>
      <button class="pdf-action-btn" id="btn-collapse-all" type="button">📁 Alle zuklappen</button>
    </div>
  </div>

  <div id="pdf-tree-root">
<details class="pdf-tree-node" data-level="0">
  <summary class="pdf-tree-summary"><span class="pdf-tree-folder">EF</span> <span class="pdf-tree-count">(9 PDFs)</span></summary>
  <div class="pdf-tree-children">
    <details class="pdf-tree-node" data-level="1">
      <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Complexity</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
      <div class="pdf-tree-children">
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Slides</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">complexity</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/EF/Complexity/Slides/complexity/output_beamer_complexity.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: complexity</a> <a href="https://files.in-form-atik.ch/EF/Complexity/Slides/complexity/output_beamer_complexity.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
          </div>
        </details>
      </div>
    </details>
    <details class="pdf-tree-node" data-level="1">
      <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Endliche Automaten</span> <span class="pdf-tree-count">(2 PDFs)</span></summary>
      <div class="pdf-tree-children">
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Skript mit Lösungen</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <ul class="pdf-tree-files">
              <li class="pdf-tree-file" data-type="skript">
                <a href="https://files.in-form-atik.ch/EF/Endliche_Automaten/Skript_mit_loesungen/output_book_mit_loesungen_Endliche_Automaten.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Skript mit Lösungen: Endliche Automaten</a> <a href="https://files.in-form-atik.ch/EF/Endliche_Automaten/Skript_mit_loesungen/output_book_mit_loesungen_Endliche_Automaten.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
              </li>
            </ul>
          </div>
        </details>
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Skript ohne Lösungen</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <ul class="pdf-tree-files">
              <li class="pdf-tree-file" data-type="skript">
                <a href="https://files.in-form-atik.ch/EF/Endliche_Automaten/Skript_ohne_loesungen/output_book_ohne_loesungen_Endliche_Automaten.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Skript ohne Lösungen: Endliche Automaten</a> <a href="https://files.in-form-atik.ch/EF/Endliche_Automaten/Skript_ohne_loesungen/output_book_ohne_loesungen_Endliche_Automaten.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
              </li>
            </ul>
          </div>
        </details>
      </div>
    </details>
    <details class="pdf-tree-node" data-level="1">
      <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Induktion und Rekursion</span> <span class="pdf-tree-count">(2 PDFs)</span></summary>
      <div class="pdf-tree-children">
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Skript mit Lösungen</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <ul class="pdf-tree-files">
              <li class="pdf-tree-file" data-type="skript">
                <a href="https://files.in-form-atik.ch/EF/Induktion_und_Rekursion/Skript_mit_loesungen/output_book_mit_loesungen_Induktion_und_Rekursion.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Skript mit Lösungen: Induktion und Rekursion</a> <a href="https://files.in-form-atik.ch/EF/Induktion_und_Rekursion/Skript_mit_loesungen/output_book_mit_loesungen_Induktion_und_Rekursion.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
              </li>
            </ul>
          </div>
        </details>
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Skript ohne Lösungen</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <ul class="pdf-tree-files">
              <li class="pdf-tree-file" data-type="skript">
                <a href="https://files.in-form-atik.ch/EF/Induktion_und_Rekursion/Skript_ohne_loesungen/output_book_ohne_loesungen_Induktion_und_Rekursion.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Skript ohne Lösungen: Induktion und Rekursion</a> <a href="https://files.in-form-atik.ch/EF/Induktion_und_Rekursion/Skript_ohne_loesungen/output_book_ohne_loesungen_Induktion_und_Rekursion.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
              </li>
            </ul>
          </div>
        </details>
      </div>
    </details>
    <details class="pdf-tree-node" data-level="1">
      <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Kolmogorov Komplexität</span> <span class="pdf-tree-count">(2 PDFs)</span></summary>
      <div class="pdf-tree-children">
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Skript mit Lösungen</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <ul class="pdf-tree-files">
              <li class="pdf-tree-file" data-type="skript">
                <a href="https://files.in-form-atik.ch/EF/Kolmogorov_Komplexitaet/Skript_mit_loesungen/output_book_mit_loesungen_Kolmogorov_Komplexitaet.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Skript mit Lösungen: Kolmogorov Komplexität</a> <a href="https://files.in-form-atik.ch/EF/Kolmogorov_Komplexitaet/Skript_mit_loesungen/output_book_mit_loesungen_Kolmogorov_Komplexitaet.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
              </li>
            </ul>
          </div>
        </details>
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Skript ohne Lösungen</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <ul class="pdf-tree-files">
              <li class="pdf-tree-file" data-type="skript">
                <a href="https://files.in-form-atik.ch/EF/Kolmogorov_Komplexitaet/Skript_ohne_loesungen/output_book_ohne_loesungen_Kolmogorov_Komplexitaet.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Skript ohne Lösungen: Kolmogorov Komplexität</a> <a href="https://files.in-form-atik.ch/EF/Kolmogorov_Komplexitaet/Skript_ohne_loesungen/output_book_ohne_loesungen_Kolmogorov_Komplexitaet.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
              </li>
            </ul>
          </div>
        </details>
      </div>
    </details>
    <details class="pdf-tree-node" data-level="1">
      <summary class="pdf-tree-summary"><span class="pdf-tree-folder">LaTeX</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
      <div class="pdf-tree-children">
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Slides</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">LaTeX</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/EF/La_Te_X/Slides/La_Te_X/output_beamer_La_Te_X.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: LaTeX</a> <a href="https://files.in-form-atik.ch/EF/La_Te_X/Slides/La_Te_X/output_beamer_La_Te_X.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
          </div>
        </details>
      </div>
    </details>
    <details class="pdf-tree-node" data-level="1">
      <summary class="pdf-tree-summary"><span class="pdf-tree-folder">article</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
      <div class="pdf-tree-children">
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Ergänzungsfach Ausschreibungstext</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <ul class="pdf-tree-files">
              <li class="pdf-tree-file" data-type="artikel">
                <a href="https://files.in-form-atik.ch/EF/article/Ergaenzungsfach_Ausschreibungstext/output_article_Ergaenzungsfach_Ausschreibungstext.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Artikel: Ergänzungsfach Ausschreibungstext</a> <a href="https://files.in-form-atik.ch/EF/article/Ergaenzungsfach_Ausschreibungstext/output_article_Ergaenzungsfach_Ausschreibungstext.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
              </li>
            </ul>
          </div>
        </details>
      </div>
    </details>
  </div>
</details>
<details class="pdf-tree-node" data-level="0">
  <summary class="pdf-tree-summary"><span class="pdf-tree-folder">FF</span> <span class="pdf-tree-count">(2 PDFs)</span></summary>
  <div class="pdf-tree-children">
    <details class="pdf-tree-node" data-level="1">
      <summary class="pdf-tree-summary"><span class="pdf-tree-folder">article</span> <span class="pdf-tree-count">(2 PDFs)</span></summary>
      <div class="pdf-tree-children">
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Freifach-Auftrag</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <ul class="pdf-tree-files">
              <li class="pdf-tree-file" data-type="artikel">
                <a href="https://files.in-form-atik.ch/FF/article/Freifach-Auftrag/output_article_Freifach-Auftrag.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Artikel: Freifach-Auftrag</a> <a href="https://files.in-form-atik.ch/FF/article/Freifach-Auftrag/output_article_Freifach-Auftrag.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
              </li>
            </ul>
          </div>
        </details>
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Freifach-GitHub</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <ul class="pdf-tree-files">
              <li class="pdf-tree-file" data-type="artikel">
                <a href="https://files.in-form-atik.ch/FF/article/Freifach-Git_Hub/output_article_Freifach-Git_Hub.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Artikel: Freifach-GitHub</a> <a href="https://files.in-form-atik.ch/FF/article/Freifach-Git_Hub/output_article_Freifach-Git_Hub.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
              </li>
            </ul>
          </div>
        </details>
      </div>
    </details>
  </div>
</details>
<details class="pdf-tree-node" data-level="0">
  <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Geografie</span> <span class="pdf-tree-count">(4 PDFs)</span></summary>
  <div class="pdf-tree-children">
    <details class="pdf-tree-node" data-level="1">
      <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Geomorphologie</span> <span class="pdf-tree-count">(2 PDFs)</span></summary>
      <div class="pdf-tree-children">
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Skript mit Lösungen</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <ul class="pdf-tree-files">
              <li class="pdf-tree-file" data-type="skript">
                <a href="https://files.in-form-atik.ch/Geografie/Geomorphologie/Skript_mit_loesungen/output_book_mit_loesungen_Geomorphologie.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Skript mit Lösungen: Geomorphologie</a> <a href="https://files.in-form-atik.ch/Geografie/Geomorphologie/Skript_mit_loesungen/output_book_mit_loesungen_Geomorphologie.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
              </li>
            </ul>
          </div>
        </details>
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Skript ohne Lösungen</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <ul class="pdf-tree-files">
              <li class="pdf-tree-file" data-type="skript">
                <a href="https://files.in-form-atik.ch/Geografie/Geomorphologie/Skript_ohne_loesungen/output_book_ohne_loesungen_Geomorphologie.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Skript ohne Lösungen: Geomorphologie</a> <a href="https://files.in-form-atik.ch/Geografie/Geomorphologie/Skript_ohne_loesungen/output_book_ohne_loesungen_Geomorphologie.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
              </li>
            </ul>
          </div>
        </details>
      </div>
    </details>
    <details class="pdf-tree-node" data-level="1">
      <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Stadtgeografie</span> <span class="pdf-tree-count">(2 PDFs)</span></summary>
      <div class="pdf-tree-children">
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Skript mit Lösungen</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <ul class="pdf-tree-files">
              <li class="pdf-tree-file" data-type="skript">
                <a href="https://files.in-form-atik.ch/Geografie/Stadtgeografie/Skript_mit_loesungen/output_book_mit_loesungen_Stadtgeografie.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Skript mit Lösungen: Stadtgeografie</a> <a href="https://files.in-form-atik.ch/Geografie/Stadtgeografie/Skript_mit_loesungen/output_book_mit_loesungen_Stadtgeografie.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
              </li>
            </ul>
          </div>
        </details>
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Skript ohne Lösungen</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <ul class="pdf-tree-files">
              <li class="pdf-tree-file" data-type="skript">
                <a href="https://files.in-form-atik.ch/Geografie/Stadtgeografie/Skript_ohne_loesungen/output_book_ohne_loesungen_Stadtgeografie.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Skript ohne Lösungen: Stadtgeografie</a> <a href="https://files.in-form-atik.ch/Geografie/Stadtgeografie/Skript_ohne_loesungen/output_book_ohne_loesungen_Stadtgeografie.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
              </li>
            </ul>
          </div>
        </details>
      </div>
    </details>
  </div>
</details>
<details class="pdf-tree-node" data-level="0">
  <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Grundlagen Info</span> <span class="pdf-tree-count">(108 PDFs)</span></summary>
  <div class="pdf-tree-children">
    <details class="pdf-tree-node" data-level="1">
      <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Computer und Kodierungen</span> <span class="pdf-tree-count">(7 PDFs)</span></summary>
      <div class="pdf-tree-children">
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Skript mit Lösungen</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <ul class="pdf-tree-files">
              <li class="pdf-tree-file" data-type="skript">
                <a href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Skript_mit_loesungen/output_book_mit_loesungen_Computer_und_Kodierungen.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Skript mit Lösungen: Computer und Kodierungen</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Skript_mit_loesungen/output_book_mit_loesungen_Computer_und_Kodierungen.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
              </li>
            </ul>
          </div>
        </details>
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Skript ohne Lösungen</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <ul class="pdf-tree-files">
              <li class="pdf-tree-file" data-type="skript">
                <a href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Skript_ohne_loesungen/output_book_ohne_loesungen_Computer_und_Kodierungen.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Skript ohne Lösungen: Computer und Kodierungen</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Skript_ohne_loesungen/output_book_ohne_loesungen_Computer_und_Kodierungen.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
              </li>
            </ul>
          </div>
        </details>
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Slides</span> <span class="pdf-tree-count">(5 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">L01 Was Ist Informatik</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Slides/L01_Was_Ist_Informatik/output_beamer_L01_Was_Ist_Informatik.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: L01 Was Ist Informatik</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Slides/L01_Was_Ist_Informatik/output_beamer_L01_Was_Ist_Informatik.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">L02 Basisgroessen und Stellenwert</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Slides/L02_Basisgroessen_und_Stellenwert/output_beamer_L02_Basisgroessen_und_Stellenwert.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: L02 Basisgroessen und Stellenwert</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Slides/L02_Basisgroessen_und_Stellenwert/output_beamer_L02_Basisgroessen_und_Stellenwert.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">L03 Umrechnung und Hex</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Slides/L03_Umrechnung_und_Hex/output_beamer_L03_Umrechnung_und_Hex.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: L03 Umrechnung und Hex</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Slides/L03_Umrechnung_und_Hex/output_beamer_L03_Umrechnung_und_Hex.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">L04 Binaer Rechnen und Bits</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Slides/L04_Binaer_Rechnen_und_Bits/output_beamer_L04_Binaer_Rechnen_und_Bits.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: L04 Binaer Rechnen und Bits</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Slides/L04_Binaer_Rechnen_und_Bits/output_beamer_L04_Binaer_Rechnen_und_Bits.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">L05 ASCIIund UTF8</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Slides/L05_ASCIIund_UTF8/output_beamer_L05_ASCIIund_UTF8.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: L05 ASCIIund UTF8</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Slides/L05_ASCIIund_UTF8/output_beamer_L05_ASCIIund_UTF8.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
          </div>
        </details>
      </div>
    </details>
    <details class="pdf-tree-node" data-level="1">
      <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Datenbanken</span> <span class="pdf-tree-count">(8 PDFs)</span></summary>
      <div class="pdf-tree-children">
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Skript mit Lösungen</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <ul class="pdf-tree-files">
              <li class="pdf-tree-file" data-type="skript">
                <a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenbanken/Skript_mit_loesungen/output_book_mit_loesungen_Datenbanken.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Skript mit Lösungen: Datenbanken</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenbanken/Skript_mit_loesungen/output_book_mit_loesungen_Datenbanken.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
              </li>
            </ul>
          </div>
        </details>
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Skript ohne Lösungen</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <ul class="pdf-tree-files">
              <li class="pdf-tree-file" data-type="skript">
                <a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenbanken/Skript_ohne_loesungen/output_book_ohne_loesungen_Datenbanken.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Skript ohne Lösungen: Datenbanken</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenbanken/Skript_ohne_loesungen/output_book_ohne_loesungen_Datenbanken.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
              </li>
            </ul>
          </div>
        </details>
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Slides</span> <span class="pdf-tree-count">(6 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">02b Slides Subqueries</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenbanken/Slides/02b_Slides_Subqueries/output_beamer_02b_Slides_Subqueries.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: 02b Slides Subqueries</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenbanken/Slides/02b_Slides_Subqueries/output_beamer_02b_Slides_Subqueries.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Slides DML</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenbanken/Slides/Slides_DML/output_beamer_Slides_DML.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: Slides DML</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenbanken/Slides/Slides_DML/output_beamer_Slides_DML.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Slides Game</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenbanken/Slides/Slides_Game/output_beamer_Slides_Game.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: Slides Game</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenbanken/Slides/Slides_Game/output_beamer_Slides_Game.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Slides Intro</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenbanken/Slides/Slides_Intro/output_beamer_Slides_Intro.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: Slides Intro</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenbanken/Slides/Slides_Intro/output_beamer_Slides_Intro.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Slides JOIN</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenbanken/Slides/Slides_JOIN/output_beamer_Slides_JOIN.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: Slides JOIN</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenbanken/Slides/Slides_JOIN/output_beamer_Slides_JOIN.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Slides SELECT</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenbanken/Slides/Slides_SELECT/output_beamer_Slides_SELECT.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: Slides SELECT</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenbanken/Slides/Slides_SELECT/output_beamer_Slides_SELECT.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
          </div>
        </details>
      </div>
    </details>
    <details class="pdf-tree-node" data-level="1">
      <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Datenbanken Cheatsheet</span> <span class="pdf-tree-count">(2 PDFs)</span></summary>
      <div class="pdf-tree-children">
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Skript mit Lösungen</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <ul class="pdf-tree-files">
              <li class="pdf-tree-file" data-type="skript">
                <a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenbanken_Cheatsheet/Skript_mit_loesungen/output_book_mit_loesungen_Datenbanken_Cheatsheet.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Skript mit Lösungen: Datenbanken Cheatsheet</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenbanken_Cheatsheet/Skript_mit_loesungen/output_book_mit_loesungen_Datenbanken_Cheatsheet.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
              </li>
            </ul>
          </div>
        </details>
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Skript ohne Lösungen</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <ul class="pdf-tree-files">
              <li class="pdf-tree-file" data-type="skript">
                <a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenbanken_Cheatsheet/Skript_ohne_loesungen/output_book_ohne_loesungen_Datenbanken_Cheatsheet.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Skript ohne Lösungen: Datenbanken Cheatsheet</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenbanken_Cheatsheet/Skript_ohne_loesungen/output_book_ohne_loesungen_Datenbanken_Cheatsheet.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
              </li>
            </ul>
          </div>
        </details>
      </div>
    </details>
    <details class="pdf-tree-node" data-level="1">
      <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Datenintegrität</span> <span class="pdf-tree-count">(7 PDFs)</span></summary>
      <div class="pdf-tree-children">
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Skript mit Lösungen</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <ul class="pdf-tree-files">
              <li class="pdf-tree-file" data-type="skript">
                <a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenintegritaet/Skript_mit_loesungen/output_book_mit_loesungen_Datenintegritaet.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Skript mit Lösungen: Datenintegrität</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenintegritaet/Skript_mit_loesungen/output_book_mit_loesungen_Datenintegritaet.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
              </li>
            </ul>
          </div>
        </details>
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Skript ohne Lösungen</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <ul class="pdf-tree-files">
              <li class="pdf-tree-file" data-type="skript">
                <a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenintegritaet/Skript_ohne_loesungen/output_book_ohne_loesungen_Datenintegritaet.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Skript ohne Lösungen: Datenintegrität</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenintegritaet/Skript_ohne_loesungen/output_book_ohne_loesungen_Datenintegritaet.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
              </li>
            </ul>
          </div>
        </details>
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Slides</span> <span class="pdf-tree-count">(5 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Fehlererkennung</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenintegritaet/Slides/Fehlererkennung/output_beamer_Fehlererkennung.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: Fehlererkennung</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenintegritaet/Slides/Fehlererkennung/output_beamer_Fehlererkennung.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Fehlerkorrektur</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenintegritaet/Slides/Fehlerkorrektur/output_beamer_Fehlerkorrektur.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: Fehlerkorrektur</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenintegritaet/Slides/Fehlerkorrektur/output_beamer_Fehlerkorrektur.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Intro</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenintegritaet/Slides/Intro/output_beamer_Intro.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: Intro</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenintegritaet/Slides/Intro/output_beamer_Intro.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Kartentrick</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenintegritaet/Slides/Kartentrick/output_beamer_Kartentrick.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: Kartentrick</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenintegritaet/Slides/Kartentrick/output_beamer_Kartentrick.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">RAID</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenintegritaet/Slides/RAID/output_beamer_RAID.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: RAID</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenintegritaet/Slides/RAID/output_beamer_RAID.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
          </div>
        </details>
      </div>
    </details>
    <details class="pdf-tree-node" data-level="1">
      <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Graphen</span> <span class="pdf-tree-count">(5 PDFs)</span></summary>
      <div class="pdf-tree-children">
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Slides</span> <span class="pdf-tree-count">(5 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Abstraktion Durch Graphen Kapitel01</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Graphen/Slides/Abstraktion_Durch_Graphen_Kapitel01/output_beamer_Abstraktion_Durch_Graphen_Kapitel01.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: Abstraktion Durch Graphen Kapitel01</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Graphen/Slides/Abstraktion_Durch_Graphen_Kapitel01/output_beamer_Abstraktion_Durch_Graphen_Kapitel01.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Abstraktion Durch Graphen Kapitel02</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Graphen/Slides/Abstraktion_Durch_Graphen_Kapitel02/output_beamer_Abstraktion_Durch_Graphen_Kapitel02.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: Abstraktion Durch Graphen Kapitel02</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Graphen/Slides/Abstraktion_Durch_Graphen_Kapitel02/output_beamer_Abstraktion_Durch_Graphen_Kapitel02.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Graphen L01</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Graphen/Slides/Graphen_L01/output_beamer_Graphen_L01.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: Graphen L01</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Graphen/Slides/Graphen_L01/output_beamer_Graphen_L01.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Graphen L02</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Graphen/Slides/Graphen_L02/output_beamer_Graphen_L02.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: Graphen L02</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Graphen/Slides/Graphen_L02/output_beamer_Graphen_L02.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Graphen L03</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Graphen/Slides/Graphen_L03/output_beamer_Graphen_L03.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: Graphen L03</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Graphen/Slides/Graphen_L03/output_beamer_Graphen_L03.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
          </div>
        </details>
      </div>
    </details>
    <details class="pdf-tree-node" data-level="1">
      <summary class="pdf-tree-summary"><span class="pdf-tree-folder">KI und Algorithmen</span> <span class="pdf-tree-count">(6 PDFs)</span></summary>
      <div class="pdf-tree-children">
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Skript mit Lösungen</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <ul class="pdf-tree-files">
              <li class="pdf-tree-file" data-type="skript">
                <a href="https://files.in-form-atik.ch/Grundlagen_Info/KI_und_Algorithmen/Skript_mit_loesungen/output_book_mit_loesungen_KI_und_Algorithmen.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Skript mit Lösungen: KI und Algorithmen</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/KI_und_Algorithmen/Skript_mit_loesungen/output_book_mit_loesungen_KI_und_Algorithmen.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
              </li>
            </ul>
          </div>
        </details>
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Skript ohne Lösungen</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <ul class="pdf-tree-files">
              <li class="pdf-tree-file" data-type="skript">
                <a href="https://files.in-form-atik.ch/Grundlagen_Info/KI_und_Algorithmen/Skript_ohne_loesungen/output_book_ohne_loesungen_KI_und_Algorithmen.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Skript ohne Lösungen: KI und Algorithmen</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/KI_und_Algorithmen/Skript_ohne_loesungen/output_book_ohne_loesungen_KI_und_Algorithmen.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
              </li>
            </ul>
          </div>
        </details>
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Slides</span> <span class="pdf-tree-count">(4 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">correlation causation</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/KI_und_Algorithmen/Slides/correlation_causation/output_beamer_correlation_causation.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: correlation causation</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/KI_und_Algorithmen/Slides/correlation_causation/output_beamer_correlation_causation.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">linear regression</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/KI_und_Algorithmen/Slides/linear_regression/output_beamer_linear_regression.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: linear regression</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/KI_und_Algorithmen/Slides/linear_regression/output_beamer_linear_regression.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">markov appendix</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/KI_und_Algorithmen/Slides/markov_appendix/output_beamer_markov_appendix.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: markov appendix</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/KI_und_Algorithmen/Slides/markov_appendix/output_beamer_markov_appendix.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">markov chains</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/KI_und_Algorithmen/Slides/markov_chains/output_beamer_markov_chains.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: markov chains</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/KI_und_Algorithmen/Slides/markov_chains/output_beamer_markov_chains.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
          </div>
        </details>
      </div>
    </details>
    <details class="pdf-tree-node" data-level="1">
      <summary class="pdf-tree-summary"><span class="pdf-tree-folder">KI und Prompting</span> <span class="pdf-tree-count">(2 PDFs)</span></summary>
      <div class="pdf-tree-children">
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Skript mit Lösungen</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <ul class="pdf-tree-files">
              <li class="pdf-tree-file" data-type="skript">
                <a href="https://files.in-form-atik.ch/Grundlagen_Info/KI_und_Prompting/Skript_mit_loesungen/output_book_mit_loesungen_KI_und_Prompting.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Skript mit Lösungen: KI und Prompting</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/KI_und_Prompting/Skript_mit_loesungen/output_book_mit_loesungen_KI_und_Prompting.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
              </li>
            </ul>
          </div>
        </details>
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Skript ohne Lösungen</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <ul class="pdf-tree-files">
              <li class="pdf-tree-file" data-type="skript">
                <a href="https://files.in-form-atik.ch/Grundlagen_Info/KI_und_Prompting/Skript_ohne_loesungen/output_book_ohne_loesungen_KI_und_Prompting.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Skript ohne Lösungen: KI und Prompting</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/KI_und_Prompting/Skript_ohne_loesungen/output_book_ohne_loesungen_KI_und_Prompting.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
              </li>
            </ul>
          </div>
        </details>
      </div>
    </details>
    <details class="pdf-tree-node" data-level="1">
      <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Kompression</span> <span class="pdf-tree-count">(6 PDFs)</span></summary>
      <div class="pdf-tree-children">
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Skript mit Lösungen</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <ul class="pdf-tree-files">
              <li class="pdf-tree-file" data-type="skript">
                <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kompression/Skript_mit_loesungen/output_book_mit_loesungen_Kompression.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Skript mit Lösungen: Kompression</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kompression/Skript_mit_loesungen/output_book_mit_loesungen_Kompression.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
              </li>
            </ul>
          </div>
        </details>
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Skript ohne Lösungen</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <ul class="pdf-tree-files">
              <li class="pdf-tree-file" data-type="skript">
                <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kompression/Skript_ohne_loesungen/output_book_ohne_loesungen_Kompression.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Skript ohne Lösungen: Kompression</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kompression/Skript_ohne_loesungen/output_book_ohne_loesungen_Kompression.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
              </li>
            </ul>
          </div>
        </details>
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Slides</span> <span class="pdf-tree-count">(4 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Kompression L01 Intro</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kompression/Slides/Kompression_L01_Intro/output_beamer_Kompression_L01_Intro.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: Kompression L01 Intro</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kompression/Slides/Kompression_L01_Intro/output_beamer_Kompression_L01_Intro.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Kompression L02 Max Bal</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kompression/Slides/Kompression_L02_Max_Bal/output_beamer_Kompression_L02_Max_Bal.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: Kompression L02 Max Bal</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kompression/Slides/Kompression_L02_Max_Bal/output_beamer_Kompression_L02_Max_Bal.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Kompression L03 Huffman</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kompression/Slides/Kompression_L03_Huffman/output_beamer_Kompression_L03_Huffman.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: Kompression L03 Huffman</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kompression/Slides/Kompression_L03_Huffman/output_beamer_Kompression_L03_Huffman.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Kompression L04 Arithm</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kompression/Slides/Kompression_L04_Arithm/output_beamer_Kompression_L04_Arithm.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: Kompression L04 Arithm</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kompression/Slides/Kompression_L04_Arithm/output_beamer_Kompression_L04_Arithm.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
          </div>
        </details>
      </div>
    </details>
    <details class="pdf-tree-node" data-level="1">
      <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Kryptologie</span> <span class="pdf-tree-count">(17 PDFs)</span></summary>
      <div class="pdf-tree-children">
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Skript mit Lösungen</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <ul class="pdf-tree-files">
              <li class="pdf-tree-file" data-type="skript">
                <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Skript_mit_loesungen/output_book_mit_loesungen_Kryptologie.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Skript mit Lösungen: Kryptologie</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Skript_mit_loesungen/output_book_mit_loesungen_Kryptologie.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
              </li>
            </ul>
          </div>
        </details>
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Skript ohne Lösungen</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <ul class="pdf-tree-files">
              <li class="pdf-tree-file" data-type="skript">
                <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Skript_ohne_loesungen/output_book_ohne_loesungen_Kryptologie.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Skript ohne Lösungen: Kryptologie</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Skript_ohne_loesungen/output_book_ohne_loesungen_Kryptologie.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
              </li>
            </ul>
          </div>
        </details>
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Slides</span> <span class="pdf-tree-count">(15 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Appendix</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/Appendix/output_beamer_Appendix.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: Appendix</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/Appendix/output_beamer_Appendix.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Kryptologie L01</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/Kryptologie_L01/output_beamer_Kryptologie_L01.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: Kryptologie L01</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/Kryptologie_L01/output_beamer_Kryptologie_L01.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Kryptologie L01prog</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/Kryptologie_L01prog/output_beamer_Kryptologie_L01prog.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: Kryptologie L01prog</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/Kryptologie_L01prog/output_beamer_Kryptologie_L01prog.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Kryptologie L04</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/Kryptologie_L04/output_beamer_Kryptologie_L04.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: Kryptologie L04</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/Kryptologie_L04/output_beamer_Kryptologie_L04.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">L02a Kryptoanalyse Caesar</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/L02a_Kryptoanalyse_Caesar/output_beamer_L02a_Kryptoanalyse_Caesar.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: L02a Kryptoanalyse Caesar</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/L02a_Kryptoanalyse_Caesar/output_beamer_L02a_Kryptoanalyse_Caesar.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">L02b Kryptoanalyse Monoalph</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/L02b_Kryptoanalyse_Monoalph/output_beamer_L02b_Kryptoanalyse_Monoalph.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: L02b Kryptoanalyse Monoalph</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/L02b_Kryptoanalyse_Monoalph/output_beamer_L02b_Kryptoanalyse_Monoalph.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">L02c Kryptoanalyse Vigenere</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/L02c_Kryptoanalyse_Vigenere/output_beamer_L02c_Kryptoanalyse_Vigenere.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: L02c Kryptoanalyse Vigenere</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/L02c_Kryptoanalyse_Vigenere/output_beamer_L02c_Kryptoanalyse_Vigenere.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">L02d Kryptoanalyse Vigenere Kasiski</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/L02d_Kryptoanalyse_Vigenere_Kasiski/output_beamer_L02d_Kryptoanalyse_Vigenere_Kasiski.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: L02d Kryptoanalyse Vigenere Kasiski</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/L02d_Kryptoanalyse_Vigenere_Kasiski/output_beamer_L02d_Kryptoanalyse_Vigenere_Kasiski.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">L02e Kryptoanalyse Vigenere Friedman</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/L02e_Kryptoanalyse_Vigenere_Friedman/output_beamer_L02e_Kryptoanalyse_Vigenere_Friedman.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: L02e Kryptoanalyse Vigenere Friedman</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/L02e_Kryptoanalyse_Vigenere_Friedman/output_beamer_L02e_Kryptoanalyse_Vigenere_Friedman.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">L02f Bin OTP</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/L02f_Bin_OTP/output_beamer_L02f_Bin_OTP.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: L02f Bin OTP</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/L02f_Bin_OTP/output_beamer_L02f_Bin_OTP.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">L03a Drei Wege Schluesseltausch</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/L03a_Drei_Wege_Schluesseltausch/output_beamer_L03a_Drei_Wege_Schluesseltausch.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: L03a Drei Wege Schluesseltausch</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/L03a_Drei_Wege_Schluesseltausch/output_beamer_L03a_Drei_Wege_Schluesseltausch.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">L03b Diffie Hellman Merkle</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/L03b_Diffie_Hellman_Merkle/output_beamer_L03b_Diffie_Hellman_Merkle.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: L03b Diffie Hellman Merkle</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/L03b_Diffie_Hellman_Merkle/output_beamer_L03b_Diffie_Hellman_Merkle.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">L04a Asymmetrische Kryptosysteme RSA</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/L04a_Asymmetrische_Kryptosysteme_RSA/output_beamer_L04a_Asymmetrische_Kryptosysteme_RSA.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: L04a Asymmetrische Kryptosysteme RSA</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/L04a_Asymmetrische_Kryptosysteme_RSA/output_beamer_L04a_Asymmetrische_Kryptosysteme_RSA.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">L04b Digitale Signaturen RSA</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/L04b_Digitale_Signaturen_RSA/output_beamer_L04b_Digitale_Signaturen_RSA.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: L04b Digitale Signaturen RSA</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/L04b_Digitale_Signaturen_RSA/output_beamer_L04b_Digitale_Signaturen_RSA.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Slides Kryptologie Gf</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/Slides_Kryptologie_Gf/output_beamer_Slides_Kryptologie_Gf.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: Slides Kryptologie Gf</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/Slides_Kryptologie_Gf/output_beamer_Slides_Kryptologie_Gf.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
          </div>
        </details>
      </div>
    </details>
    <details class="pdf-tree-node" data-level="1">
      <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Netzwerke</span> <span class="pdf-tree-count">(5 PDFs)</span></summary>
      <div class="pdf-tree-children">
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Skript mit Lösungen</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <ul class="pdf-tree-files">
              <li class="pdf-tree-file" data-type="skript">
                <a href="https://files.in-form-atik.ch/Grundlagen_Info/Netzwerke/Skript_mit_loesungen/output_book_mit_loesungen_Netzwerke.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Skript mit Lösungen: Netzwerke</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Netzwerke/Skript_mit_loesungen/output_book_mit_loesungen_Netzwerke.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
              </li>
            </ul>
          </div>
        </details>
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Skript ohne Lösungen</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <ul class="pdf-tree-files">
              <li class="pdf-tree-file" data-type="skript">
                <a href="https://files.in-form-atik.ch/Grundlagen_Info/Netzwerke/Skript_ohne_loesungen/output_book_ohne_loesungen_Netzwerke.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Skript ohne Lösungen: Netzwerke</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Netzwerke/Skript_ohne_loesungen/output_book_ohne_loesungen_Netzwerke.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
              </li>
            </ul>
          </div>
        </details>
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Slides</span> <span class="pdf-tree-count">(3 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Netzwerke L00</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Netzwerke/Slides/Netzwerke_L00/output_beamer_Netzwerke_L00.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: Netzwerke L00</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Netzwerke/Slides/Netzwerke_L00/output_beamer_Netzwerke_L00.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Netzwerke L01</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Netzwerke/Slides/Netzwerke_L01/output_beamer_Netzwerke_L01.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: Netzwerke L01</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Netzwerke/Slides/Netzwerke_L01/output_beamer_Netzwerke_L01.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Netzwerke L02</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Netzwerke/Slides/Netzwerke_L02/output_beamer_Netzwerke_L02.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: Netzwerke L02</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Netzwerke/Slides/Netzwerke_L02/output_beamer_Netzwerke_L02.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
          </div>
        </details>
      </div>
    </details>
    <details class="pdf-tree-node" data-level="1">
      <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Programmieren</span> <span class="pdf-tree-count">(23 PDFs)</span></summary>
      <div class="pdf-tree-children">
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Skript mit Lösungen</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <ul class="pdf-tree-files">
              <li class="pdf-tree-file" data-type="skript">
                <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Skript_mit_loesungen/output_book_mit_loesungen_Programmieren.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Skript mit Lösungen: Programmieren</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Skript_mit_loesungen/output_book_mit_loesungen_Programmieren.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
              </li>
            </ul>
          </div>
        </details>
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Skript ohne Lösungen</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <ul class="pdf-tree-files">
              <li class="pdf-tree-file" data-type="skript">
                <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Skript_ohne_loesungen/output_book_ohne_loesungen_Programmieren.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Skript ohne Lösungen: Programmieren</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Skript_ohne_loesungen/output_book_ohne_loesungen_Programmieren.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
              </li>
            </ul>
          </div>
        </details>
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Slides</span> <span class="pdf-tree-count">(21 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">K01K02Intro</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/K01K02Intro/output_beamer_K01K02Intro.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: K01K02Intro</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/K01K02Intro/output_beamer_K01K02Intro.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">K03a Variablen</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/K03a_Variablen/output_beamer_K03a_Variablen.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: K03a Variablen</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/K03a_Variablen/output_beamer_K03a_Variablen.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">K03b Input</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/K03b_Input/output_beamer_K03b_Input.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: K03b Input</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/K03b_Input/output_beamer_K03b_Input.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">K03c Modulo</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/K03c_Modulo/output_beamer_K03c_Modulo.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: K03c Modulo</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/K03c_Modulo/output_beamer_K03c_Modulo.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">K04Zeit Tabellen</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/K04Zeit_Tabellen/output_beamer_K04Zeit_Tabellen.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: K04Zeit Tabellen</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/K04Zeit_Tabellen/output_beamer_K04Zeit_Tabellen.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">K04a Funktionen</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/K04a_Funktionen/output_beamer_K04a_Funktionen.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: K04a Funktionen</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/K04a_Funktionen/output_beamer_K04a_Funktionen.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">K04b Parameter</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/K04b_Parameter/output_beamer_K04b_Parameter.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: K04b Parameter</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/K04b_Parameter/output_beamer_K04b_Parameter.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">K04c Funktionen Einzelne</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/K04c_Funktionen_Einzelne/output_beamer_K04c_Funktionen_Einzelne.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: K04c Funktionen Einzelne</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/K04c_Funktionen_Einzelne/output_beamer_K04c_Funktionen_Einzelne.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">K04c Funktionen Mehrere</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/K04c_Funktionen_Mehrere/output_beamer_K04c_Funktionen_Mehrere.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: K04c Funktionen Mehrere</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/K04c_Funktionen_Mehrere/output_beamer_K04c_Funktionen_Mehrere.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">K05a If Elif Else</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/K05a_If_Elif_Else/output_beamer_K05a_If_Elif_Else.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: K05a If Elif Else</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/K05a_If_Elif_Else/output_beamer_K05a_If_Elif_Else.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">K05b Logische Operatoren</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/K05b_Logische_Operatoren/output_beamer_K05b_Logische_Operatoren.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: K05b Logische Operatoren</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/K05b_Logische_Operatoren/output_beamer_K05b_Logische_Operatoren.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">K05c Negation</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/K05c_Negation/output_beamer_K05c_Negation.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: K05c Negation</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/K05c_Negation/output_beamer_K05c_Negation.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">K05d Break While</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/K05d_Break_While/output_beamer_K05d_Break_While.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: K05d Break While</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/K05d_Break_While/output_beamer_K05d_Break_While.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">K06a Listen</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/K06a_Listen/output_beamer_K06a_Listen.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: K06a Listen</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/K06a_Listen/output_beamer_K06a_Listen.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">K06b Bubble Sort</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/K06b_Bubble_Sort/output_beamer_K06b_Bubble_Sort.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: K06b Bubble Sort</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/K06b_Bubble_Sort/output_beamer_K06b_Bubble_Sort.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">K06c Binary Search</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/K06c_Binary_Search/output_beamer_K06c_Binary_Search.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: K06c Binary Search</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/K06c_Binary_Search/output_beamer_K06c_Binary_Search.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">K06d Listen Teil2</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/K06d_Listen_Teil2/output_beamer_K06d_Listen_Teil2.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: K06d Listen Teil2</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/K06d_Listen_Teil2/output_beamer_K06d_Listen_Teil2.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">K06e Dictionaries</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/K06e_Dictionaries/output_beamer_K06e_Dictionaries.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: K06e Dictionaries</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/K06e_Dictionaries/output_beamer_K06e_Dictionaries.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">K06f Sets</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/K06f_Sets/output_beamer_K06f_Sets.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: K06f Sets</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/K06f_Sets/output_beamer_K06f_Sets.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">K07Klassen</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/K07Klassen/output_beamer_K07Klassen.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: K07Klassen</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/K07Klassen/output_beamer_K07Klassen.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Turtle Grafik</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/Turtle_Grafik/output_beamer_Turtle_Grafik.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: Turtle Grafik</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/Turtle_Grafik/output_beamer_Turtle_Grafik.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
          </div>
        </details>
      </div>
    </details>
    <details class="pdf-tree-node" data-level="1">
      <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Randomisierte Algorithmen</span> <span class="pdf-tree-count">(2 PDFs)</span></summary>
      <div class="pdf-tree-children">
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Skript mit Lösungen</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <ul class="pdf-tree-files">
              <li class="pdf-tree-file" data-type="skript">
                <a href="https://files.in-form-atik.ch/Grundlagen_Info/Randomisierte_Algorithmen/Skript_mit_loesungen/output_book_mit_loesungen_Randomisierte_Algorithmen.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Skript mit Lösungen: Randomisierte Algorithmen</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Randomisierte_Algorithmen/Skript_mit_loesungen/output_book_mit_loesungen_Randomisierte_Algorithmen.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
              </li>
            </ul>
          </div>
        </details>
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Skript ohne Lösungen</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <ul class="pdf-tree-files">
              <li class="pdf-tree-file" data-type="skript">
                <a href="https://files.in-form-atik.ch/Grundlagen_Info/Randomisierte_Algorithmen/Skript_ohne_loesungen/output_book_ohne_loesungen_Randomisierte_Algorithmen.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Skript ohne Lösungen: Randomisierte Algorithmen</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Randomisierte_Algorithmen/Skript_ohne_loesungen/output_book_ohne_loesungen_Randomisierte_Algorithmen.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
              </li>
            </ul>
          </div>
        </details>
      </div>
    </details>
    <details class="pdf-tree-node" data-level="1">
      <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Tabellenkalkulation</span> <span class="pdf-tree-count">(2 PDFs)</span></summary>
      <div class="pdf-tree-children">
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Skript mit Lösungen</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <ul class="pdf-tree-files">
              <li class="pdf-tree-file" data-type="skript">
                <a href="https://files.in-form-atik.ch/Grundlagen_Info/Tabellenkalkulation/Skript_mit_loesungen/output_book_mit_loesungen_Tabellenkalkulation.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Skript mit Lösungen: Tabellenkalkulation</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Tabellenkalkulation/Skript_mit_loesungen/output_book_mit_loesungen_Tabellenkalkulation.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
              </li>
            </ul>
          </div>
        </details>
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Skript ohne Lösungen</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <ul class="pdf-tree-files">
              <li class="pdf-tree-file" data-type="skript">
                <a href="https://files.in-form-atik.ch/Grundlagen_Info/Tabellenkalkulation/Skript_ohne_loesungen/output_book_ohne_loesungen_Tabellenkalkulation.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Skript ohne Lösungen: Tabellenkalkulation</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Tabellenkalkulation/Skript_ohne_loesungen/output_book_ohne_loesungen_Tabellenkalkulation.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
              </li>
            </ul>
          </div>
        </details>
      </div>
    </details>
    <details class="pdf-tree-node" data-level="1">
      <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Various</span> <span class="pdf-tree-count">(2 PDFs)</span></summary>
      <div class="pdf-tree-children">
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Slides</span> <span class="pdf-tree-count">(2 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Intro FDU</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Various/Slides/Intro_FDU/output_beamer_Intro_FDU.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: Intro FDU</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Various/Slides/Intro_FDU/output_beamer_Intro_FDU.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Semesterplanung Slides</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Various/Slides/Semesterplanung_Slides/output_beamer_Semesterplanung_Slides.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: Semesterplanung Slides</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Various/Slides/Semesterplanung_Slides/output_beamer_Semesterplanung_Slides.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
          </div>
        </details>
      </div>
    </details>
    <details class="pdf-tree-node" data-level="1">
      <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Zahlendarstellungen und Kodierungen</span> <span class="pdf-tree-count">(7 PDFs)</span></summary>
      <div class="pdf-tree-children">
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Skript mit Lösungen</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <ul class="pdf-tree-files">
              <li class="pdf-tree-file" data-type="skript">
                <a href="https://files.in-form-atik.ch/Grundlagen_Info/Zahlendarstellungen_und_Kodierungen/Skript_mit_loesungen/output_book_mit_loesungen_Zahlendarstellungen_und_Kodierungen.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Skript mit Lösungen: Zahlendarstellungen und Kodierungen</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Zahlendarstellungen_und_Kodierungen/Skript_mit_loesungen/output_book_mit_loesungen_Zahlendarstellungen_und_Kodierungen.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
              </li>
            </ul>
          </div>
        </details>
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Skript ohne Lösungen</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <ul class="pdf-tree-files">
              <li class="pdf-tree-file" data-type="skript">
                <a href="https://files.in-form-atik.ch/Grundlagen_Info/Zahlendarstellungen_und_Kodierungen/Skript_ohne_loesungen/output_book_ohne_loesungen_Zahlendarstellungen_und_Kodierungen.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Skript ohne Lösungen: Zahlendarstellungen und Kodierungen</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Zahlendarstellungen_und_Kodierungen/Skript_ohne_loesungen/output_book_ohne_loesungen_Zahlendarstellungen_und_Kodierungen.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
              </li>
            </ul>
          </div>
        </details>
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Slides</span> <span class="pdf-tree-count">(5 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Zahlensysteme L01</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Zahlendarstellungen_und_Kodierungen/Slides/Zahlensysteme_L01/output_beamer_Zahlensysteme_L01.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: Zahlensysteme L01</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Zahlendarstellungen_und_Kodierungen/Slides/Zahlensysteme_L01/output_beamer_Zahlensysteme_L01.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Zahlensysteme L02</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Zahlendarstellungen_und_Kodierungen/Slides/Zahlensysteme_L02/output_beamer_Zahlensysteme_L02.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: Zahlensysteme L02</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Zahlendarstellungen_und_Kodierungen/Slides/Zahlensysteme_L02/output_beamer_Zahlensysteme_L02.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Zahlensysteme L03</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Zahlendarstellungen_und_Kodierungen/Slides/Zahlensysteme_L03/output_beamer_Zahlensysteme_L03.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: Zahlensysteme L03</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Zahlendarstellungen_und_Kodierungen/Slides/Zahlensysteme_L03/output_beamer_Zahlensysteme_L03.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Zahlensysteme L04</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Zahlendarstellungen_und_Kodierungen/Slides/Zahlensysteme_L04/output_beamer_Zahlensysteme_L04.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: Zahlensysteme L04</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Zahlendarstellungen_und_Kodierungen/Slides/Zahlensysteme_L04/output_beamer_Zahlensysteme_L04.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Zahlensysteme L05</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Zahlendarstellungen_und_Kodierungen/Slides/Zahlensysteme_L05/output_beamer_Zahlensysteme_L05.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: Zahlensysteme L05</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Zahlendarstellungen_und_Kodierungen/Slides/Zahlensysteme_L05/output_beamer_Zahlensysteme_L05.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
          </div>
        </details>
      </div>
    </details>
    <details class="pdf-tree-node" data-level="1">
      <summary class="pdf-tree-summary"><span class="pdf-tree-folder">article</span> <span class="pdf-tree-count">(7 PDFs)</span></summary>
      <div class="pdf-tree-children">
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Benotung</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <ul class="pdf-tree-files">
              <li class="pdf-tree-file" data-type="artikel">
                <a href="https://files.in-form-atik.ch/Grundlagen_Info/article/Benotung/output_article_Benotung.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Artikel: Benotung</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/article/Benotung/output_article_Benotung.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
              </li>
            </ul>
          </div>
        </details>
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Benotung FDU</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <ul class="pdf-tree-files">
              <li class="pdf-tree-file" data-type="artikel">
                <a href="https://files.in-form-atik.ch/Grundlagen_Info/article/Benotung_FDU/output_article_Benotung_FDU.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Artikel: Benotung FDU</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/article/Benotung_FDU/output_article_Benotung_FDU.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
              </li>
            </ul>
          </div>
        </details>
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Excel-Projekte</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <ul class="pdf-tree-files">
              <li class="pdf-tree-file" data-type="artikel">
                <a href="https://files.in-form-atik.ch/Grundlagen_Info/article/Excel-Projekte/output_article_Excel-Projekte.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Artikel: Excel-Projekte</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/article/Excel-Projekte/output_article_Excel-Projekte.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
              </li>
            </ul>
          </div>
        </details>
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Hannah Fry</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <ul class="pdf-tree-files">
              <li class="pdf-tree-file" data-type="artikel">
                <a href="https://files.in-form-atik.ch/Grundlagen_Info/article/Hannah_Fry/output_article_Hannah_Fry.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Artikel: Hannah Fry</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/article/Hannah_Fry/output_article_Hannah_Fry.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
              </li>
            </ul>
          </div>
        </details>
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Semesterplanung</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <ul class="pdf-tree-files">
              <li class="pdf-tree-file" data-type="artikel">
                <a href="https://files.in-form-atik.ch/Grundlagen_Info/article/Semesterplanung/output_article_Semesterplanung.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Artikel: Semesterplanung</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/article/Semesterplanung/output_article_Semesterplanung.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
              </li>
            </ul>
          </div>
        </details>
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Semesterplanung FDU</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <ul class="pdf-tree-files">
              <li class="pdf-tree-file" data-type="artikel">
                <a href="https://files.in-form-atik.ch/Grundlagen_Info/article/Semesterplanung_FDU/output_article_Semesterplanung_FDU.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Artikel: Semesterplanung FDU</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/article/Semesterplanung_FDU/output_article_Semesterplanung_FDU.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
              </li>
            </ul>
          </div>
        </details>
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Vertiefungsthema</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <ul class="pdf-tree-files">
              <li class="pdf-tree-file" data-type="artikel">
                <a href="https://files.in-form-atik.ch/Grundlagen_Info/article/Vertiefungsthema/output_article_Vertiefungsthema.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Artikel: Vertiefungsthema</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/article/Vertiefungsthema/output_article_Vertiefungsthema.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
              </li>
            </ul>
          </div>
        </details>
      </div>
    </details>
  </div>
</details>
<details class="pdf-tree-node" data-level="0">
  <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Interessenwochen</span> <span class="pdf-tree-count">(2 PDFs)</span></summary>
  <div class="pdf-tree-children">
    <details class="pdf-tree-node" data-level="1">
      <summary class="pdf-tree-summary"><span class="pdf-tree-folder">article</span> <span class="pdf-tree-count">(2 PDFs)</span></summary>
      <div class="pdf-tree-children">
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Interessenwoche Ablauf</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <ul class="pdf-tree-files">
              <li class="pdf-tree-file" data-type="artikel">
                <a href="https://files.in-form-atik.ch/Interessenwochen/article/Interessenwoche_Ablauf/output_article_Interessenwoche_Ablauf.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Artikel: Interessenwoche Ablauf</a> <a href="https://files.in-form-atik.ch/Interessenwochen/article/Interessenwoche_Ablauf/output_article_Interessenwoche_Ablauf.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
              </li>
            </ul>
          </div>
        </details>
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Interessenwoche Auftrag</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <ul class="pdf-tree-files">
              <li class="pdf-tree-file" data-type="artikel">
                <a href="https://files.in-form-atik.ch/Interessenwochen/article/Interessenwoche_Auftrag/output_article_Interessenwoche_Auftrag.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Artikel: Interessenwoche Auftrag</a> <a href="https://files.in-form-atik.ch/Interessenwochen/article/Interessenwoche_Auftrag/output_article_Interessenwoche_Auftrag.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
              </li>
            </ul>
          </div>
        </details>
      </div>
    </details>
  </div>
</details>
<details class="pdf-tree-node" data-level="0">
  <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Various</span> <span class="pdf-tree-count">(9 PDFs)</span></summary>
  <div class="pdf-tree-children">
    <details class="pdf-tree-node" data-level="1">
      <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Wahlpflichtmodul Statistik</span> <span class="pdf-tree-count">(3 PDFs)</span></summary>
      <div class="pdf-tree-children">
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Skript mit Lösungen</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <ul class="pdf-tree-files">
              <li class="pdf-tree-file" data-type="skript">
                <a href="https://files.in-form-atik.ch/Various/Wahlpflichtmodul_Statistik/Skript_mit_loesungen/output_book_mit_loesungen_Wahlpflichtmodul_Statistik.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Skript mit Lösungen: Wahlpflichtmodul Statistik</a> <a href="https://files.in-form-atik.ch/Various/Wahlpflichtmodul_Statistik/Skript_mit_loesungen/output_book_mit_loesungen_Wahlpflichtmodul_Statistik.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
              </li>
            </ul>
          </div>
        </details>
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Skript ohne Lösungen</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <ul class="pdf-tree-files">
              <li class="pdf-tree-file" data-type="skript">
                <a href="https://files.in-form-atik.ch/Various/Wahlpflichtmodul_Statistik/Skript_ohne_loesungen/output_book_ohne_loesungen_Wahlpflichtmodul_Statistik.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Skript ohne Lösungen: Wahlpflichtmodul Statistik</a> <a href="https://files.in-form-atik.ch/Various/Wahlpflichtmodul_Statistik/Skript_ohne_loesungen/output_book_ohne_loesungen_Wahlpflichtmodul_Statistik.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
              </li>
            </ul>
          </div>
        </details>
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Slides</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">K01 Deskriptive Statistik</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Various/Wahlpflichtmodul_Statistik/Slides/K01_Deskriptive_Statistik/output_beamer_K01_Deskriptive_Statistik.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien: K01 Deskriptive Statistik</a> <a href="https://files.in-form-atik.ch/Various/Wahlpflichtmodul_Statistik/Slides/K01_Deskriptive_Statistik/output_beamer_K01_Deskriptive_Statistik.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
          </div>
        </details>
      </div>
    </details>
    <details class="pdf-tree-node" data-level="1">
      <summary class="pdf-tree-summary"><span class="pdf-tree-folder">article</span> <span class="pdf-tree-count">(6 PDFs)</span></summary>
      <div class="pdf-tree-children">
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Filme</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <ul class="pdf-tree-files">
              <li class="pdf-tree-file" data-type="artikel">
                <a href="https://files.in-form-atik.ch/Various/article/Filme/output_article_Filme.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Artikel: Filme</a> <a href="https://files.in-form-atik.ch/Various/article/Filme/output_article_Filme.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
              </li>
            </ul>
          </div>
        </details>
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Fun Quotes</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <ul class="pdf-tree-files">
              <li class="pdf-tree-file" data-type="artikel">
                <a href="https://files.in-form-atik.ch/Various/article/Fun_Quotes/output_article_Fun_Quotes.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Artikel: Fun Quotes</a> <a href="https://files.in-form-atik.ch/Various/article/Fun_Quotes/output_article_Fun_Quotes.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
              </li>
            </ul>
          </div>
        </details>
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">MA Thesis Guidelines</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <ul class="pdf-tree-files">
              <li class="pdf-tree-file" data-type="artikel">
                <a href="https://files.in-form-atik.ch/Various/article/MA_Thesis_Guidelines/output_article_MA_Thesis_Guidelines.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Artikel: MA Thesis Guidelines</a> <a href="https://files.in-form-atik.ch/Various/article/MA_Thesis_Guidelines/output_article_MA_Thesis_Guidelines.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
              </li>
            </ul>
          </div>
        </details>
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">MA Thesis Guidelines de</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <ul class="pdf-tree-files">
              <li class="pdf-tree-file" data-type="artikel">
                <a href="https://files.in-form-atik.ch/Various/article/MA_Thesis_Guidelines_de/output_article_MA_Thesis_Guidelines_de.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Artikel: MA Thesis Guidelines de</a> <a href="https://files.in-form-atik.ch/Various/article/MA_Thesis_Guidelines_de/output_article_MA_Thesis_Guidelines_de.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
              </li>
            </ul>
          </div>
        </details>
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">MA Thesis Ideas</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <ul class="pdf-tree-files">
              <li class="pdf-tree-file" data-type="artikel">
                <a href="https://files.in-form-atik.ch/Various/article/MA_Thesis_Ideas/output_article_MA_Thesis_Ideas.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Artikel: MA Thesis Ideas</a> <a href="https://files.in-form-atik.ch/Various/article/MA_Thesis_Ideas/output_article_MA_Thesis_Ideas.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
              </li>
            </ul>
          </div>
        </details>
        <details class="pdf-tree-node" data-level="2">
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Tabu</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <ul class="pdf-tree-files">
              <li class="pdf-tree-file" data-type="artikel">
                <a href="https://files.in-form-atik.ch/Various/article/Tabu/output_article_Tabu.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Artikel: Tabu</a> <a href="https://files.in-form-atik.ch/Various/article/Tabu/output_article_Tabu.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
              </li>
            </ul>
          </div>
        </details>
      </div>
    </details>
  </div>
</details>
  </div>
</div>

<script>
(function() {
  function initPdfControls() {
    const searchInput = document.getElementById('pdf-search');
    const filterBtns = document.querySelectorAll('.pdf-filter-btn');
    const expandBtn = document.getElementById('btn-expand-all');
    const collapseBtn = document.getElementById('btn-collapse-all');
    const allFiles = document.querySelectorAll('.pdf-tree-file');
    const allNodes = document.querySelectorAll('.pdf-tree-node');

    if (!searchInput || !allFiles.length) return;

    let activeFilter = 'all';

    function applyFilter() {
      const query = searchInput.value.toLowerCase().trim();

      allFiles.forEach(file => {
        const docType = file.getAttribute('data-type');
        const text = (file.textContent || '').toLowerCase();
        const matchesFilter = (activeFilter === 'all' || docType === activeFilter);
        const matchesSearch = (!query || text.includes(query));

        if (matchesFilter && matchesSearch) {
          file.classList.remove('pdf-hidden');
        } else {
          file.classList.add('pdf-hidden');
        }
      });

      allNodes.forEach(node => {
        const visibleFiles = node.querySelectorAll('.pdf-tree-file:not(.pdf-hidden)');
        if (visibleFiles.length > 0) {
          node.classList.remove('pdf-hidden');
          if (query || activeFilter !== 'all') {
            node.open = true;
            node.setAttribute('open', '');
          }
        } else {
          if (query || activeFilter !== 'all') {
            node.classList.add('pdf-hidden');
            node.open = false;
            node.removeAttribute('open');
          } else {
            node.classList.remove('pdf-hidden');
          }
        }
      });
    }

    searchInput.addEventListener('input', applyFilter);
    searchInput.addEventListener('keyup', applyFilter);
    searchInput.addEventListener('change', applyFilter);

    filterBtns.forEach(btn => {
      btn.addEventListener('click', function(e) {
        e.preventDefault();
        filterBtns.forEach(b => b.classList.remove('active'));
        this.classList.add('active');
        activeFilter = this.getAttribute('data-filter') || 'all';
        applyFilter();
      });
    });

    if (expandBtn) {
      expandBtn.addEventListener('click', function(e) {
        e.preventDefault();
        allNodes.forEach(node => {
          node.classList.remove('pdf-hidden');
          node.open = true;
          node.setAttribute('open', '');
        });
      });
    }

    if (collapseBtn) {
      collapseBtn.addEventListener('click', function(e) {
        e.preventDefault();
        allNodes.forEach(node => {
          node.open = false;
          node.removeAttribute('open');
        });
      });
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initPdfControls);
  } else {
    initPdfControls();
  }
})();
</script>
