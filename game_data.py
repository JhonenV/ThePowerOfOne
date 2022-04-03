from settings import game_height, game_width

level_2 = {'node_pos': (450, (game_height / 2)), 'content': 'this is level 2', 'unlock': 2}
level_3 = {'node_pos': (750, (game_height / 2)), 'content': 'this is level 3', 'unlock': 3}
level_4 = {'node_pos': (1050, (game_height / 2)), 'content': 'this is level 4', 'unlock': 3}

level_1_base_path = "assets/levels/level_1/level/"
level_1 = {
    'terrain': level_1_base_path + 'level_1_outside_terrain.csv',
    'grass': level_1_base_path + 'level_1_grass.csv',
    'sky': level_1_base_path + 'level_1_sky.csv',
    'tree': level_1_base_path + 'level_1_trees.csv',
    'house': level_1_base_path + 'level_1_house.csv',
    'flower': level_1_base_path + 'level_1_flowers.csv',
    'enemies': level_1_base_path + 'level_1_enemy.csv',
    'constraints': level_1_base_path + 'level_1_constraints.csv',
    'player': level_1_base_path + 'level_1_player.csv',
    'node_pos': (150, game_height / 2),
    'background_color': 'cyan',
    'unlock': 1
}

levels = {
    0: level_1,
    1: level_2,
    2: level_3,
    3: level_4
}
