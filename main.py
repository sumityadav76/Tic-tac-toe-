# Task 2: Tic-Tac-Toe AI using Minimax
import math

def print_board(board):
    for row in board:
        print("|".join(row))
    print()

def check_winner(board):
    for row in board:
        if row.count(row[0]) == 3 and row[0] != " ":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == "O":
        return 1
    elif winner == "X":
        return -1
    elif is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Tic-Tac-Toe AI Game 🕹️ (You = X, AI = O)")
    print_board(board)

    while True:
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter col (0-2): "))

        if board[row][col] == " ":
            board[row][col] = "X"
        else:
            print("Cell already taken, try again!")
            continue

        if check_winner(board):
            print_board(board)
            print("🎉 You Win!")
            break
        if is_full(board):
            print_board(board)
            print("😐 It's a Draw!")
            break

        ai_move = best_move(board)
        board[ai_move[0]][ai_move[1]] = "O"

        print_board(board)

        if check_winner(board):
            print("💻 AI Wins!")
            break
        if is_full(board):
            print("😐 It's a Draw!")
            break

if __name__ == "__main__":
    play_game()