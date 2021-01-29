from tictactoe.board import *
from tictactoe.engine import *
from tictactoe.engine import *
from tictactoe.player import *
from tictactoe.computer import *

if __name__ == "__main__":
    # Setup a new game
    print("Welcome to a game of tic-tac-toe.")
    b = Board()

    # Select players
    players = get_players()

    #Play game
    play_game(b, players)

# Sometimes my unit tests pass, but my game fails. How can I rectify this?
