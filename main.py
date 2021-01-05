from tictactoe.board import Board
from tictactoe.engine import get_player_move, choose_first_mover
from tictactoe.engine import declare_result, toggle_player

# Have kept all imports minimal and clean for traceability

if __name__ == "__main__":
    b = Board() # Create a new game and start it
    print("Welcome to a game of tic-tac-toe.")
    player = choose_first_mover()
    while True: # Looks like an infinite loop
        get_player_move(player, b)  # How can I indicate where to find this? Imports?
        result = b.check_result(player)
        if result == "win":
            declare_result(player)
        elif result == "draw":
            declare_result("draw")
        else:
            player = toggle_player(player)

        # New game
        # Game.start
        # If game continues:
            #pass
        #Else:
            #exit

        # The game itself and the way it is run are mixed at this level
