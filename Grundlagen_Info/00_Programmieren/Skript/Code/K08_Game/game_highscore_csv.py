import csv
import os

CSV_FILE = "highscores.csv"


def load_leaderboard() -> list[tuple[str, int]]:
    """Lädt die Leaderboard-Tabelle aus einer CSV-Datei.

    Gibt eine Liste von Tuples (Name, Score) zurück, sortiert nach Score.
    """
    scores = []
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader, None)  # Header-Zeile überspringen
            for row in reader:
                if len(row) == 2:
                    name, score_str = row
                    try:
                        scores.append((name, int(score_str)))
                    except ValueError:
                        continue
    return sorted(scores, key=lambda item: item[1], reverse=True)


def save_score(player_name: str, score: int) -> None:
    """Speichert ein neues Spieler-Ergebnis in der CSV-Datei."""
    file_exists = os.path.exists(CSV_FILE)
    with open(CSV_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Player", "Score"])  # Header schreiben
        writer.writerow([player_name, score])


# Beispielhafte Verwendung:
save_score("Anna", 240)
save_score("Ben", 180)
save_score("Clara", 310)

leaderboard = load_leaderboard()
print("--- TOP SPIELER ---")
for rank, (player, score) in enumerate(leaderboard, start=1):
    print(f"{rank}. {player}: {score} Punkte")
