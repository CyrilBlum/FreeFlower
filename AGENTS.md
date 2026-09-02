# AGENTS.md

Instructions and guidelines for AI coding agents and automated tools working on the **FreeFlower** repository.

---

## 1. Overview & Purpose

**FreeFlower** is an open-source repository containing high-quality educational materials (lecture notes, exercise books, slides, exams, and scripts) tailored for Swiss upper-secondary education (Gymnasium, Sek II, *Grundlagenfach Informatik*).

All materials are written in LaTeX (primarily using LuaLaTeX) and supporting Python/Shell scripts. Automated agents working in this repository must maintain strict consistency with existing style patterns, pedagogical standards, and compilation rules.

---

## 2. Core Rules for Collaboration & Contribution

These rules are strictly enforced and based on the official [FreeFlower Collaboration Guidelines](https://cyrilblum.github.io/FreeFlower/zusammenarbeit.html):

### 2.1 Branching & Pull Requests
- **Never push directly to `main`**.
- Always create a dedicated branch (e.g., `feature/...`, `fix/...`, `docs/...`) and submit work via a **Pull Request**.
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

### 2.5 Compilation Policy & Quality Standard
- **No Automatic Compilation**: AI agents do **not** need to compile edited `.tex` files unless the user explicitly requests it.
- **Zero-Error Standard (when compilation is requested)**: If the user explicitly asks for compilation, all modified TeX documents must compile without errors, fatal warnings, or unresolved reference/citation issues under LuaLaTeX.

### 2.6 Synchronizing Exercises: Slides vs. Handouts/Scripts
- **Manual Exercise Sync**: Exercise and task numberings in Beamer slides are **not** updated automatically when corresponding parts in scripts or exercise handouts are changed.
- **Agent Rule**: Whenever you modify or add exercises in script/book sections, check and manually update the corresponding slide numbers and Beamer presentations in the repository.

### 2.7 Cleanup of Temporary Rendered Artifacts
- **Always Clean Up Rendered Images**: When using tools like `pdftoppm` to generate temporary `.png` files for visual inspection and verification, always delete all agent-generated `.png` files from the repository directory before finishing the task.

### 2.8 Cleanup of LaTeX Auxiliary Files
- **Always Clean Up Aux Files**: After every build, delete all LaTeX auxiliary files from the repository directory before finishing the task. This includes (but is not limited to):
  `aux`, `log`, `out`, `toc`, `lof`, `lot`, `glo`, `idx`, `fls`, `fdb_latexmk`, `synctex.gz`
- You can remove them with a command such as:
  ```bash
  rm -f main.{aux,log,out,toc,lof,lot,glo,idx,fls,fdb_latexmk,synctex.gz}
  ```

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

#### Compilation Sequences
- **`book` documentclass**:
  ```bash
  lualatex main.tex -> biber main -> makeglossaries main -> lualatex main.tex -> lualatex main.tex
  ```
- **Other documentclasses** (`article`, `beamer`, `exam`, `flashcards`):
  ```bash
  lualatex main.tex -> lualatex main.tex
  ```

#### Batch Script (`compile_tex.sh`)
- **Never use `compile_tex.sh` to compile documents**: AI agents must **never** run `compile_tex.sh` to build or verify documents. Only compile manually using direct `lualatex` / `biber` / `makeglossaries` commands when needed, unless the explicit task is specifically to debug or test `compile_tex.sh` itself.

---

## 4. Operational Checklist for AI Agents

Before submitting changes or marking a task complete:

1. [ ] **Verify Compilation (Only if explicitly requested)**: If the user requested compilation, ensure the edited `.tex` file compiles clean using LuaLaTeX without syntax errors or broken package dependencies.
2. [ ] **Check Vector/TikZ Graphics**: Ensure new figures use TikZ or `.pdf`/`.svg` vector formats.
3. [ ] **Check Slide Sync**: If tasks or numbering in scripts were updated, verify and update the corresponding slide deck (`beamer`).
4. [ ] **Respect Licensing**: Verify no unlicensed third-party materials or code were introduced.
5. [ ] **Preserve Formatting & Comments**: Keep inline comments clean and informative.
6. [ ] **Clean Up Rendered PNGs**: Delete all temporary PNG files generated during visual verification (`pdftoppm`) before finishing.
7. [ ] **Clean Up Aux Files**: Delete all LaTeX auxiliary files (`aux`, `log`, `out`, `toc`, `lof`, `lot`, `glo`, `idx`, `fls`, `fdb_latexmk`, `synctex.gz`) generated during compilation before finishing.
