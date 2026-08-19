#!/usr/bin/env python3
"""
Automated Build Script: Advanced TeX to Quarto Web Skript Converter
Converts FreeFlower LaTeX chapter files into ultra-compact, interactive Quarto (.qmd) Web pages.
Configures auto-hiding sticky navbar, VS Code Dark listings, full article layout, and exact tcolorbox color schemes.
"""

import os
import re
import sys
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CHAPTERS_DIR = REPO_ROOT / "Grundlagen_Info" / "00_Programmieren" / "Skript" / "Chapters"
WEB_DIR = REPO_ROOT / "web_mvp"

CHAPTER_MAPPING = [
    {"tex": "K01_Getting_Started.tex", "qmd": "01_getting_started.qmd", "num": "1", "title": "Getting Started"},
    {"tex": "K02_Intro.tex", "qmd": "02_intro.qmd", "num": "2", "title": "Einführung & Schleifen"},
    {"tex": "K03_Variables_Debugging.tex", "qmd": "03_variables_debugging.qmd", "num": "3", "title": "Variablen & Debugging"},
    {"tex": "K04_Functions.tex", "qmd": "04_functions.qmd", "num": "4", "title": "Funktionen"},
    {"tex": "K05_Logical_Expressions.tex", "qmd": "05_logical_expressions.qmd", "num": "5", "title": "Verzweigungen"},
    {"tex": "K06_Datenstrukturen.tex", "qmd": "06_datenstrukturen.qmd", "num": "6", "title": "Datenstrukturen"},
    {"tex": "K07_Klassen.tex", "qmd": "07_klassen.qmd", "num": "7", "title": "OOP & Klassen"},
    {"tex": "K08_Game.tex", "qmd": "08_game.qmd", "num": "8", "title": "Game-Entwicklung"},
]

EMOJI_MAP = {
    'face-with-monocle': '🧐',
    'books': '📚',
    'key': '🔑',
    'check-mark': '✅',
    'cross-mark': '❌',
    'trophy': '🏆',
    'light-bulb': '💡',
    'fire': '🔥',
    'star': '⭐',
    'warning': '⚠️',
    'rocket': '🚀',
    'smiling-face': '😊',
}

def format_code_block(code_content, caption_str=""):
    """Determines whether code should be an interactive pyodide block or static python block."""
    code_content = code_content.strip()
    if "import turtle" in code_content or "from turtle import" in code_content or "import pygame" in code_content or "from pygame" in code_content:
        note = "\n:::{.env-remark}\n:::{.callout-note icon=false}\n💡 **Hinweis**: Dieses Skript verwendet grafische Desktop-Bibliotheken (`turtle` / `pygame`). Führen Sie diesen Code in Ihrer lokalen Entwicklungsumgebung (z.B. VS Code) aus.\n:::\n:::\n"
        return f"\n\n```python\n{caption_str}{code_content}\n```\n{note}\n"
    else:
        return f"\n\n```{{pyodide-python}}\n{caption_str}{code_content}\n```\n\n"

def resolve_lstinputlisting(match):
    """Replaces \\lstinputlisting[...]{path} with actual Python code."""
    full_match = match.group(0)
    rel_path = match.group(1).strip()
    code_file = REPO_ROOT / rel_path

    caption_match = re.search(r'caption=(?:\\texttt\{)?([^,\]\}]+)', full_match)
    caption_str = f"# File: {caption_match.group(1)}\n" if caption_match else ""

    if code_file.exists():
        try:
            code_content = code_file.read_text(encoding="utf-8").strip()
            return format_code_block(code_content, caption_str)
        except Exception as e:
            return f"\n```python\n# Failed to read {rel_path}: {e}\n```\n"
    return f"\n```python\n# Listing file not found: {rel_path}\n```\n"

