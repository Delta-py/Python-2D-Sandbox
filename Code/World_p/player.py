from settings import *
from entity import Entity
import keyboard_layout
import copy

class Player(Entity):
	def __init__(self):
		super().__init__()
		self.VERSION = VERSION
		self.logger_level = logging.INFO
		self.texture = CHARACTER_TEXTURES['idle_f']
		self.keyboard: keyboard_layout.Keyboard
		self.keyboard_loaded = False

		self.accelerate = False

		self.action = 'idle'
		self.animation_direction = (0, 1)

	def handle_events(self):
		self.accelerate = False
		self.direction = pygame.math.Vector2(0, 0)
		events = pygame.key.get_pressed()
		if events[self.keyboard[keyboard_layout.Key.w]]:
			self.direction.y = -1
			self.accelerate = True
		elif events[self.keyboard[keyboard_layout.Key.s]]:
			self.direction.y = 1
			self.accelerate = True
		if events[self.keyboard[keyboard_layout.Key.a]]:
			self.direction.x = -1
			self.accelerate = True
		elif events[self.keyboard[keyboard_layout.Key.d]]:
			self.direction.x = 1
			self.accelerate = True

	def update_velocity(self, delta_time):
		self.handle_events()
		self.velocity = min(self.velocity, PLAYER_SPEED)
		if self.accelerate:
			self.velocity += (1 * PLAYER_SPEED - self.velocity) / 0.05 * delta_time
		else:
			self.velocity /= 1.5
		if abs(self.direction.y) > 0.2 and abs(self.direction.x) > 0.2:
			self.position.y = int(self.position.y) + (self.position.x - int(self.position.x)) * sign(self.position.x * self.position.y)
		temp = copy.copy(self.direction)
		try: temp.scale_to_length(delta_time * self.velocity)
		except ValueError: temp = pygame.math.Vector2(0, 0)
		self.position += temp

	def update(self, delta_time, total_time):
		if not self.keyboard_loaded:
			self.keyboard = keyboard_layout.Keyboard()
			self.keyboard_loaded = True
		super().update(delta_time, total_time)
		self.update_velocity(delta_time)

		self.animation_direction = temp if (temp := (0.0 if abs(self.direction.y) > abs(self.direction.x) * 1.05 else sign(self.direction.x), \
											   		 0.0 if abs(self.direction.y) < abs(self.direction.x) * 1.05 else sign(self.direction.y))) != (0, 0) else self.animation_direction
		self.texture = CHARACTER_TEXTURES[f"{self.action}_{DIRECTIONS[self.animation_direction]}"]
		self.animation_time = int(total_time * 4)
		logging.info(f'Action: {self.action} Velocity, Direction: {self.velocity, self.direction}')

	def draw(self, displacement):
		super().draw(displacement)
		self.screen.blit(self.texture[self.animation_time % len(self.texture)], self.position + displacement)
		pygame.draw.line(self.screen, (255, 0, 0), self.position + displacement, self.position + self.velocity * self.direction + displacement)
