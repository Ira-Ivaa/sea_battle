import os
from game.board import create_board, render_board, has_ships_left
from game.shots import ask_shot, apply_shot
from game.ships import random_place_fleet

def clear_screen() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

def header(current_player: int) -> None:
    print(f'''========================
       Player's turn {current_player}
========================''')

def switch_player(current: int) -> int:
    return 2 if current == 1 else 1

def select_boards(board1: list[list[str]], board2: list[list[str]], current: int):
    return board1 if current == 1 else board2, board2 if current == 1 else board1

def render_turn(my_board: list[list[str]], enemy_board: list[list[str]]) -> None:
    render_board(my_board, True)
    print('')
    render_board(enemy_board, False)

def check_win(enemy_board: list[list[str]], player: int) -> bool:
    if has_ships_left(enemy_board):
        return False
    else:
        clear_screen()
        print('Player 1(2) win!')
        return True

def pause(message: str = "Press Enter to continue...") -> None:
    input(message)

def play_game() -> None:
    board1 = create_board()
    board2 = create_board()

    random_place_fleet(board1)
    random_place_fleet(board2)

    current = 1
    while True:
        clear_screen()
        my_board, enemy_board = select_boards(board1, board2, current)
        header(current)
        render_turn(my_board, enemy_board)
        shot = ask_shot()
        result = apply_shot(enemy_board, shot)
        match result:
            case 'repeat':
                print("\\n⚠ You’ve already shot at this cell")
                pause()
            case 'miss':
                print("\\n❌ Miss")
                pause()
                current = switch_player(current)
            case 'hit':
                print("\\n🎯 Hit!")
                if check_win(enemy_board, current):
                    break
                pause()