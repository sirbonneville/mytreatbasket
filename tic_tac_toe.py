# going to try out cursor's generative AI technology by following the suggestions and asking for a command line interface based tictactoe program


# Tic Tac Toe Game

# Instructions:
# - The game is played on a 3x3 grid.
# - Each player takes turns marking a square with their symbol (X or O).
# - The first player to get 3 of their symbols in a row (horizontally, vertically, or diagonally) wins.
# - If all squares are filled and no player has won, the game is a tie.

# Pseudocode:
# 1. Create a 3x3 grid to represent the game board.
# 2. Create a variable to keep track of the current player (X or O).
# 3. Create a variable to keep track of the game status (ongoing, won, or tie).
# 4. Display the initial game board.
# 5. Repeat until the game is over:
#    6. Ask the current player for their move.
#    7. Validate the move and update the game board.
#    8. Check if the current player has won.
#    9. If the current player has won, set the game status to "won" and end the game.
#    10. If all squares are filled and no player has won, set the game status to "tie" and end the game.
#    11. Switch the current player to the other player.
# 12. Display the final game board and the game result.

# Tic Tac Toe Game

# Create a 3x3 grid to represent the game board
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

# Create a variable to keep track of the current player (X or O)
current_player = 'X'

# Create a variable to keep track of the game status (ongoing, won, or tie)
game_status = 'ongoing'

# Function to display the game board
def display_board():
    print('---------')
    for row in board:
        print('|', end='')
        for cell in row:
            print(cell, end='|')
        print('\n---------')

# Function to ask the current player for their move
def get_move():
    while True:
        row = int(input('Enter the row (0-2): '))
        col = int(input('Enter the column (0-2): '))
        if 0 <= row <= 2 and 0 <= col <= 2:
            return row, col
        else:
            print('Invalid move. Try again.')

# Function to validate the move and update the game board
def make_move(row, col):
    if board[row][col] == ' ':
        board[row][col] = current_player
        return True
    else:
        return False

# Function to check if the current player has won
def check_win():
    for row in board:
        if row[0] == row[1] == row[2] == current_player:
            return True
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == current_player:
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == current_player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == current_player:
        return True
    return False

# Function to check if the game is a tie
def check_tie():
    for row in board:
        if ' ' in row:
            return False
    return True

# Function to make the AI move
def make_ai_move():
    best_score = float('-inf')
    best_move = None

    # Iterate over all possible moves
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                # Make the move
                board[row][col] = 'O'
                score = minimax(board, 0, False)
                # Undo the move
                board[row][col] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (row, col)

    # Make the best move
    row, col = best_move
    board[row][col] = 'O'

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    if check_win():
        if current_player == 'O':
            return 1
        elif current_player == 'X':
            return -1
    elif check_tie():
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[row][col] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[row][col] = ' '
                    best_score = min(score, best_score)
        return best_score

# Main game loop
while game_status == 'ongoing':
    display_board()
    if current_player == 'X':
        move = get_move()
        if make_move(move[0], move[1]):
            if check_win():
                game_status = 'won'
            elif check_tie():
                game_status = 'tie'
            else:
                current_player = 'O'
        else:
            print('Invalid move. Try again.')
    else:
        make_ai_move()
        if check_win():
            game_status = 'won'
        elif check_tie():
            game_status = 'tie'
        else:
            current_player = 'X'

# Display the final game board and the game result
display_board()
if game_status == 'won':
    print(f'Player {current_player} wins!')
elif game_status == 'tie':
    print('It\'s a tie!')