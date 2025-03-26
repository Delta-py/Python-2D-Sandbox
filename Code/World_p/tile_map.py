import World_p.chunk
import World_p.Tiles.tile
from settings import *
import World_p

class Tile_Map(Pickleable_Object):
	def __init__(self):
		super().__init__()
		self.screen = pygame.display.get_surface()
		self.logger_level = logging.INFO
		self.chunks: dict[tuple[int, int], World_p.chunk.Chunk] = {}
		self.chunks[(0, 0)] = World_p.chunk.Chunk((0, 0))
		self.chunks[(1, 0)] = World_p.chunk.Chunk((1, 0))

	def update(self, delta_time, total_time):
		for chunk in self.chunks.values():
			chunk.update(delta_time, total_time)

	def get_visible_chunks(self, displacement: pygame.Vector2):
		return [chunk for chunk in self.chunks.values() if displacement.x - WINDOW_SIZE.x <= -chunk.id[0] * CHUNK_SIZE * TILE_SIZE <= displacement.x + CHUNK_SIZE * TILE_SIZE and \
															displacement.y - WINDOW_SIZE.y <= -chunk.id[1] * CHUNK_SIZE * TILE_SIZE <= displacement.y + CHUNK_SIZE * TILE_SIZE]

	def draw(self, displacement: pygame.Vector2):
		for chunk in self.get_visible_chunks(displacement):
			chunk.draw(*displacement)
