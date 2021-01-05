from tictactoe.board import *
import pytest


def test_assign_marker():
    assert assign_marker("human") == "X"
    assert assign_marker("comp") == "O"
    assert assign_marker("Computer") == "O"
    with pytest.raises(MoveError):
        assign_marker("Waldo")

def test_generate_matrix():     # How do I test if the function creates all blank cells?
    for length in (2, 3, 5):
        matrix = generate_matrix(length)
        assert len(matrix) == length
        for row in matrix:
            assert len(row) == length

def test_mark_move():
    b = Board()
    results = {(0, 0): "X",
               (1, 1): "X",}
    for key in results.keys():
        b.mark_move(key, "human")
        assert b.matrix[key[0]][key[1]] == results[key]


def test_check_result_win():
    b = Board()
    b.mark_move((0, 0), "human")
    b.mark_move((0, 1), "human")
    b.mark_move((0, 2), "human")
    assert b.check_result("human") == ("win")

    b = Board()
    b.mark_move((0, 0), "computer")
    b.mark_move((1, 0), "computer")
    b.mark_move((2, 0), "computer")
    assert b.check_result("computer") == ("win")

    b = Board()
    b.mark_move((0, 0), "human")
    b.mark_move((1, 1), "human")
    b.mark_move((2, 2), "human")
    assert b.check_result("human") == ("win")

    b = Board()
    b.mark_move((0, 0), "human")
    b.mark_move((0, 1), "computer")
    b.mark_move((0, 2), "human")
    b.mark_move((1, 0), "computer")
    b.mark_move((1, 1), "human")
    b.mark_move((1, 2), "computer")
    b.mark_move((2, 0), "computer")
    b.mark_move((2, 1), "human")
    b.mark_move((2, 2), "computer")
    assert b.check_result("human") == "draw"

    b = Board()
    b.mark_move((0, 0), "human")
    b.mark_move((0, 1), "computer")
    b.mark_move((1, 0), "computer")
    b.mark_move((1, 1), "human")
    b.mark_move((2, 0), "computer")
    b.mark_move((2, 1), "human")
    assert b.check_result("human") == "near win"

    b = Board()
    b.mark_move((0, 0), "human")
    b.mark_move((0, 1), "computer")
    b.mark_move((0, 2), "human")
    b.mark_move((1, 0), "computer")
    b.mark_move((1, 1), "human")
    b.mark_move((2, 0), "computer")
    b.mark_move((2, 1), "human")
    b.mark_move((2, 2), "computer")
    assert b.check_result("human") == "unclear"

def test_mark_human_move():
    b = Board()
    with pytest.raises(MoveError):
        b.mark_human_move('mx')
    b.mark_human_move('tl')
    assert b.matrix[0][0] == "X"
    with pytest.raises(MoveError):
        b.mark_human_move('tl')
    b.mark_human_move('br')
    assert b.matrix[2][2] == "X"

def test_find_near_win():
    b = Board()
    b.mark_move((0, 0), "computer")
    b.mark_move((0, 1), "computer")

def test_get_empty_positions():
    b = Board()
    b.mark_move((0, 0), "human")
    b.mark_move((0, 1), "computer")
    b.mark_move((1, 0), "computer")
    b.mark_move((1, 1), "human")
    b.mark_move((2, 0), "computer")
    b.mark_move((2, 1), "human")
    result = b.get_empty_positions()
    assert result == [(0, 2), (1, 2), (2, 2)]
