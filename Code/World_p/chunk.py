
from settings import *
import World_p
import World_p.Tiles.grass

class Chunk(Pickleable_Object):
	def __init__(self, id):
		super().__init__()
		self.screen = pygame.display.get_surface()
		self.tiles = [World_p.Tiles.grass.Grass_Tile() for _ in range(CHUNK_SIZE_SQUARED)]
		self.id: tuple[int, int] = id

	def update(self, delta_time, total_time):
		self.delta_time = delta_time
		self.total_time = total_time
		for tile in self.tiles:
			tile.update(delta_time, total_time)

	def draw(self, dx, dy):
		for pos, tile in enumerate(self.tiles):
			self.screen.blit(TILE_TEXTURES[tile.texture][int(self.total_time * 4) % 4], (dx + self.id[0] * TILE_SIZE * CHUNK_SIZE + int(pos / CHUNK_SIZE) * TILE_SIZE, dy + self.id[1] * TILE_SIZE * CHUNK_SIZE + pos % CHUNK_SIZE * TILE_SIZE))
			logger.debug(f'CHUNK ({self.id}): drawing tile {tile.texture}')
