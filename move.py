from enum import Enum

class Move(Enum):
    # описываем текущее состояние игрока (движение вправо,влево, вверх, вниз или стоит)
    RIGHT = "right"
    LEFT = "left"
    UP = "up"
    DOWN = "down"
    STOP = "stop"