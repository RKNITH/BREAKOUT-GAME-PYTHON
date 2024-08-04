from src.settings import *


@dataclass
class Player:
    hearts: int = 3
    score: int = 0
    level: int = 1
    broken_blocks: int = 0
    speed: int = 8

    def update_player(self, score: int, level: int, blocks: int):
        self.score = score
        self.level = level
        self.broken_blocks = blocks

    def reset_player(self):
        self.score = 0
        self.level = 1
        self.hearts = 3
        self.broken_blocks = 0
