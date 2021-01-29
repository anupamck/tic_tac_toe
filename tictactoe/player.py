import numpy
from tictactoe.board import *

class Player:
    def __init__(self, name= "Player", type="human", symbol="X"):
        self.name = name
        self.type = type
        self.symbol = symbol

    def __get_name(self):
        return self.__name
    def __set_name(self, name):
        self.__name = name
    name = property(__get_name, __set_name)

    def __get_type(self):
        return self.__type
    def __set_type(self, type):
        self.__type = type
    type = property(__get_type, __set_type)

    def __get_symbol(self):
        return self.__symbol
    def __set_symbol(self, symbol):
        self.__symbol = symbol
    symbol = property(__get_symbol, __set_symbol)




    def find_win(self, board):      # Refactor this!
        result = self.find_win_row_column(board)

        if result != None:
            return result

        result = self.find_win_diagonal(board)

        if result != None:
            return result
        else:
            raise MoveError("Winning position unavailable.")


    def find_win_row_column(self, board):
        for transpose in (False, True):
            if transpose:
                matrix = numpy.transpose(board.matrix).tolist()
            else:
                matrix = board.matrix
            n_row = 0
            for row in matrix:
                if ''.join(row).replace(' ', '') == 2 * self.symbol:
                    n_column = find_empty_column(row)
                    if transpose:
                        return(n_column, n_row)
                    else:
                        return(n_row, n_column)
                else:
                    n_row += 1


    def find_win_diagonal(self, board):  # In such cases, do I pass the board or the matrix as argument?
        for lead_diagonal in (True, False):
            if lead_diagonal:
                diagonal = numpy.diagonal(board.matrix).tolist()
            else:
                diagonal = numpy.diagonal(numpy.fliplr(board.matrix)).tolist()

            if ''.join(diagonal).replace(' ', '') == 2 * self.symbol:
                return find_empty_diagonal_slot(diagonal, lead_diagonal)


    def get_move(self, board):
        move = input(f"{self.name}, enter your move > ") # In which module do I put this function?
        try:
            board.mark_human_move(self, move)
        except(MoveError):
            print("Invalid move. Try again.")
            self.get_move(board)  # Recursion


def find_empty_column(row): # Can I leave these outside the class? Read up about helper functions
    n_column = 0
    for column in row:
        if column == ' ':
            return n_column
        else:
            n_column += 1


def find_empty_diagonal_slot(diagonal, lead_diagonal): # Can I leave these outside the class?
    n_row_column = 0
    for element in diagonal:
        if element == ' ':
            if lead_diagonal:
                return(n_row_column, n_row_column)
            else:
                return(n_row_column, len(diagonal) - 1 - n_row_column)
        else:
            n_row_column += 1
