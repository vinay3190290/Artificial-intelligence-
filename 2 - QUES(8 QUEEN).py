def solve(n):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
                return False
        return True

    def place_queens(n, row, board):
        if row == n:
            result.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                place_queens(n, row + 1, board)

    result = []
    place_queens(n, 0, [-1]*n)
    return result

def print_board(board):
    n = len(board)
    for col in board:
        row = ['Q' if i == col else '.' for i in range(n)]
        print(' '.join(row))

n = 8
solutions = solve(n)
print(f"Found {len(solutions)} solutions:")
for i, solution in enumerate(solutions):
    print(f"Solution {i+1}:")
    print_board(solution)
    print()