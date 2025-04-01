from settings import *

class Tile(Pickleable_Object):
	def __init__(self):
		super().__init__()
		self.hitbox: pygame.rect.Rect | None
		self.texture: str

	def update(self, delta_time, total_time):
		pass

class Air(Tile):
	def __init__(self):
		super().__init__()
		self.texture = "air"
