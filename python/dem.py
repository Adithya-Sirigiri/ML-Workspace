import tkinter as tk
import random

# Main logic function
def play(user_choice):
    computer_choice = random.randint(0, 2)

    if computer_choice == user_choice:
        result = "It's a draw!"
    elif user_choice == 0 and computer_choice == 2:
        result = "You win!"
    elif user_choice == 2 and computer_choice == 0:
        result = "You lose!"
    elif computer_choice > user_choice:
        result = "You lose!"
    elif user_choice > computer_choice:
        result = "You win!"
    
    # Update UI with results
    user_label.config(text=f"You chose: {choices[user_choice]}")
    comp_label.config(text=f"Computer chose: {choices[computer_choice]}")
    result_label.config(text=f"Result: {result}")

# Tkinter setup
window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("350x250")

choices = ['Rock', 'Paper', 'Scissors']

# Buttons
tk.Label(window, text="Choose one:", font=("Arial", 12)).pack(pady=10)
for i, choice in enumerate(choices):
    tk.Button(window, text=choice, width=15, command=lambda i=i: play(i)).pack(pady=2)

# Result Labels
user_label = tk.Label(window, text="", font=("Arial", 10))
user_label.pack(pady=5)

comp_label = tk.Label(window, text="", font=("Arial", 10))
comp_label.pack(pady=5)

result_label = tk.Label(window, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

window.mainloop()

