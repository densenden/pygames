
class GameManager:
    def __init__(self):
        self.level = 1

    def run(self):
        print(f"Starte Spiel auf Level {self.level}")
        self.load_level()

    def load_level(self):
        print(f"Lade Level {self.level}...")
