import pygame
import sys
from settings import *
from level import Level
from overworld import Overworld
from pygame import mixer


def main() -> None:
    class Game:
        def __init__(self):
            self.max_level: int = 0
            self.overworld: Overworld = Overworld(0, self.max_level, screen, self.create_level)
            self.status = 'overworld'

        def create_level(self, current_level):
            self.level = Level(current_level, screen, self.create_overworld)
            self.status = 'level'

        def create_overworld(self, current_level, new_max_level):
            if new_max_level > self.max_level:
                self.max_level = new_max_level

            self.overworld = Overworld(current_level, self.max_level, screen, self.create_level)
            self.status = 'overworld'

        def run(self):
            if self.status == 'overworld':
                self.overworld.run()
            else:
                self.level.draw_level()

    pygame.init()
    engage_brand()  # Add window icon, set window title

    mixer.init()
    mixer.music.load('assets/music/music.mp3')
    mixer.music.play()

    screen = pygame.display.set_mode((game_width, game_height))
    clock = pygame.time.Clock()
    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill('black')
        game.run()

        pygame.display.update()
        clock.tick(60)


def engage_brand():
    pygame.display.set_caption("The power of one!")
    icon = pygame.image.load("assets/icon32.png")
    pygame.display.set_icon(icon)


if __name__ == '__main__':
    main()
