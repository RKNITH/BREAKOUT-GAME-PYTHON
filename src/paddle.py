from src.settings import *


class Paddle:
    def __init__(self, width, height, x, y, speed):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.speed = speed

        self.rect = pg.Rect(
            GAMEFIELD_W // 2 - self.width // 2,
            (GAMEFIELD_H - MENU_H) - self.height + 10,
            self.width,
            self.height,
        )

    def draw(self, screen):
        pg.draw.rect(screen, pg.Color("darkred"), self.rect, border_radius=15)

    def reset_position(self):
        self.rect.move(
            GAMEFIELD_W // 2 - self.width // 2,
            (GAMEFIELD_H - MENU_H) - self.height + 10,
        )

    def move(self, direction):
        if direction == MoveDirection.LEFT:
            self.rect.left -= self.speed
        elif direction == MoveDirection.RIGHT:
            self.rect.right += self.speed

        # print("move ", direction)
