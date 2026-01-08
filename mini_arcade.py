"""
- Python File to contain the games that we want to play in our gui.
- Each game is written in its own function so that to play each game all you have to do is call the function and the game plays
- To add a new game to the GUI:
    - create a function for the game
    - import the function into the gui.py file
    - create a tk.Button that calls the function when pressed
"""
# libaries.
import tkinter as tk 
import random
from tkinter import messagebox



#--------------------------------------------------------------------#
#                        Constants                                   #
#--------------------------------------------------------------------#

# Colour constants

MIDNIGHT_BLUE  = '#2c3e50'
WET_ASHPHALT   = '#34495e'
EMERALD_GREEN  = '#2ecc71'
ALIZARIN_RED   = '#e74c3c'
SUN_FLOWER     = '#f1c40f'
CLOUDS         = '#ecf0f1'
SILVER         = '#bdc3c7'
ASBESTOS       = '#95a5a6'

# Usage constants
MAIN_BG        = MIDNIGHT_BLUE
GAME_BG        = WET_ASHPHALT
BUTTON_BG      = MIDNIGHT_BLUE
WIN_COLOR      = EMERALD_GREEN
LOSE_COLOR     = ALIZARIN_RED
TIE_COLOR      = SUN_FLOWER
EXIT_BUTTON    = ASBESTOS
PRIMARY_TEXT = CLOUDS
SECONDARY_TEXT = SILVER

# feature constants
RESTART_DELAY = 1500
HEADER_FONT = ('Helvetica', 12,'bold')
STATUS_WAITING = ' Status: Waiting'
TIMER_TIMEOUT = 15000

# ------------------------------------------------------------------ #
#                          Functions                                 #
# -------------------------------------------------------------------#
"""
Bellow are functions that are called on in multiple games 
"""
# -------------------------------------------------------------------#
"""
Play again function :

After each game this function prompts users if the want to play again 
"""
def ask_play_again(window, game_function,status_label=None):
    answer = messagebox.askyesno('Confirmation', 'Do you want to play again?',parent = window) # pop up to ask users if they are still playing
    window.destroy()
    if answer:
        game_function(status_label)
    else:
        if status_label:
            status_label.config(text='Status: Waiting',fg = EMERALD_GREEN)


# ------------------------------------------------------------------ #
"""
Time Delay:
Creates a timer to track if a users has made a move in a game or not and if not asks the users if they are still playing 
"""
def start_timer_manager(window,timeout_ms=TIMER_TIMEOUT):
    idle_timer_id = [None]

    def show_timeout():
        if window.winfo_exists():
            messagebox.showinfo('Timeout','Are you still playing')
            reset_idle_timer()
    def reset_idle_timer():
        if idle_timer_id[0]:
            window.after_cancel(idle_timer_id[0])
        idle_timer_id[0] = window.after(timeout_ms,show_timeout)
    reset_idle_timer()
    return reset_idle_timer

# ------------------------------------------------------------------ #
"""
Close and reset"
Function to close any game window and reset the main menu status label to waiting
"""
def close_and_reset(window,status_label=None):
   window.destroy()
   if status_label:
    status_label.config(text='Status: Waiting',fg = EMERALD_GREEN)


# ------------------------------------------------------------------ #
"""
Standard footer

creates an exit button to exit the games 
"""
def add_standard_footer(window,status_label):
    tk.Button(window,text='Close Game',bg = EXIT_BUTTON,fg=PRIMARY_TEXT,command=lambda: close_and_reset(window,status_label)).pack(pady=20)

    window.protocol('WM_DELETE_WINDOW', lambda: close_and_reset(window,status_label))

# ------------------------------------------------------------------ #
#                          GAMES                                     #
# -------------------------------------------------------------------#
"""
Bellow are games that are to be displayed in the menu (gui.py).
Games that users will be able to play 
"""

# -------------------------------------------------------------------#
#                       Rock Paper Scissors                          #
# -------------------------------------------------------------------#


