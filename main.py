import sys
import os
import importlib

class GameManager:
    def __init__(self):
        self.level = 1
        self.max_level = 3  # Change this as new levels are added

    def run(self):
        while self.level <= self.max_level:
            print(f"Starting Level {self.level}...")
            level_completed = self.load_level()
            if level_completed:
                self.level += 1  # Move to the next level
            else:
                print("Game Over!")
                return  # Exit game loop if a level fails
        print("Congratulations! You've completed the game.")

    def load_level(self):
        try:
            level_module = importlib.import_module(f"src.levels.level_{self.level}")
            level = level_module.Level()
            return level.start()  # True if level is completed, False if failed
        except ModuleNotFoundError:
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
