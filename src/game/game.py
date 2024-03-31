from src.choice.choice_factory import ChoiceFactory
from src.game.result_enum import ResultEnum


class Game:
    @staticmethod
    def throw_result(first_player_choice, second_player_choice) -> ResultEnum:
        return ChoiceFactory.get_choice(first_player_choice).get_result(second_player_choice)