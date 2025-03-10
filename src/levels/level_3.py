import tkinter as tk
import random
import json
import os


class Level:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Level 3: Trivia Quiz")
        self.root.geometry("500x400")
        self.completed = False
        self.questions = self.load_questions()
        self.current_question = random.choice(self.questions)

    def load_questions(self):
        """Load trivia questions from an external JSON file."""
        json_path = os.path.join(os.path.dirname(__file__), "trivia_questions.json")
        with open(json_path, "r") as file:
            return json.load(file)

    def check_answer(self, selected_answer):
        """Check if the selected answer is correct."""
        if selected_answer == self.current_question["correct"]:
            self.completed = True
            self.root.destroy()
        else:
            self.question_label.config(text="Wrong! Try again.", fg="red")

    def start(self):
        """Create the quiz GUI with multiple-choice buttons."""
        self.question_label = tk.Label(self.root, text=self.current_question["question"], font=("Arial", 14),
                                       wraplength=400)
        self.question_label.pack(pady=20)

        answers = self.current_question["incorrect"] + [self.current_question["correct"]]
        random.shuffle(answers)  # Shuffle answer order

        for answer in answers:
            btn = tk.Button(self.root, text=answer, command=lambda a=answer: self.check_answer(a), font=("Arial", 12))
            btn.pack(pady=5, padx=20, fill=tk.X)

        self.root.mainloop()
        return self.completed  # True → Move to next level
