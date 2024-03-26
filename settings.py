import pygame

# Game size
collumns = 10
rows = 20
cell_size = 40
game_width, game_height = collumns * cell_size, rows * cell_size

# Side bar size
sidebar_width = 200
preview_height = 0.7
score_height = 1 - preview_height

# Window
padding = 20
window_width = game_width + sidebar_width + padding * 3
window_height = game_height + padding * 2

# Game behaviour
update_start_speed = 800
move_wait_time = 200
rotate_wait_time = 200
block_offset = pygame.Vector2(collumns // 2, -1)

# Colour
yellow = '#f1e60d'
red = '#e51b20'
blue = '#204b9b'
green = '#65b32e'
purple = '#7b217f'
cyan = '#6cc6d9'
orange = '#f07e13'
gray = '#1C1C1C'
line_colour = '#000000'

# Shapes
tetrominos = {
	'T': {'shape': [(0,0), (-1,0), (1,0), (0,-1)], 'colour': purple},
	'O': {'shape': [(0,0), (0,-1), (1,0), (1,-1)], 'colour': yellow},
	'J': {'shape': [(0,0), (0,-1), (0,1), (-1,1)], 'colour': blue},
	'L': {'shape': [(0,0), (0,-1), (0,1), (1,1)], 'colour': orange},
	'I': {'shape': [(0,0), (0,-1), (0,-2), (0,1)], 'colour': cyan},
	'S': {'shape': [(0,0), (-1,0), (0,-1), (1,-1)], 'colour': green},
	'Z': {'shape': [(0,0), (1,0), (0,-1), (-1,-1)], 'colour': red}
}

# Score
score_data = {1: 40, 2: 100, 3: 300, 4: 1200}