from enum import Enum

class CollisionType(Enum):
    NONE = -1,
    LEFT = 0,
    RIGHT = 1,
    UP = 2,
    DOWN = 3