"""
This is a game of rock paper scissors. 
When the gui opens user is faced with three tk.Buttons 1) rock 2) paper 3) scissors.
User clicks one of the Buttons to play the game. 
Computer also chooses either rock paper or scissors. 
Computers choice is compared to users choice and a winner is chosen 
Rock beats Scissors. 
Scissors beats Paper. 
Paper beats Rock. 
"""
def rock_paper_scissors(status_label=None): # function to hold the rock paper scissors game

    window = tk.Toplevel() # create a window
    window.title('Rock Paper Scissors') # give the window a title
    window.geometry('500x500')
    window.configure(bg=GAME_BG)

    # keeping track of user time spent playing
    reset_idle_timer = start_timer_manager(window)

    def play(player_choice): # sets the rules for the game
        reset_idle_timer() # start the timmer
        player_choice = player_choice.lower() # get the users choice
        choices = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(choices) # the computers choice is made by randomly choosing either rock, paper, or scissors from the choices list

        # create a dictionary to hold the rules where the keys of the dictionary are the choices rock, paper or scissors, and the values are what each key beats e.g rock beats scissors etc

        rules = {
            'rock': 'scissors',
            'paper': 'rock',
            'scissors': 'paper',
        }

        # Determine the winner of the game
        if player_choice == computer_choice: # if the player and the computer make the same choice then there is a tie.
            result = "IT'S A TIE!"
            result_color = TIE_COLOR

        # take the players choice and look it up in the rules dictionary
        elif rules[player_choice] == computer_choice:
            result = "YOU WIN!"
            result_color = WIN_COLOR

        else:
            result = "YOU LOSE!"
            result_color = LOSE_COLOR


        # Update the UI Labels (Instead of printing)
        result_label.config(text=result, fg=result_color)
        choice_label.config(text=f"Computer: {computer_choice.capitalize()}\nPlayer: {player_choice.capitalize()}") # reveal the computer choice and the players choice

        window.after(RESTART_DELAY,lambda: ask_play_again(window, lambda sl: rock_paper_scissors(sl),status_label))
    # create labels
    title_label = tk.Label(window, text='Rock Paper Scissors', font= HEADER_FONT, bg=GAME_BG, fg=PRIMARY_TEXT)
    title_label.pack(pady=20)

    result_label = tk.Label(window, text='Make your choice', font= HEADER_FONT, bg= GAME_BG, fg=PRIMARY_TEXT)
    result_label.pack(pady=20)

    choice_label = tk.Label(window, text='', font= ('Helvetica',12) , bg=GAME_BG, fg=SECONDARY_TEXT)
    choice_label.pack(pady=10)

    # 4. The tk.Button Container
    Button_frame = tk.Frame(window, bg=GAME_BG)
    Button_frame.pack(pady=30)

    # Creating tk.Buttons for rock paper and scissors so that the user can make a choice
    tk.Button(Button_frame, text='Rock', width=10, bg = BUTTON_BG, fg=PRIMARY_TEXT, command=lambda: play('Rock')).grid(row=0, column=0, padx=5)
    tk.Button(Button_frame, text='Paper', width=10, bg = BUTTON_BG, fg=PRIMARY_TEXT ,command=lambda: play('Paper')).grid(row=0, column=1, padx=5)
    tk.Button(Button_frame, text='Scissors', width=10, bg = BUTTON_BG,fg = PRIMARY_TEXT, command=lambda: play('Scissors')).grid(row=0, column=2, padx=5)

    add_standard_footer(window,status_label)
