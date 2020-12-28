from tictactoe.board import MoveError
from tictactoe.computer import find_win, make_random_move

import random

# How do I organize functions on such pages?

def get_player_move(player, board):
    if player == "human": # This function does too much. How can I refactor?
        move = input("Enter your move > ") # In which module do I put this function?
        try:
            board.mark_human_move(move)
        except(MoveError):
            print("Invalid move. Try again.")
            get_player_move(player, board)  # Recursion
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


def toggle_player(player):
    if player == "human":
        return "computer"
    elif player == "computer":
        return "human"
    else:
        raise MoveError("Player must be human or computer")


def choose_first_mover():
    first_mover = random.choice(["human", "computer"])
    if first_mover == "human":
        print("You get to play the first move.")
    elif first_mover == "computer":
        print("Computer goes first.")
    else:
        raise MoveError("First mover must be human or computer")
    return first_mover

def declare_result(winner):  
    if winner == "computer": # Should I have included  this as a method inside Board?
        print("Game over. Computer wins!")
        exit(0)
    elif winner == "human":
        print("Game over. You win!")
        exit(0)
    elif winner == "draw":
        print("Game over. Game drawn.")
        exit(0)
    else:
        MoveError("Invalid argument. Must be 'human', 'computer or 'draw")
