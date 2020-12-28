from tictactoe.board import MoveError, assign_marker
import random

# Should I have a class for Computer?

def find_win(board, player):
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


def make_random_move(board):
    empty_cells = board.get_empty_positions()
    move = random.choice(empty_cells)
    board.mark_move(move, "computer")


def find_winning_position(sequence, board):
    for position in sequence:
        if board.status[position] == ' ':
            return position
        else:
            pass
