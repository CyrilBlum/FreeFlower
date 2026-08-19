import os

HIGHSCORE_FILE = "highscore.txt"


def load_highscore() -> int:
    """Lädt den Highscore aus der Datei highscore.txt. Gibt 0 zurück, falls die Datei nicht existiert."""
    if os.path.exists(HIGHSCORE_FILE):
        try:
            with open(HIGHSCORE_FILE, "r", encoding="utf-8") as file:
                return int(file.read().strip())
        except ValueError:
            return 0
    return 0


def save_highscore(score: int) -> None:
    """Speichert den aktuellen Highscore in der Datei highscore.txt."""
    with open(HIGHSCORE_FILE, "w", encoding="utf-8") as file:
        file.write(str(score))


# Beispielhafte Verwendung:
current_score = 150
best_score = load_highscore()

if current_score > best_score:
    print(f"Neuer Rekord! Alter Highscore: {best_score} -> Neuer Highscore: {current_score}")
    save_highscore(current_score)
else:
    print(f"Highscore nicht geknackt. Aktueller Rekord: {best_score}")
