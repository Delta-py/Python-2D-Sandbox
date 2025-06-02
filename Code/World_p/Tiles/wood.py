from settings import *
import World_p.Tiles
import World_p.Tiles.tile

class Wooden_Board_Tile(World_p.Tiles.tile.Tile):
	def __init__(self, position):
		super().__init__()
		self.texture = 'wood_boards'
		self.hitbox = pygame.Rect(position, (TILE_SIZE, TILE_SIZE))
