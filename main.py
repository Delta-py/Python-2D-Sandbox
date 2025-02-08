import pygame
import time
from settings import *

class Player:
	def __init__(self):
		self.position = pygame.math.Vector2(0, 100)
		self.texture = CHARACTER_TEXTURES['idle_f']
		self.display = pygame.display.get_surface()

	def update(self, delta_time):
		self.position.x += delta_time

	def draw(self, total_time):
		self.display.blit(self.texture[int(total_time * 4) % len(self.texture)], self.position)

class Game:
	def __init__(self):
		pygame.init()
		pygame.display.set_mode(WINDOW_SIZE, pygame.RESIZABLE | pygame.SCALED)

		self.screen = pygame.display.get_surface()
		self.clock = pygame.time.Clock()

		self.player = Player()

	def update(self, delta_time):
		self.player.update(delta_time)

	def draw(self, delta_time, total_time):
		self.screen.fill((0, 0, 0))
		for x in range(0, int(WINDOW_SIZE.x), TILE_TEXTURES['grass'][0].get_width()):
				for y in range(0, int(WINDOW_SIZE.y), TILE_TEXTURES['grass'][0].get_height()):
					self.screen.blit(TILE_TEXTURES['grass'][int(total_time * 2) % len(TILE_TEXTURES['grass'])], (x, y))
		self.player.draw(total_time)
		pygame.display.update()

	def run(self):
		running = True
		while running:
			delta_time = 1 / self.clock.tick(pygame.display.get_current_refresh_rate())
			total_time = time.time()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
			self.update(delta_time)
			self.draw(delta_time, total_time)
		pygame.quit()

if __name__ == "__main__":
	game = Game()
	game.run()
