# Create board positions
board = {
    'a1': ' ', 'a2': ' ', 'a3': ' ',
    'b1': ' ', 'b2': ' ', 'b3': ' ',
    'c1': ' ', 'c2': ' ', 'c3': ' '
}

game_end = False
current_player = 'X'


def print_board():
    print(f"""
a |{board['a1']}|{board['a2']}|{board['a3']}|
b |{board['b1']}|{board['b2']}|{board['b3']}|
c |{board['c1']}|{board['c2']}|{board['c3']}|
   1 2 3
""")


def check_winner(player):
    win_combinations = [
        ['a1', 'a2', 'a3'],
        ['b1', 'b2', 'b3'],
        ['c1', 'c2', 'c3'],
        ['a1', 'b1', 'c1'],
        ['a2', 'b2', 'c2'],
        ['a3', 'b3', 'c3'],
        ['a1', 'b2', 'c3'],
        ['a3', 'b2', 'c1']
    ]

    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False


def check_draw():
    for key in board:
        if board[key] == ' ':
            return False
    return True


# Game Start
print_board()

while not game_end:
    move = input(f"{current_player} turn. Enter position (e.g. a1): ").lower()

    if move not in board:
        print("Invalid position! Try again.")
        continue

    if board[move] != ' ':
        print("Position already taken! Try again.")
        continue

    board[move] = current_player
    print_board()

    if check_winner(current_player):
        print(f"🎉 Player {current_player} wins!")
        game_end = True
    elif check_draw():
        print("It's a draw!")
        game_end = True
    else:
        current_player = 'O' if current_player == 'X' else 'X'
