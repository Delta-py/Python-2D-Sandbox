import pygame

class Entity:
	def __init__(self):
		self.display = pygame.display.get_surface()
		self.position = pygame.math.Vector2(0, 0)
		self.direction = pygame.math.Vector2(0, 1)
		self.velocity = 0
		self.hitbox: pygame.rect

	def update(self, delta_time, total_time):
		pass

	def draw(self):
		pass
