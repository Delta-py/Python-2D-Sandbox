
import World_p.Tiles.tile
import World_p.Tiles.wood
from settings import *
import World_p
import World_p.Tiles.grass

class Chunk(Pickleable_Object):
	def __init__(self, id, level):
		super().__init__()
		self.screen = pygame.display.get_surface()
		self.level = level
		self.tiles = [World_p.Tiles.grass.Grass_Tile() if self.level == 0 \
														else World_p.Tiles.wood.Wooden_Board_Tile() \
															if pos in [0,                               1, 2,                  3,                  4,
																	 CHUNK_SIZE,                                                CHUNK_SIZE     + 4,
																	 CHUNK_SIZE * 2,                                            CHUNK_SIZE * 2 + 4,
																	 CHUNK_SIZE * 3,                                            CHUNK_SIZE * 3 + 4,

																	 CHUNK_SIZE * 4, CHUNK_SIZE * 4 + 1,    CHUNK_SIZE * 4 + 3, CHUNK_SIZE * 4 + 4]
													   else World_p.Tiles.tile.Air() for pos in range(CHUNK_SIZE_SQUARED)]
		self.id: tuple[int, int] = id

	def update(self, delta_time, total_time):
		self.delta_time = delta_time
		self.total_time = total_time
		for tile in self.tiles:
			tile.update(delta_time, total_time)

	def draw(self, level, render_in_front_of_player, player_y_pos, dx, dy):
		for pos, tile in enumerate(self.tiles):
			if not render_in_front_of_player * ((level == 1) - (self.id[1] * CHUNK_SIZE * TILE_SIZE + TILE_SIZE * 2 + int(pos / CHUNK_SIZE) * TILE_SIZE > player_y_pos + PLAYER_SIZE.y)):
				logger.debug(f'CHUNK ({self.id}): drawing tile {tile.texture} at {(self.id[0] * CHUNK_SIZE + pos % CHUNK_SIZE) * TILE_SIZE,
																				(self.id[1] * CHUNK_SIZE + int(pos / CHUNK_SIZE)) * TILE_SIZE}')
				self.screen.blit(TILE_TEXTURES[tile.texture][int(self.total_time * len(TILE_TEXTURES[tile.texture])) % len(TILE_TEXTURES[tile.texture])],
						((dx + self.id[0] * TILE_SIZE * CHUNK_SIZE + (pos % CHUNK_SIZE) * TILE_SIZE),
						dy + self.id[1] * TILE_SIZE * CHUNK_SIZE + int(pos / CHUNK_SIZE) * TILE_SIZE))
