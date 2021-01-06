from tictactoe.board import MoveError, assign_marker
import random
import numpy

# Should I have a class for Computer?

def find_win(board, player):
    result = find_win_row_column(board.matrix, player)

    if result != None:
        return result

    result = find_win_diagonal(board.matrix, player)

    if result != None:
        return result
    else:
        raise MoveError("Winning position unavailable.")


def make_random_move(board):
    empty_cells = board.get_empty_positions()
    move = random.choice(empty_cells)
    board.mark_move(move, "computer")


def find_win_row_column(matrix, player):
    marker = assign_marker(player)
    for transpose in (False, True):
        if transpose:
            matrix = numpy.transpose(matrix).tolist()
        n_row = 0
        for row in matrix:
            if ''.join(row).replace(' ', '') == 2 * marker:
                n_column = find_empty_column(row)
                if transpose:
                    return(n_column, n_row)
                else:
                    return(n_row, n_column)
            else:
                n_row += 1


def find_win_diagonal(matrix, player):
    marker = assign_marker(player)
    for lead_diagonal in (True, False):
        if lead_diagonal:
            diagonal = numpy.diagonal(matrix).tolist()
        else:
            diagonal = numpy.diagonal(numpy.fliplr(matrix)).tolist()
        n_row_column = 0
        if ''.join(diagonal).replace(' ', '') == 2 * marker:
            for element in diagonal:
                if element == ' ':
                    if lead_diagonal:
                        return(n_row_column, n_row_column)
                    else:
                        return(n_row_column, len(matrix) - 1 - n_row_column)
                else:
                    n_row_column += 1

def find_empty_position_row_column(matrix):
    n_row = 0
    for row in matrix:
        if ''.join(row).replace(' ', '') == 2 * marker:
            n_column = find_empty_column(row)
            if transpose:
                return(n_column, n_row)
            else:
                return(n_row, n_column)
        else:
            n_row += 1

def find_empty_column(row):
    n_column = 0
    for column in row:
        if column == ' ':
            return n_column
        else:
            n_column += 1