def convert_tabular_to_markdown(match):
    """Converts a LaTeX tabular environment into a clean Markdown table."""
    table_body = match.group(1).strip()
    lines = [line.strip() for line in table_body.split('\n') if line.strip()]

    parsed_rows = []
    for line in lines:
        if any(line.startswith(cmd) for cmd in [r'\midrule', r'\toprule', r'\bottomrule', r'\hline']):
            continue
        line = re.sub(r'\\\\.*$', '', line).strip()
        if not line:
            continue
        cells = [cell.strip() for cell in line.split('&')]
        cleaned_cells = []
        for cell in cells:
            cell = re.sub(r'\\smallField\{[^\}]*\}', '___', cell)
            cell = re.sub(r'\\textcolor\{[^\}]+\}\{([^\}]+)\}', r'\1', cell)
            cell = re.sub(r'\\textbf\{([^\}]+)\}', r'**\1**', cell)
            cell = re.sub(r'\\textit\{([^\}]+)\}', r'*\1*', cell)
            cell = re.sub(r'\\lstinline[\|!]([^\|!]+)[\|!]', r'`\1`', cell)
            cell = re.sub(r'\\texttt\{([^\}]+)\}', r'`\1`', cell)
            cleaned_cells.append(cell)
        parsed_rows.append(cleaned_cells)

    if not parsed_rows:
        return ""

    num_cols = max(len(row) for row in parsed_rows)
    md_lines = []

    header = parsed_rows[0]
    while len(header) < num_cols:
        header.append("")
    md_lines.append("| " + " | ".join(header) + " |")
    md_lines.append("| " + " | ".join(["---"] * num_cols) + " |")

    for row in parsed_rows[1:]:
        while len(row) < num_cols:
            row.append("")
        md_lines.append("| " + " | ".join(row) + " |")

    return "\n\n" + "\n".join(md_lines) + "\n\n"

def convert_enumerate(match):
    """Converts LaTeX enumerate environment to numbered markdown list."""
    content = match.group(1)
    items = re.split(r'\\item\s*', content)
    md_items = []
    idx = 1
    for item in items:
        cleaned = item.strip()
        if cleaned:
            md_items.append(f"{idx}. {cleaned}")
            idx += 1
    return "\n\n" + "\n".join(md_items) + "\n\n"

def clean_tex_escapes(text):
    """Clean TeX escape characters for YAML and Markdown."""
    text = text.replace(r'\&', '&')
    text = text.replace(r'\_', '_')
    text = text.replace(r'\%', '%')
    text = text.replace(r'\$', '$')
    text = text.replace(r'\iftoggle{exerciseonly}{}{', '')
    text = text.replace(r'\iftoggle{exerciseonly}{}', '')
    text = text.replace(r'\end{lstlisting}', '')
    return text

def process_nested_command(text, cmd_name, convert_fn):
    r"""Finds occurrences of \cmd_name{arg1}{arg2}... handling nested braces properly."""
    pattern = r'\\' + cmd_name + r'\{'
    while True:
        m = re.search(pattern, text)
        if not m:
            break
        start_pos = m.start()
        curr_pos = m.end() - 1
        args = []
        while curr_pos < len(text) and text[curr_pos] == '{':
            depth = 1
            idx = curr_pos + 1
            while idx < len(text) and depth > 0:
                if text[idx] == '{':
                    depth += 1
                elif text[idx] == '}':
                    depth -= 1
                idx += 1
            if depth == 0:
                args.append(text[curr_pos + 1 : idx - 1])
                curr_pos = idx
                while curr_pos < len(text) and text[curr_pos].isspace():
                    curr_pos += 1
            else:
                break
        replacement = convert_fn(args)
        text = text[:start_pos] + replacement + text[curr_pos:]
    return text

