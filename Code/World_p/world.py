import World_p.player
import World_p.tile_map
from settings import *
import World_p

class World(Pickleable_Object):
	def __init__(self):
		super().__init__()
		self.screen = pygame.display.get_surface()
		self.player = World_p.player.Player()
		self.tile_map = World_p.tile_map.Tile_Map()

		self.displacement = pygame.Vector2(0, 0)

	def update(self, delta_time, total_time):
		self.tile_map.update(delta_time, total_time)
		self.player.update(delta_time, total_time)
		self.displacement = pygame.Vector2(WINDOW_SIZE / 2, WINDOW_SIZE / 2) - self.player.position

	def draw(self):
		self.tile_map.draw(self.displacement)
		self.player.draw(self.displacement)
