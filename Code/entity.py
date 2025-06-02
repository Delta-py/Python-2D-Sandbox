from settings import *

class Entity(Pickleable_Object):
	def __init__(self):
		super().__init__()
		self.screen = pygame.display.get_surface()
		self.position = pygame.math.Vector2(0, 0)
		self.direction = pygame.math.Vector2(0, 1)
		self.velocity = 0
		self.hitbox: pygame.Rect
		self.debug: bool

	def update(self, delta_time, total_time, debug):
		self.debug = debug

	def draw(self, displacement):
		pass
