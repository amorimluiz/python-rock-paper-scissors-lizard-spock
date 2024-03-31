from src.game.result_enum import ResultEnum

class Choice:
    def __init__(self, losing_case, winning_case, draw_case):
        self._losing_case = losing_case
        self._winning_case = winning_case
        self._draw_case = draw_case

    def get_result(self, second_player_choice) -> ResultEnum:
        match second_player_choice:
            case self._losing_case:
                return ResultEnum.SECOND_PLAYER_WON
            case self._winning_case:
                return ResultEnum.FIRST_PLAYER_WON
            case self._draw_case:
                return ResultEnum.DRAW
            case _:
                raise Exception('Escolha do jogador 2 inválida.')
    pass