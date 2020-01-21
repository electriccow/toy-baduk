from enum import Enum

class Stone(Enum):
    BLACK = 1
    WHITE = 2
    EMPTY = 0

class Board:
    def get_stone_at(self, x, y):
        return Stone.EMPTY
    def put_stone_at(x, y, stone):
        pass
