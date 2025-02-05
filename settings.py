from pydoc import text
import pygame
import os

WINDOW_SIZE = pygame.math.Vector2(16, 9) * 32

def load_texture(filename, type):
	texture = pygame.image.load(os.path.join('C:\\', *((__file__.split(':')[1]).split('\\')[:-1]), 'Assets', 'Images', type, f'{filename}.png'))
	return texture

def load_tile_animation(tile):
	texture = load_texture(tile, 'Tiles')
	animation_frames = []
	for i in range(int(texture.get_width() / texture.get_height())):
		animation_frames.append(texture.subsurface((i * texture.get_height(), 0, texture.get_height(), texture.get_height())))
	return animation_frames

TEXTURES: dict[str, list[pygame.Surface]] = {
	'grass': load_tile_animation('grass'),
	'water': load_tile_animation('water')
}
