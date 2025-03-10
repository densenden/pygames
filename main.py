import sys
import os
from src.engine.game import GameManager


def main():
    print("Willkommen zu Evolution Game!")

    # Prüfen, ob src-Ordner existiert
    if not os.path.exists("src"):
        print("Fehlende Spielstruktur. Bitte sicherstellen, dass alle Module vorhanden sind.")
        sys.exit(1)

    game = GameManager()
    game.run()


if __name__ == "__main__":
    main()


# --- Verzeichnisstruktur erstellen ---
def setup_project_structure():
    directories = [
        "src/engine", "src/levels", "src/ui", "src/utils", "data", "assets", "tests"
    ]
    files = {
        "src/engine/game.py": """
class GameManager:
    def __init__(self):
        self.level = 1

    def run(self):
        print(f"Starte Spiel auf Level {self.level}")
        self.load_level()

    def load_level(self):
        print(f"Lade Level {self.level}...")
""",
        "src/levels/level_1.py": """
def play():
    print("Level 1: Textbasiertes Rätselspiel gestartet.")
    answer = input("Was ist 2 + 2? ")
    if answer == "4":
        print("Richtig!")
    else:
        print("Falsch! Probiere es erneut.")
""",
        "README.md": """
# Evolution Game - Python Project

Ein Spiel, das sich von einer Kommandozeile bis zu einem 3D-Multiplayer entwickelt.

## Starten:
```bash
python main.py
```
""",
        ".gitignore": """
__pycache__/
*.pyc
.DS_Store
.env
"""
    }

    for directory in directories:
        os.makedirs(directory, exist_ok=True)

    for file, content in files.items():
        with open(file, "w") as f:
            f.write(content)

    print("Projektstruktur eingerichtet.")


setup_project_structure()
