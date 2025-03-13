import World_p.player
from settings import *
import World_p

class World(Pickleable_Object):
	def __init__(self):
		super().__init__()
		self.screen = pygame.display.get_surface()
		self.player = World_p.player.Player()

	def update(self, delta_time, total_time):
		self.player.update(delta_time, total_time)

	def draw(self):
		self.player.draw()
