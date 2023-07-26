import random

# Tic-Tac-Toe Board
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

# Possible winning combinations
winning_combinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
    [0, 4, 8], [2, 4, 6]              # Diagonals
]

# AI and player symbols
ai_symbol = 'X'
player_symbol = 'O'


def display_board():
    """Display the tic-tac-toe board."""
    print('-------------')
    print('|', board[0], '|', board[1], '|', board[2], '|')
    print('-------------')
    print('|', board[3], '|', board[4], '|', board[5], '|')
    print('-------------')
    print('|', board[6], '|', board[7], '|', board[8], '|')
    print('-------------')


def is_board_full():
    """Check if the board is full."""
    return ' ' not in board


def is_winner(symbol):
    """Check if the specified symbol is a winner."""
    for combination in winning_combinations:
        if all(board[i] == symbol for i in combination):
            return True
    return False


def evaluate_board():
    """Evaluate the current state of the board for the AI player."""
    if is_winner(ai_symbol):
        return 1  # AI wins
    elif is_winner(player_symbol):
        return -1  # Player wins
    else:
        return 0  # Draw


def minimax(board, depth, is_maximizing_player):
    """Apply the minimax algorithm to find the best move."""
    if is_winner(ai_symbol):
        return 1
    elif is_winner(player_symbol):
        return -1
    elif is_board_full():
        return 0

    if is_maximizing_player:
        best_score = float('-inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = ai_symbol
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = player_symbol
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score


def get_best_move():
    """Find the best move for the AI player."""
    best_score = float('-inf')
    best_move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = ai_symbol
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    return best_move


def play_game():
    """Play the tic-tac-toegame between the AI and the player."""
    display_board()
    print("Welcome to Tic-Tac-Toe!")
    print("You are playing as 'O'. Make your move by entering a number from 0 to 8.")

    while not is_board_full():
        player_move = int(input("Your move: "))
        if board[player_move] == ' ':
            board[player_move] = player_symbol
            display_board()

            if is_winner(player_symbol):
                print("You win!")
                return

            if is_board_full():
                print("It's a draw!")
                return

            ai_move = get_best_move()
            board[ai_move] = ai_symbol
            print("AI's move:", ai_move)
            display_board()

            if is_winner(ai_symbol):
                print("AI wins!")
                return
        else:
            print("Invalid move. Try again.")

    print("It's a draw!")

# Start the game
play_game()
