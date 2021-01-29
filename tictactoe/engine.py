from tictactoe.board import *
from tictactoe.computer import *

import random

# How do I organize functions on such pages? Highest level first? In order that they are referenced?

def get_players():
    players = []
    player_attributes = [("1", "X"), ("2", "O")]
    for number, symbol in player_attributes:
        players.append(get_player_type(number, symbol))
    return (players)


def get_player_type(number, symbol):
    player_type = input(f"Enter player {number} type - 'h' or 'c'")
    if player_type.lower() in ('h', 'c'):
        if player_type == 'h':
            return Player(f"Player {number}", "human", symbol)
        elif player_type == 'c':
            return Computer(f"Computer {number}", "computer", symbol, "Easy")
        else:
            print("Invalid input")
            get_player_type(number, symbol)


def play_game(board, players):
    player = choose_first_mover(players)
    while True:
        get_player_move(player, board, players)
        result = board.check_result(player)
        if result == "win":
            declare_result(player)
            break
        elif result == "none":
            declare_result("none")
            break
        else:
            player = toggle_player(player, players)


def choose_first_mover(players):
    first_mover = random.choice(players)
    print(f"{first_mover.name} gets to play the first move.")
    return first_mover


def get_player_move(player, board, players): # Should I write unit tests for this function?
    rival = toggle_player(player, players)
    if player.type == "human":
        player.get_move(board)
    elif player.type == "computer":
        player.get_move(board, rival) # The only difference is the additional argument. How can I refector this?
    board.print_board()


def toggle_player(current_player,players):
    if current_player in players:
        for player in players:
            if current_player != player:
                return player
    else:
        raise MoveError("Current player not part of players")


def declare_result(winner):
    if winner == "none":
        print("Game over. Game drawn.")
    else:
        print(f"Game over. {winner.name} wins!")
