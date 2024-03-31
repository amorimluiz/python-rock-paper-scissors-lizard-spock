from enum import Enum

class ResultEnum(Enum):
    DRAW = 'draw',
    FIRST_PLAYER_WON = 'first_player_won',
    SECOND_PLAYER_WON = 'second_player_won'