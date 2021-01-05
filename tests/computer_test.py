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

def test_find_winnning_position():
    b = Board()
    b.mark_move((0, 0), "human")
    b.mark_move((0, 1), "human")
    marker = assign_marker("human")
    assert find_win_row_column(b.matrix, marker) == (0, 2)

    b = Board()
    b.mark_move((0, 1), "computer")
    b.mark_move((1, 1), "computer")
    marker = assign_marker("computer")
    assert find_win_row_column(b.matrix, marker, True) == (2, 1)
