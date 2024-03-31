from src.choice.choice import Choice
from src.choice.choice_enum import ChoiceEnum

class Rock(Choice):
    def __init__(self):
        super().__init__(
            losing_case = ChoiceEnum.PAPER,
            winning_case = ChoiceEnum.SCISSORS,
            draw_case = ChoiceEnum.ROCK
        )