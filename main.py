from tictactoe.board import *
from tictactoe.computer import *
import random
                        # How do I organize functions on such pages?


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


def get_player_move(player, board): # gets and makes player move from both computer and human player
    if player == "human": # This function does too much. How can I refactor?
        move = input("Enter your move > ") # In which module do I put this function?
        try:
            board.mark_human_move(move)
        except(MoveError):
            print("Invalid move. Try again.")
            get_player_move(player, board)
    elif player == "computer":
        if board.check_result(player) == "near win":
            next_move = find_win(board, player)
            board.mark_move(next_move, player)
        elif board.check_result("human") == "near win":
            next_move = find_win(board, "human")
            board.mark_move(next_move, player)
        else:
            make_random_move(board)
    board.print_board()


def toggle_player(player):  # toggles between human and computer player
    if player == "human":
        return "computer"
    elif player == "computer":
        return "human"
    else:
        raise MoveError("Player must be human or computer")


def choose_first_mover():   # chooses whether human or comp goes first
    first_mover = random.choice(["human", "computer"])
    if first_mover == "human":
        print("You get to play the first move.")
    elif first_mover == "computer":
        print("Computer goes first.")
    else:
        raise MoveError("First mover must be human or computer")
    return first_mover
