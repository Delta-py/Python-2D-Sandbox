import World_p.player
import World_p.tile_map
from settings import *
import World_p

class World(Pickleable_Object):
	def __init__(self):
		super().__init__()
		self.screen = pygame.display.get_surface()
		self.logger_level = logging.INFO

		self.player = World_p.player.Player()
		self.tile_map = World_p.tile_map.Tile_Map()

		self.displacement = pygame.Vector2(0, 0)

	def update(self, delta_time, total_time):
		self.tile_map.update(delta_time, total_time)
		self.player.update(delta_time, total_time)
		self.displacement = pygame.Vector2(WINDOW_SIZE / 2, WINDOW_SIZE / 2) - self.player.position

	def draw(self):
		for object in sorted([self.player.draw(self.displacement), *[x for xs in self.tile_map.draw(self.displacement) for x in xs]], \
						key=lambda object: object.level * abs(1 + self.displacement.y) * 1000 + object.y_position):
			object.render()
