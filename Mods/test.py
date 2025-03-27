import pygame
from API.template import ModTemplate

class Test(ModTemplate):
	def __init__(self, settings, tools):
		super().__init__(settings, tools)
		self.display = pygame.display.get_surface()

	def draw(self, displacement):
		super().draw(displacement)
		pygame.draw.line(self.display, (0, 0, 0), self.settings.WINDOW_SIZE / 4 + displacement, self.settings.WINDOW_SIZE / 4 * 3 + displacement)
		self.settings.logging.info('drawing test')
