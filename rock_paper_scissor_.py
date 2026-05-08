import tkinter as tk
import random

# Main window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("500x500")
root.config(bg="#1e1e2f")

choices = ["Rock", "Paper", "Scissors"]

player_score = 0
computer_score = 0

# Title
title = tk.Label(
    root,
    text="Rock Paper Scissors",
    font=("Arial", 24, "bold"),
    bg="#1e1e2f",
    fg="white"
)
title.pack(pady=20)

# Result Label
result_label = tk.Label(
    root,
    text="Choose an option",
    font=("Arial", 16),
    bg="#1e1e2f",
    fg="cyan"
)
result_label.pack(pady=20)

# Score Label
score_label = tk.Label(
    root,
    text="Player: 0   Computer: 0",
    font=("Arial", 14),
    bg="#1e1e2f",
    fg="white"
)
score_label.pack(pady=10)


def play(player_choice):
    global player_score, computer_score

    computer_choice = random.choice(choices)

    if player_choice == computer_choice:
        result = "It's a Tie!"
    elif (
        (player_choice == "Rock" and computer_choice == "Scissors") or
        (player_choice == "Paper" and computer_choice == "Rock") or
        (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win!"
        player_score += 1
    else:
        result = "Computer Wins!"
        computer_score += 1

    result_label.config(
        text=f"You: {player_choice}\nComputer: {computer_choice}\n\n{result}"
    )

    score_label.config(
        text=f"Player: {player_score}   Computer: {computer_score}"
    )


# Buttons Frame
button_frame = tk.Frame(root, bg="#1e1e2f")
button_frame.pack(pady=30)

# Rock Button
rock_btn = tk.Button(
    button_frame,
    text="Rock",
    font=("Arial", 14, "bold"),
    width=10,
    bg="#ff4b5c",
    fg="white",
    command=lambda: play("Rock")
)
rock_btn.grid(row=0, column=0, padx=10)

# Paper Button
paper_btn = tk.Button(
    button_frame,
    text="Paper",
    font=("Arial", 14, "bold"),
    width=10,
    bg="#4e9af1",
    fg="white",
    command=lambda: play("Paper")
)
paper_btn.grid(row=0, column=1, padx=10)

# Scissors Button
scissors_btn = tk.Button(
    button_frame,
    text="Scissors",
    font=("Arial", 14, "bold"),
    width=10,
    bg="#32c766",
    fg="white",
    command=lambda: play("Scissors")
)
scissors_btn.grid(row=0, column=2, padx=10)

root.mainloop()