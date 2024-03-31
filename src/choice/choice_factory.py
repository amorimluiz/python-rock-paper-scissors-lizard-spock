from src.choice.lizzard import Lizzard
from src.choice.spock import Spock
from src.choice.choice_enum import ChoiceEnum
from src.choice.rock import Rock
from src.choice.choice import Choice
from src.choice.paper import Paper
from src.choice.scissors import Scissors

class ChoiceFactory:
    @staticmethod
    def get_choice(choice) -> Choice:
        match choice:
            case ChoiceEnum.ROCK:
                return Rock()
            case ChoiceEnum.PAPER:
                return Paper()
            case ChoiceEnum.SCISSORS:
                return Scissors()
            case ChoiceEnum.LIZARD:
                return Lizzard()
            case ChoiceEnum.SPOCK:
                return Spock()
            case _:
                raise Exception('Escolha do Jogador 1 inválida.')
            