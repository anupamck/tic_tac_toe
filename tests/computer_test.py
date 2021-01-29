from tictactoe.computer import *
from tictactoe.board import *
import pytest
from tictactoe.player import *

def test_make_random_move(): # How can I link these test names automatically to the methods they test?
    c = Computer()
    h = Player()
    test_list = {
    "six moves": [[((0, 0), h), ((0, 1), c), ((1, 0), c), ((1, 1), h),
                    ((2, 0), c), ((2, 1), h)], 2]
    }

    for test_name, test_case in test_list.items():
        print(test_name)
        b = Board()
        move_list = test_case[0]
        result = test_case[1]
        for move, mover in move_list:
            b.mark_move(move, mover)
        c.make_random_move(b)
        assert len(b.get_empty_positions()) == result


def test_get_move():
    c = Computer()
    h = Player()
    test_list = {
    "go for win": [([(0, 0), c], [(0, 1), c]), (0, 2)],
    "block rival win": [([(0, 0), h], [(1, 1), h]), (2, 2)]
    }

    for test_name, test_case in test_list.items():
        print(test_name)
        b = Board()
        move_list = test_case[0]
        row = test_case[1][0]
        col = test_case[1][1]
        for move, mover in move_list:
            b.mark_move(move, mover)
        c.get_move(b, h)
        assert b.matrix[row][col] == c.symbol