# -------------------------------------------------------------------#
#                       Number Guessing Game                         #
# -------------------------------------------------------------------#
"""
In this game the computer picks a random number between 1 and 10. 
When the gui is opened the users is prompted to guess this number in an entry box. 
The user gets 3 guesses to guess the number. 
After each guess the user is told if there guess is to high or to low. 
"""
def guess_a_number(status_label=None): # function to set up the guess a number game.
    window = tk.Toplevel() # create a window
    window.title('Guess a number') # give the window a title
    window.geometry('500x500') # set the size of the window
    window.config(bg=GAME_BG)

    target_number = random.randint(1,10) # computer picks a random number between 1 and 10
    attempts = 0

    reset_idle_timer = start_timer_manager(window)

    def check_guess(event=None):  # check the users guess and compare it to the computers number
        nonlocal attempts
        reset_idle_timer()
        player = entry.get()

        try:
            player_guess = int(player)
            attempts += 1

            if player_guess == target_number:
                result_label.config(text='Correct! You guessed the right number', fg=WIN_COLOR)
                finish_game()
            elif attempts >= 3:
                result_label.config(text=f'Out of tries! The number was {target_number}', fg=LOSE_COLOR)
                finish_game()
            elif player_guess < target_number:
                result_label.config(text='Too Low! Guess a higher number', fg=TIE_COLOR)
                entry.delete(0, END)  # Clear only if they get to try again
            else:
                result_label.config(text='Too High! Guess a lower number', fg=TIE_COLOR)
                entry.delete(0, tk.END)

        except ValueError:
            result_label.config(text='Please enter a number between 1 and 10', fg=LOSE_COLOR)
    def finish_game():
        entry.config(state=tk.DISABLED)
        btn_guess.config(state=tk.DISABLED)
        window.unbind('<Return>')
        window.after(RESTART_DELAY,lambda: ask_play_again(window, lambda sl : guess_a_number(sl),status_label))
    window.bind('<Return>', check_guess)

    tk.Label(window,text='Guess a number between 1 and 10',font=HEADER_FONT, bg = GAME_BG, fg = PRIMARY_TEXT).pack(pady=10)

    entry = (tk.Entry(window,width=20,font= HEADER_FONT,justify='center')) # entry box to receive the users guess
    entry.pack(pady=10)
    entry.focus_set()
    btn_guess =tk.Button(window,text = 'Submit number',command=check_guess,bg=BUTTON_BG,fg=PRIMARY_TEXT) # submit tk.Button to submit guess
    btn_guess.pack(pady=10)
    result_label = tk.Label(window,text = 'Good Luck', font= HEADER_FONT, bg = GAME_BG, fg=SECONDARY_TEXT)
    result_label.pack(pady=20)


    add_standard_footer(window,status_label)

# -------------------------------------------------------------------#
#                       Coin Toss Game                               #
# -------------------------------------------------------------------#

"""
In this game the computer randomly chooses between heads or tails simulating a coin toss. 
When the gui is opened the user is prompted by two tk.Buttons 1) head 2) tails.
User clicks one of the tk.Buttons and enters a guess. 
Users guess is compared to the computers choice and a winner is chosen. 
"""
def coin_toss(status_label=None):
    window = tk.Toplevel() # create a window
    window.title('Coin Toss') # give window a title
    window.geometry('500x500') # set the size of the window
    window.config(bg=GAME_BG)

    reset_idle_timer = start_timer_manager(window,timeout_ms=TIMER_TIMEOUT)

    def play(user_choice):
        reset_idle_timer()
        coin = ['heads', 'tails'] # list to hold the choices
        tossed_coin = random.choice(coin) # computer randomly picks between heads or tails simulating the toss of a coin.

        # determine winner
        if user_choice == tossed_coin:
            result_text = f'The coin landed on {tossed_coin.upper()} you win'
            result_color = WIN_COLOR
        else:
            result_text= f'The coin landed on {tossed_coin.upper()} you lose'
            result_color = LOSE_COLOR
        result_label.config(text=result_text,fg=result_color)

        window.after(RESTART_DELAY,lambda : ask_play_again(window, lambda sl: coin_toss(sl),status_label))


    tk.Label(window,text='Heads or Tails', font=HEADER_FONT,bg=GAME_BG,fg=PRIMARY_TEXT).pack(pady=20)
    result_label = tk.Label(window,text ='Chose heads or tails', font = HEADER_FONT,bg=GAME_BG,fg=SECONDARY_TEXT)
    result_label.pack(pady=30)
    Button_frame = tk.Frame(window, bg=GAME_BG)
    Button_frame.pack(pady=20)

    tk.Button(Button_frame,text='Heads',width=12, bg = BUTTON_BG,fg=PRIMARY_TEXT,command=lambda: play('heads')).grid(row=0,column=0,padx=10) # Create tk.Button for heads
    tk.Button(Button_frame,text='Tails',width=12,bg =BUTTON_BG,fg=PRIMARY_TEXT,command=lambda: play('tails')).grid(row=0,column=1,padx=10) # create tk.Button for tails
    add_standard_footer(window,status_label)

