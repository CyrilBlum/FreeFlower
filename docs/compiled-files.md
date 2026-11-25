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
    <div class="pdf-stats-title">📊 Übersichtsstatistik (Stand: <strong>148 PDFs</strong>)</div>
    <div class="pdf-stats-badges">
      <span class="pdf-badge">EF: 9</span><span class="pdf-badge">FF: 2</span><span class="pdf-badge">Geografie: 4</span><span class="pdf-badge">Grundlagen Info: 122</span><span class="pdf-badge">Interessenwochen: 2</span><span class="pdf-badge">Various: 9</span>
    </div>
  </div>

  <div class="pdf-controls">
    <input type="text" id="pdf-search" class="pdf-search-input" placeholder="🔍 PDF oder Thema suchen..." aria-label="PDFs durchsuchen">
    <div style="display: flex; gap: 0.4rem; flex-wrap: wrap;">
      <button class="pdf-filter-btn active" data-filter="all" type="button">Alle (148)</button>
      <button class="pdf-filter-btn" data-filter="skript" type="button">📘 Skripte (38)</button>
      <button class="pdf-filter-btn" data-filter="folien" type="button">📊 Folien (92)</button>
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
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">01 complexity</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/EF/Complexity/Slides/01_complexity/output_beamer_01_complexity.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 01: complexity</a> <a href="https://files.in-form-atik.ch/EF/Complexity/Slides/01_complexity/output_beamer_01_complexity.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
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
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">01 La Te X</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/EF/La_Te_X/Slides/01_La_Te_X/output_beamer_01_La_Te_X.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 01: LaTeX</a> <a href="https://files.in-form-atik.ch/EF/La_Te_X/Slides/01_La_Te_X/output_beamer_01_La_Te_X.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
          </div>
        </details>
      </div>
    </details>
    <details class="pdf-tree-node" data-level="1">
      <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Artikel</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
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
      <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Artikel</span> <span class="pdf-tree-count">(2 PDFs)</span></summary>
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
  <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Grundlagen Info</span> <span class="pdf-tree-count">(122 PDFs)</span></summary>
  <div class="pdf-tree-children">
    <details class="pdf-tree-node" data-level="1">
      <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Computer und Kodierungen</span> <span class="pdf-tree-count">(14 PDFs)</span></summary>
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
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Slides</span> <span class="pdf-tree-count">(12 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">01 Was Ist Informatik</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Slides/01_Was_Ist_Informatik/output_beamer_01_Was_Ist_Informatik.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 01: Was Ist Informatik</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Slides/01_Was_Ist_Informatik/output_beamer_01_Was_Ist_Informatik.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">02 Basisgroessen und Stellenwert</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Slides/02_Basisgroessen_und_Stellenwert/output_beamer_02_Basisgroessen_und_Stellenwert.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 02: Basisgroessen und Stellenwert</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Slides/02_Basisgroessen_und_Stellenwert/output_beamer_02_Basisgroessen_und_Stellenwert.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">03 Umrechnung und Hex</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Slides/03_Umrechnung_und_Hex/output_beamer_03_Umrechnung_und_Hex.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 03: Umrechnung und Hex</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Slides/03_Umrechnung_und_Hex/output_beamer_03_Umrechnung_und_Hex.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">04 Binaer Rechnen und Bits</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Slides/04_Binaer_Rechnen_und_Bits/output_beamer_04_Binaer_Rechnen_und_Bits.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 04: Binaer Rechnen und Bits</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Slides/04_Binaer_Rechnen_und_Bits/output_beamer_04_Binaer_Rechnen_und_Bits.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">05 ASCII und UTF8</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Slides/05_ASCIIund_UTF8/output_beamer_05_ASCIIund_UTF8.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 05: ASCII und UTF8</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Slides/05_ASCIIund_UTF8/output_beamer_05_ASCIIund_UTF8.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">06 Bilder und Farben</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Slides/06_Bilder_und_Farben/output_beamer_06_Bilder_und_Farben.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 06: Bilder und Farben</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Slides/06_Bilder_und_Farben/output_beamer_06_Bilder_und_Farben.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">07 Dateiformate und Speicher</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Slides/07_Dateiformate_und_Speicher/output_beamer_07_Dateiformate_und_Speicher.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 07: Dateiformate und Speicher</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Slides/07_Dateiformate_und_Speicher/output_beamer_07_Dateiformate_und_Speicher.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">08 Logische Gatter I</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Slides/08_Logische_Gatter_I/output_beamer_08_Logische_Gatter_I.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 08: Logische Gatter I</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Slides/08_Logische_Gatter_I/output_beamer_08_Logische_Gatter_I.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">09 Logische Gatter II</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Slides/09_Logische_Gatter_II/output_beamer_09_Logische_Gatter_II.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 09: Logische Gatter II</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Slides/09_Logische_Gatter_II/output_beamer_09_Logische_Gatter_II.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">10 Aufbau Computer I</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Slides/10_Aufbau_Computer_I/output_beamer_10_Aufbau_Computer_I.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 10: Aufbau Computer I</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Slides/10_Aufbau_Computer_I/output_beamer_10_Aufbau_Computer_I.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">11 Aufbau Computer II</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Slides/11_Aufbau_Computer_II/output_beamer_11_Aufbau_Computer_II.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 11: Aufbau Computer II</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Slides/11_Aufbau_Computer_II/output_beamer_11_Aufbau_Computer_II.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">12 Betriebssystem</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Slides/12_Betriebssystem/output_beamer_12_Betriebssystem.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 12: Betriebssystem</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Computer_und_Kodierungen/Slides/12_Betriebssystem/output_beamer_12_Betriebssystem.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
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
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">01 Intro</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenbanken/Slides/01_Intro/output_beamer_01_Intro.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 01: Intro</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenbanken/Slides/01_Intro/output_beamer_01_Intro.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">02 SELECT</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenbanken/Slides/02_SELECT/output_beamer_02_SELECT.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 02: SELECT</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenbanken/Slides/02_SELECT/output_beamer_02_SELECT.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">03 Subqueries</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenbanken/Slides/03_Subqueries/output_beamer_03_Subqueries.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 03: Subqueries</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenbanken/Slides/03_Subqueries/output_beamer_03_Subqueries.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">04 JOIN</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenbanken/Slides/04_JOIN/output_beamer_04_JOIN.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 04: JOIN</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenbanken/Slides/04_JOIN/output_beamer_04_JOIN.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">05 DML</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenbanken/Slides/05_DML/output_beamer_05_DML.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 05: DML</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenbanken/Slides/05_DML/output_beamer_05_DML.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">06 Game</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenbanken/Slides/06_Game/output_beamer_06_Game.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 06: Game</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenbanken/Slides/06_Game/output_beamer_06_Game.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
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
      <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Datenintegrität</span> <span class="pdf-tree-count">(8 PDFs)</span></summary>
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
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Slides</span> <span class="pdf-tree-count">(6 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">01 Intro</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenintegritaet/Slides/01_Intro/output_beamer_01_Intro.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 01: Intro</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenintegritaet/Slides/01_Intro/output_beamer_01_Intro.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">02 Fehlererkennung</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenintegritaet/Slides/02_Fehlererkennung/output_beamer_02_Fehlererkennung.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 02: Fehlererkennung</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenintegritaet/Slides/02_Fehlererkennung/output_beamer_02_Fehlererkennung.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">03 Fehlerkorrektur</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenintegritaet/Slides/03_Fehlerkorrektur/output_beamer_03_Fehlerkorrektur.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 03: Fehlerkorrektur</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenintegritaet/Slides/03_Fehlerkorrektur/output_beamer_03_Fehlerkorrektur.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">04 Kartentrick</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenintegritaet/Slides/04_Kartentrick/output_beamer_04_Kartentrick.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 04: Kartentrick</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenintegritaet/Slides/04_Kartentrick/output_beamer_04_Kartentrick.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">05 Hamming</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenintegritaet/Slides/05_Hamming/output_beamer_05_Hamming.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 05: Hamming</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenintegritaet/Slides/05_Hamming/output_beamer_05_Hamming.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">06 RAID</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenintegritaet/Slides/06_RAID/output_beamer_06_RAID.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 06: RAID</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Datenintegritaet/Slides/06_RAID/output_beamer_06_RAID.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
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
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">01 Graphen L01</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Graphen/Slides/01_Graphen_L01/output_beamer_01_Graphen_L01.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 01: Graphen L01</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Graphen/Slides/01_Graphen_L01/output_beamer_01_Graphen_L01.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">02 Graphen L02</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Graphen/Slides/02_Graphen_L02/output_beamer_02_Graphen_L02.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 02: Graphen L02</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Graphen/Slides/02_Graphen_L02/output_beamer_02_Graphen_L02.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">03 Graphen L03</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Graphen/Slides/03_Graphen_L03/output_beamer_03_Graphen_L03.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 03: Graphen L03</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Graphen/Slides/03_Graphen_L03/output_beamer_03_Graphen_L03.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">04 Abstraktion Durch Graphen Kapitel01</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Graphen/Slides/04_Abstraktion_Durch_Graphen_Kapitel01/output_beamer_04_Abstraktion_Durch_Graphen_Kapitel01.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 04: Abstraktion Durch Graphen Kapitel01</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Graphen/Slides/04_Abstraktion_Durch_Graphen_Kapitel01/output_beamer_04_Abstraktion_Durch_Graphen_Kapitel01.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">05 Abstraktion Durch Graphen Kapitel02</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Graphen/Slides/05_Abstraktion_Durch_Graphen_Kapitel02/output_beamer_05_Abstraktion_Durch_Graphen_Kapitel02.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 05: Abstraktion Durch Graphen Kapitel02</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Graphen/Slides/05_Abstraktion_Durch_Graphen_Kapitel02/output_beamer_05_Abstraktion_Durch_Graphen_Kapitel02.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
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
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">01 correlation causation</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/KI_und_Algorithmen/Slides/01_correlation_causation/output_beamer_01_correlation_causation.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 01: correlation causation</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/KI_und_Algorithmen/Slides/01_correlation_causation/output_beamer_01_correlation_causation.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">02 linear regression</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/KI_und_Algorithmen/Slides/02_linear_regression/output_beamer_02_linear_regression.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 02: linear regression</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/KI_und_Algorithmen/Slides/02_linear_regression/output_beamer_02_linear_regression.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">03 markov chains</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/KI_und_Algorithmen/Slides/03_markov_chains/output_beamer_03_markov_chains.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 03: markov chains</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/KI_und_Algorithmen/Slides/03_markov_chains/output_beamer_03_markov_chains.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">04 markov appendix</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/KI_und_Algorithmen/Slides/04_markov_appendix/output_beamer_04_markov_appendix.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 04: markov appendix</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/KI_und_Algorithmen/Slides/04_markov_appendix/output_beamer_04_markov_appendix.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
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
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">01 Intro</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kompression/Slides/01_Intro/output_beamer_01_Intro.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 01: Intro</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kompression/Slides/01_Intro/output_beamer_01_Intro.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">02 Max Bal</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kompression/Slides/02_Max_Bal/output_beamer_02_Max_Bal.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 02: Max Bal</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kompression/Slides/02_Max_Bal/output_beamer_02_Max_Bal.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">03 Huffman</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kompression/Slides/03_Huffman/output_beamer_03_Huffman.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 03: Huffman</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kompression/Slides/03_Huffman/output_beamer_03_Huffman.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">04 Arithm</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kompression/Slides/04_Arithm/output_beamer_04_Arithm.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 04: Arithm</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kompression/Slides/04_Arithm/output_beamer_04_Arithm.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
          </div>
        </details>
      </div>
    </details>
    <details class="pdf-tree-node" data-level="1">
      <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Kryptologie</span> <span class="pdf-tree-count">(19 PDFs)</span></summary>
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
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Slides</span> <span class="pdf-tree-count">(17 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">01 Slides Kryptologie Gf</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/01_Slides_Kryptologie_Gf/output_beamer_01_Slides_Kryptologie_Gf.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 01: Slides Kryptologie Gf</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/01_Slides_Kryptologie_Gf/output_beamer_01_Slides_Kryptologie_Gf.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">02 Kryptologie L01</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/02_Kryptologie_L01/output_beamer_02_Kryptologie_L01.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 02: Kryptologie L01</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/02_Kryptologie_L01/output_beamer_02_Kryptologie_L01.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">03 Kryptologie L01prog</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/03_Kryptologie_L01prog/output_beamer_03_Kryptologie_L01prog.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 03: Kryptologie L01prog</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/03_Kryptologie_L01prog/output_beamer_03_Kryptologie_L01prog.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">04 L02a Kryptoanalyse Caesar</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/04_L02a_Kryptoanalyse_Caesar/output_beamer_04_L02a_Kryptoanalyse_Caesar.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 04: L02a Kryptoanalyse Caesar</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/04_L02a_Kryptoanalyse_Caesar/output_beamer_04_L02a_Kryptoanalyse_Caesar.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">05 L02b Kryptoanalyse Monoalph</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/05_L02b_Kryptoanalyse_Monoalph/output_beamer_05_L02b_Kryptoanalyse_Monoalph.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 05: L02b Kryptoanalyse Monoalph</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/05_L02b_Kryptoanalyse_Monoalph/output_beamer_05_L02b_Kryptoanalyse_Monoalph.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">06 L02c Kryptoanalyse Vigenere</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/06_L02c_Kryptoanalyse_Vigenere/output_beamer_06_L02c_Kryptoanalyse_Vigenere.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 06: L02c Kryptoanalyse Vigenere</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/06_L02c_Kryptoanalyse_Vigenere/output_beamer_06_L02c_Kryptoanalyse_Vigenere.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">07 L02d Kryptoanalyse Vigenere Kasiski</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/07_L02d_Kryptoanalyse_Vigenere_Kasiski/output_beamer_07_L02d_Kryptoanalyse_Vigenere_Kasiski.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 07: L02d Kryptoanalyse Vigenere Kasiski</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/07_L02d_Kryptoanalyse_Vigenere_Kasiski/output_beamer_07_L02d_Kryptoanalyse_Vigenere_Kasiski.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">08 L02e Kryptoanalyse Vigenere Friedman</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/08_L02e_Kryptoanalyse_Vigenere_Friedman/output_beamer_08_L02e_Kryptoanalyse_Vigenere_Friedman.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 08: L02e Kryptoanalyse Vigenere Friedman</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/08_L02e_Kryptoanalyse_Vigenere_Friedman/output_beamer_08_L02e_Kryptoanalyse_Vigenere_Friedman.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">09 L02f Bin OTP</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/09_L02f_Bin_OTP/output_beamer_09_L02f_Bin_OTP.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 09: L02f Bin OTP</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/09_L02f_Bin_OTP/output_beamer_09_L02f_Bin_OTP.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">10 L03a Drei Wege Schluesseltausch</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/10_L03a_Drei_Wege_Schluesseltausch/output_beamer_10_L03a_Drei_Wege_Schluesseltausch.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 10: L03a Drei Wege Schluesseltausch</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/10_L03a_Drei_Wege_Schluesseltausch/output_beamer_10_L03a_Drei_Wege_Schluesseltausch.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">11 L03b Diffie Hellman Merkle</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/11_L03b_Diffie_Hellman_Merkle/output_beamer_11_L03b_Diffie_Hellman_Merkle.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 11: L03b Diffie Hellman Merkle</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/11_L03b_Diffie_Hellman_Merkle/output_beamer_11_L03b_Diffie_Hellman_Merkle.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">12 Kryptologie L04</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/12_Kryptologie_L04/output_beamer_12_Kryptologie_L04.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 12: Kryptologie L04</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/12_Kryptologie_L04/output_beamer_12_Kryptologie_L04.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">13 L04a Asymmetrische Kryptosysteme RSA</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/13_L04a_Asymmetrische_Kryptosysteme_RSA/output_beamer_13_L04a_Asymmetrische_Kryptosysteme_RSA.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 13: L04a Asymmetrische Kryptosysteme RSA</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/13_L04a_Asymmetrische_Kryptosysteme_RSA/output_beamer_13_L04a_Asymmetrische_Kryptosysteme_RSA.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">14 L04b Digitale Signaturen RSA</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/14_L04b_Digitale_Signaturen_RSA/output_beamer_14_L04b_Digitale_Signaturen_RSA.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 14: L04b Digitale Signaturen RSA</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/14_L04b_Digitale_Signaturen_RSA/output_beamer_14_L04b_Digitale_Signaturen_RSA.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">15 Kryptologie L05</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/15_Kryptologie_L05/output_beamer_15_Kryptologie_L05.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 15: Kryptologie L05</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/15_Kryptologie_L05/output_beamer_15_Kryptologie_L05.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">16 L05 Digitale Zertifikate PKI</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/16_L05_Digitale_Zertifikate_PKI/output_beamer_16_L05_Digitale_Zertifikate_PKI.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 16: L05 Digitale Zertifikate PKI</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/16_L05_Digitale_Zertifikate_PKI/output_beamer_16_L05_Digitale_Zertifikate_PKI.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">17 Appendix</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/17_Appendix/output_beamer_17_Appendix.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 17: Appendix</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Kryptologie/Slides/17_Appendix/output_beamer_17_Appendix.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
          </div>
        </details>
      </div>
    </details>
    <details class="pdf-tree-node" data-level="1">
      <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Netzwerke</span> <span class="pdf-tree-count">(9 PDFs)</span></summary>
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
          <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Slides</span> <span class="pdf-tree-count">(7 PDFs)</span></summary>
          <div class="pdf-tree-children">
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">00 Geschichte</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Netzwerke/Slides/00_Geschichte/output_beamer_00_Geschichte.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 00: Geschichte</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Netzwerke/Slides/00_Geschichte/output_beamer_00_Geschichte.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">01 Schichtenmodell</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Netzwerke/Slides/01_Schichtenmodell/output_beamer_01_Schichtenmodell.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 01: Schichtenmodell</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Netzwerke/Slides/01_Schichtenmodell/output_beamer_01_Schichtenmodell.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">02 Netzzugangsschicht</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Netzwerke/Slides/02_Netzzugangsschicht/output_beamer_02_Netzzugangsschicht.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 02: Netzzugangsschicht</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Netzwerke/Slides/02_Netzzugangsschicht/output_beamer_02_Netzzugangsschicht.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">03 Vermittlungsschicht</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Netzwerke/Slides/03_Vermittlungsschicht/output_beamer_03_Vermittlungsschicht.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 03: Vermittlungsschicht</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Netzwerke/Slides/03_Vermittlungsschicht/output_beamer_03_Vermittlungsschicht.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">04 Transportschicht</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Netzwerke/Slides/04_Transportschicht/output_beamer_04_Transportschicht.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 04: Transportschicht</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Netzwerke/Slides/04_Transportschicht/output_beamer_04_Transportschicht.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">05 Anwendungsschicht</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Netzwerke/Slides/05_Anwendungsschicht/output_beamer_05_Anwendungsschicht.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 05: Anwendungsschicht</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Netzwerke/Slides/05_Anwendungsschicht/output_beamer_05_Anwendungsschicht.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">06 Chat Sockets</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Netzwerke/Slides/06_Chat_Sockets/output_beamer_06_Chat_Sockets.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 06: Chat Sockets</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Netzwerke/Slides/06_Chat_Sockets/output_beamer_06_Chat_Sockets.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
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
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">01 K01K02Intro</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/01_K01K02Intro/output_beamer_01_K01K02Intro.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 01: K01K02Intro</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/01_K01K02Intro/output_beamer_01_K01K02Intro.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">02 K03a Variablen</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/02_K03a_Variablen/output_beamer_02_K03a_Variablen.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 02: K03a Variablen</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/02_K03a_Variablen/output_beamer_02_K03a_Variablen.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">03 K03b Input</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/03_K03b_Input/output_beamer_03_K03b_Input.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 03: K03b Input</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/03_K03b_Input/output_beamer_03_K03b_Input.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">04 K03c Modulo</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/04_K03c_Modulo/output_beamer_04_K03c_Modulo.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 04: K03c Modulo</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/04_K03c_Modulo/output_beamer_04_K03c_Modulo.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">05 K04a Funktionen</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/05_K04a_Funktionen/output_beamer_05_K04a_Funktionen.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 05: K04a Funktionen</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/05_K04a_Funktionen/output_beamer_05_K04a_Funktionen.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">06 K04b Parameter</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/06_K04b_Parameter/output_beamer_06_K04b_Parameter.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 06: K04b Parameter</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/06_K04b_Parameter/output_beamer_06_K04b_Parameter.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">07 K04c Funktionen Einzelne</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/07_K04c_Funktionen_Einzelne/output_beamer_07_K04c_Funktionen_Einzelne.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 07: K04c Funktionen Einzelne</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/07_K04c_Funktionen_Einzelne/output_beamer_07_K04c_Funktionen_Einzelne.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">08 K04c Funktionen Mehrere</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/08_K04c_Funktionen_Mehrere/output_beamer_08_K04c_Funktionen_Mehrere.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 08: K04c Funktionen Mehrere</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/08_K04c_Funktionen_Mehrere/output_beamer_08_K04c_Funktionen_Mehrere.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">09 K04Zeit Tabellen</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/09_K04Zeit_Tabellen/output_beamer_09_K04Zeit_Tabellen.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 09: K04Zeit Tabellen</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/09_K04Zeit_Tabellen/output_beamer_09_K04Zeit_Tabellen.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">10 K05a If Elif Else</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/10_K05a_If_Elif_Else/output_beamer_10_K05a_If_Elif_Else.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 10: K05a If Elif Else</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/10_K05a_If_Elif_Else/output_beamer_10_K05a_If_Elif_Else.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">11 K05b Logische Operatoren</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/11_K05b_Logische_Operatoren/output_beamer_11_K05b_Logische_Operatoren.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 11: K05b Logische Operatoren</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/11_K05b_Logische_Operatoren/output_beamer_11_K05b_Logische_Operatoren.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">12 K05c Negation</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/12_K05c_Negation/output_beamer_12_K05c_Negation.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 12: K05c Negation</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/12_K05c_Negation/output_beamer_12_K05c_Negation.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">13 K05d Break While</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/13_K05d_Break_While/output_beamer_13_K05d_Break_While.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 13: K05d Break While</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/13_K05d_Break_While/output_beamer_13_K05d_Break_While.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">14 K06a Listen</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/14_K06a_Listen/output_beamer_14_K06a_Listen.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 14: K06a Listen</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/14_K06a_Listen/output_beamer_14_K06a_Listen.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">15 K06b Bubble Sort</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/15_K06b_Bubble_Sort/output_beamer_15_K06b_Bubble_Sort.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 15: K06b Bubble Sort</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/15_K06b_Bubble_Sort/output_beamer_15_K06b_Bubble_Sort.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">16 K06c Binary Search</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/16_K06c_Binary_Search/output_beamer_16_K06c_Binary_Search.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 16: K06c Binary Search</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/16_K06c_Binary_Search/output_beamer_16_K06c_Binary_Search.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">17 K06d Listen Teil2</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/17_K06d_Listen_Teil2/output_beamer_17_K06d_Listen_Teil2.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 17: K06d Listen Teil2</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/17_K06d_Listen_Teil2/output_beamer_17_K06d_Listen_Teil2.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">18 K06e Dictionaries</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/18_K06e_Dictionaries/output_beamer_18_K06e_Dictionaries.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 18: K06e Dictionaries</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/18_K06e_Dictionaries/output_beamer_18_K06e_Dictionaries.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">19 K06f Sets</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/19_K06f_Sets/output_beamer_19_K06f_Sets.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 19: K06f Sets</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/19_K06f_Sets/output_beamer_19_K06f_Sets.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">20 K07Klassen</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/20_K07Klassen/output_beamer_20_K07Klassen.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 20: K07Klassen</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/20_K07Klassen/output_beamer_20_K07Klassen.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">21 Turtle Grafik</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/21_Turtle_Grafik/output_beamer_21_Turtle_Grafik.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 21: Turtle Grafik</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Programmieren/Slides/21_Turtle_Grafik/output_beamer_21_Turtle_Grafik.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
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
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">01 Semesterplanung Slides</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Various/Slides/01_Semesterplanung_Slides/output_beamer_01_Semesterplanung_Slides.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 01: Semesterplanung Slides</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Various/Slides/01_Semesterplanung_Slides/output_beamer_01_Semesterplanung_Slides.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">02 Intro FDU</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Various/Slides/02_Intro_FDU/output_beamer_02_Intro_FDU.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 02: Intro FDU</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Various/Slides/02_Intro_FDU/output_beamer_02_Intro_FDU.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
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
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">01 Zahlensysteme L01</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Zahlendarstellungen_und_Kodierungen/Slides/01_Zahlensysteme_L01/output_beamer_01_Zahlensysteme_L01.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 01: Zahlensysteme L01</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Zahlendarstellungen_und_Kodierungen/Slides/01_Zahlensysteme_L01/output_beamer_01_Zahlensysteme_L01.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">02 Zahlensysteme L02</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Zahlendarstellungen_und_Kodierungen/Slides/02_Zahlensysteme_L02/output_beamer_02_Zahlensysteme_L02.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 02: Zahlensysteme L02</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Zahlendarstellungen_und_Kodierungen/Slides/02_Zahlensysteme_L02/output_beamer_02_Zahlensysteme_L02.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">03 Zahlensysteme L03</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Zahlendarstellungen_und_Kodierungen/Slides/03_Zahlensysteme_L03/output_beamer_03_Zahlensysteme_L03.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 03: Zahlensysteme L03</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Zahlendarstellungen_und_Kodierungen/Slides/03_Zahlensysteme_L03/output_beamer_03_Zahlensysteme_L03.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">04 Zahlensysteme L04</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Zahlendarstellungen_und_Kodierungen/Slides/04_Zahlensysteme_L04/output_beamer_04_Zahlensysteme_L04.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 04: Zahlensysteme L04</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Zahlendarstellungen_und_Kodierungen/Slides/04_Zahlensysteme_L04/output_beamer_04_Zahlensysteme_L04.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
            <details class="pdf-tree-node" data-level="3">
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">05 Zahlensysteme L05</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Grundlagen_Info/Zahlendarstellungen_und_Kodierungen/Slides/05_Zahlensysteme_L05/output_beamer_05_Zahlensysteme_L05.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 05: Zahlensysteme L05</a> <a href="https://files.in-form-atik.ch/Grundlagen_Info/Zahlendarstellungen_und_Kodierungen/Slides/05_Zahlensysteme_L05/output_beamer_05_Zahlensysteme_L05.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
          </div>
        </details>
      </div>
    </details>
    <details class="pdf-tree-node" data-level="1">
      <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Artikel</span> <span class="pdf-tree-count">(7 PDFs)</span></summary>
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
      <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Artikel</span> <span class="pdf-tree-count">(2 PDFs)</span></summary>
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
              <summary class="pdf-tree-summary"><span class="pdf-tree-folder">01 Deskriptive Statistik</span> <span class="pdf-tree-count">(1 PDFs)</span></summary>
              <div class="pdf-tree-children">
                <ul class="pdf-tree-files">
                  <li class="pdf-tree-file" data-type="folien">
                    <a href="https://files.in-form-atik.ch/Various/Wahlpflichtmodul_Statistik/Slides/01_Deskriptive_Statistik/output_beamer_01_Deskriptive_Statistik.pdf" target="_blank" rel="noopener" class="pdf-file-link">📄 Folien 01: Deskriptive Statistik</a> <a href="https://files.in-form-atik.ch/Various/Wahlpflichtmodul_Statistik/Slides/01_Deskriptive_Statistik/output_beamer_01_Deskriptive_Statistik.log" target="_blank" rel="noopener" class="pdf-log-link" title="Kompilations-Log anzeigen">🪵 Log</a>
                  </li>
                </ul>
              </div>
            </details>
          </div>
        </details>
      </div>
    </details>
    <details class="pdf-tree-node" data-level="1">
      <summary class="pdf-tree-summary"><span class="pdf-tree-folder">Artikel</span> <span class="pdf-tree-count">(6 PDFs)</span></summary>
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
