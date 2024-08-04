from src.settings import *


class GameBlocks:
    def __init__(self, width, height, rows: int, column: int) -> None:
        self.width = width
        self.height = height
        self.rows = rows
        self.column = column
        self.reward_score = 120
        self.block_list = [
            pg.Rect(
                10 + (self.width + 10) * i,
                10 + (self.height + 5) * j,
                self.width,
                self.height,
            )
            for i in range(column)
            for j in range(rows)
        ]
        self.color_list = [
            (255, 0, random.randrange(1, 256))
            for i in range(column)
            for j in range(rows)
        ]
        self.block_sprites = self.load_sprites()
        self.new_color_list = [
            (BLOCK_COLORS[random.randint(0, 7)]) for x in self.block_list
        ]

    def reset_current(self):
        self.block_list = [
            pg.Rect(
                10 + (self.width + 5) * i,
                10 + (self.height + 5) * j,
                self.width,
                self.height,
            )
            for i in range(self.column)
            for j in range(self.rows)
        ]
        self.new_color_list = [
            (BLOCK_COLORS[random.randint(0, 7)]) for x in self.block_list
        ]

    def draw(self, screen):
        [
            pg.draw.rect(screen, self.new_color_list[color], block)
            for color, block in enumerate(self.block_list)
        ]

    def load_sprites(self) -> list:
        files = [
            item
            for item in pathlib.Path("./assets/img/tiles/blocks").rglob("*.png")
            if item.is_file()
        ]
        sprites = [pg.image.load(file).convert_alpha() for file in files]
        sprites = [pg.transform.scale(sprite, (BLOCK_H, BLOCK_W)) for sprite in sprites]
        return sprites


class ParticleEffect:
    def __init__(
        self, screen, pos, color, max_particles=50, particle_speed=8, particle_size=1
    ):
        self.screen = screen
        self.pos = pos
        self.color = color
        self.max_particles = max_particles
        self.particle_speed = particle_speed
        self.particle_size = particle_size
        self.particles = []
        self.create_particles()
        self.active = True
        self.time = 0

    def create_particles(self):
        for i in range(self.max_particles):
            particle = {
                "pos": [
                    self.pos[0] + random.uniform(-35, 35),
                    self.pos[1] + random.uniform(-35, 35),
                ],
                "speed": [
                    random.uniform(-self.particle_speed, self.particle_speed),
                    random.uniform(-self.particle_speed, self.particle_speed),
                ],
                "color": self.color,
                "life": random.uniform(0.2, 0.5),
            }
            self.particles.append(particle)

    def update(self, dt):
        self.time += dt
        if self.time > 1:
            self.active = False
        for particle in self.particles:
            particle["pos"][0] += particle["speed"][0] * (dt * 4)
            particle["pos"][1] += particle["speed"][1] * (dt * 4)
            particle["life"] -= dt
            particle["color"][3] = max(0, min(255, int(255 * (particle["life"] / 2))))
            particle

    def draw(self):
        for particle in self.particles:
            pg.draw.circle(
                self.screen,
                particle["color"],
                (int(particle["pos"][0]), int(particle["pos"][1])),
                self.particle_size,
            )
