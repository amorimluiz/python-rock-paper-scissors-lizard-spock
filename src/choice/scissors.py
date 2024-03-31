from src.choice.choice import Choice
from src.choice.choice_enum import ChoiceEnum

class Scissors(Choice):
    def __init__(self):
        super().__init__(
            losing_cases = (ChoiceEnum.ROCK, ChoiceEnum.SPOCK),
            winning_cases = (ChoiceEnum.PAPER, ChoiceEnum.LIZARD),
            draw_case = ChoiceEnum.SCISSORS
        )