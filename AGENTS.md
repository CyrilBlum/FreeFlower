# AGENTS.md

Instructions and guidelines for AI coding agents and automated tools working on the **FreeFlower** repository.

---

## 1. Overview & Purpose

**FreeFlower** is an open-source repository containing high-quality educational materials (lecture notes, exercise books, slides, exams, and scripts) tailored for Swiss upper-secondary education (Gymnasium, Sek II, *Grundlagenfach Informatik*).

All materials are written in LaTeX (primarily using LuaLaTeX) and supporting Python/Shell scripts. Automated agents working in this repository must maintain strict consistency with existing style patterns, pedagogical standards, and compilation rules.

---

## 2. Core Rules for Collaboration & Contribution

These rules are strictly enforced and based on the official [FreeFlower Collaboration Guidelines](https://cyrilblum.github.io/FreeFlower/zusammenarbeit.html):

### 2.1 Branching, Pushing & Pull Requests
- **Pushing to `main` is allowed**: Pushing directly to `main` is permitted for users/maintainers with write permissions (branches or pull requests are optional and not strictly required).
- **Contributors without direct push access**: Note that not all users have permissions to push directly to `main`. Contributors without write permissions must use a dedicated branch (e.g., `feature/...`, `fix/...`) and submit work via a Pull Request.
- Before starting significant new modules or structural changes, ensure contact has been established with the project maintainers.

### 2.2 LaTeX & Code Style
- **Maintain a clean, polished code style**: Follow existing formatting across TeX files, preamble imports, and code listings.
- **Inline Comments**: Include meaningful inline comments (in German or English, matching the file context) to explain complex TeX macros, custom environments, or non-obvious formatting logic.
- **Formatting & Indentation**: Keep indentation clean and readable. Use standard environment structures without trailing unnecessary whitespace.

### 2.3 Licensing & Media Rights
- **No Commercial or Unlicensed Content**: Never include copyrighted text, images, or assets without explicit permission and proper license compatibility.
- **Educational Content License**: Licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).
- **Code & Tooling License**: Source code, scripts, LaTeX classes/packages, and build scripts are licensed under [GPL-3.0-or-later](https://www.gnu.org/licenses/gpl-3.0.html).

### 2.4 Graphics & Visuals Policy
- **Avoid Screenshots / Raster Images**: Do **not** use raster graphics (PNG, JPG, GIF) for diagrams, formulas, or UI mockups.
- **Prioritize Native LaTeX / TikZ**: Generate diagrams, flowcharts, and technical drawings natively in LaTeX using TikZ (see `Preambles/pre_3_tikz.tex`).
- **Use Vector Formats**: When a graphic cannot be rendered natively in TikZ, use vector formats strictly (`.pdf` or `.svg`).
- **Scope of the TikZ/vector rule**: It applies to algorithms, formal content, diagrams, formulas and technical drawings. **Illustrative material** (e.g. realistic mockups of SMS/e-mails/apps, story illustrations, photos for exercises) may be raster images (PNG/JPG) when TikZ would be disproportionately laborious. Such images must be self-made or properly licensed, use fictional names/brands, and live in the topic's `Figures/` (or `Material/`) folder.

### 2.5 Compilation Policy & Quality Standard
- **No Automatic Compilation**: AI agents do **not** need to compile edited `.tex` files unless the user explicitly requests it.
- **Zero-Error Standard (when compilation is requested)**: If the user explicitly asks for compilation, all modified TeX documents must compile without errors, fatal warnings, or unresolved reference/citation issues under LuaLaTeX.
- **Always Compile in `build/` Subfolder**: Compilation must **always** be directed to the `build/` subfolder (using `--output-directory=build`). Never compile directly into the root repository directory.
- **Server TeX Live Version**: The remote build server (Hetzner self-hosted runner) runs **TeX Live 2024** (`tlnet-final`, LuaHBTeX 1.18.0, Biber 2.20). This exact version is required to successfully build files on the server.

### 2.6 Synchronizing Exercises: Slides vs. Handouts/Scripts
- **Manual Exercise Sync**: Exercise and task numberings in Beamer slides are **not** updated automatically when corresponding parts in scripts or exercise handouts are changed.
- **Agent Rule**: Whenever you modify or add exercises in script/book sections, check and manually update the corresponding slide numbers and Beamer presentations in the repository.

### 2.7 Cleanup of Temporary Rendered Artifacts
- **Always Clean Up Rendered Images**: When using tools like `pdftoppm` to generate temporary `.png` files for visual inspection and verification, always delete all agent-generated `.png` files from the repository directory before finishing the task.

### 2.8 Compilation in `build/` Subfolder & Cleanup
- **Always Compile in `build/`**: All compilation runs must output to the `build/` subfolder (`--output-directory=build`). This keeps the repository root directory completely clean of auxiliary files.
- **Auxiliary Files in `build/`**: The `build/` directory is ignored by Git (`.gitignore`). Ensure auxiliary files never leak into the root directory. To clean up build artifacts or reset build state, remove files inside `build/`:
  ```bash
  rm -rf build/*
  ```
- **Never Leave Root Aux Files**: If any auxiliary files (`aux`, `log`, `out`, `toc`, `lof`, `lot`, `glo`, `idx`, `fls`, `fdb_latexmk`, `synctex.gz`) are generated in the root directory, remove them immediately before finishing:
  ```bash
  rm -f main.{aux,log,out,toc,lof,lot,glo,idx,fls,fdb_latexmk,synctex.gz}
  ```

### 2.9 Chapters Under Construction (Do Not Compile by Default)
- **Drafts / Work-in-Progress**: Chapters and sections marked as "under construction" are incomplete drafts and **must not be compiled normally** into the main document.
- **Always Commented Out**: In the respective topic's sub-main file (e.g., `Skript.tex`), their `\input{...}` statement must remain commented out at all times.
- **Currently designated WIP chapters**:
  - `% \input{Grundlagen_Info/03_Kryptologie/Skript/Kapitel_06.tex} % Kapitel 6: Post-Quanten-Kryptographie` (in `Grundlagen_Info/03_Kryptologie/Skript/Skript.tex`)
- **Agent Rule**: Never uncomment these WIP chapters when compiling, building, or refactoring unless the user explicitly requests to work on or test that specific draft chapter.

### 2.10 Active Topic & Document Class in `main.tex` During Development vs. Commits
- **Activate Target File & Document Class During Development**: Whenever you modify or work on a document (e.g., a script chapter, presentation slides, or an article), activate that topic's `\input{...}` in `main.tex` AND set the corresponding `\documentToggle` (along with the matching active `\documentclass`) for that document type (e.g., `0` for `book`, `3` for `beamer`, `1` for `article`). This allows the user to immediately and easily compile and preview the document within an IDE such as VS Code without manual configuration.
- **Faster Compilation During Iterative Checks**: In sub-main files (e.g., `Skript.tex`), you may temporarily comment out sibling chapters or appendices to accelerate local testing. Always restore these within the sub-main files before finishing.
- **Never Commit Development Changes to `main.tex`**: When creating Git commits, **never commit session-specific changes to `main.tex`**. In principle, `main.tex` must remain unchanged in commits. Discard or unstage active topic/toggle changes in `main.tex` (e.g., via `git checkout main.tex`) before committing, **unless** an intentional structural change was made (such as adding a newly created document, updating a moved document path, or modifying global preamble includes).

### 2.11 Glossaries & Acronyms (`\gls{...}`)
- **Consistent Glossary Usage**: All acronyms and technical abbreviations used in scripts and materials (e.g., `CPU`, `RAM`, `ALU`, `HDD`, `SSD`, `SI`, `OS`, `API`, `SQL`, `RGB`) must be defined in `Preambles/pre_6_glossaries.tex`.
- **Referencing in Text**: Always reference acronyms in `.tex` script files using `\gls{ACRONYM}` (singular) or `\glspl{ACRONYM}` (plural). In section headings, use `\glsentryshort{ACRONYM}` where appropriate to avoid hyperref / PDF bookmark warnings.

### 2.12 Git Commit Messages
- **Detailed but Concise Messages**: Commit messages must be informative and substantive, but not overly long or verbose.
- **Length**: Depending on the scope of changes, keep the body to a couple of lines, up to a **maximum of 10 lines** for very comprehensive edits.
- **Structure**: Include a concise subject line followed by bullet points summarizing *what* was changed and *why* (mentioning key touched modules, exercises, or figures where relevant). Avoid terse, generic one-liners as well as overly verbose multi-paragraph essays.

### 2.13 GitHub CLI (`gh`)
- **Tool Available**: The GitHub CLI (`gh`) is installed and available in the environment. Agents can use `gh` commands to check GitHub Actions CI/CD runs (`gh run list`), view failed build logs (`gh run view <id> --log-failed`), and interact with GitHub repository workflows.

---

## 3. Project Structure & Compilation Workflow

### 3.1 Repository Structure
```
FreeFlower/
├── main.tex                 # Main entry point with documentclass toggles
├── Preambles/               # Modular LaTeX preamble definitions
│   ├── pre_0_packages.tex   # Package imports
│   ├── pre_1_options.tex    # Package settings & options
│   ├── pre_2_macros.tex     # Custom macros & shortcuts
│   ├── pre_3_tikz.tex       # TikZ libraries & styles
│   ├── pre_4_custom_envs.tex# Custom boxes & environments
│   ├── pre_5_misc.tex       # Miscellaneous macros & overrides
│   └── pre_6_glossaries.tex # Glossary definitions
├── docs/                    # GitHub Pages documentation source
├── EF/                      # Ergänzungsfach materials
├── FF/                      # Freifach materials
├── Figures/                 # TikZ, vector graphics, and image assets
├── compile_tex.sh           # Automated TeX compilation script
└── AGENTS.md                # Agent instructions (this file)
```

### 3.2 Compiling Documents
The main entry point is `main.tex`. Document types are controlled via the `\documentToggle` switch in `main.tex`:

- `0` = `book` (Comprehensive script / exercise collection)
- `1` = `article` (Standalone handout / short script)
- `2` = `exam` (Exam / Test sheet)
- `3` = `beamer` (Presentation slides)
- `4` = `flashcards` (Learning cards)

#### Build Directory & CLI Tool Options
Compilation must **always** be performed using the `build/` subfolder. Ensure the directory exists before compiling (`mkdir -p build`).

The exact CLI tool options (matching the project's VS Code LaTeX Workshop configuration) are:
- **LuaLaTeX** (`lualatex`):
  ```bash
  lualatex --output-directory=build --interaction=nonstopmode --synctex=1 main.tex
  ```
- **Bibliography** (`biber`):
  ```bash
  biber --input-directory=build --output-directory=build main
  ```
- **Glossaries** (`makeglossaries`):
  ```bash
  makeglossaries -d build main
  ```

#### Compilation Sequences
*Target environment: TeX Live 2024 (`tlnet-final`, LuaHBTeX 1.18.0, Biber 2.20)*
- **`book` documentclass** (Full cycle with bibliography and glossaries):
  ```bash
  mkdir -p build
  lualatex --output-directory=build --interaction=nonstopmode --synctex=1 main.tex
  biber --input-directory=build --output-directory=build main
  makeglossaries -d build main
  lualatex --output-directory=build --interaction=nonstopmode --synctex=1 main.tex
  lualatex --output-directory=build --interaction=nonstopmode --synctex=1 main.tex
  ```
  *(Output PDF: `build/main.pdf`)*

- **Other documentclasses** (`article`, `beamer`, `exam`, `flashcards`):
  ```bash
  mkdir -p build
  lualatex --output-directory=build --interaction=nonstopmode --synctex=1 main.tex
  lualatex --output-directory=build --interaction=nonstopmode --synctex=1 main.tex
  ```
  *(Output PDF: `build/main.pdf`)*

#### Batch Script (`compile_tex.sh`)
- **Never use `compile_tex.sh` to compile documents**: AI agents must **never** run `compile_tex.sh` to build or verify documents. Only compile manually using direct `lualatex` / `biber` / `makeglossaries` commands when needed, unless the explicit task is specifically to debug or test `compile_tex.sh` itself.

### 3.3 Creating a New Script (`book`)
- **Skeleton**: A topic's sub-main file (e.g. `Skript.tex`) is `\input` by `main.tex` *after* the preamble and contains its own `\begin{document} … \end{document}`. Commands/environments specific to the script may be defined at its top, before `\begin{document}`. Minimal pattern (see `Grundlagen_Info/16_ComputerUndKodierungen/Skript/Skript.tex` or `Medienkompetenzwoche/UG_Datenschutz/Skript.tex`): `\settoggle{includelogo}{true}`, define `\thesubject`, `\thetopic`, `\thelogo`, `\logosize`, set `\lhead`/`\rhead`, `\settoggle{emoji}{false}`, `\def\arrayB{…}`, `\maketitlepage{<title>}{<subtitle>}` (empty subtitle prints «Skript»), `\tableofcontents`, then one `\input` per chapter file (`\chapter{…}` each), `\appendix`, and `\printglossaries` if acronyms are used. Register the new file in `main.tex` (commented line in the matching toggle section).
- **Environments** (`Preambles/pre_4_custom_envs.tex`): `myexercise[Title]`, `mychallenge[Title]` (share one counter, numbered per chapter), `myanswer` (inside an exercise/challenge; solution box), `myremark`, `mysummary[Title]`, `myprocedure[Title]`, `myattention`, `myexample`, `myexcursion`, `mydefinition`, `mycaution[Title]`, `mybox`; list `aenum` for (a), (b), …; macro `\tib{…}` (bold italic key term). Custom boxes can reuse `tcolorboxTemplate[title=…, colback=…, colframe=…, colbacktitle=…]`.
- **Student version without solutions**: compile with the class option `exerciseonly` (second `book` line in `main.tex`); it hides all `myanswer` boxes. Restore the default class line afterwards.
- **Glossary pitfalls**: the first `\gls{X}` prints «long (short)». Do not write the long form yourself before `\gls{X}`, and use `\acrshort{X}` in compounds (e.g. `\acrshort{GPS}-Koordinaten`) or right after spelling the term out. In the `exerciseonly` version, solutions are skipped, so the «first use» can move.
- **Tables**: give `p{…}` columns a total width clearly below `\textwidth` (column padding adds up); inside tcolorboxes less. `\small` before `tabular` helps for wide grids. Check the log for `Overfull \hbox` and fix anything above a few pt.
- **Long URLs and compounds** cause overfull lines: put long `\url{…}` on their own line or add discretionary hyphens (`Daten\-schutz\-…`); a word with an explicit hyphen (`Sicherheits-`) cannot be hyphenated elsewhere.
- **Language**: Swiss Standard German (no «ß»; search the new files for `ß` before compiling), formal «Sie» for students, quotes via `\enquote{…}`.
- **Local build notes**: `biber` may fail locally on macOS (`lipo` extraction error); this is harmless for documents without citations (`citations` toggle false). When copying compiled PDFs elsewhere, take `build/main.pdf` after the final LuaLaTeX pass.

---

## 4. Operational Checklist for AI Agents

Before submitting changes or marking a task complete:

1. [ ] **Verify Compilation in `build/` (Only if explicitly requested)**: If the user requested compilation, ensure the edited `.tex` file compiles clean using LuaLaTeX into the `build/` subfolder (`--output-directory=build`) without syntax errors or broken package dependencies.
2. [ ] **Check Vector/TikZ Graphics**: Ensure new figures use TikZ or `.pdf`/`.svg` vector formats.
3. [ ] **Check Slide Sync**: If tasks or numbering in scripts were updated, verify and update the corresponding slide deck (`beamer`).
4. [ ] **Respect Licensing**: Verify no unlicensed third-party materials or code were introduced.
5. [ ] **Preserve Formatting & Comments**: Keep inline comments clean and informative.
6. [ ] **Keep WIP Chapters Commented Out**: Ensure chapters marked as 'under construction' (e.g. `Kapitel_06.tex` in `Skript.tex`) remain commented out.
7. [ ] **Clean Up Rendered PNGs**: Delete all temporary PNG files generated during visual verification (`pdftoppm`) before finishing.
8. [ ] **Clean Up Aux Files & Ensure Clean Root**: Ensure compilation was run with output directed to `build/` so no auxiliary files (`aux`, `log`, `out`, `toc`, etc.) leak into the repository root directory. If temporary files in `build/` need clearing, remove them (`rm -rf build/*`).
9. [ ] **Use Glossaries (`\gls{...}`) for Acronyms**: Ensure all acronyms are defined in `Preambles/pre_6_glossaries.tex` and referenced via `\gls{...}` / `\glspl{...}`.
10. [ ] **Keep `main.tex` Unchanged in Commits**: Ensure session-specific `\input{...}` activations and `\documentToggle` switches in `main.tex` are NOT committed (revert via `git checkout main.tex`), unless a new document was added or paths were restructured.
