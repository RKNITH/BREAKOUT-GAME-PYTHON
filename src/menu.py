from src.settings import *


class BDMenu:
    def __init__(self, manager: pgGUI.UIManager) -> None:
        self.manager: pgGUI.UIManager = manager
        self.data = ScoreData()
        self.highscore_labels = []
        self.highscores = self.data.load()
        self.best_score = self.data.get_best_score(self.highscores)
        self.nameinput_button = None
        self.score_backbutton = None
        self.title_label = None
        self.version_label = None
        self.highscore_button = None
        self.play_button = None
        self.help_back_button = None
        self.help_labels = []

        # self.data.save(self.highscores)

    def clear_screen(self):
        self.manager.clear_and_reset()

    def show_mainmenu(self):
        self.clear_screen()

        self.title_label = GUI.UILabel(
            relative_rect=pg.Rect(
                (DISPLAY_W * 0.50) - 400, (DISPLAY_H * 0.15) - 25, 800, 100
            ),
            text="BreakDown",
            manager=self.manager,
        )

        self.play_button = GUI.UIButton(
            relative_rect=pg.Rect(
                (DISPLAY_W * 0.50) - 150, (DISPLAY_H * 0.4) - 10, 300, 65
            ),
            text="Play",
            manager=self.manager,
        )

        self.highscore_button = GUI.UIButton(
            relative_rect=pg.Rect(
                (DISPLAY_W * 0.50) - 150, (DISPLAY_H * 0.475) - 10, 300, 65
            ),
            text="Highscore",
            manager=self.manager,
        )

        self.help_button = GUI.UIButton(
            relative_rect=pg.Rect(
                (DISPLAY_W * 0.50) - 150, (DISPLAY_H * 0.550) - 10, 300, 65
            ),
            text="Help",
            manager=self.manager,
        )

        self.exit_button = GUI.UIButton(
            relative_rect=pg.Rect(
                (DISPLAY_W * 0.50) - 150, (DISPLAY_H * 0.625) - 10, 300, 65
            ),
            text="Exit",
            manager=self.manager,
        )

        # self.test_button = GUI.UIButton(
        #     relative_rect=pg.Rect((DISPLAY_W  * 0.50) - 150, (DISPLAY_H * 0.7 ) - 10, 300, 65),
        #     text='Test',
        #     manager=self.manager)

        # Versionstext
        self.version_label = GUI.UILabel(
            relative_rect=pg.Rect(
                (DISPLAY_W * 0.50) - 350, (DISPLAY_H * 0.95), 700, 50
            ),
            text=f"{VERSIONTEXT}",
            manager=self.manager,
            object_id=pgGUI.core.ObjectID("#versionlabel"),
        )

    def show_score(self):
        self.clear_screen()
        self.highscores = self.data.load()
        self.title_label = GUI.UILabel(
            relative_rect=pg.Rect(
                (DISPLAY_W * 0.50) - 400, (DISPLAY_H * 0.15) - 25, 800, 100
            ),
            text="BreakDown",
            manager=self.manager,
        )

        self.title_label = GUI.UILabel(
            relative_rect=pg.Rect(
                (DISPLAY_W * 0.50) - 400, (DISPLAY_H * 0.25) - 25, 800, 100
            ),
            text="Highscores",
            manager=self.manager,
            object_id=pgGUI.core.ObjectID("#subtitlelabel"),
        )

        for i, highscore in enumerate(self.highscores):
            label = pgGUI.elements.UILabel(
                relative_rect=pg.Rect(
                    (DISPLAY_W * 0.5) - 200, (DISPLAY_H * 0.4) + i * 50, 400, 50
                ),
                text="{}. {}: {}".format(i + 1, highscore["name"], highscore["score"]),
                manager=self.manager,
                object_id=pgGUI.core.ObjectID("#scoreitemlabel"),
            )
            self.highscore_labels.append(label)
            if i == 4:
                break

        self.score_backbutton = GUI.UIButton(
            relative_rect=pg.Rect(
                (DISPLAY_W * 0.50) - 150, (DISPLAY_H * 0.9) - 10, 300, 65
            ),
            text="Back",
            manager=self.manager,
        )

        self.version_label = GUI.UILabel(
            relative_rect=pg.Rect(
                (DISPLAY_W * 0.50) - 350, (DISPLAY_H * 0.95), 700, 50
            ),
            text=f"{VERSIONTEXT}",
            manager=self.manager,
            object_id=pgGUI.core.ObjectID("#versionlabel"),
        )

    def show_highscoreinput(self):
        self.clear_screen()
        self.title_label = GUI.UILabel(
            relative_rect=pg.Rect(
                (DISPLAY_W * 0.50) - 400, (DISPLAY_H * 0.15) - 25, 800, 100
            ),
            text="BreakDown",
            manager=self.manager,
        )
        self.new_score_gameover = GUI.UILabel(
            relative_rect=pg.Rect(
                (DISPLAY_W * 0.50) - 400, (DISPLAY_H * 0.3) - 25, 800, 100
            ),
            text="GAME OVER!",
            manager=self.manager,
            object_id=pgGUI.core.ObjectID("#gameoverlabel"),
        )

        self.new_score_subtitle = GUI.UILabel(
            relative_rect=pg.Rect(
                (DISPLAY_W * 0.50) - 400, (DISPLAY_H * 0.475) - 25, 800, 100
            ),
            text="New Highscore!",
            manager=self.manager,
            object_id=pgGUI.core.ObjectID("#newhighscorelabel"),
        )

        self.score_name_input = GUI.UITextEntryLine(
            relative_rect=pg.Rect(
                (DISPLAY_W * 0.5) - 200, (DISPLAY_H * 0.575) - 10, 400, 50
            ),
            placeholder_text="Enter your Name...",
            manager=self.manager,
            object_id=pgGUI.core.ObjectID("#nameinput"),
        )

        self.nameinput_button = GUI.UIButton(
            relative_rect=pg.Rect(
                (DISPLAY_W * 0.50) - 150, (DISPLAY_H * 0.75) - 10, 300, 65
            ),
            text="Okay",
            manager=self.manager,
        )

        # Versionstext
        self.version_label = GUI.UILabel(
            relative_rect=pg.Rect(
                (DISPLAY_W * 0.50) - 350, (DISPLAY_H * 0.95), 700, 50
            ),
            text=f"{VERSIONTEXT}",
            manager=self.manager,
            object_id=pgGUI.core.ObjectID("#versionlabel"),
        )

    def show_gameinfo(self, player):
        self.clear_screen()
        self.playername_heart_label = GUI.UILabel(
            relative_rect=pg.Rect(
                (DISPLAY_W * 0.355) - 150, (DISPLAY_H * 0.875), 300, 50
            ),
            text="Hearts:",
            manager=self.manager,
            object_id=pgGUI.core.ObjectID("#gameinfolabel-l"),
        )
        self.player_heart_label = GUI.UILabel(
            relative_rect=pg.Rect(
                (DISPLAY_W * 0.645) - 150, (DISPLAY_H * 0.875), 300, 50
            ),
            text=f"{player.hearts}",
            manager=self.manager,
            object_id=pgGUI.core.ObjectID("#gameinfolabel-r"),
        )

        self.scorename_info_label = GUI.UILabel(
            relative_rect=pg.Rect(
                (DISPLAY_W * 0.355) - 150, (DISPLAY_H * 0.9), 300, 50
            ),
            text="Score:",
            manager=self.manager,
            object_id=pgGUI.core.ObjectID("#gameinfolabel-l"),
        )
        self.score_info_label = GUI.UILabel(
            relative_rect=pg.Rect(
                (DISPLAY_W * 0.645) - 150, (DISPLAY_H * 0.9), 300, 50
            ),
            text=f"{player.score}",
            manager=self.manager,
            object_id=pgGUI.core.ObjectID("#gameinfolabel-r"),
        )

        self.levelname_info_label = GUI.UILabel(
            relative_rect=pg.Rect(
                (DISPLAY_W * 0.355) - 150, (DISPLAY_H * 0.925), 300, 50
            ),
            text="Level:",
            manager=self.manager,
            object_id=pgGUI.core.ObjectID("#gameinfolabel-l"),
        )
        self.level_info_label = GUI.UILabel(
            relative_rect=pg.Rect(
                (DISPLAY_W * 0.645) - 150, (DISPLAY_H * 0.925), 300, 50
            ),
            text=f"{player.level}",
            manager=self.manager,
            object_id=pgGUI.core.ObjectID("#gameinfolabel-r"),
        )

        self.blockname_info_label = GUI.UILabel(
            relative_rect=pg.Rect(
                (DISPLAY_W * 0.355) - 150, (DISPLAY_H * 0.95), 300, 50
            ),
            text="Blocks:",
            manager=self.manager,
            object_id=pgGUI.core.ObjectID("#gameinfolabel-l"),
        )
        self.block_info_label = GUI.UILabel(
            relative_rect=pg.Rect(
                (DISPLAY_W * 0.645) - 150, (DISPLAY_H * 0.95), 300, 50
            ),
            text=f"{player.broken_blocks}",
            manager=self.manager,
            object_id=pgGUI.core.ObjectID("#gameinfolabel-r"),
        )

    def show_help(self):
        self.clear_screen()
        self.title_label = GUI.UILabel(
            relative_rect=pg.Rect(
                (DISPLAY_W * 0.50) - 400, (DISPLAY_H * 0.15) - 25, 800, 100
            ),
            text="BreakDown",
            manager=self.manager,
        )

        self.help_subtitle = GUI.UILabel(
            relative_rect=pg.Rect(
                (DISPLAY_W * 0.50) - 400, (DISPLAY_H * 0.25) - 25, 800, 100
            ),
            text="Help",
            manager=self.manager,
            object_id=pgGUI.core.ObjectID("#subtitlelabel"),
        )

        space = 0.4
        for i in HELP_TEXT:
            label = pgGUI.elements.UILabel(
                relative_rect=pg.Rect(
                    (DISPLAY_W * 0.5) - 300, (DISPLAY_H * space) - 25, 600, 50
                ),
                text=str(i),
                manager=self.manager,
                object_id=pgGUI.core.ObjectID("#scoreitemlabel"),
            )
            self.help_labels.append(label)
            space += 0.050

        self.help_back_button = GUI.UIButton(
            relative_rect=pg.Rect(
                (DISPLAY_W * 0.50) - 150, (DISPLAY_H * 0.9) - 10, 300, 65
            ),
            text="Back",
            manager=self.manager,
        )

        self.version_label = GUI.UILabel(
            relative_rect=pg.Rect(
                (DISPLAY_W * 0.50) - 350, (DISPLAY_H * 0.95), 700, 50
            ),
            text=f"{VERSIONTEXT}",
            manager=self.manager,
            object_id=pgGUI.core.ObjectID("#versionlabel"),
        )


class ScoreData:
    def __init__(self) -> None:
        self.file_path = os.curdir + "\\data\\scores.json"

    def add_new_highscore(self, name: str, score: int):
        highscores = self.load()
        item = {"name": name, "score": score}
        highscores.append(item)
        new = sorted(highscores, key=lambda d: d["score"], reverse=True)
        self.save(new)

    def get_best_score(self, highscores: list) -> int:
        if not len(highscores) > 0:
            return 0
        score_list = [(score["score"]) for i, score in enumerate(highscores)]
        return int(min(score_list))

    def save(self, highscores: list):
        with open(self.file_path, "w") as f:
            json.dump(highscores, f)

    def load(self) -> list:
        with open(self.file_path, "r") as f:
            loaded_scores = json.load(f)
        return loaded_scores
