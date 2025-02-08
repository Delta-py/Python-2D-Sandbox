import pygame
import os

WINDOW_SIZE = pygame.math.Vector2(16, 9) * 16
PLAYER_SIZE = pygame.math.Vector2(16, 24)

def load_texture(filename, type):
	texture = pygame.image.load(os.path.join('C:\\', *((__file__.split(':')[1]).split('\\')[:-1]), 'Assets', 'Images', type, f'{filename}.png'))
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

CHARACTER_TEXTURES: dict[str, list[pygame.Surface]] = {
	f'{state.name}'.split('.')[0]: load_character_animation(state.name.split('.')[0]) for state in \
		os.scandir(os.path.join('C:\\', *((__file__.split(':')[1]).split('\\')[:-1]), 'Assets', 'Images', 'Characters')) if state.name.split('.')[1] =='png'
}

TILE_TEXTURES: dict[str, list[pygame.Surface]] = {
	'grass': load_tile_animation('grass'),
	'water': load_tile_animation('water')
}
