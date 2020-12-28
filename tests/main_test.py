from tictactoe.board import *
from main import *
import pytest

def test_get_player_move(monkeypatch):
    b = Board()
    b.mark_move("tl", "computer")
    b.mark_move("cl", "computer")
    get_player_move("computer", b)
    marker = assign_marker("computer")
    assert b.status['bl'] == marker

    b = Board()
    b.mark_move("tl", "human")
    b.mark_move("cl", "human")
    get_player_move("computer", b)
    marker = assign_marker("computer")
    assert b.status['bl'] == marker

    b = Board() # mocked user input!
    monkeypatch.setattr('builtins.input', lambda _: "tr") # '_' :is a placeholder for an input parameter
    next_move = get_player_move("human", b)
    marker = assign_marker("human")
    assert b.status['tr'] == marker

def test_toggle_player():
    assert toggle_player("human") == "computer"
    assert toggle_player("computer") == "human"
    with pytest.raises(MoveError):
        toggle_player("Waldo")

def test_choose_first_mover():
    assert choose_first_mover() in ("human", "computer")

# def test_play_next_move():
#         b = Board()
#         b.mark_move("tl", "human")
#         b.mark_move("cl", "human")
