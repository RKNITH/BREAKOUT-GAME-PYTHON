import pygame as pg
import pygame_gui as pgGUI
import pygame_gui.elements as GUI
import enum

import random, json, os, sys
from typing import Final
from dataclasses import dataclass
import pathlib

VERSION: Final = "1.5.7"
VERSIONTEXT: Final = f"Version {VERSION} | Design & Development © 2023 S3R43o3"

MENU_W, MENU_H = 1200, 75
GAMEFIELD_W, GAMEFIELD_H = 1200, 800
DISPLAY_W, DISPLAY_H = 1200, MENU_H + GAMEFIELD_H
FPS: Final = 60
BLOCK_W, BLOCK_H = 160, 40

PADDLE_W, PADDLE_H = 350, 15
COLOR_BGWIN = (36, 36, 36)

BLOCK_COLORS: list = [
    (0, 203, 255),
    (21, 0, 255),
    (255, 0, 239),
    (0, 255, 16),
    (255, 239, 0),
    (255, 112, 0),
    (143, 0, 255),
    (255, 0, 0),
]

LEVEL_BREAKPOINTS: dict = {
    "1": 500,
    "2": 1500,
    "3": 5000,
    "4": 7500,
    "5": 12500,
    "6": 20000,
}


class MoveDirection(enum.Enum):
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"


class State(enum.Enum):
    MENU = 0
    INGAME = 1
    HIGHSCORE = 2
    NAMEINPUT = 3
    HELP = 4


HELP_TEXT = [
    "ESC - Exit Game / Mainmenu",
    "P - Game pause",
    "ENTER - Start game",
    "A or Arrow Left - Move Left",
    "D or Arrow Right - Move Right",
]
