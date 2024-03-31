from src.choice.choice_enum import ChoiceEnum
from src.choice.choice import Choice

class Lizzard(Choice):
    def __init__(self):
        super().__init__(
            losing_cases = (ChoiceEnum.ROCK, ChoiceEnum.SCISSORS),
            winning_cases = (ChoiceEnum.PAPER, ChoiceEnum.SPOCK),
            draw_case = ChoiceEnum.LIZARD
        )