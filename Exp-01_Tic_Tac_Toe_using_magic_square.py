import random

def print_board(board):
    print("-------------")
    for i in range(3):
        print("|", end="")
        for j in range(3):
            print(" {} |".format(board[i*3+j]), end="")
        print("\n-------------")

def get_human_move(board):
    while True:
        move = input("Enter your move (1-9): ")
        if move.isdigit() and int(move) in range(1, 10) and board[int(move)-1] == " ":
            return int(move) - 1
        print("Invalid move. Please try again.")

def get_ai_move(board):
    magic_square = [8, 1, 6, 3, 5, 7, 4, 9, 2]
    corners = [0, 2, 6, 8]
    empty_cells = [i for i in range(9) if board[i] == " "]
    if len(empty_cells) == 9:
        return random.choice(corners)
    for cell in empty_cells:
        temp_board = board.copy()
        temp_board[cell] = "O"
        if check_win(temp_board) == "O":
            return cell
    for cell in empty_cells:
        temp_board = board.copy()
        temp_board[cell] = "X"
        if check_win(temp_board) == "X":
            return cell
    for cell in magic_square:
        if cell in empty_cells:
            return cell
    return random.choice(empty_cells)

def check_win(board):
    magic_square = [8, 1, 6, 3, 5, 7, 4, 9, 2]
    for i in range(0, 9, 3):
        if board[i:i+3] == ["X", "X", "X"]:
            return "X"
        elif board[i:i+3] == ["O", "O", "O"]:
            return "O"
    for i in range(3):
        if board[i::3] == ["X", "X", "X"]:
            return "X"
        elif board[i::3] == ["O", "O", "O"]:
            return "O"
    if board[0:9:4] == ["X", "X", "X"] or board[2:7:2] == ["X", "X", "X"]:
        return "X"
    elif board[0:9:4] == ["O", "O", "O"] or board[2:7:2] == ["O", "O", "O"]:
        return "O"
    if " " not in board:
        return None
    return False

def play():
    board = [" "] * 9
    print_board(board)
    while True:
        human_move = get_human_move(board)
        board[human_move] = "X"
        print_board(board)
        winner = check_win(board)
        if winner:
            print("You win!" if winner == "X" else "You lose!")
            break
        elif winner is None:
            print("It's a tie.")
            break
        ai_move = get_ai_move(board)
        board[ai_move] = "O"
        print("AI chooses cell", ai_move+1)
        print_board(board)
        winner = check_win(board)
        if winner:
            print("You win!" if winner == "X" else "You lose!")
            break

play()
