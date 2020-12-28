from tictactoe.board import *
from tictactoe.computer import *
from tictactoe.engine import *


if __name__ == "__main__":  # Main function that starts and runs the game
    b = Board()
    print("Welcome to a game of tic-tac-toe.")
    player = choose_first_mover()
    while True:
        get_player_move(player, b)
        result = b.check_result(player)
        if result == "win":
            declare_result(player)
        elif result == "draw":
            declare_result("draw")
        else:
            player = toggle_player(player)
