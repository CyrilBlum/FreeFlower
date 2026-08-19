---
layout: default
title: Lokale Installation von LaTeX
parent: Technische Seiten
nav_order: 5
permalink: /latex-setup.html
---

# Lokale Installation von LaTeX

Diese Anleitung beschreibt die lokale Installation von LaTeX unter macOS und Windows sowie die Einrichtung und Kompilierung in VS Code mit der Erweiterung LaTeX Workshop.

## Anleitung für macOS

Öffnen Sie ein neues Terminal-Fenster, indem Sie zunächst die Spotlight-Suche mit `Cmd` + `Leertaste` öffnen. Geben Sie dort `Terminal` ein und bestätigen Sie mit `Enter`.

Falls Homebrew noch nicht installiert ist, installieren Sie es bitte zunächst gemäss der [Anleitung zur Homebrew-Installation]({{ '/vscode-python-setup.html' | relative_url }}).

Führen Sie danach diesen Befehl aus:

```bash
brew install --cask mactex
```

## Anleitung für Windows

Öffnen Sie PowerShell als Administrator und führen Sie die folgenden Befehle nacheinander aus:

```powershell
winget install --id MiKTeX.MiKTeX
winget install --id StrawberryPerl.StrawberryPerl
```

## Kompilieren des Projekts

Sie können nun jedes LaTeX-Projekt kompilieren. Navigieren Sie dazu im Terminal in das Verzeichnis, in dem sich Ihre `main.tex` befindet, und führen Sie die folgenden Befehle aus:

```bash
echo "Step 1 of 5: lualatex" ; lualatex -synctex=1 -interaction=nonstopmode main.tex ; echo "Step 2 of 5: biber" ; biber main ; echo "Step 3 of 5: makeglossaries" ; makeglossaries main ; echo "Step 4 of 5: lualatex" ; lualatex -synctex=1 -interaction=nonstopmode main.tex ; echo "Step 5 of 5: lualatex" ; lualatex -synctex=1 main.tex ; echo "Compilation complete"
```

## Kompilieren mit LaTeX Workshop

Alternativ zur Kompilation über das Terminal kann das Projekt direkt in VS Code mit der Extension LaTeX Workshop kompiliert werden. Installieren Sie dazu die Extension **LaTeX Workshop** von James Yu.

![LaTeX Workshop im VS-Code-Erweiterungsbereich](assets/images/latex-setup/latex_extension.png)

Öffnen Sie anschliessend in VS Code die Kommando-Palette:

- **macOS:** `Cmd` + `Shift` + `P`
- **Windows:** `Ctrl` + `Shift` + `P`

Suchen Sie nach `Preferences: Open User Settings (JSON)` und wählen Sie den Befehl aus.

![User Settings JSON öffnen](assets/images/latex-setup/open_json.png)

Löschen Sie den bisherigen Inhalt Ihrer Benutzereinstellungen vollständig und ersetzen Sie ihn durch den vollständigen Inhalt von `settings.json`. Die Konfiguration enthält die Werkzeuge `lualatex`, `biber` und `makeglossaries` sowie die vollständigen Kompilierungsrezepte.

```json
{
    "[latex]": {
        "editor.defaultFormatter": "James-Yu.latex-workshop"
    },
    "latex-workshop.formatting.latex": "latexindent",
    "latex-workshop.latex.clean.command": "latexmk",
    "latex-workshop.latex.clean.method": "glob",
    "latex-workshop.latex.autoClean.run": "onBuilt",
    "latex-workshop.latex.clean.subfolder.enabled": true,
    "latex-workshop.latex.clean.fileTypes": [
        "aux",
        "log",
        "out",
        "toc",
        "lof",
        "lot",
        "glo",
        "idx",
        "fls",
        "fdb_latexmk",
        "synctex.gz"
    ],
    "latex-workshop.intellisense.citation.backend": "biblatex",
    "latex-workshop.latex.tools": [
        {
            "name": "biber",
            "command": "biber",
            "args": [
                "--input-directory=build",
                "--output-directory=build",
                "%DOCFILE%"
            ],
            "env": {}
        },
        {
            "name": "makeglossaries",
            "command": "makeglossaries",
            "args": [
                "-d",
                "build",
                "%DOCFILE%"
            ]
        },
        {
            "name": "makeglossaries-lite",
            "command": "makeglossaries-lite",
            "args": [
                "%DOCFILE%"
            ]
        },
        {
            "name": "lualatex",
            "command": "lualatex",
            "args": [
                "--output-directory=build",
                "--interaction=nonstopmode",
                "--synctex=1",
                "%DOC%"
            ]
        }
    ],
    "latex-workshop.latex.recipes": [
        {
            "name": "lualatex",
            "tools": [
                "lualatex"
            ]
        },
        {
            "name": "lualatex -> lualatex",
            "tools": [
                "lualatex",
                "lualatex"
            ]
        },
        {
            "name": "lualatex -> biber -> makeglossaries -> 2 x lualatex",
            "tools": [
                "lualatex",
                "biber",
                "makeglossaries",
                "lualatex",
                "lualatex"
            ]
        }
    ],
    "latex-workshop.latex.recipe.default": "lastUsed",
    "latex-workshop.message.log.show": true,
    "latex-workshop.latex.outDir": "./build",
    "latex-workshop.latex.rootFile.useSubFile": true,
    "latex-workshop.latex.rootFile.doNotPrompt": true,
    "latex-workshop.latex.build.enableMagicComments": false
}
```

So können Sie Ihr LaTeX-Dokument kompilieren: Wählen Sie ein Kompilierungsrezept aus, zum Beispiel **lualatex**:

![LaTeX-Workshop-Kompilierungsrezept auswählen](assets/images/latex-setup/recipes.png)
