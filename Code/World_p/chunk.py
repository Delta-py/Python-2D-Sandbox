
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
														else (World_p.Tiles.wood.Wooden_Board_Tile() \
															if pos in [0,                             1, 2,                  3,                  4,
																	 CHUNK_SIZE,                                                CHUNK_SIZE     + 4,
																	 CHUNK_SIZE * 2,                                            CHUNK_SIZE * 2 + 4,
																	 CHUNK_SIZE * 3,                                            CHUNK_SIZE * 3 + 4,
																	 CHUNK_SIZE * 4, CHUNK_SIZE * 4 + 1,    CHUNK_SIZE * 4 + 3, CHUNK_SIZE * 4 + 4]
													   else World_p.Tiles.tile.Air()) for pos in range(CHUNK_SIZE_SQUARED)]
		self.id: tuple[int, int] = id

	def update(self, delta_time, total_time):
		self.delta_time = delta_time
		self.total_time = total_time
		for tile in self.tiles:
			tile.update(delta_time, total_time)

	def draw(self, displacement):
		render_objects = []
		for pos, tile in enumerate(self.tiles):
			if tile.texture != 'air':
				render_object = Render_Object(self.level, TILE_SIZE * (CHUNK_SIZE * self.id[1] + pos // CHUNK_SIZE - 1))
				def render(pos = pos, tile = tile):
					self.screen.blit(TILE_TEXTURES[tile.texture][int(self.total_time) % len(TILE_TEXTURES[tile.texture])], \
						TILE_SIZE * pygame.Vector2(CHUNK_SIZE * self.id[0] + pos % CHUNK_SIZE, CHUNK_SIZE * self.id[1] + pos // CHUNK_SIZE - 1) + displacement)
					#logger.debug(f'Rendering tile {tile.__class__} with pos:{pos} and level: {self.level} at {TILE_SIZE * pygame.Vector2(CHUNK_SIZE * self.id[0] + pos % CHUNK_SIZE, CHUNK_SIZE * self.id[1] + pos // CHUNK_SIZE)}')
				render_object.render = render
				render_objects.append(render_object)
		return render_objects

