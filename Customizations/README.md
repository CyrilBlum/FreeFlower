# FreeFlower Customizations & School Themes

This directory contains optional school-specific themes, branding assets, and footline layouts for the **FreeFlower** open-source educational repository.

---

## 1. Open-Source Philosophy

**FreeFlower** is designed as a neutral, open-source repository for Swiss upper-secondary education (*Gymnasium / Sek II, Grundlagenfach Informatik*). 

- **Neutral by Default**: Out of the box, FreeFlower slide decks compile using a clean, unbranded, open-source layout with standard Beamer framing and page numbering.
- **Opt-in School Branding**: Any teacher or institution can easily activate or create their own school-specific theme (logos, corporate colors, custom footlines, wave designs) without modifying the core educational content or LaTeX slide decks.

---

## 2. Choosing Slide Aspect Ratios

You can select your preferred slide aspect ratio in `main.tex` at the top of the file:

- **16:9 Widescreen** (*Default / Recommended for modern projectors*):
  ```latex
  \documentclass[aspectratio=169,xcolor={table,dvipsnames,svgnames},hyphens]{beamer}
  ```
- **4:3 Standard** (*Traditional square ratio*):
  ```latex
  \documentclass[aspectratio=43,xcolor={table,dvipsnames,svgnames},hyphens]{beamer}
  ```
- **16:10 Widescreen**:
  ```latex
  \documentclass[aspectratio=1610,xcolor={table,dvipsnames,svgnames},hyphens]{beamer}
  ```

---

## 3. Toggling School Customizations in `main.tex`

In `main.tex`, use the `schoolcustomization` toggle to switch between neutral open-source mode and school-customized mode:

### Option A: Neutral Open-Source Layout (Default)
```latex
\newtoggle{schoolcustomization} \settoggle{schoolcustomization}{false}
```
This renders slides with standard neutral styling, standard frametitles, and clean page numbering.

### Option B: Custom School Branding (e.g. FDU Theme)
```latex
\newtoggle{schoolcustomization} \settoggle{schoolcustomization}{true}
\def\schoolTheme{FDU}
```
This automatically loads `Customizations/FDU/fdu_theme.tex` and applies school corporate colors (`FDUgreen`, `FDUblue`, `FDUteal`, `FDUink`), custom bottom wave graphic footlines, and school logo overlays.

---

## 4. Directory Structure

```
Customizations/
├── README.md               # Theme & customization guide (this file)
├── Default/                # Open-source neutral fallback theme
│   └── default_theme.tex
└── FDU/                    # FDU (Filiale Dübendorf) theme
    ├── fdu_theme.tex       # Colors, footlines, and presentation macros
    └── assets/             # Logos, wave graphics, and images
        ├── 02_System_Stempelversion_Logo_RZ_schwarz.pdf
        ├── Glatt_Linie_3_farbig_lang.pdf
        └── logo-negativ.pdf
```

---

## 5. How to Add Your Own School Theme

To create a theme for your school (e.g. `KSA`, `KUE`, `KCR`):

1. Create a new folder: `Customizations/YourSchool/`
2. Create `Customizations/YourSchool/YourSchool_theme.tex` (or `fdu_theme.tex` template format).
3. Place any school logos or graphics in `Customizations/YourSchool/assets/`.
4. In `YourSchool_theme.tex`, define your custom colors and redefine the Beamer `footline` template or macros:
   ```latex
   \definecolor{MySchoolColor}{RGB}{0, 102, 204}
   \setbeamercolor{frametitle}{fg=MySchoolColor}
   \setbeamertemplate{footline}{%
     % Your custom TikZ or text footline here
   }
   ```
5. Set `\settoggle{schoolcustomization}{true}` and `\def\schoolTheme{YourSchool}` in `main.tex`.
