from src.choice.choice import Choice
from src.choice.choice_enum import ChoiceEnum

class Rock(Choice):
    def __init__(self):
        super().__init__(
            losing_cases = (ChoiceEnum.PAPER, ChoiceEnum.SPOCK),
            winning_cases = (ChoiceEnum.SCISSORS, ChoiceEnum.LIZARD),
            draw_case = ChoiceEnum.ROCK
        )