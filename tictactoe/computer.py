from tictactoe.board import MoveError
import random
import numpy
from tictactoe.player import Player

class Computer(Player):
    def __init__(self, name = "Computer", type='computer', symbol='O', level='Easy'):
        Player.__init__(self, name, type, symbol)
        self.level = level

    def __get_level(self):
            return self.__level

    def __set_level(self, level):
        self.__level = level

    level = property(__get_level, __set_level)

    def make_random_move(self, board):
        empty_cells = board.get_empty_positions()
        move = random.choice(empty_cells)
        board.mark_move(move, self)

    def get_move(self, board, rival):
        if board.check_result(self) == "near win":
            next_move = self.find_win(board)
            board.mark_move(next_move, self)
        elif board.check_result(rival) == "near win":
            next_move = rival.find_win(board)
            board.mark_move(next_move, self)
        else:
            self.make_random_move(board)
