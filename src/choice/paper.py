from src.choice.choice import Choice
from src.choice.choice_enum import ChoiceEnum

class Paper(Choice):
    def __init__(self):
        super().__init__(
            losing_cases = (ChoiceEnum.SCISSORS, ChoiceEnum.LIZARD),
            winning_cases = (ChoiceEnum.ROCK, ChoiceEnum.SPOCK),
            draw_case = ChoiceEnum.PAPER
        )