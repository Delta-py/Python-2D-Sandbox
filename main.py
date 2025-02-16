import copy
import math
import pygame
import time
from settings import *
import keyboard_layout

class Player:
	def __init__(self):
		self.display = pygame.display.get_surface()
		self.texture = CHARACTER_TEXTURES['idle_f']
		self.keyboard = keyboard_layout.Keyboard()

		self.position = pygame.math.Vector2(0, 0)
		self.direction = pygame.math.Vector2(0, 1)
		self.velocity = 0
		self.action = 'idle'

		self.accelerate = False

	def handle_events(self, delta_time):
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

	def update(self, delta_time, total_time):
		self.handle_events(delta_time)
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
		print(f'{self.action}_{self.velocity, self.direction, temp}')
		self.position += temp

	def draw(self, total_time):
		self.display.blit(self.texture[int(total_time * 4) % len(self.texture)], self.position + WINDOW_SIZE / 2)
		pygame.draw.line(self.display, (255, 0, 0), self.position + WINDOW_SIZE / 2, self.position + self.velocity * self.direction + WINDOW_SIZE / 2)

class Game:
	def __init__(self):
		pygame.init()
		pygame.display.set_mode(WINDOW_SIZE, pygame.RESIZABLE | pygame.SCALED)

		self.screen = pygame.display.get_surface()
		self.clock = pygame.time.Clock()
		self.clock.tick()
		time.sleep(0.1)

		self.player = Player()

	def update(self, delta_time, total_time):
		self.player.update(delta_time, total_time)

	def draw(self, delta_time, total_time):
		self.screen.fill((0, 0, 0))
		for x in range(0, int(WINDOW_SIZE.x), TILE_TEXTURES['grass'][0].get_width()):
				for y in range(0, int(WINDOW_SIZE.y), TILE_TEXTURES['grass'][0].get_height()):
					self.screen.blit(TILE_TEXTURES['grass'][int(total_time * 2) % len(TILE_TEXTURES['grass'])], (x, y))
		pygame.draw.line(self.screen, (0, 0, 0), (0, WINDOW_SIZE.y / 2), (WINDOW_SIZE.x, WINDOW_SIZE.y / 2))
		pygame.draw.line(self.screen, (0, 0, 0), (WINDOW_SIZE.x / 2, 0), (WINDOW_SIZE.x / 2, WINDOW_SIZE.y))
		self.player.draw(total_time)
		pygame.display.update()

	def run(self):
		running = True
		while running:
			self.clock.tick(pygame.display.get_current_refresh_rate())
			delta_time = self.clock.get_time() / 1000
			total_time = time.time()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
			self.update(delta_time, total_time)
			self.draw(delta_time, total_time)
		pygame.quit()

if __name__ == "__main__":
	game = Game()
	game.run()
