from settings import *

class Tile(Pickleable_Object):
	def __init__(self):
		super().__init__()
		self.hitbox: pygame.rect.Rect | None = None
		self.texture: str
		self.debug: bool

	def update(self, delta_time, total_time, debug):
		self.debug = debug

class Air(Tile):
	def __init__(self):
		super().__init__()
		self.texture = "air"
