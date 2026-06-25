#!/usr/bin/env python3
"""
Tabu.tex Generator - Generiert randomisierte Tabu-Kartendatei
Nutzt tabu_words.txt (organisiert nach Kategorien) und tabu_config.txt (Toggles)
"""

import random
import os
from pathlib import Path

# Pfade
SCRIPT_DIR = Path(__file__).parent
WORDS_FILE = SCRIPT_DIR / "tabu_words.txt"
CONFIG_FILE = SCRIPT_DIR / "tabu_config.txt"
OUTPUT_FILE = SCRIPT_DIR / "Tabu.tex"
TEMPLATE_FILE = SCRIPT_DIR / "Tabu_template.tex"

def load_config():
    """Liest tabu_config.txt und gibt Dictionary mit aktivierten Kategorien zurück"""
    config = {}
    with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                parts = line.split(': ')
                if len(parts) == 2:
                    category = parts[0].strip()
                    enabled = parts[1].strip().lower() == 'true'
                    config[category] = enabled
    return config

def load_words():
    """Liest tabu_words.txt und organisiert Wörter nach Kategorien"""
    words_by_category = {}
    current_category = None
    
    with open(WORDS_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line.startswith('category: '):
                current_category = line.replace('category: ', '')
                words_by_category[current_category] = []
            elif line and current_category:
                word_data = line.split(' | ')
                if len(word_data) == 2:
                    word = word_data[0].strip()
                    tabu_words = word_data[1].strip()
                    words_by_category[current_category].append((word, tabu_words))
    
    return words_by_category

def load_template():
    """Liest die Template-Datei (Header und Regeln)"""
    with open(TEMPLATE_FILE, 'r', encoding='utf-8') as f:
        return f.read()

def generate_tex(config, words_by_category):
    """Generiert die .tex Datei mit randomisierten Wörtern"""
    template = load_template()
    
    # Sammle alle aktivierten Wörter
    all_words = []
    for category, enabled in config.items():
        if enabled and category in words_by_category:
            all_words.extend(words_by_category[category])
    
    # Randomisiere die Wörter
    random.shuffle(all_words)
    
    # Generiere die tabucard Befehle
    cards = []
    for word, tabu_words in all_words:
        cards.append(f"\\tabucard{{{word}}}{{\n{tabu_words}\n}}\n")
    
    # Füge die Karten ans Template an und schließe mit \end{document}
    output = template + "\n".join(cards) + "\n\\end{document}"
    
    # Schreibe die Output-Datei
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(output)
    
    print(f"✓ Tabu.tex generiert mit {len(all_words)} Wörtern")
    print(f"  Kategorien: {', '.join([cat for cat, enabled in config.items() if enabled])}")

def main():
    if not WORDS_FILE.exists():
        print(f"✗ Fehler: {WORDS_FILE} nicht gefunden")
        return
    
    if not CONFIG_FILE.exists():
        print(f"✗ Fehler: {CONFIG_FILE} nicht gefunden")
        return
    
    if not TEMPLATE_FILE.exists():
        print(f"✗ Fehler: {TEMPLATE_FILE} nicht gefunden")
        return
    
    config = load_config()
    words_by_category = load_words()
    generate_tex(config, words_by_category)

if __name__ == "__main__":
    main()
