from src.settings import *
from src.paddle import Paddle
from src.ball import Ball
from src.blocks import GameBlocks, ParticleEffect
from src.ui_text import TextOverlay
from src.menu import BDMenu
from src.player import Player

BASE_DIR = os.path.dirname(__file__)


class BreakOut:
    def __init__(self) -> None:
        pg.init()
        self.screen = pg.display.set_mode((DISPLAY_W, DISPLAY_H))
        self.manager = pgGUI.UIManager((DISPLAY_W, DISPLAY_H), "theme.json")
        self.Menu = BDMenu(self.manager)
        self.load_files()
        pg.display.set_caption("BreakOut PyGame")
        pg.display.set_icon(self.icon)
        pg.mixer.music.play(-1, 0, 0)
        pg.mixer.music.set_volume(0.4)
        self.state = State.MENU
        self.Menu.show_mainmenu()

        self.blockboard = GameBlocks(BLOCK_W, BLOCK_H, 6, 9)
        self.menu_text = TextOverlay(self)
        self.paddle = Paddle(PADDLE_W, PADDLE_H, 0, 0, 15)
        self.ball = Ball(10, 10, 10, img=self.ball_img)
        self.player = Player()
        self.ballRect = self.ball.ballRect
        self.clock = pg.time.Clock()

        # self.blockboard_new = BlockPattern(DISPLAY_W-10, DISPLAY_H - 10, 80,40)
        # self.blockboard_new.reset_to_level(1)
        self.running = False
        self.pause = False
        self.game_over = False
        self.game_started = False
        self.blockanim = None
        self.wallanim = None
        self.score_next = LEVEL_BREAKPOINTS["1"]
        self.broken_blocks = 0
        self.fps = FPS
        self.dx, self.dy = 1, -1

    def load_files(self):
        self.icon = pg.image.load(
            os.path.join(BASE_DIR + "\\assets\\img\\", "gameicon.png")
        )
        self.bg_img = pg.image.load(
            os.path.join(BASE_DIR + "\\assets\\img\\", "bg.jpg")
        ).convert_alpha()
        self.ball_img = pg.image.load(
            os.path.join(os.curdir + "\\assets\\img\\", "ball.png")
        ).convert_alpha()
        self.bg_music = pg.mixer.music.load(
            os.path.join(BASE_DIR + "\\assets\\sound\\", "Music.mp3")
        )
        self.menu_sound = pg.mixer.Sound(
            os.path.join(BASE_DIR + "\\assets\\sound\\", "click.mp3")
        )
        self.blockhit_sound = pg.mixer.Sound(
            os.path.join(BASE_DIR + "\\assets\\sound\\", "blockhit.wav")
        )
        self.bg_img = pg.transform.scale(self.bg_img, (DISPLAY_W, DISPLAY_H))

    def check_level_up(self):
        if self.player.score >= self.score_next:
            self.player.level += 1
            self.score_next = LEVEL_BREAKPOINTS[str(self.player.level)]
        else:
            return

    def get_reward(self):
        self.fps += 2
        self.player.score += self.blockboard.reward_score
        self.player.broken_blocks += 1
        self.check_level_up()
        self.update_player()

    def check_win(self) -> bool:
        if not len(self.blockboard.block_list):
            self.game_over = True
            return True
        return False

    def update_player(self):
        self.Menu.show_gameinfo(self.player)

    def start_game(self):
        self.Menu.show_gameinfo(self.player)
        if not self.game_started:
            self.game_started = True
        if self.game_over:
            self.game_over = False
        if not self.ball.active:
            self.ball.set_active(True)

    def reset_game(self):
        self.player.reset_player()
        self.fps = FPS
        self.game_started = False
        self.score_next = LEVEL_BREAKPOINTS["1"]
        self.ball.set_active(False)
        self.ball.reset_position()
        self.blockboard.reset_current()
        self.update_player()

    def play_state(self):
        # paddle + ball collision
        if self.ballRect.colliderect(self.paddle) and self.dy > 0:
            self.dx, self.dy = self.check_block_collision(
                self.dx, self.dy, self.ballRect, self.paddle.rect
            )
            self.ball.play_sound()

        # block + ball collision
        hit_index = self.ballRect.collidelist(self.blockboard.block_list)
        if hit_index != -1:
            pg.mixer.Sound.play(self.blockhit_sound)
            hit_rect = self.blockboard.block_list.pop(hit_index)
            hit_color = self.blockboard.new_color_list.pop(hit_index)
            self.dx, self.dy = self.check_block_collision(
                self.dx, self.dy, self.ballRect, hit_rect
            )
            hit_rect.inflate_ip(self.ball.width * 4, self.ball.height * 4)
            pg.draw.rect(self.screen, hit_color, hit_rect)
            self.get_reward()
            self.check_win()

        self.check_collision()
        # paddle controls
        key = pg.key.get_pressed()
        if (key[pg.K_a] or key[pg.K_LEFT]) and self.paddle.rect.left > 10:
            self.paddle.move(MoveDirection.LEFT)
        elif (
            key[pg.K_d] or key[pg.K_RIGHT]
        ) and self.paddle.rect.right < DISPLAY_W - 10:
            self.paddle.move(MoveDirection.RIGHT)

    def draw(self):
        self.paddle.draw(self.screen)
        self.blockboard.draw(self.screen)
        # self.blockboard_new.draw(self.screen)

    def check_block_collision(self, dx, dy, ball, rect):
        if dx > 0:
            delta_x = ball.right - rect.left
        else:
            delta_x = rect.right - ball.left

        if dy > 0:
            delta_y = ball.bottom - rect.top
        else:
            delta_y = rect.bottom - ball.top

        if abs(delta_x - delta_y) < 10:
            dx, dy = -dx, -dy
        elif delta_x > delta_y:
            dy = -dy
        elif delta_y > delta_x:
            dx = -dx
        return dx, dy

    def check_gameover(self):
        print(f"Game: Check Gameover Hearts: {self.player.hearts}")

        if self.player.hearts <= 0:
            self.game_over = True
            if self.player.score > self.Menu.best_score:
                self.state = State.NAMEINPUT
                self.Menu.show_highscoreinput()
        else:
            return

    def check_collision(self):
        if (
            self.ball.ballRect.centerx < self.ball.radius
            or self.ball.ballRect.centerx > GAMEFIELD_W - self.ball.radius
        ):
            self.dx = -self.dx
            self.blockanim = ParticleEffect(
                self.screen, self.ballRect.center, pg.Color(169, 44, 0)
            )
            self.blockanim.active = True
            self.blockanim.draw()
            self.ball.play_sound()

        if self.ballRect.centery < self.ball.radius:
            self.dy = -self.dy
            self.ball.play_sound()
            self.blockanim = ParticleEffect(
                self.screen, self.ballRect.center, pg.Color(169, 44, 0)
            )
            self.blockanim.active = True
            self.blockanim.draw()

        if self.ballRect.centery > (GAMEFIELD_H - MENU_H) + self.ball.radius:
            self.ball.set_active(False)
            self.paddle.reset_position()
            self.ball.reset_position()
            self.dx, self.dy = 1, -1
            self.game_started = False
            self.player.hearts -= 1
            self.update_player()
            self.check_gameover()

    def set_new_highscore(self):
        if not self.Menu.score_name_input.get_text() == "":
            self.Menu.data.add_new_highscore(
                self.Menu.score_name_input.get_text(), self.player.score
            )
            self.Menu.highscores = self.Menu.data.load()
            self.Menu.best_score = self.Menu.data.get_best_score(self.Menu.highscores)
            print("Game: Highscore saved!")

    def reset_screen(self):
        self.screen.blit(self.bg_img, (0, 0))

    def run(self):
        self.running = True
        self.state = State.MENU
        dev = True
        while self.running:
            time_delta = self.clock.tick(self.fps) / 1000.0

            for event in pg.event.get():
                if event.type == pg.QUIT or (
                    event.type == pg.KEYDOWN
                    and event.key == pg.K_ESCAPE
                    and not self.state == State.INGAME
                ):
                    self.running = False
                # keyboard events
                if event.type == pg.KEYUP:
                    k = event.key
                    if k == pg.K_p:
                        if self.game_started:
                            self.pause = not self.pause
                            if self.ball.active and self.pause:
                                self.ball.set_active(False)
                                print("Game paused!")
                            else:
                                self.ball.set_active(True)
                                print("Game resumed!")
                    if k == pg.K_t and self.state == State.INGAME:
                        if self.wallanim == None:
                            self.wallanim = ParticleEffect(
                                self.screen, self.ballRect.center, pg.Color(3, 252, 94)
                            )
                            self.wallanim.active = True

                    elif k == pg.K_ESCAPE and self.state == State.INGAME:
                        self.reset_game()
                        self.Menu.show_mainmenu()
                        self.state = State.MENU
                    elif (
                        k == pg.K_RETURN
                        and self.state == State.INGAME
                        and self.game_over
                    ):
                        self.reset_game()
                        self.start_game()
                    elif (
                        k == pg.K_RETURN
                        and self.state == State.INGAME
                        and not self.game_started
                    ):
                        self.start_game()

                # Menu Button events
                if event.type == pgGUI.UI_BUTTON_PRESSED:
                    pg.mixer.Sound.play(self.menu_sound)
                    if event.ui_element == self.Menu.highscore_button:
                        self.Menu.show_score()
                        self.state = State.HIGHSCORE
                        print("Highscore pressed")

                    elif event.ui_element == self.Menu.nameinput_button:
                        self.set_new_highscore()
                        self.reset_game()
                        self.Menu.show_score()
                        self.state = State.HIGHSCORE

                    elif event.ui_element == self.Menu.play_button:
                        self.Menu.show_gameinfo(self.player)
                        self.state = State.INGAME

                    elif event.ui_element == self.Menu.score_backbutton:
                        self.Menu.show_mainmenu()
                        self.state = State.MENU

                    # elif event.ui_element == self.Menu.test_button:
                    #     pass
                    elif event.ui_element == self.Menu.help_back_button:
                        self.Menu.show_mainmenu()
                        self.state = State.MENU

                    elif event.ui_element == self.Menu.help_button:
                        self.Menu.show_help()
                        self.state = State.HELP

                    elif event.ui_element == self.Menu.exit_button:
                        self.running = False
                self.manager.process_events(event)

            self.reset_screen()
            if self.blockanim != None:
                if self.blockanim.active:
                    self.blockanim.update(dt=time_delta * 4)
                    self.blockanim.draw()
                elif not self.blockanim.active:
                    self.blockanim = None
            if self.wallanim != None:
                if self.wallanim.active:
                    self.wallanim.update(dt=time_delta * 4)
                    self.wallanim.draw()
                elif not self.wallanim.active:
                    self.wallanim = None
            if self.state == State.MENU:
                self.manager.draw_ui(self.screen)
            elif self.state == State.HIGHSCORE:
                self.manager.draw_ui(self.screen)
            elif self.state == State.NAMEINPUT:
                self.manager.draw_ui(self.screen)
            elif self.state == State.HELP:
                self.manager.draw_ui(self.screen)
            elif self.state == State.INGAME:
                # self.menu_text.draw_infotext()
                self.manager.draw_ui(self.screen)
                if not self.game_started:
                    self.menu_text.draw_startText()
                    if self.player.score != 0:
                        self.draw()
                else:
                    self.draw()
                    self.ball.move(self.screen, self)
                if self.pause:
                    self.reset_screen()
                    self.menu_text.draw_pause()
                elif self.game_over:
                    self.reset_screen()
                    self.menu_text.draw_gameover()
                else:
                    self.play_state()
            self.manager.update(time_delta)

            pg.display.update()
            pg.display.flip()
            self.clock.tick(self.fps)

        pg.quit()


if __name__ == "__main__":
    game = BreakOut()
    try:
        game.run()
    except KeyboardInterrupt:
        print("ESC Breakout Game")
    except Exception as e:
        print(e)

    finally:
        pg.quit()
        sys.exit()
