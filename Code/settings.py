from re import DEBUG
from typing import Any
import pickleable_surface.pickleable_surface
import pygame
import os
import math
import sys
import time
import logging
import datetime
import pickleable_surface

log_file = f'Logs\\{datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')}.log'
logger = logging.getLogger(__name__)
logging.basicConfig(filename=log_file, \
					format='%(asctime)s.%(msecs)09d %(levelname)s: %(message)s', datefmt='%m/%d/%Y %H:%M:%S', encoding='utf-8', level=logging.INFO)
terminal = logging.StreamHandler(sys.stdout)
terminal.setLevel(logging.WARN)
logger.addHandler(terminal)

TILE_SIZE = 16
PLAYER_SIZE = pygame.math.Vector2(16, 24)
WINDOW_SIZE = pygame.math.Vector2(16, 9) * 16 * 1.5

get_file_path = lambda *folders: os.path.join('C:\\', *((__file__.split(':')[1]).split('\\')[:-2]), *folders)

def load_texture(filename, type):
	texture = pickleable_surface.pickleable_surface.PickleableSurface(logger, pygame.image.load(get_file_path('Assets', 'Images', type, f'{filename}.png')))#.convert_alpha())
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
		animation_frames.append(pickleable_surface.pickleable_surface.PickleableSurface(logger, textures.subsurface((i * PLAYER_SIZE.x, 0, PLAYER_SIZE.x, PLAYER_SIZE.y))))
	return animation_frames

sign = lambda x: int(x/abs(x)) if x != 0 else 0

CHARACTER_TEXTURES: dict[str, list[pickleable_surface.pickleable_surface.PickleableSurface]] = {
	f'{state.name}'.split('.')[0]: load_character_animation(state.name.split('.')[0]) for state in \
		os.scandir(get_file_path('Assets', 'Images', 'Characters')) if state.name.split('.')[1] =='png'
}

TILE_TEXTURES: dict[str, list[pickleable_surface.pickleable_surface.PickleableSurface]] = {
	'grass': load_tile_animation('grass'),
	'water': load_tile_animation('water')
}

DIRECTIONS: dict[tuple[float, float], str] = {
	(0.0, -1.0): 'b',
	(0.0, 1.0): 'f',
	(-1.0, 0.0): 'l',
	(1.0, 0.0): 'r'
}

PLAYER_SPEED = 128

CHUNK_SIZE = 16
CHUNK_SIZE_SQUARED = CHUNK_SIZE * CHUNK_SIZE

VERSION = 0.1

class Pickleable_Object:
	def __init__(self):
		self.VERSION = VERSION
		self.logger_level = logging.DEBUG

	def __getstate__(self):
		logger.info(f"Pickling Pickleable_Object {self.__class__.__name__}")
		state = self.__dict__.copy()
		if "screen" in state:
			logger.info("Popping screen")
			state.pop("screen")
		return state

	def __setstate__(self, state):
		try:
			if state["logger_level"] > logging.DEBUG:
				logger.info(f"Unpickling Pickleable_Object {self.__class__.__name__}")
				logger.info(self.__class__.__dict__)
			else:
				logger.debug(f"Unpickling Pickleable_Object {self.__class__.__name__}")
				logger.debug(self.__class__.__dict__)
		except Exception as e:
			logger.error(f'{e}')
		if state["VERSION"] != VERSION:
			try:
				if state["logger_level"] > logging.DEBUG:
					logger.warning(f"Older version of Pickleable_Object {self.__class__.__name__}, current VERSION: {VERSION}, VERSION of file: {state["VERSION"]}")
				else:
					logger.debug(f"Older version of Pickleable_Object {self.__class__.__name__}, current VERSION: {VERSION}, VERSION of file: {state["VERSION"]}")
			except Exception as e:
				logger.error(f'{e}')
				logger.info(f"Older version of Pickleable_Object {self.__class__.__name__}, current VERSION: {VERSION}, VERSION of file: {state["VERSION"]}")
		state["screen"] = pygame.display.get_surface()
		self.__dict__.update(state)
