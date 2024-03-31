from src.choice.choice_factory import ChoiceFactory
from src.game.result_enum import ResultEnum


class Game:
    @staticmethod
    def throw_result(first_player_choice, second_player_choice) -> ResultEnum:
        first_player_choice = ChoiceFactory.get_choice(first_player_choice)

        if second_player_choice in first_player_choice.get_winning_cases():
            return ResultEnum.FIRST_PLAYER_WON
        
        if second_player_choice in first_player_choice.get_loosing_cases():
            return ResultEnum.SECOND_PLAYER_WON
        
        return ResultEnum.DRAW