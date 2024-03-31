from src.game.game import Game
from src.game.result_enum import ResultEnum
from src.choice.choice_enum import ChoiceEnum

def test_rock_combinations():
    assert Game.throw_result(ChoiceEnum.ROCK, ChoiceEnum.ROCK) == ResultEnum.DRAW
    assert Game.throw_result(ChoiceEnum.ROCK, ChoiceEnum.SCISSORS) == ResultEnum.FIRST_PLAYER_WON
    assert Game.throw_result(ChoiceEnum.ROCK, ChoiceEnum.LIZARD) == ResultEnum.FIRST_PLAYER_WON
    assert Game.throw_result(ChoiceEnum.ROCK, ChoiceEnum.PAPER) == ResultEnum.SECOND_PLAYER_WON
    assert Game.throw_result(ChoiceEnum.ROCK, ChoiceEnum.SPOCK) == ResultEnum.SECOND_PLAYER_WON

def test_paper_combinations():
    assert Game.throw_result(ChoiceEnum.PAPER, ChoiceEnum.PAPER) == ResultEnum.DRAW
    assert Game.throw_result(ChoiceEnum.PAPER, ChoiceEnum.ROCK) == ResultEnum.FIRST_PLAYER_WON
    assert Game.throw_result(ChoiceEnum.PAPER, ChoiceEnum.SPOCK) == ResultEnum.FIRST_PLAYER_WON
    assert Game.throw_result(ChoiceEnum.PAPER, ChoiceEnum.SCISSORS) == ResultEnum.SECOND_PLAYER_WON
    assert Game.throw_result(ChoiceEnum.PAPER, ChoiceEnum.LIZARD) == ResultEnum.SECOND_PLAYER_WON

def test_scirssors_combinations():
    assert Game.throw_result(ChoiceEnum.SCISSORS, ChoiceEnum.SCISSORS) == ResultEnum.DRAW
    assert Game.throw_result(ChoiceEnum.SCISSORS, ChoiceEnum.PAPER) == ResultEnum.FIRST_PLAYER_WON
    assert Game.throw_result(ChoiceEnum.SCISSORS, ChoiceEnum.LIZARD) == ResultEnum.FIRST_PLAYER_WON
    assert Game.throw_result(ChoiceEnum.SCISSORS, ChoiceEnum.SPOCK) == ResultEnum.SECOND_PLAYER_WON
    assert Game.throw_result(ChoiceEnum.SCISSORS, ChoiceEnum.ROCK) == ResultEnum.SECOND_PLAYER_WON

def test_lizard_combinations():
    assert Game.throw_result(ChoiceEnum.LIZARD, ChoiceEnum.LIZARD) == ResultEnum.DRAW
    assert Game.throw_result(ChoiceEnum.LIZARD, ChoiceEnum.PAPER) == ResultEnum.FIRST_PLAYER_WON
    assert Game.throw_result(ChoiceEnum.LIZARD, ChoiceEnum.SPOCK) == ResultEnum.FIRST_PLAYER_WON
    assert Game.throw_result(ChoiceEnum.LIZARD, ChoiceEnum.SCISSORS) == ResultEnum.SECOND_PLAYER_WON
    assert Game.throw_result(ChoiceEnum.LIZARD, ChoiceEnum.ROCK) == ResultEnum.SECOND_PLAYER_WON

def test_spock_combinations():
    assert Game.throw_result(ChoiceEnum.SPOCK, ChoiceEnum.SPOCK) == ResultEnum.DRAW
    assert Game.throw_result(ChoiceEnum.SPOCK, ChoiceEnum.ROCK) == ResultEnum.FIRST_PLAYER_WON
    assert Game.throw_result(ChoiceEnum.SPOCK, ChoiceEnum.SCISSORS) == ResultEnum.FIRST_PLAYER_WON
    assert Game.throw_result(ChoiceEnum.SPOCK, ChoiceEnum.PAPER) == ResultEnum.SECOND_PLAYER_WON
    assert Game.throw_result(ChoiceEnum.SPOCK, ChoiceEnum.LIZARD) == ResultEnum.SECOND_PLAYER_WON