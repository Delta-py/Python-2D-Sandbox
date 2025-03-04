import pygame
from Mods.API.template import ModTemplate

class Test(ModTemplate):
	def __init__(self, settings):
		super().__init__(settings)
		self.display = pygame.display.get_surface()

	def draw(self):
		pygame.draw.line(self.display, (0, 0, 0), self.settings.WINDOW_SIZE / 4, self.settings.WINDOW_SIZE / 4 * 3)
		print('drawing test')
