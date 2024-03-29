import pygame
from utils import import_folder
from settings import game_width
from random import choice, randint
from tiles import StaticTile


class Clouds:
    def __init__(self, horizon, level_width, cloud_number):
        cloud_surfaces = import_folder('assets/levels/universal/clouds')
        min_x = -game_width
        max_x = level_width + game_width
        min_y = 0
        max_y = horizon
        self.cloud_sprites = pygame.sprite.Group()

        for cloud in range(cloud_number):
            cloud = choice(cloud_surfaces)
            x = randint(min_x, max_x)
            y = randint(min_y, max_y)
            sprite = StaticTile(0, x, y, cloud)
            self.cloud_sprites.add(sprite)

    def draw(self, surface, shift):
        self.cloud_sprites.update(shift)
        self.cloud_sprites.draw(surface)