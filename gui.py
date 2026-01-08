"""
Program for a GUI menu where users can choose which game they want to play
- Create window with a menu for each game.
- Each game would be a button.
- Once a button is pressed call on the game to open
- to add a game to the menu first import the game function and then create a button for the game.
"""

#-------------------------------------------------------------#
#                 Import libaries                             #
#          Import games from games.py file                    #
#          - This allows for games to be added or taken away  #
#          Import tkinter                                     #
#          - This is used to create the GUI                   #
#-------------------------------------------------------------#
from mini_arcade import rock_paper_scissors
from mini_arcade import guess_a_number
from mini_arcade import coin_toss
from mini_arcade import quiz_game
from mini_arcade import tic_tac_toe
from mini_arcade import snake_game
from mini_arcade import dice_roll
import tkinter as tk

# setting up the window

def main():

    # creating the GUI
    root = tk.Tk()
    root.title('Game Gui Menu')
    root.minsize(400, 400)
    root.configure(background='#2c3e50')

    games = [
        ('Rock Paper Scissors', rock_paper_scissors),
        ('Guess a number', guess_a_number),
        ('Coin Toss', coin_toss),
        ('Tic Tac Toe', tic_tac_toe),
        ('Snake Game', snake_game),
        ('Dice Roll', dice_roll),
        ('Quiz Game', quiz_game),
    ]


    status_label = tk.Label(root, text='Welcome to the Arcade!', font=('Helvetica', 12), bg='#2c3e50', fg='#bdc3c7')

    # function to launch the games.
    # If there is a bug in one of the games that causes it to crash this function keeps all of the other games working
    def launch_game(game_func):
        try:
            display_name = game_func.__name__.replace('_', ' ').title()
            status_label.config(text=f'Now Playing: {display_name}', fg='#2ecc71')
            game_func(status_label)
        except Exception as e:
            status_label.config(text='Error: Game failed to load', fg='#e74c3c')
            print(f"Log: {game_func.__name__} crashed: {e}")

    # UI Setup
    tk.Label(root, text='Main Menu', font=('Helvetica', 24, 'bold'), bg='#2c3e50', fg='white').pack(pady=20)
    status_label.pack(pady=10)

    menu_frame = tk.Frame(root, bg='#2c3e50')
    menu_frame.pack(pady=10)


    # Create buttons for the games
    for i, (name, game_func) in enumerate(games):
        btn = tk.Button(
            menu_frame,
            text=name,
            font=('Helvetica', 11),
            width=20,
            height=2,
            bg='#34495e',
            fg='white',
            command=lambda f=game_func: launch_game(f)
        )
        # Row/Column grid math
        btn.grid(row=i // 2, column=i % 2, padx=10, pady=10)

    tk.Button(root, text='Exit Arcade', font=('Helvetica', 10, 'bold'),
              bg='#c0392b', fg='white', width=15, command=root.destroy).pack(pady=30)

    root.mainloop()


if __name__ == '__main__':
    main()