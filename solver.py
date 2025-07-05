from typing import List, Tuple, Optional

Board = List[List[int]]  # 9×9 board

def find_empty(board: Board) -> Optional[Tuple[int, int]]:
    """Return the row, col of the first empty (0) cell, or None if full."""
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return r, c
    return None

def valid(board: Board, num: int, pos: Tuple[int, int]) -> bool:
    """Check if placing num at pos (row, col) keeps the board valid."""
    r, c = pos
    
    # Row
    if any(board[r][x] == num for x in range(9) if x != c):
        return False
    
    # Column
    if any(board[x][c] == num for x in range(9) if x != r):
        return False
    
    # 3×3 box
    box_r, box_c = 3 * (r // 3), 3 * (c // 3)
    for i in range(box_r, box_r + 3):
        for j in range(box_c, box_c + 3):
            if (i, j) != pos and board[i][j] == num:
                return False
    
    return True

def solve(board: Board) -> bool:
    """
    Mutates the board in-place to a solved state.
    Returns True if solvable, False otherwise.
    """
    empty = find_empty(board)
    if not empty:          # solved
        return True
    r, c = empty
    
    for num in range(1, 10):
        if valid(board, num, (r, c)):
            board[r][c] = num
            if solve(board):
                return True
            board[r][c] = 0  # backtrack
    return False

# ---------------- Demo ----------------
if __name__ == "__main__":
    puzzle = [
        [0, 0, 0, 2, 6, 0, 7, 0, 1],
        [6, 8, 0, 0, 7, 0, 0, 9, 0],
        [1, 9, 0, 0, 0, 4, 5, 0, 0],
        [8, 2, 0, 1, 0, 0, 0, 4, 0],
        [0, 0, 4, 6, 0, 2, 9, 0, 0],
        [0, 5, 0, 0, 0, 3, 0, 2, 8],
        [0, 0, 9, 3, 0, 0, 0, 7, 4],
        [0, 4, 0, 0, 5, 0, 0, 3, 6],
        [7, 0, 3, 0, 1, 8, 0, 0, 0],
    ]

    if solve(puzzle):
        for row in puzzle:
            print(row)
    else:
        print("No solution exists.")
