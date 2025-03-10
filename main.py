import sys
import os
import importlib

class GameManager:
    def __init__(self):
        self.level = 1
        self.max_level = 3  # Updated to include Level 3

    def run(self):
        while self.level <= self.max_level:
            print(f"Starting Level {self.level}...")
            level_completed = self.load_level()
            if level_completed:
                self.level += 1  # Move to the next level
            else:
                print("Game Over!")
                return
        print("Congratulations! You've completed the game.")

    def load_level(self):
        module_name = f"src.levels.level_{self.level}"
        print(f"Loading module: {module_name}")

        try:
            level_module = importlib.import_module(module_name)
            print(f"Successfully loaded {module_name}")
            level = level_module.Level()
            return level.start()
        except ModuleNotFoundError as e:
            print(f"Error: {e}")
            print(f"Level {self.level} not found!")
            return False
        except AttributeError:
            print(f"Level {self.level} is not correctly defined!")
            return False

# Main function to start the game
def main():
    game = GameManager()
    game.run()

if __name__ == "__main__":
    main()
