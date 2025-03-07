import pygame
from API.template import ModTemplate

class Test(ModTemplate):
	def __init__(self, settings, tools):
		super().__init__(settings, tools)
		self.display = pygame.display.get_surface()

	def draw(self):
		pygame.draw.line(self.display, (0, 0, 0), self.settings.WINDOW_SIZE / 4, self.settings.WINDOW_SIZE / 4 * 3)
		self.settings.logging.info('drawing test')
