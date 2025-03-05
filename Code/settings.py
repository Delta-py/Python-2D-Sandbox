import pygame
import os
import math
import time
import logging
import datetime

logger = logging.getLogger(__name__)
logging.basicConfig(filename=f'Logs/{datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')}.log', \
					format='%(asctime)s.%(msecs)06d %(levelname)s: %(message)s', datefmt='%m/%d/%Y %H:%M:%S', encoding='utf-8', level=logging.DEBUG)

TILE_SIZE = 16
PLAYER_SIZE = pygame.math.Vector2(16, 24)
WINDOW_SIZE = pygame.math.Vector2(16, 9) * 16

get_file_path = lambda *folders: os.path.join('C:\\', *((__file__.split(':')[1]).split('\\')[:-2]), *folders)

def load_texture(filename, type):
	texture = pygame.image.load(get_file_path('Assets', 'Images', type, f'{filename}.png'))
	return texture

def load_tile_animation(tile):
	texture = load_texture(tile, 'Tiles')
	animation_frames = []
	for i in range(int(texture.get_width() / texture.get_height())):
		animation_frames.append(texture.subsurface((i * texture.get_height(), 0, texture.get_height(), texture.get_height())))
	return animation_frames

def load_character_animation(state):
	textures = load_texture(state, 'Characters')
	animation_frames = []
	for i in range(int((pygame.Vector2(textures.get_width(), textures.get_height()) / PLAYER_SIZE.x).x)):
		animation_frames.append(textures.subsurface((i * PLAYER_SIZE.x, 0, PLAYER_SIZE.x, PLAYER_SIZE.y)))
	return animation_frames

sign = lambda x: int(x/abs(x)) if x != 0 else 0

CHARACTER_TEXTURES: dict[str, list[pygame.Surface]] = {
	f'{state.name}'.split('.')[0]: load_character_animation(state.name.split('.')[0]) for state in \
		os.scandir(get_file_path('Assets', 'Images', 'Characters')) if state.name.split('.')[1] =='png'
}

TILE_TEXTURES: dict[str, list[pygame.Surface]] = {
	'grass': load_tile_animation('grass'),
	'water': load_tile_animation('water')
}

DIRECTIONS: dict[tuple[float, float], str] = {
	(0.0, -1.0): 'b',
    (0.0, 1.0): 'f',
    (-1.0, 0.0): 'l',
    (1.0, 0.0): 'r'
}

PLAYER_SPEED = 16
