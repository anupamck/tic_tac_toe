from tictactoe.board import MoveError, assign_marker
import random
import numpy

# Should I have a class for Computer?

def find_win(board, player):
    marker = assign_marker(player)
    result = find_win_row_column(board.matrix, marker)
    if result == None:
        result = find_win_row_column(board.matrix, marker, True)

    if result != None:
        return result

    result = find_win_diagonal(board, marker)

    if result != None:
        return result
    else:
        raise MoveError("Winning position unavailable.")


def make_random_move(board):
    empty_cells = board.get_empty_positions()
    move = random.choice(empty_cells)
    board.mark_move(move, "computer")


def find_win_row_column(matrix, marker, transpose=False):
    if transpose:
        matrix = numpy.transpose(matrix).tolist()

    n_row = 0
    for row in matrix:
        if ''.join(row).replace(' ', '') == 2 * marker:
            n_column = 0
            for column in row:
                if column == ' ':
                    break
                else:
                    n_column += 1
            if transpose:
                return(n_column, n_row)
            else:
                return(n_row, n_column)
            break
        else:
            n_row += 1

def find_win_diagonal(board, marker):
    diagonal = numpy.diagonal(board.matrix).tolist()
    n_row_column = 0
    if ''.join(diagonal).replace(' ', '') == 2 * marker:
        for element in diagonal:
            if element == ' ':
                return(n_row_column, n_row_column)
            else:
                n_row_column += 1

    diagonal = numpy.diagonal(numpy.fliplr(board.matrix)).tolist()
    n_row_column = 0
    if ''.join(diagonal).replace(' ', '') == 2 * marker:
        for element in diagonal:
            if element == ' ':
                return(n_row_column, board.length - 1 - n_row_column)
            else:
                n_row_column += 1