# -------------------------------------------------------------------#
#                       Quiz Game                                    #
# -------------------------------------------------------------------#
"""
This game is a multiple choice style quiz. 
when the gui is opened the first question is displayed along with 4 choices 1) A. ..... 2) B. ..... 3) C. ..... 4) D. ....
The user will then click there choice and the next question is shown.
This will then iterate over all of the questions. 
At the end of the game the users answers are compared to the correct answers and a score is given. 
"""

def quiz_game(status_label=None):
    window = tk.Toplevel() #create a window
    window.title('Quiz game')
    window.geometry('500x500')
    window.config(bg=MIDNIGHT_BLUE)
    reset_idle_timer = start_timer_manager(window,timeout_ms=TIMER_TIMEOUT)

# Create a dictionary to hold the questions
    questions = {
        '1). Who created Python?: ': 'A',
        '2). What year was python created?: ' : 'B',
        '3). Python is a tribute to which comedy group?: ': 'C',
        '4). Is the Earth round?: ' :'D'
    }

    # 2-D list to hold the choices for each questions
    options = [
        ['A. Guido van Rossum', 'B. Elon Musk', 'C. Bill Gates', 'D. Mark Zuckerburg'],
        ['A. 1989','B. 1991', 'C.2003', 'D.2025'],
        ['A. Lonely Island', 'B. Smosh','C. Monty Python', 'D. SNL'],
        ['A. True', 'B. False', 'C. Sometimes','D. Whats Earth?']
    ]

    question_keys = list(questions.keys())
    current_question_index = 0
    score = 0
    def check_answer(guess): #function to check the users answer
        nonlocal  current_question_index,score
        reset_idle_timer()
        correct_guess = questions[question_keys[current_question_index]]
        if guess == correct_guess:
            score += 1
        current_question_index += 1
        if current_question_index < len(question_keys):
            update_question()
        else:
            show_results()
    def update_question():
        question_label.config(text=question_keys[current_question_index]) #update the question text

    # update the tk.Buttons with choices from you options list
        current_choices = options[current_question_index]
        Button1.config(text=current_choices[0], command = lambda: check_answer('A'))
        Button2.config(text=current_choices[1],command=lambda:check_answer('B'))
        Button3.config(text=current_choices[2],command=lambda:check_answer('C'))
        Button4.config(text=current_choices[3],command=lambda:check_answer('D'))
    def show_results():
        # clear tk.Buttons and show final score
        final_score = int((score/ len(question_keys))*100)
        result_text = f'Quiz over you score is {final_score}%'
        color = WIN_COLOR if final_score >= 50 else LOSE_COLOR
        question_label.config(text=result_text,fg=color)
        Button_frame.pack_forget() # removes the tk.Buttons from view
        window.after(RESTART_DELAY, lambda: ask_play_again(window, lambda sl: quiz_game(sl), status_label))



    # --- UI Elements ---
    question_label = tk.Label(window, text='', font=HEADER_FONT, fg=PRIMARY_TEXT,
                           bg=GAME_BG, wraplength=450, justify="center")
    question_label.pack(pady=40)

    Button_frame = tk.Frame(window, bg=GAME_BG)
    Button_frame.pack(pady=10)

    # Styling tk.Buttons with your Usage Constants
    BUTTON_STYLE = {"width": 40, "pady": 10, "bg": BUTTON_BG, "fg": PRIMARY_TEXT, "font": ('Helvetica', 10)}

    Button1 = tk.Button(Button_frame, **BUTTON_STYLE)
    Button1.pack(pady=5)

    Button2 = tk.Button(Button_frame, **BUTTON_STYLE)
    Button2.pack(pady=5)

    Button3 = tk.Button(Button_frame, **BUTTON_STYLE)
    Button3.pack(pady=5)

    Button4 = tk.Button(Button_frame, **BUTTON_STYLE)
    Button4.pack(pady=5)

    update_question()
    add_standard_footer(window, status_label)