def convert_tex_content(tex_text, ch_num="1"):
    """Applies transformation rules to convert TeX markup to clean Quarto Markdown."""
    text = tex_text
    exercise_counter = [0]
    label_to_info = {}

    # Extract chapter title
    chapter_match = re.search(r'\\chapter\{([^\}]+)\}', text)
    raw_chapter_title = chapter_match.group(1) if chapter_match else "Kapitel"
    chapter_title = clean_tex_escapes(raw_chapter_title)

    # Remove chapter declaration & minipages
    text = re.sub(r'\\chapter\{[^\}]+\}(?:\\label\{[^\}]+\})?', '', text)
    text = re.sub(r'\\begin\{minipage\}\{[^\}]*\}', '', text)
    text = re.sub(r'\\end\{minipage\}', '', text)

    # 1. Protect lstlisting blocks from comment stripping
    lst_blocks = []
    def save_lst(m):
        lst_blocks.append(m.group(0))
        return f"___LSTLISTING_PLACEHOLDER_{len(lst_blocks)-1}___"
    text = re.sub(r'\\begin\{lstlisting\}.*?\\end\{lstlisting\}', save_lst, text, flags=re.DOTALL)

    # 2. Protect escaped percent signs (\%)
    text = text.replace(r'\%', '___ESCAPED_PERCENT___')

    # 3. Strip all TeX comments (% to end of line)
    text = re.sub(r'%.*$', '', text, flags=re.MULTILINE)

    # 4. Restore escaped percent signs
    text = text.replace('___ESCAPED_PERCENT___', '%')

    # 5. Restore lstlisting blocks
    for i, block in enumerate(lst_blocks):
        text = text.replace(f"___LSTLISTING_PLACEHOLDER_{i}___", block)

    # Clean standalone TeX closing braces (e.g. from \iftoggle{...}{...}{})
    text = re.sub(r'^\s*\}\s*$', '', text, flags=re.MULTILINE)

    # Clean texorpdfstring
    text = re.sub(r'\\texorpdfstring\{[^\}]*\\lstinline[\|!]([^\|!]+)[\|!][^\}]*\}\{([^\}]+)\}', r'`\1`', text)

    # Convert sections and subsections
    text = re.sub(r'\\section\{([^\}]+)\}(?:\\label\{[^\}]+\})?', r'\n\n## \1\n\n', text)
    text = re.sub(r'\\subsection\{([^\}]+)\}(?:\\label\{[^\}]+\})?', r'\n\n### \1\n\n', text)
    text = re.sub(r'\\subsubsection\{([^\}]+)\}(?:\\label\{[^\}]+\})?', r'\n\n#### \1\n\n', text)

    # Convert \lstinputlisting to pyodide / static blocks
    text = re.sub(r'\\lstinputlisting(?:\[[^\]]*\])?\{([^\}]+)\}', resolve_lstinputlisting, text)

    # Convert \begin{lstlisting}[opts] ... \end{lstlisting}
    def convert_lstlisting(m):
        code = m.group(2).strip()
        code = code.replace(r'\end{lstlisting}', '')
        return format_code_block(code)

    text = re.sub(r'\\begin\{lstlisting\}(?:\[([^\]]*)\])?(.*?)\\end\{lstlisting\}', convert_lstlisting, text, flags=re.DOTALL)

    # Convert inline code & text formatting
    text = re.sub(r'\\lstinline[\|!]([^\|!]+)[\|!]', r'`\1`', text)
    text = re.sub(r'\\texttt\{([^\}]+)\}', r'`\1`', text)
    text = re.sub(r'\\textbf\{([^\}]+)\}', r'**\1**', text)
    text = re.sub(r'\\textit\{([^\}]+)\}', r'*\1*', text)
    text = re.sub(r'\\emph\{([^\}]+)\}', r'*\1*', text)
    text = re.sub(r'\\enquote\{([^\}]+)\}', r'"\1"', text)
    text = re.sub(r'\\smallField\{[^\}]*\}', '___', text)
    text = re.sub(r'\\textcolor\{[^\}]+\}\{([^\}]+)\}', r'\1', text)

    # Convert Emojis
    text = re.sub(r'\\emoji\{([^\}]+)\}', lambda m: EMOJI_MAP.get(m.group(1), ''), text)

    # Convert LaTeX Tabular to Markdown Table
    text = re.sub(r'\\begin\{table\}(?:\[[^\]]*\])?\s*\\centering\s*\\begin\{tabular\}\{[^\}]+\}(.*?)\\end\{tabular\}\s*(?:\\caption\{[^\}]*\})?\s*(?:\\label\{[^\}]*\})?\s*\\end\{table\}', convert_tabular_to_markdown, text, flags=re.DOTALL)
    text = re.sub(r'\\begin\{tabular\}\{[^\}]+\}(.*?)\\end\{tabular\}', convert_tabular_to_markdown, text, flags=re.DOTALL)

    # Clean leftover LaTeX line breaks (\\) in prose text
    text = re.sub(r'\\\\', '', text)

    # Convert Enumerate List
    text = re.sub(r'\\begin\{enumerate\}(.*?)\\end\{enumerate\}', convert_enumerate, text, flags=re.DOTALL)

    # Convert Custom Environments to Quarto Callouts wrapped in outer div for 100% CSS targeting
    def convert_env(txt, env_name, callout_type, env_class, default_title):
        pattern = r'\\begin\{' + env_name + r'\}(?:\[([^\]]+)\])?(?:\s*\\label\{([^\}]+)\})?'
        def replacer(m):
            raw_title = m.group(1) if m.group(1) else ""
            label = m.group(2) if m.group(2) else ""
            clean_title = clean_tex_escapes(raw_title)

            if env_name in ("myexercise", "mychallenge"):
                exercise_counter[0] += 1
                num_str = f"{ch_num}.{exercise_counter[0]}"
                prefix = "Aufgabe" if env_name == "myexercise" else "Challenge"
                if clean_title:
                    display_title = f"{prefix} {num_str}: {clean_title}"
                else:
                    display_title = f"{prefix} {num_str}"
                if label:
                    label_to_info[label] = {
                        "num_str": num_str,
                        "display_title": display_title,
                        "prefix": prefix
                    }
            else:
                display_title = clean_title if clean_title else default_title

            id_attr = f" #{label}" if label else ""
            return f"\n\n::: {{{env_class}{id_attr}}}\n::: {{{callout_type} icon=false}}\n### {display_title}\n"
        txt = re.sub(pattern, replacer, txt)
        txt = txt.replace(r'\end{' + env_name + r'}', '\n:::\n:::\n\n')
        return txt

    text = convert_env(text, "mydefinition", ".callout-note", ".env-definition", "Definition")
    text = convert_env(text, "myexample", ".callout-note", ".env-example", "Beispiel")
    text = convert_env(text, "myexercise", ".callout-tip", ".env-exercise", "Aufgabe")
    text = convert_env(text, "myremark", ".callout-note", ".env-remark", "Bemerkung")
    text = convert_env(text, "myoverview", ".callout-note", ".env-overview", "Übersicht")
    text = convert_env(text, "myattention", ".callout-warning", ".env-attention", "Wichtiger Hinweis")
    text = convert_env(text, "mychallenge", ".callout-warning", ".env-challenge", "Challenge")

    # Convert Solutions \begin{myanswer}[optional_label] ... \end{myanswer} into Collapsible Callouts
    def convert_answer(m):
        opt_arg = m.group(1)
        ans = m.group(2).strip()
        if opt_arg:
            label = opt_arg.strip()
            info = label_to_info.get(label)
            if info:
                title = f"💡 Musterlösung zu {info['display_title']}"
                ans = f"[↩ Zurück zu {info['display_title']}](#{label})\n\n" + ans
            else:
                title = "💡 Musterlösung anzeigen"
                ans = f"[↩ Zurück zur Aufgabe](#{label})\n\n" + ans
        else:
            title = "💡 Musterlösung anzeigen"
        return f"\n\n::: {{.env-answer}}\n::: {{.callout-caution collapse=\"true\" icon=false}}\n### {title}\n{ans}\n:::\n:::\n\n"

    text = re.sub(r'\\begin\{myanswer\}(?:\[([^\]]+)\])?(.*?)\\end\{myanswer\}', convert_answer, text, flags=re.DOTALL)

    # Convert \url{}, \href{}{}, and \footnote{} with support for nested braces
    text = process_nested_command(text, "url", lambda args: f"[{args[0]}]({args[0]})" if args else "")
    text = process_nested_command(text, "href", lambda args: f"[{args[1]}]({args[0]})" if len(args) >= 2 else "")
    text = process_nested_command(text, "footnote", lambda args: f"^[{args[0]}]" if args else "")

    # Convert Align Math
    text = re.sub(r'\\begin\{align\*\}(.*?)\\end\{align\*\}', r'\n\n$$\n\1\n$$\n\n', text, flags=re.DOTALL)

    # Remove TikZ marks and formatting leftovers
    text = re.sub(r'\\tikzmark(?:node)?\{[^\}]+\}', '', text)
    text = re.sub(r'\\leavevmode', '', text)
    text = re.sub(r'\\noindent', '', text)
    text = re.sub(r'\\pagebreak', '', text)
    text = re.sub(r'\\clearpage', '', text)
    text = re.sub(r'\\small', '', text)
    text = re.sub(r'\\large', '', text)
    text = re.sub(r'\\faListUl', '', text)

    # Clean up TeX artifacts: \cref{}, \label{}, \index{}
    def convert_cref(m):
        ref_id = m.group(1).strip()
        if "sol" in ref_id:
            return "[Längere Lösungen](#laengere-loesungen)"
        elif "fig:" in ref_id:
            return "Abbildung"
        elif ref_id in label_to_info:
            info = label_to_info[ref_id]
            return f"[{info['display_title']}](#{ref_id})"
        else:
            return "Abschnitt"

    text = re.sub(r'\\cref\{([^\}]+)\}', convert_cref, text)
    text = re.sub(r'\\label\{[^\}]+\}', '', text)
    text = re.sub(r'\\index\{[^\}]+\}', '', text)

    # Remove TeX figure environments and clean up unneeded TeX commands
    text = re.sub(r'\\begin\{figure\}.*?\\end\{figure\}', '', text, flags=re.DOTALL)
    text = re.sub(r'\\begin\{center\}', '', text)
    text = re.sub(r'\\end\{center\}', '', text)
    text = re.sub(r'\\begin\{itemize\}', '', text)
    text = re.sub(r'\\end\{itemize\}', '', text)

    # Clean leading spaces and tabs outside explicit triple-backtick code blocks to prevent accidental indented code blocks
    cleaned_lines = []
    in_code_block = False
    for line in text.split('\n'):
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            cleaned_lines.append(line)
        elif in_code_block:
            cleaned_lines.append(line)
        else:
            cleaned_lines.append(line.strip())
    text = '\n'.join(cleaned_lines)

    text = re.sub(r'\\item\s*', '- ', text)

    # Clean escape sequences
    text = clean_tex_escapes(text)

    # Clean multiple blank lines
    text = re.sub(r'\n{3,}', '\n\n', text)

    return chapter_title, text.strip()

