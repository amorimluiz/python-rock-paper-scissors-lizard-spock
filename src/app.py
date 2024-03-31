from src.game.game import Game
from src.game.result_enum import ResultEnum
from src.choice.choice_enum import ChoiceEnum

print(Game.throw_result(ChoiceEnum.ROCK, ChoiceEnum.ROCK) == ResultEnum.DRAW)