from src.game.result_enum import ResultEnum

class Choice:
    def __init__(self, losing_cases, winning_cases, draw_case):
        self._losing_cases = losing_cases
        self._winning_cases = winning_cases
        self._draw_case = draw_case

    def get_result(self, second_player_choice) -> ResultEnum:
            if second_player_choice == self._draw_case:
                return ResultEnum.DRAW
            
            if second_player_choice in self._winning_cases:
                return ResultEnum.FIRST_PLAYER_WON
            
            return ResultEnum.SECOND_PLAYER_WON
    pass