from typing import List

board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]

def flood_fill(input_board: List[str], old: str, new: str, x: int, y: int) -> List[str]:
    if x < 0 or x >= len(input_board) or y < 0 or y >= len(input_board[0]) or input_board[x][y] != old:
        # Base case: out of bounds or value is not the old value, stop.
        return input_board

    # Replace the old value with the new value at the current position.
    input_board[x] = input_board[x][:y] + new + input_board[x][y + 1:]

    # Recursive calls for neighboring cells (up, down, left, right).
    flood_fill(input_board, old, new, x + 1, y)
    flood_fill(input_board, old, new, x - 1, y)
    flood_fill(input_board, old, new, x, y + 1)
    flood_fill(input_board, old, new, x, y - 1)

    return input_board

modified_board = flood_fill(input_board=board, old=".", new="-", x=5, y=12)

for a in modified_board:
    print(a)

from typing import List

#Updated by Xinran
board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]

def flood_fill(input_board: List[str], old: str, new: str, x: int, y: int) -> List[str]:
    if x < 0 or x >= len(input_board) or y < 0 or y >= len(input_board[0]) or input_board[x][y] != old:
        # Base case: out of bounds or value is not the old value, stop.
        return input_board

    # Convert the row to a list so that you can modify it.
    row = list(input_board[x])
    # Replace the old value with the new value at the current position.
    row[y] = new
    input_board[x] = ''.join(row)

    # Recursive calls for neighboring cells (up, down, left, right).
    flood_fill(input_board, old, new, x + 1, y)
    flood_fill(input_board, old, new, x - 1, y)
    flood_fill(input_board, old, new, x, y + 1)
    flood_fill(input_board, old, new, x, y - 1)

    return input_board

modified_board = flood_fill(input_board=board, old=".", new="-", x=5, y=12)

for a in modified_board:
    print(a)
