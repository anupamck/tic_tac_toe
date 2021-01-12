from tictactoe.computer import *
from tictactoe.board import *
import pytest

def test_find_win():
    b = Board()
    b.mark_move((0, 0), "computer")
    b.mark_move((0, 1), "computer")
    assert find_win(b, "computer") == (0, 2)

    b = Board()
    b.mark_move((0, 0), "human")
    b.mark_move((0, 1), "human")
    assert find_win(b, "human") == (0, 2)

    b = Board()
    b.mark_move((0, 0), "human")
    with pytest.raises(MoveError):
        assert find_win(b, "human") == (0, 2)

    b = Board()
    b.mark_move((0, 0), "human")
    b.mark_move((0, 1), "computer")
    b.mark_move((1, 0), "computer")
    b.mark_move((1, 1), "human")
    b.mark_move((2, 0), "computer")
    assert find_win(b, "human") == (2, 2)

    b = Board()
    b.mark_move((2, 0), "human")
    b.mark_move((0, 1), "computer")
    b.mark_move((1, 2), "computer")
    b.mark_move((1, 1), "human")
    b.mark_move((0, 0), "computer")
    assert find_win(b, "human") == (0, 2)

def test_make_random_move():
    b = Board()
    b.mark_move((0, 0), "human")
    b.mark_move((0, 1), "computer")
    b.mark_move((1, 0), "computer")
    b.mark_move((1, 1), "human")
    b.mark_move((2, 0), "computer")
    b.mark_move((2, 1), "human")
    make_random_move(b)
    assert len(b.get_empty_positions()) == 2

def test_find_win_row_column():
    test_list = {
    "top_row": [[((0, 0), "human"), ((0, 1), "human")], "human", (0, 2)],
    "mid_column": [[((0, 1), "comp"), ((1, 1), "comp")], "comp", (2, 1)]
    }
    for test_case in test_list.values():
        b = Board()
        for move_player in test_case[0]:
            move = move_player[0]
            player = move_player[1]
            b.mark_move(move, player)
        assert find_win_row_column(b.matrix, test_case[1]) == test_case[2]


def test_find_win_diagonal():
    test_list = {
    "lead diagonal": [[((0, 0), "human"), ((1, 1), "human")], "human", (2, 2)],
    "opp diagonal": [[((0, 2), "comp"), ((1, 1), "comp")], "comp", (2, 0)]
    }
    for test_case in test_list.values():
        b = Board()
        for move_player in test_case[0]:
            move = move_player[0]
            player = move_player[1]
            b.mark_move(move, player)
        assert find_win_diagonal(b.matrix, test_case[1]) == test_case[2]


def test_find_empty_column():
    test_list = {
    "first_column": [(' ', 'X', 'X'), 0],
    "second_column": [('X',' ','X'), 1],
    "third_column": [('X','X',' '), 2]
    }
    for test_case in test_list.values():
        assert find_empty_column(test_case[0]) == test_case[1]

def test_find_empty_diagonal_slot():
    test_list = {
    "lead_diagonal": [(' ', 'X', 'X'), True, (0, 0)],
    "opp_diagonal": [('X','X',' '), False, (2, 0)]
    }
    for test_case in test_list.values():
        result = find_empty_diagonal_slot(test_case[0], test_case[1])
        assert result == test_case[2]
