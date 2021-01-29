from tictactoe.board import *
from tictactoe.engine import *


import pytest

def test_get_player_type(monkeypatch):
    test_list = {
    "human": ['h', ('1', 'X'), ('human', 'X')],
    "computer": ['c', ('2', 'O'), ('computer', 'O')]
    }
    for test_name, test_case in test_list.items():
        print(test_name)
        input, parameters, result = test_case
        monkeypatch.setattr('builtins.input', lambda _: input)
        number, symbol = parameters
        return_value = get_player_type(number, symbol)
        assert result == (return_value.type, return_value.symbol)
        # How can I test a case with invalid input here? 


def test_toggle_player():
    c = Computer()
    h = Player()
    f = Player()
    test_list = {
    "human": (h, c),
    "computer": (c, h),
    }
    for test_name, test_case in test_list.items():
        print(test_name)
        player, rival = test_case
        assert toggle_player(player, (player, rival)) == rival

    with pytest.raises(MoveError):
        toggle_player(f, (c, h))


def test_choose_first_mover():
    c = Computer()
    h = Player()
    assert choose_first_mover((c, h)) in (h, c)

# def test_play_next_move():
#         b = Board()
#         b.mark_move("tl", h)
#         b.mark_move("cl", h)
