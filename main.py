def utility(board):
    # Count the number of Black Coins on the board.
    return board.count('B')

def is_terminal_state(board):
    # Check if there are no Empty Blocks on the board.
    return '0' not in board

def convert_coins(board):
    # Convert consecutive Black Coins to white coins and vice versa.
    new_board = list(board)

    for i in range(len(new_board)):
        if new_board[i] == 'B':
            new_board[i] = 'W'
        elif new_board[i] == 'W':
            new_board[i] = 'B'

    return ''.join(new_board)

def min_value(board):
    if is_terminal_state(board):
        return utility(board)

    v = float('inf')
    empty_blocks = [i for i, block in enumerate(board) if block == '0']

    for block in empty_blocks:
        new_board = board[:block] + 'W' + board[block+1:]
        new_board = convert_coins(new_board)
        v = min(v, max_value(new_board))
    return v

def max_value(board):
    if is_terminal_state(board):
        return utility(board)

    v = float('-inf')
    empty_blocks = [i for i, block in enumerate(board) if block == '0']

    for block in empty_blocks:
        new_board = board[:block] + 'B' + board[block+1:]
        new_board = convert_coins(new_board)
        v = max(v, min_value(new_board))
    return v

def mini_max(board):
    return max_value(board)

input_board = input("Enter the Board State : ")
result = mini_max(input_board)
print("Utility of Player 1 (Player MAX):", result)