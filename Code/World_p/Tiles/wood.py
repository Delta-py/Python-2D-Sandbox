import World_p.Tiles
import World_p.Tiles.tile

class Wooden_Board_Tile(World_p.Tiles.tile.Tile):
	def __init__(self):
		super().__init__()
		self.texture = "wood_boards"
