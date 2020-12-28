from tictactoe.computer import *
from tictactoe.board import *
import pytest

def test_find_win():
    b = Board()
    b.mark_move("tl", "computer")
    b.mark_move("tm", "computer")
    assert find_win(b, "computer") == "tr"

    b = Board()
    b.mark_move("tl", "human")
    b.mark_move("tm", "human")
    assert find_win(b, "human") == "tr"

    b = Board()
    b.mark_move("tl", "human")
    with pytest.raises(MoveError):
        assert find_win(b, "human") == "tr"

    b = Board()
    b.mark_move("tl", "human")
    b.mark_move("tm", "computer")
    b.mark_move("cl", "computer")
    b.mark_move("cm", "human")
    b.mark_move("bl", "computer")
    b.mark_move("bm", "human")
    assert find_win(b, "human") == "br"

def test_make_random_move():
    b = Board()
    b.mark_move("tl", "human")
    b.mark_move("tm", "computer")
    b.mark_move("cl", "computer")
    b.mark_move("cm", "human")
    b.mark_move("bl", "computer")
    b.mark_move("bm", "human")
    make_random_move(b)
    assert len(b.get_empty_positions()) == 2

def test_find_winnning_position():
    b = Board()
    b.mark_move("tl", "human")
    b.mark_move("tm", "human")
    assert find_winning_position(("tl", "tm", "tr"), b) == "tr"
    b = Board()
    b.mark_move("tl", "computer")
    b.mark_move("cm", "computer")
    assert find_winning_position(("tl", "cm", "br"), b) == "br"
