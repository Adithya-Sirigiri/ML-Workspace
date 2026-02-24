import tkinter as tk
from tkinter import messagebox
import random

class GuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("🎯 Ultimate Number Guessing Game")
        self.master.geometry("500x600")
        self.master.resizable(False, False)
        self.master.configure(bg="#1e1e2e")
        self.setup_widgets()
        self.reset_variables()

    def setup_widgets(self):
        self.title_frame = tk.Frame(self.master, bg="#1e1e2e")
        self.title_frame.pack(pady=20)

        self.title_label = tk.Label(self.title_frame, text="🎮 GUESS THE NUMBER 🎮", font=("Arial Black", 20), fg="#89b4fa", bg="#1e1e2e")
        self.title_label.pack()

        self.subtitle_label = tk.Label(self.master, text="Choose a number between 1 and 50", font=("Calibri", 14), fg="#cdd6f4", bg="#1e1e2e")
        self.subtitle_label.pack(pady=10)

        self.difficulty_frame = tk.Frame(self.master, bg="#1e1e2e")
        self.difficulty_frame.pack(pady=10)

        self.easy_button = tk.Button(self.difficulty_frame, text="Easy (10 attempts)", width=15, font=("Arial", 12),
                                     command=lambda: self.start_game("easy"), bg="#a6e3a1", fg="#1e1e2e")
        self.easy_button.grid(row=0, column=0, padx=10)

        self.hard_button = tk.Button(self.difficulty_frame, text="Hard (5 attempts)", width=15, font=("Arial", 12),
                                     command=lambda: self.start_game("hard"), bg="#f38ba8", fg="#1e1e2e")
        self.hard_button.grid(row=0, column=1, padx=10)

        self.info_label = tk.Label(self.master, text="", font=("Calibri", 12), fg="#cdd6f4", bg="#1e1e2e")
        self.info_label.pack(pady=5)

        self.input_entry = tk.Entry(self.master, font=("Arial", 14), width=10, justify='center', state=tk.DISABLED)
        self.input_entry.pack(pady=10)

        self.submit_button = tk.Button(self.master, text="Submit Guess", font=("Arial", 12), state=tk.DISABLED,
                                       command=self.check_guess, bg="#89dceb", fg="#1e1e2e", width=15)
        self.submit_button.pack(pady=5)

        self.result_label = tk.Label(self.master, text="", font=("Calibri", 12), fg="#f9e2af", bg="#1e1e2e")
        self.result_label.pack(pady=10)

        self.attempts_label = tk.Label(self.master, text="", font=("Calibri", 12), fg="#fab387", bg="#1e1e2e")
        self.attempts_label.pack(pady=5)

        self.play_again_button = tk.Button(self.master, text="Play Again", font=("Arial", 12), command=self.play_again,
                                           state=tk.DISABLED, bg="#b4befe", fg="#1e1e2e", width=15)
        self.play_again_button.pack(pady=20)

        self.exit_button = tk.Button(self.master, text="Exit", font=("Arial", 12), command=self.master.quit,
                                     bg="#f2cdcd", fg="#1e1e2e", width=15)
        self.exit_button.pack(pady=10)

    def reset_variables(self):
        self.secret_number = 0
        self.attempts = 0
        self.max_attempts = 0
        self.difficulty = ""
        self.game_active = False

    def start_game(self, level):
        self.difficulty = level
        self.secret_number = random.randint(1, 50)
        self.attempts = 0
        self.max_attempts = 10 if level == "easy" else 5
        self.game_active = True

        self.easy_button.config(state=tk.DISABLED)
        self.hard_button.config(state=tk.DISABLED)
        self.input_entry.config(state=tk.NORMAL)
        self.submit_button.config(state=tk.NORMAL)
        self.play_again_button.config(state=tk.DISABLED)

        self.info_label.config(text=f"You have {self.max_attempts} attempts to guess the number.")
        self.result_label.config(text="")
        self.attempts_label.config(text=f"Attempts Remaining: {self.max_attempts}")
        self.input_entry.delete(0, tk.END)

    def check_guess(self):
        if not self.game_active:
            return

        guess = self.input_entry.get().strip()
        if not guess.isdigit():
            self.result_label.config(text="Please enter a valid number.")
            return

        guess = int(guess)
        self.attempts += 1
        remaining = self.max_attempts - self.attempts
        self.input_entry.delete(0, tk.END)

        if guess == self.secret_number:
            self.result_label.config(text="🎉 Correct! You guessed the number.")
            self.end_game()
        elif guess < self.secret_number and guess >= self.secret_number - 5:
            self.result_label.config(text="Close! Try a slightly higher number.")
        elif guess < self.secret_number - 5 and guess >= self.secret_number - 15:
            self.result_label.config(text="Too low! Aim higher.")
        elif guess < self.secret_number - 15:
            self.result_label.config(text="Way too low! You're far off.")
        elif guess > self.secret_number and guess <= self.secret_number + 5:
            self.result_label.config(text="Close! Try a slightly lower number.")
        elif guess > self.secret_number + 5 and guess <= self.secret_number + 15:
            self.result_label.config(text="Too high! Aim lower.")
        elif guess > self.secret_number + 15:
            self.result_label.config(text="Way too high! You're far off.")

        if remaining > 0:
            self.attempts_label.config(text=f"Attempts Remaining: {remaining}")
        else:
            self.result_label.config(text=f"❌ Out of attempts! The number was {self.secret_number}.")
            self.end_game()

    def end_game(self):
        self.game_active = False
        self.input_entry.config(state=tk.DISABLED)
        self.submit_button.config(state=tk.DISABLED)
        self.play_again_button.config(state=tk.NORMAL)

    def play_again(self):
        self.reset_variables()
        self.input_entry.config(state=tk.DISABLED)
        self.submit_button.config(state=tk.DISABLED)
        self.play_again_button.config(state=tk.DISABLED)
        self.easy_button.config(state=tk.NORMAL)
        self.hard_button.config(state=tk.NORMAL)
        self.input_entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.attempts_label.config(text="")
        self.info_label.config(text="Choose a difficulty to start")

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()
