from src.choice.choice import Choice
from src.choice.choice_enum import ChoiceEnum

class Scissors(Choice):
    def __init__(self):
        super().__init__(
            losing_case = ChoiceEnum.ROCK,
            winning_case = ChoiceEnum.PAPER,
            draw_case = ChoiceEnum.SCISSORS
        )