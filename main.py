import pygame
from settings import *
from player import Player

class Game:
	def __init__(self):
		pygame.init()
		pygame.display.set_mode(WINDOW_SIZE, pygame.RESIZABLE | pygame.SCALED)

		self.screen = pygame.display.get_surface()
		self.clock = pygame.time.Clock()
		self.clock.tick()
		time.sleep(0.1)

		self.player = Player()

	def update(self, delta_time, total_time):
		self.player.update(delta_time, total_time)

	def draw(self, delta_time, total_time):
		self.screen.fill((0, 0, 0))
		for x in range(0, int(WINDOW_SIZE.x), TILE_TEXTURES['grass'][0].get_width()):
				for y in range(0, int(WINDOW_SIZE.y), TILE_TEXTURES['grass'][0].get_height()):
					self.screen.blit(TILE_TEXTURES['grass'][int(total_time * 2) % len(TILE_TEXTURES['grass'])], (x, y))
		pygame.draw.line(self.screen, (0, 0, 0), (0, WINDOW_SIZE.y / 2), (WINDOW_SIZE.x, WINDOW_SIZE.y / 2))
		pygame.draw.line(self.screen, (0, 0, 0), (WINDOW_SIZE.x / 2, 0), (WINDOW_SIZE.x / 2, WINDOW_SIZE.y))
		self.player.draw(total_time)
		pygame.display.update()

	def run(self):
		running = True
		while running:
			self.clock.tick(pygame.display.get_current_refresh_rate())
			delta_time = self.clock.get_time() / 1000
			total_time = time.time()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
			self.update(delta_time, total_time)
			self.draw(delta_time, total_time)
		pygame.quit()

if __name__ == "__main__":
	game = Game()
	game.run()
