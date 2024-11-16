N = 8  # Size of the chessboard (8x8)

def print_solution(board):
    for row in board:
        line = ""
        for cell in row:
            line += "Q " if cell else ". "
        print(line)
    print()

def is_safe(board, row, col):
    # Check the column
    for i in range(row):
        if board[i][col]:
            return False

    # Check the upper left diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i][j]:
            return False

    # Check the upper right diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, N)):
        if board[i][j]:
            return False

    return True

def solve_n_queens(board, row):
    if row >= N:
        print_solution(board)
        return True

    res = False
    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = True
            res = solve_n_queens(board, row + 1) or res
            board[row][col] = False  # Backtrack

    return res

def eight_queens():
    board = [[False] * N for _ in range(N)]
    if not solve_n_queens(board, 0):
        print("No solution exists.")
    else:
        print("Solutions printed above.")

# Run the 8-queen problem
eight_queens()
