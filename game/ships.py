import random
from game.constants import FLEET, WATER, SHIP, BOARD_SIZE

def _ship_cells(start: tuple[int, int], length: int, horizontal: bool) -> list[tuple[int, int]]:
    row, col = start
    if horizontal:
        return [(row, col + i) for i in range(length)]
    else: return [(row + i, col) for i in range(length)]

def _can_place(board: list[list[str]], cells: list[tuple[int, int]]) -> bool:
    for row, col in cells:
        if not (0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE):
            return False
        if board[row][col] != WATER:
            return  False
        r = (-1, 0, 1)
        for delta_row in r:
            for delta_col in r:
                nr = row + delta_row
                nc = col + delta_col
                if not (0 <= nr < BOARD_SIZE and 0 <= nc < BOARD_SIZE):
                    continue
                if board[nr][nc] != WATER:
                    return False
    return True

def random_place_fleet(board: list[list[str]]) -> None:
    while True:
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                board[row][col] = WATER
        ok = True
        for ship_length in FLEET:
            placed = False
            for _ in range(300):
                horizontal = random.choice([True, False])
                start_cell = (random.randint(0, BOARD_SIZE - 1), random.randint(0, BOARD_SIZE - 1))
                cells = _ship_cells(start_cell, ship_length, horizontal)
                if _can_place(board, cells):
                    for row, col in cells:
                        board[row][col] = SHIP
                    placed = True
                    break
            if not placed:
                ok = False
                break
        if ok:
            break