from src.choice.choice_enum import ChoiceEnum
from src.choice.choice import Choice

class Spock(Choice):
    def __init__(self):
        super().__init__(
            losing_cases = (ChoiceEnum.PAPER, ChoiceEnum.LIZARD),
            winning_cases = (ChoiceEnum.ROCK, ChoiceEnum.SCISSORS),
            draw_case = ChoiceEnum.SPOCK
        )