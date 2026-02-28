from game.constants import WATER, MISS, SHIP, HIT

def parse_shot(text: str) -> tuple[int, int] | None:
    if text == '': return None
    letter = ord(text[0].lower()) - 97
    num = int(text[1:]) - 1
    if letter >= 10 or num >= 10:
        return None
    return num, letter

def ask_shot() -> tuple[int, int] | None:
    while True:
        text = input('Enter correct coordinates A-B 1-10 example(A5)')
        shot = parse_shot(text)
        if shot is not None: return shot
        print('No shots available. Enter correct coordinates A-B 1-10 example(A5)')

def apply_shot(board: list[list[str]], shot: tuple[int, int]) -> str:
    row, col = shot
    cell = board[row][col]
    if  cell == WATER:
        board[row][col] = MISS
        return 'miss'
    elif cell == SHIP:
        board[row][col] = HIT
        return 'hit'
    else: return 'repeat'