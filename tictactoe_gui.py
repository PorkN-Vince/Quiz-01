# tictactoe_gui.py

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic Tac Toe - GUI Version")

board = [' ' for _ in range(9)]
current_player = 'X'


def check_winner(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False


def check_draw():
    return ' ' not in board


def button_click(index):
    global current_player

    if board[index] == ' ':
        board[index] = current_player
        buttons[index].config(text=current_player)

        if check_winner(current_player):
            messagebox.showinfo("Game Over", f"Player {current_player} wins!")
            reset_game()
        elif check_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_game()
        else:
            current_player = 'O' if current_player == 'X' else 'X'


def reset_game():
    global board, current_player
    board = [' ' for _ in range(9)]
    current_player = 'X'
    for button in buttons:
        button.config(text='')


buttons = []

for i in range(9):
    button = tk.Button(root, text=' ', font=('Arial', 24),
                       width=5, height=2,
                       command=lambda i=i: button_click(i))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

root.mainloop()
