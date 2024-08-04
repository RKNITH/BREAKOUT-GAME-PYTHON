from src.settings import *
import pygame.freetype as ft


class TextOverlay:
    def __init__(self, mainframe, text="") -> None:
        self.app = mainframe
        self.text = text
        self.font = ft.Font(".\\assets\\fonts\\mainFont.otf", True)
        self.p_text = "GAME PAUSED"
        self.gameover_text = "GAME OVER"

    def draw_pause(self):
        self.font.render_to(
            self.app.screen,
            (DISPLAY_W * 0.05, DISPLAY_H * 0.3),
            text=self.p_text,
            fgcolor="green",
            size=100.0,
            bgcolor=pg.Color(0, 0, 0, 0),
        )

    def draw_gameover(self):
        self.font.render_to(
            self.app.screen,
            (DISPLAY_W * 0.05, DISPLAY_H * 0.3),
            text=self.gameover_text,
            fgcolor="red",
            size=100.0,
            bgcolor=pg.Color(0, 0, 0, 0),
        )

    def draw_startText(self):
        self.font.render_to(
            self.app.screen,
            (DISPLAY_W * 0.05, DISPLAY_H * 0.45),
            text="Press 'Enter' to Start",
            fgcolor="orange",
            size=60.0,
            bgcolor=pg.Color(0, 0, 0, 0),
        )

    def draw_infotext(self):
        self.font.render_to(
            self.app.screen,
            (DISPLAY_W * 0.25, DISPLAY_H * 0.9),
            text=f"Player: {self.app.player.name}",
            fgcolor="red",
            size=20.0,
            bgcolor=pg.Color(0, 0, 0, 0),
        )
        self.font.render_to(
            self.app.screen,
            (DISPLAY_W * 0.25, DISPLAY_H * 0.933),
            text=f"Level: {self.app.level}",
            fgcolor="red",
            size=20.0,
            bgcolor=pg.Color(0, 0, 0, 0),
        )
        self.font.render_to(
            self.app.screen,
            (DISPLAY_W * 0.25, DISPLAY_H * 0.966),
            text=f"Score: {self.app.score}",
            fgcolor="red",
            size=20.0,
            bgcolor=pg.Color(0, 0, 0, 0),
        )
        self.font.render_to(
            self.app.screen,
            (DISPLAY_W * 0.55, DISPLAY_H * 0.9),
            text=f"Speed: {self.app.ball._speed}",
            fgcolor="red",
            size=20.0,
            bgcolor=pg.Color(0, 0, 0, 0),
        )
        self.font.render_to(
            self.app.screen,
            (DISPLAY_W * 0.55, DISPLAY_H * 0.933),
            text=f"Required: {self.app.score_next}",
            fgcolor="red",
            size=20.0,
            bgcolor=pg.Color(0, 0, 0, 0),
        )
        self.font.render_to(
            self.app.screen,
            (DISPLAY_W * 0.55, DISPLAY_H * 0.966),
            text=f"Blocks: {self.app.broken_blocks}",
            fgcolor="red",
            size=20.0,
            bgcolor=pg.Color(0, 0, 0, 0),
        )

    def draw_highscore(self):
        self.font.render_to(
            self.app.screen,
            (DISPLAY_W * 0.05, DISPLAY_H * 0.3),
            text="Highscore",
            fgcolor="red",
            size=100.0,
            bgcolor=pg.Color(0, 0, 0, 0),
        )
