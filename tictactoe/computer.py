from tictactoe.board import MoveError, assign_marker
import random
import numpy
from player import Player

class Computer(Player):
    def __init__(self, name='Computer', symbol='O', level='Easy'):
        Player.__init__(name, symbol)
        self.level = level

    def __get_level(self):
            return self.__level

    def __set_level(self, level):
        self.__level = level

    level = property(__get_level, __set_level)

    def find_win(self, board):
        result = find_win_row_column(board.matrix, self.player)

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


def find_win_diagonal(matrix, player):  # In such cases, do I pass the board or the matrix as argument?
    marker = assign_marker(player)
    for lead_diagonal in (True, False):
        if lead_diagonal:
            diagonal = numpy.diagonal(matrix).tolist()
        else:
            diagonal = numpy.diagonal(numpy.fliplr(matrix)).tolist()

        if ''.join(diagonal).replace(' ', '') == 2 * marker:
            return find_empty_diagonal_slot(diagonal, lead_diagonal)


def find_empty_column(row):
    n_column = 0
    for column in row:
        if column == ' ':
            return n_column
        else:
            n_column += 1


def find_empty_diagonal_slot(diagonal, lead_diagonal):
    n_row_column = 0
    for element in diagonal:
        if element == ' ':
            if lead_diagonal:
                return(n_row_column, n_row_column)
            else:
                return(n_row_column, len(diagonal) - 1 - n_row_column)
        else:
            n_row_column += 1