def update_quarto_yml(chapters):
    """Generates _quarto.yml dynamically with top navbar only (no sidebar) & auto-hide navbar script."""
    nav_links = [{"href": "index.qmd", "text": "Übersicht"}]

    for ch in chapters:
        nav_links.append({"href": ch["qmd"], "text": f"{ch['num']}. {ch['title']}"})

    yml_content = f"""project:
  type: website
  output-dir: _site

website:
  title: "FreeFlower | Programmieren"
  navbar:
    background: "#1e1e1e"
    left:
"""
    for link in nav_links:
        yml_content += f"      - href: {link['href']}\n        text: \"{link['text']}\"\n"

    yml_content += """    right:
      - icon: github
        href: "https://github.com/CyrilBlum/FreeFlower"

execute:
  eval: false

format:
  html:
    page-layout: article
    toc: true
    toc-depth: 3
    toc-location: right
    toc-title: "Auf dieser Seite"
    highlight-style: dracula
    css: styles.css
    code-copy: true
    code-fold: false
    include-in-header:
      text: |
        <script>
        document.addEventListener("DOMContentLoaded", function() {
          let lastScrollTop = 0;
          let navbar = document.querySelector(".navbar");
          if (!navbar) return;

          navbar.style.position = "sticky";
          navbar.style.top = "0";
          navbar.style.zIndex = "1000";
          navbar.style.transition = "transform 0.25s ease-in-out";

          window.addEventListener("scroll", function() {
            let scrollTop = window.pageYOffset || document.documentElement.scrollTop;
            if (scrollTop > lastScrollTop && scrollTop > 50) {
              navbar.style.transform = "translateY(-100%)";
            } else {
              navbar.style.transform = "translateY(0)";
            }
          document.addEventListener("click", function(e) {
            let link = e.target.closest(".callout-header a");
            if (link) {
              e.stopPropagation();
            }
          }, true);
        });
        </script>
    filters:
      - coatless-quarto/pyodide
"""
    (WEB_DIR / "_quarto.yml").write_text(yml_content, encoding="utf-8")
    print("[✓] Generated web_mvp/_quarto.yml (No sidebar, top navbar auto-hide on scroll)")

