# Sudoku

## Overview
A **simple, self‑contained Sudoku solver** in pure Python.  
Feed it a 9 × 9 grid (use `0` for blanks) and it fills in the solution with classic back‑tracking search.

```
solver.py   # main script containing the solver logic
```

---

## Getting Started

1. Download or copy **`solver.py`**.
2. Make sure you have **Python 3.8+** (standard library only).

```bash
python solver.py     # runs the demo puzzle embedded in the file
```

To solve your own puzzle, replace the `puzzle` variable in the `__main__` block or import the function as a library.

---

## Using as a Library

```python
from solver import solve

grid = [
    [0, 7, 0, 0, 5, 0, 0, 3, 0],
    [1, 0, 0, 6, 0, 0, 0, 0, 8],
    ...
]

if solve(grid):
    for row in grid:
        print(row)
else:
    print("No solution found.")
```

`solve(board)` **mutates** the board in place and returns **`True`** if it succeeds.

---

## How the Algorithm Works

1. **Find the next empty square** (`find_empty`).
2. **Try digits 1‑9**:
   * `valid` checks row, column, and 3 × 3 box constraints.
3. **Recurse** (`solve`) with the candidate placed.
4. If recursion fails, **backtrack** (reset to 0) and try the next digit.
5. When no empty cell remains, the puzzle is solved.

### Complexity
Worst‑case time is **O(9^n)** for *n* empty cells, but practical puzzles solve in milliseconds thanks to pruning.

---

## Extending & Improving

* **Heuristics** – choose the square with the fewest legal moves first.
* **Constraint propagation** – apply human techniques (naked singles, hidden pairs) before recursion.
* **UI** – wrap with `argparse`, build a Tkinter GUI, or put behind a web‑app.
