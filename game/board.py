from game.constants import WATER, SHIP, BOARD_SIZE

def create_board() -> list[list[str]]:
    board = []
    for i in range(BOARD_SIZE):
        row = [WATER] * BOARD_SIZE
        board.append(row)
    return board

def render_board(board: list[list[str]], show_ships: bool = True) -> None:
    print('     A B C D E F G H I J')

    for i in range (BOARD_SIZE):
        row = f'{i + 1:2} |'
        for j in range(BOARD_SIZE):
            if(show_ships == False and board[i][j] == SHIP):
                row += ' ' + WATER
            else: row += ' ' + board[i][j]
        print(row)

def has_ships_left(board: list[list[str]]) -> bool:
    for row in board:
        if SHIP in row:
            return True
    return False