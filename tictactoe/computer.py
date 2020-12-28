from tictactoe.board import *
import random

class Computer:
    pass

def find_winning_position(sequence, board): # Find winning position in near win sequence
    for position in sequence:
        if board.status[position] == ' ':
            return position
        else:
            pass


def find_win(board, player):   # Finds winning position in near win board status
    marker = assign_marker(player)
    result = None
    for sequence in board.sequences:
        sequence_string = board.get_sequence_string(sequence)
        if sequence_string.replace(' ', '') == 2 * marker:      # Find sequence with 2 markers
            result = find_winning_position(sequence, board)
        else:
            pass
    if result == None:
        raise MoveError('Sequence has no near win')
    else:
        return result


def get_empty_positions(board): # get all empty positions from board
    result = []
    for k, v in board.status.items():
        if v == ' ':
            result.append(k)
        else:
            pass
    return result

def make_random_move(board): # makes random move in empty positions
    empty_cells = board.get_empty_positions()
    move = random.choice(empty_cells)
    board.mark_move(move, "computer")
