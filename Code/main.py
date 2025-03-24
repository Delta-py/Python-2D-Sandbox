import dill
from settings import *
from World_p.world import World
from Mods_p.mod_loader import load_mods

class Game(Pickleable_Object):
	def __init__(self):
		pygame.init()
		pygame.display.set_mode(WINDOW_SIZE, pygame.RESIZABLE | pygame.SCALED)

		self.screen = pygame.display.get_surface()
		self.clock = pygame.time.Clock()
		self.clock.tick()
		time.sleep(0.1)

		self.world = World()
		self.mods = load_mods()

		self.mods.on_init(self)

	def update(self, delta_time, total_time):
		self.world.update(delta_time, total_time)
		self.mods.update(delta_time, total_time)
		pygame.display.set_caption(f'{1 / delta_time}')

	def draw(self):
		self.screen.fill((0, 0, 0))
		pygame.draw.line(self.screen, (0, 0, 0), (0, WINDOW_SIZE.y / 2), (WINDOW_SIZE.x, WINDOW_SIZE.y / 2))
		pygame.draw.line(self.screen, (0, 0, 0), (WINDOW_SIZE.x / 2, 0), (WINDOW_SIZE.x / 2, WINDOW_SIZE.y))
		self.world.draw()
		self.mods.draw(self.world.displacement)
		pygame.display.update()

	def run(self):
		running = True
		while running:
			self.clock.tick(pygame.display.get_current_refresh_rate())
			delta_time = (self.clock.get_time() / 1000)
			total_time = time.time()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_s:
						with open(get_file_path('Worlds', 'world.plk'), 'wb') as file:
							logger.info("Saving save")
							dill.dump(self.world, file)
					if event.key == pygame.K_l:
						with open(get_file_path('Worlds', 'world.plk'), 'rb') as file:
							logger.info("Loading save")
							self.world = dill.load(file)
				self.mods.handle_event(event)
			self.update(delta_time, total_time)
			self.draw()
		pygame.quit()

if __name__ == "__main__":
	print(f'Log at {get_file_path(log_file)}')
	game = Game()
	game.run()
