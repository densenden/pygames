
import importlib

class GameManager:
    def __init__(self):
        self.level = 1

    def run(self):
        print(f"Starting game at Level {self.level}")
        self.load_level()

    def load_level(self):
        try:
            level_module = importlib.import_module(f"src.levels.level_{self.level}")
            level = level_module.Level()
            level.start()
        except ModuleNotFoundError:
            print(f"Level {self.level} not found!")
        except AttributeError:
            print(f"Level {self.level} is not correctly defined!")