def main():
    print("=== FreeFlower TeX -> Quarto Web Converter (VS Code Dark & Ultra-Compact) ===")
    converted_chapters = []

    for ch in CHAPTER_MAPPING:
        tex_file = CHAPTERS_DIR / ch["tex"]
        qmd_file = WEB_DIR / ch["qmd"]

        if tex_file.exists():
            tex_text = tex_file.read_text(encoding="utf-8")
            chapter_title, qmd_body = convert_tex_content(tex_text, ch["num"])

            qmd_content = f"""---
title: "{ch['num']}. {chapter_title}"
---

{qmd_body}
"""
            qmd_file.write_text(qmd_content, encoding="utf-8")
            print(f"[✓] Converted {ch['tex']} -> web_mvp/{ch['qmd']}")
            converted_chapters.append(ch)
        else:
            print(f"[!] Warning: {ch['tex']} not found.")

    update_quarto_yml(converted_chapters)

    quarto_bin = Path.home() / ".local" / "bin" / "quarto"
    quarto_cmd = str(quarto_bin) if quarto_bin.exists() else "quarto"

    print("\nExecuting Quarto Render...")
    try:
        subprocess.run([quarto_cmd, "render"], cwd=WEB_DIR, check=True)
        print("\n[✓] Build Successful! Web site rendered into web_mvp/_site/")
    except Exception as e:
        print(f"\n[❌] Quarto render error: {e}")

if __name__ == "__main__":
    main()