# -------------------------------------------------------------------#
#                       Dice Roll Game                               #
# -------------------------------------------------------------------#
"""
Game where two dice are rolled one for the computer and one for the user. 
who ever has the lowest number wins 
"""
def dice_roll(status_label=None):
    window = tk.Toplevel()
    window.title('Dice Roll')
    window.geometry('500x500')
    window.config(bg=WET_ASHPHALT)

    reset_idle_timer = start_timer_manager(window, timeout_ms=TIMER_TIMEOUT)

    def roll_dice():
        computer_roll = random.randint(1, 6)
        user_roll = random.randint(1, 6)
        reset_idle_timer()

        computer_label.config(text=f'The Computer rolled: {computer_roll}')
        user_label.config(text=f'You rolled: {user_roll}')

        # Win logic based on LOWEST number as requested
        if user_roll < computer_roll:
            result_label.config(text='YOU WIN!', fg=WIN_COLOR)
        elif computer_roll < user_roll:
            result_label.config(text='YOU LOSE!', fg=LOSE_COLOR)
        else:
            result_label.config(text="IT'S A TIE!", fg=TIE_COLOR)

        window.after(RESTART_DELAY, lambda: ask_play_again(window, lambda sl: dice_roll(sl), status_label))

    # UI Elements
    tk.Label(window, text='Dice Roll Battle', font=HEADER_FONT, bg=GAME_BG, fg=PRIMARY_TEXT).pack(pady=20)

    computer_label = tk.Label(window, text='Computer: ', font=('Helvetica', 14), bg=GAME_BG, fg=SECONDARY_TEXT)
    computer_label.pack(pady=5)

    user_label = tk.Label(window, text='You: ', font=('Helvetica', 14), bg=GAME_BG, fg=SECONDARY_TEXT)
    user_label.pack(pady=5)

    result_label = tk.Label(window, text='Press to roll', font=HEADER_FONT, bg=GAME_BG, fg=PRIMARY_TEXT)
    result_label.pack(pady=30)

    tk.Button(window, text='Roll Dice', width=15, bg=BUTTON_BG, fg=PRIMARY_TEXT, command=roll_dice).pack(pady=5)

    add_standard_footer(window,status_label)
# -------------------------------------------------------------------#
#                       Tic Tac Toe                                  #
# -------------------------------------------------------------------#
"""
This game is a game of tic tac toe 
The game is played against the computer where the computer is o and the user is x 
"""


