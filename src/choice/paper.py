from src.choice.choice import Choice
from src.choice.choice_enum import ChoiceEnum

class Paper(Choice):
    def __init__(self):
        super().__init__(
            losing_case = ChoiceEnum.SCISSORS,
            winning_case = ChoiceEnum.ROCK,
            draw_case = ChoiceEnum.PAPER
        )