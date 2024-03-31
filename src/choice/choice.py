from src.game.result_enum import ResultEnum

class Choice:
    def __init__(self, losing_cases, winning_cases, draw_case):
        self._losing_cases = losing_cases
        self._winning_cases = winning_cases
        self._draw_case = draw_case

    def get_loosing_cases(self):
        return self._losing_cases
    
    def get_winning_cases(self):
        return self._winning_cases
    
    def get_draw_case(self):
        return self._draw_case
    
    pass