# -------------------------------------------------------------------#
#                       Tic Tac Toe (FIXED)                          #
# -------------------------------------------------------------------#
def tic_tac_toe(status_label=None):
    window = tk.Toplevel()
    window.title('Tic Tac Toe')
    window.configure(bg=GAME_BG)

    clicked = True
    count = 0
    game_over = False
    buttons_list = []
    reset_idle_timer = start_timer_manager(window)

    def checkifwon():
        nonlocal count, game_over
        winning_combos = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]  # Diagonals
        ]
        for combo in winning_combos:
            if buttons_list[combo[0]]['text'] == buttons_list[combo[1]]['text'] == buttons_list[combo[2]][
                'text'] != ' ':
                for index in combo:
                    buttons_list[index].config(bg=ALIZARIN_RED)
                game_over = True
                messagebox.showinfo('Tic Tac Toe', f"{buttons_list[combo[0]]['text']} wins!")
                window.after(RESTART_DELAY, lambda: ask_play_again(window, tic_tac_toe, status_label))
                return True

        if count == 9:
            game_over = True
            messagebox.showinfo('Tic Tac Toe', 'The game ends in a tie')
            window.after(RESTART_DELAY, lambda: ask_play_again(window, tic_tac_toe, status_label))
            return True
        return False

    def computer_move():
        nonlocal clicked, count
        if game_over: return
        empty_buttons = [b for b in buttons_list if b['text'] == ' ']
        if empty_buttons:
            choice = random.choice(empty_buttons)
            choice.config(text='O', fg=SECONDARY_TEXT)
            count += 1
            clicked = True
            checkifwon()

    def b_click(b):
        nonlocal clicked, count
        reset_idle_timer()
        if b['text'] == ' ' and clicked and not game_over:
            b.config(text='X', fg=WIN_COLOR)
            clicked = False
            count += 1
            if not checkifwon():
                window.after(600, computer_move)

    frame = tk.Frame(window, bg=GAME_BG)
    frame.pack(pady=20, padx=20)

    for i in range(9):
        # FIXED: Removed 'tk.' from Button_BG
        btn = tk.Button(frame, text=' ', font=HEADER_FONT, height=3, width=6, bg=BUTTON_BG, fg=PRIMARY_TEXT)
        btn.config(command=lambda b=btn: b_click(b))
        btn.grid(row=i // 3, column=i % 2 if i == 0 else i % 3)  # Simple grid logic
        btn.grid(row=i // 3, column=i % 3, padx=2, pady=2)
        buttons_list.append(btn)

    add_standard_footer(window, status_label)


# -------------------------------------------------------------------#
#                          Snake Game (FIXED)                        #
# -------------------------------------------------------------------#
def snake_game(status_label=None):
    ROWS, COLS, TILE_SIZE = 25, 25, 25
    WINDOW_WIDTH, WINDOW_HEIGHT = TILE_SIZE * ROWS, TILE_SIZE * COLS

    window = tk.Toplevel()
    window.title('Snake Game')
    window.resizable(False, False)

    canvas = tk.Canvas(window, bg='black', width=WINDOW_WIDTH, height=WINDOW_HEIGHT, highlightthickness=0)
    canvas.pack()

    snake = Tile(5 * TILE_SIZE, 5 * TILE_SIZE)
    food = Tile(10 * TILE_SIZE, 10 * TILE_SIZE)
    snake_body, velocity_x, velocity_y = [], 0, 0
    game_over, score = False, 0

    def change_direction(e):
        nonlocal velocity_x, velocity_y
        if game_over: return
        # FIXED: Velocity must move by TILE_SIZE to stay on the grid
        if e.keysym == 'Up' and velocity_y != TILE_SIZE:
            velocity_x, velocity_y = 0, -TILE_SIZE
        elif e.keysym == 'Down' and velocity_y != -TILE_SIZE:
            velocity_x, velocity_y = 0, TILE_SIZE
        elif e.keysym == 'Left' and velocity_x != TILE_SIZE:
            velocity_x, velocity_y = -TILE_SIZE, 0
        elif e.keysym == 'Right' and velocity_x != -TILE_SIZE:
            velocity_x, velocity_y = TILE_SIZE, 0

    def move():
        nonlocal game_over, score
        if game_over or (velocity_x == 0 and velocity_y == 0): return

        # Collision with food
        if snake.x == food.x and snake.y == food.y:
            snake_body.append(Tile(food.x, food.y))
            score += 1
            food.x = random.randint(0, COLS - 1) * TILE_SIZE
            food.y = random.randint(0, ROWS - 1) * TILE_SIZE

        # Move body
        for i in range(len(snake_body) - 1, 0, -1):
            snake_body[i].x, snake_body[i].y = snake_body[i - 1].x, snake_body[i - 1].y
        if snake_body:
            snake_body[0].x, snake_body[0].y = snake.x, snake.y

        snake.x += velocity_x
        snake.y += velocity_y

        # Death conditions
        if (snake.x < 0 or snake.x >= WINDOW_WIDTH or snake.y < 0 or snake.y >= WINDOW_HEIGHT or
                any(t.x == snake.x and t.y == snake.y for t in snake_body)):
            game_over = True

    def draw():
        if game_over:
            canvas.create_text(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, text=f"GAME OVER\nScore: {score}", fill="white",
                               font=HEADER_FONT, justify=tk.CENTER)
            window.after(RESTART_DELAY, lambda: ask_play_again(window, snake_game, status_label))
            return

        move()
        canvas.delete("all")
        canvas.create_rectangle(food.x, food.y, food.x + TILE_SIZE, food.y + TILE_SIZE, fill=LOSE_COLOR)
        canvas.create_rectangle(snake.x, snake.y, snake.x + TILE_SIZE, snake.y + TILE_SIZE, fill=WIN_COLOR)
        for tile in snake_body:
            canvas.create_rectangle(tile.x, tile.y, tile.x + TILE_SIZE, tile.y + TILE_SIZE, fill=EMERALD_GREEN)

        window.after(100, draw)

    window.bind('<KeyPress>', change_direction)
    draw()
    add_standard_footer(window, status_label)
