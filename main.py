import pygame
import time
from settings import *

class Game:
	def __init__(self):
		pygame.init()
		pygame.display.set_mode(WINDOW_SIZE, pygame.RESIZABLE | pygame.SCALED)

		self.screen = pygame.display.get_surface()
		self.clock = pygame.time.Clock()

	def draw(self, delta_time, total_time):
		self.screen.fill((0, 0, 0))
		for x in range(0, int(WINDOW_SIZE.x), TEXTURES['grass'][0].get_width()):
				for y in range(0, int(WINDOW_SIZE.y), TEXTURES['grass'][0].get_height()):
					self.screen.blit(TEXTURES['grass'][int(total_time) % len(TEXTURES['grass'])], (x, y))
		pygame.display.update()

	def run(self):
		running = True
		while running:
			delta_time = self.clock.tick(pygame.display.get_current_refresh_rate())
			total_time = time.gmtime().tm_sec
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
			self.draw(delta_time, total_time)
		pygame.quit()

if __name__ == "__main__":
	game = Game()
	game.run()
