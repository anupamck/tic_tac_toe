from tictactoe.computer import *
from tictactoe.board import *
import pytest
from tictactoe.player import *

def test_find_win():    # How can I improve traceablility using test name?
    c = Computer()
    h = Player()
    test_list = {
    "top row": [[((0, 0), c), ((0, 1), c)], c, (0, 2)],
    "left col": [[((0, 0), h), ((1, 0), h)], h, (2, 0)],
    "lead diag": [[((0, 0), h), ((0, 1), c), ((1, 0), c),
                   ((1, 1), h), ((2, 0), c)], h, (2, 2)],
    "opp diag": [[((2, 0), h), ((0, 1), c), ((1, 2), c),
                   ((1, 1), h), ((0, 0), c)], h, (0, 2)],
    "double trouble": [[((0, 0), h), ((0, 1), c), ((0, 2), c),
                        ((1, 1), h), ((2, 0), h)], h, (1, 0)]
    }

    for test_name, test_case in test_list.items():
        print(test_name)
        b = Board()
        move_list = test_case[0]
        player = test_case[1]
        result = test_case[2]
        for move,mover in move_list:
            b.mark_move(move, mover)
        assert player.find_win(b) == result


def test_find_win_row_column():
    c = Computer()
    h = Player()
    test_list = {
    "top_row": [[((0, 0), h), ((0, 1), h)], h, (0, 2)],
    "mid_column": [[((0, 1), c), ((1, 1), c)], c, (2, 1)],
    "double trouble": [[((0, 0), h), ((0, 1), c), ((0, 2), c),
                        ((1, 1), h), ((2, 0), h)], h, (1, 0)]
    }
    for test_name, test_case in test_list.items():
        print(test_name)
        b = Board()
        for move, player in test_case[0]:
            b.mark_move(move, player)
        assert test_case[1].find_win_row_column(b) == test_case[2]


def test_find_win_diagonal():
    c = Computer()
    h = Player()
    test_list = {
    "lead diagonal": [[((0, 0), h), ((1, 1), h)], h, (2, 2)],
    "opp diagonal": [[((0, 2), c), ((1, 1), c)], c, (2, 0)]
    }
    for test_name, test_case in test_list.items():
        print(test_name)
        b = Board()
        for move, player in test_case[0]:
            b.mark_move(move, player)
        assert test_case[1].find_win_diagonal(b) == test_case[2]


def test_find_empty_column():
    test_list = {
    "first_column": [(' ', 'X', 'X'), 0],
    "second_column": [('X',' ','X'), 1],
    "third_column": [('X','X',' '), 2]
    }
    for test_name, test_case in test_list.items():
        print(test_name)
        assert find_empty_column(test_case[0]) == test_case[1]

def test_find_empty_diagonal_slot():
    test_list = {
    "lead_diagonal": [(' ', 'X', 'X'), True, (0, 0)],
    "opp_diagonal": [('X','X',' '), False, (2, 0)]
    }
    for test_name, test_case in test_list.items():
        print(test_name)
        result = find_empty_diagonal_slot(test_case[0], test_case[1])
        assert result == test_case[2]

def test_get_move(monkeypatch):
    h = Player()
    test_list = {
    "top right": ("tr", (0, 2)),
    "bottom left": ("bl", (2, 0))
    }

    for test_name, test_case in test_list.items():
        print(test_name)
        b = Board()
        monkeypatch.setattr('builtins.input', lambda _: test_case[0])
        h.get_move(b)
        for row, col in [test_case[1]]:
            assert b.matrix[row][col] == h.symbol


@pytest.mark.skip(reason="Leads to infinite recursion") # How can I test something like this?
def test_get_move_negative(monkeypatch):
    h = Player()
    test_list = {
    "invalid": [("to", (0, 2))],
    "duplicate": [("bl", (2, 0)), ("bl", (2, 0))]
    }

    for test_name, test_case in test_list.items():
        print(test_name)
        b = Board()
        for input, move in test_case:
            with pytest.raises(MoveError):
                monkeypatch.setattr('builtins.input', lambda _: input)
                h.get_move(b)
