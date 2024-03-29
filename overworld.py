import pygame
from game_data import levels


class LevelNode(pygame.sprite.Sprite):
    def __init__(self, pos, status, icon_speed):
        super().__init__()

        if status == 'available':
            self.image = pygame.image.load("assets/overworld/0.png").convert_alpha()
        else:
            self.image = pygame.image.load('assets/overworld/1.png').convert_alpha()

        self.rect: pygame.Rect = self.image.get_rect(center=pos)

        self.detection_zone = pygame.Rect(self.rect.centerx - (icon_speed / 2),
                                          self.rect.centery - (icon_speed / 2),
                                          icon_speed,
                                          icon_speed)


class Icon(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.pos = pos
        self.image: pygame.Surface = pygame.image.load('assets/icon64.png').convert_alpha()
        self.rect: pygame.Rect = self.image.get_rect(center=pos)

    def update(self):
        self.rect.center = self.pos


class Overworld:
    def __init__(self, starting_level: int, max_level: int, surface: pygame.Surface, create_level):
        self.display_surface: pygame.Surface = surface
        self.max_level: int = max_level
        self.current_level: int = starting_level
        self.create_level = create_level

        self.moving = False
        self.move_direction = pygame.math.Vector2(0, 0)
        self.speed = 8

        self.setup_nodes()
        self.setup_icon()

    def setup_nodes(self) -> None:
        self.node_sprites = pygame.sprite.Group()

        for node_index, node_data in enumerate(levels.values()):
            if node_index <= self.max_level:
                node_sprite: LevelNode = LevelNode(node_data.get('node_pos'), 'available', self.speed)
                self.node_sprites.add(node_sprite)
            else:
                node_sprite: LevelNode = LevelNode(node_data.get('node_pos'), 'locked', self.speed)
            self.node_sprites.add(node_sprite)

    def draw_paths(self) -> None:
        if self.max_level > 0:
            points: list[str] = [node.get('node_pos') for index, node in enumerate(levels.values()) if index <= self.max_level]
            pygame.draw.lines(self.display_surface, '#ffd700', False, points, 20)

    def setup_icon(self) -> None:
        self.icon = pygame.sprite.GroupSingle()
        icon_sprite = Icon(self.node_sprites.sprites()[self.current_level].rect.center)
        self.icon.add(icon_sprite)

    def register_input(self) -> None:
        keys = pygame.key.get_pressed()

        if not self.moving:
            if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.current_level < self.max_level:
                self.move_direction = self.get_movement_data('next')
                self.current_level += 1
                self.moving = True
            elif (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.current_level > 0:
                self.move_direction = self.get_movement_data('previous')
                self.current_level -= 1
                self.moving = True
            elif keys[pygame.K_SPACE] or keys[pygame.K_RETURN]:
                self.create_level(self.current_level)

    def get_movement_data(self, target) -> pygame.math.Vector2:
        start = pygame.math.Vector2(self.node_sprites.sprites()[self.current_level].rect.center)

        if target == 'next':
            end = pygame.math.Vector2(self.node_sprites.sprites()[self.current_level + 1].rect.center)
        else:
            end = pygame.math.Vector2(self.node_sprites.sprites()[self.current_level - 1].rect.center)

        return (end - start).normalize()

    def update_icon_position(self) -> None:
        if self.moving and self.move_direction:
            self.icon.sprite.pos += self.move_direction * self.speed
            target_node = self.node_sprites.sprites()[self.current_level]

            if target_node.detection_zone.collidepoint(self.icon.sprite.pos):
                self.moving = False
                self.move_direction = pygame.math.Vector2(0, 0)

    def run(self):
        # https://stackoverflow.com/questions/28005641/how-to-add-a-background-image-into-pygame
        bg = pygame.image.load('assets/overworld/background.png').convert_alpha()
        self.display_surface.blit(bg, (0, 0))

        self.register_input()
        self.update_icon_position()
        self.icon.update()
        self.draw_paths()
        self.node_sprites.draw(self.display_surface)
        self.icon.draw(self.display_surface)
