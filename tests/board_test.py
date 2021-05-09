from tictactoe.board import *
import pytest
from tictactoe.player import *
from tictactoe.computer import *

def test_generate_matrix():     # How do I refactor this to have only 1 assert?
    for length in (2, 3, 5):
        char = ' '
        matrix = generate_matrix(length, ' ')
        assert len(matrix) == length
        for row in matrix:
            assert len(row) == length
            for slot in row:
                assert slot == char

def test_mark_move():
    b = Board()
    h = Player()
    results = {"top left": (0, 0),
               "center mid": (1, 1)}
    for test_name, test_case in results.items():
        print(test_name)
        b.mark_move(test_case, h)
        assert b.matrix[test_case[0]][test_case[1]] == h.symbol


def test_mark_move_negative():
    b = Board()
    h = Player()
    marker = h.symbol
    test_list = {"top left": ([0, 0], [0, 0]),
                 "center mid": ([1, 1], [1, 1])}
    for test_name, test_case in test_list.items():
        print(test_name)
        with pytest.raises(MoveError):
            for move in test_case:
                b.mark_move(move, h)



def test_check_result():
    h = Player()
    c = Computer()
    test_list = {
    "top row win": ([((0, 0), h), ((0, 1), h), ((0, 2), h)], h, "win"),
    "left col win": ([((0, 0), c), ((1, 0), c), ((2, 0), c)], c, "win"),
    "lead diag win":([((0, 0), h), ((1, 1), h), ((2, 2), h)], h, "win"),
    "opp diag win":([((0, 2), c), ((1, 1), c), ((2, 0), c)], c, "win"),
    "draw": ([((0, 0), h), ((0, 1), c), ((0, 2), h), ((1, 0), c),
              ((1, 1), h), ((1, 2), c), ((2, 0), c), ((2, 1), h),
              ((2, 2), c)], h, "none"),
    "near win": ([((0, 0), h), ((0, 1), c), ((1, 0), c), ((1, 1), h),
                ((2, 0), c),((2, 1), h)], h, "near win"),
    "unclear": ([((0, 0), h), ((0, 1), c), ((0, 2), h), ((1, 0), c),
               ((1, 1), h), ((2, 0), c), ((2, 1), h), ((2, 2), c)], h, "unclear")}

    for test_name, test_case in test_list.items():
        print(test_name)     # Check if there is a better way to do this in pytest
        b = Board()
        move_list = test_case[0]
        player = test_case[1]
        result = test_case[2]

        for move,mover in move_list:
            b.mark_move(move, mover)

        assert b.check_result(player) == result


def test_mark_human_move_positive():
    b = Board()
    h = Player()
    marker = h.symbol
    test_list = {
    "bottom right": [('br', h), (2, 2), marker],
    "dead center": [('cm', h), (1, 1), marker],
    "top left": [('tl', h), (0, 0), marker]
    }

    for test_name, test_case in test_list.items():
        print(test_name)
        human_move = test_case[0][0]
        mover = test_case[0][1]
        row = test_case[1][0]
        col = test_case[1][1]
        b.mark_human_move(mover, human_move)
        assert b.matrix[row][col] == marker
# Test case coverage - do you have to write one test per test path?


def test_mark_human_move_negative(): # Is this the correct way to split +ve and -ve test cases?
    b = Board()
    h = Player()
    test_list = {
    "illegal position": [('mx', h)],
    "duplicate mark": [('tl', h), ('tl', h)]
    }

    for test_name, test_case in test_list.items():
        print(test_name)
        with pytest.raises(MoveError):
            for move, mover in test_case:
                b.mark_human_move(mover, move)


def test_get_empty_positions():
    h = Player()
    c = Computer()
    test_list = {
    "right col": ([((0, 0), h), ((0, 1), c), ((1, 0), c), ((1, 1), h),
                   ((2, 0), c), ((2, 1), h)],
                  [(0, 2), (1, 2), (2, 2)]),
    "lead diag": ([((0, 1), c), ((0, 2), h), ((1, 0), c), ((1, 2), h),
                    ((2, 0), c), ((2, 1), h)],
                  [(0, 0), (1, 1), (2, 2)])
    }

    for test_name, test_case in test_list.items():
        print(test_name)
        b = Board()
        move_list = test_case[0]
        result = test_case[1]
        for move, mover in move_list:
            b.mark_move(move, mover)
        assert b.get_empty_positions() == result
