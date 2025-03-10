class Level:
    def start(self):
        print("Level 1: Text-based puzzle game started.")

        while True:  # Allow retrying until correct
            answer = input("What is 2 + 2? ")
            if answer == "4":
                print("Correct! Moving to the next level.")
                return True  # ✅ Weiter zu Level 2
            else:
                print("Wrong! Try again.")