from tictactoe.board import *
import pytest

b = Board()
b.print_board()


def test_assign_marker():
    assert assign_marker("human") == "X"
    assert assign_marker("comp") == "O"
    assert assign_marker("Computer") == "O"
    with pytest.raises(MoveError):
        assign_marker("Waldo")


def test_mark_move():
    b = Board()
    b.mark_move("tl", "human")
    assert b.status["tl"] == "X"
    with pytest.raises(MoveError):
        b.mark_move("tl", "human")
    b.mark_move("tm", "computer")
    assert b.status["tm"] == "O"
    with pytest.raises(MoveError):
        b.mark_move("tm", "computer")
    # b.print_board()

def test_check_result():
    b = Board()
    b.mark_move("tl", "human")
    b.mark_move("tm", "human")
    b.mark_move("tr", "human")
    assert b.check_result("human") == ("win")

    b = Board()
    b.mark_move("tl", "computer")
    b.mark_move("cl", "computer")
    b.mark_move("bl", "computer")
    assert b.check_result("computer") == ("win")

    b = Board()
    b.mark_move("tl", "human")
    b.mark_move("tm", "computer")
    b.mark_move("tr", "human")
    b.mark_move("cl", "computer")
    b.mark_move("cm", "human")
    b.mark_move("cr", "computer")
    b.mark_move("bl", "computer")
    b.mark_move("bm", "human")
    b.mark_move("br", "computer")
    assert b.check_result("human") == "draw"

    b = Board()
    b.mark_move("tl", "human")
    b.mark_move("tm", "computer")
    b.mark_move("cl", "computer")
    b.mark_move("cm", "human")
    b.mark_move("bl", "computer")
    b.mark_move("bm", "human")
    assert b.check_result("human") == "near win"

    b = Board()
    b.mark_move("tl", "human")
    b.mark_move("tm", "computer")
    b.mark_move("tr", "human")
    b.mark_move("cl", "computer")
    b.mark_move("cm", "human")
    b.mark_move("bl", "computer")
    b.mark_move("bm", "human")
    b.mark_move("br", "computer")
    assert b.check_result("human") == "unclear"

def test_mark_human_move():
    b = Board()
    with pytest.raises(MoveError):
        b.mark_human_move('mx')
    b.mark_human_move('tl')
    assert b.status["tl"] == "X"
    with pytest.raises(MoveError):
        b.mark_human_move('tl')

def test_find_near_win():
    b = Board()
    b.mark_move("tl", "computer")
    b.mark_move("tm", "computer")

def test_get_empty_positions():
    b = Board()
    b.mark_move("tl", "human")
    b.mark_move("tm", "computer")
    b.mark_move("cl", "computer")
    b.mark_move("cm", "human")
    b.mark_move("bl", "computer")
    b.mark_move("bm", "human")
    result = b.get_empty_positions()
    assert result == ['tr', 'cr', 'br']
