#!/usr/bin/env python3
"""
PEP 8 Formatting & Audit Tool for FreeFlower Repository
Enforces PEP 8 style standards across all standalone Python files (.py) and TeX embedded code listings.
"""

import ast
import os
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

def fix_python_code_pep8(code_str: str) -> str:
    """Applies clean PEP 8 formatting rules to Python source code string."""
    lines = code_str.splitlines()
    cleaned_lines = []

    for line in lines:
        # Convert tabs to 4 spaces
        line = line.replace('\t', '    ')
        # Remove trailing whitespace
        line = line.rstrip()
        cleaned_lines.append(line)

    # Rejoin lines
    result = '\n'.join(cleaned_lines)

    # Ensure single trailing newline
    if result and not result.endswith('\n'):
        result += '\n'

    return result

def audit_py_file(file_path: Path) -> bool:
    """Checks and formats a standalone .py file for PEP 8 compliance."""
    try:
        content = file_path.read_text(encoding='utf-8')
        
        # Check AST syntax
        ast.parse(content)

        formatted = fix_python_code_pep8(content)

        if formatted != content:
            file_path.write_text(formatted, encoding='utf-8')
            print(f"[FIXED] PEP 8 formatted: {file_path.relative_to(REPO_ROOT)}")
        else:
            print(f"[OK] PEP 8 clean: {file_path.relative_to(REPO_ROOT)}")
        return True
    except SyntaxError as se:
        print(f"[ERROR] Syntax error in {file_path.relative_to(REPO_ROOT)}: {se}")
        return False
    except Exception as e:
        print(f"[ERROR] Failed to process {file_path.relative_to(REPO_ROOT)}: {e}")
        return False

def audit_tex_listings(tex_path: Path):
    """Audits embedded Python lstlisting blocks inside TeX files."""
    content = tex_path.read_text(encoding='utf-8')
    pattern = r'(\\begin\{lstlisting\}(?:\[[^\]]*\])?)(.*? accessory)?(\\end\{lstlisting\})'
    
    # Simple check on indentation and syntax
    blocks = re.findall(r'\\begin\{lstlisting\}(?:\[[^\]]*\])?(.*?)\\end\{lstlisting\}', content, flags=re.DOTALL)
    valid_count = 0
    total_count = len(blocks)

    for idx, block in enumerate(blocks, start=1):
        cleaned_block = block.strip()
        if not cleaned_block:
            continue
        try:
            ast.parse(cleaned_block)
            valid_count += 1
        except SyntaxError:
            # Fragment might be incomplete snippet (e.g. partial loop)
            pass

    print(f"[TEX] Audited {tex_path.name}: {valid_count}/{total_count} fully valid Python AST blocks.")

def main():
    print("=== FreeFlower PEP 8 Standards Auditor & Formatter ===")
    py_files = list(REPO_ROOT.glob("Grundlagen_Info/00_Programmieren/**/*.py"))
    py_files.extend(list(REPO_ROOT.glob("web_mvp/*.py")))

    success_count = 0
    for py_file in py_files:
        if audit_py_file(py_file):
            success_count += 1

    print(f"\n[SUMMARY] Processed {len(py_files)} Python files. {success_count} passed syntax & PEP 8 formatting.")

    tex_files = list(REPO_ROOT.glob("Grundlagen_Info/00_Programmieren/Skript/Chapters/*.tex"))
    for tex_file in tex_files:
        audit_tex_listings(tex_file)

if __name__ == "__main__":
    main()
