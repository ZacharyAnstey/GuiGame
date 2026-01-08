# Python mini arcade 
A modular, interactive game collection built with Tkinter. This project features a central GUI manager that launches various classic games, each following a standardized interface contract for seamless integration.

# Games Included
Snake: Classic survival game. Eat food to grow, but don't hit the walls or yourself!

Tic Tac Toe: Play against a defensive AI that blocks your moves.

Rock Paper Scissors: A classic battle against the computer.

Quiz Game: Test your Python knowledge with a timed multiple-choice quiz.

Guess a Number: You have 3 tries to find the secret number.

Dice Roll & Coin Toss: Simple games of chance.

Prerequisites
Python 3.x

Tkinter (usually included with Python)

# Instalation 
1) Clone repository : git clone https://github.com/yourusername/python-desktop-arcade.git
2) Navigate to folder : cd python-desktop-arcade
3) Run the application: Run the gui.py file

# Features 
Standardized Game Contract: Every game function accepts a status_label parameter to update the main menu in real-time.

Idle Timer Manager: Automatically prompts the user if they are still playing after a period of inactivity.

Defensive AI: The Tic Tac Toe computer move logic checks for winning or blocking opportunities before moving randomly.

Consistent UI: Uses a unified color palette (Midnight Blue, Emerald Green, Alizarin Red) for a professional look.

# Architecture 
Define your function: def new_game(status_label=None):

Use the standard footer: Call add_standard_footer(window, status_label) to handle window closing logic.

Use the restart helper: Call ask_play_again(...) to prompt the user after the game ends.

# Future directions: 
1) fix up consitancy issues.
2) Add a high score tracker for all games
3) Add mulitple difficulties to tictactoe
4) Add multiple difficulties to snake

5) 
