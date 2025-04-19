import pickle
import cProfile
from settings import *
from World_p.world import World
from Mods_p.mod_loader import load_mods
from Menus_p.tkinter_menu import Setting_Menu

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
		pygame.draw.line(self.screen, (255, 0, 0), (WINDOW_SIZE.x, 0), WINDOW_SIZE)
		pygame.draw.line(self.screen, (255, 0, 0), (0, WINDOW_SIZE.y), WINDOW_SIZE)
		pygame.display.update()

	def pickle(self, save_name = 'world'):
		with open(get_file_path('Worlds', f'{save_name}.plk'), 'wb') as file:
			logger.info("Pickling save")
			pickle.dump(self.world, file)

	def unpickle(self, save_name = 'world'):
		with open(get_file_path('Worlds', f'{save_name}.plk'), 'rb') as file:
			logger.info("Unpickling save")
			self.world = pickle.load(file)

	def handle_event(self, event):
		if event.type == pygame.QUIT:
			self.running = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				settings = Setting_Menu(self.pickle, self.unpickle).run()
				if settings != None:
					self.world.player.keyboard.set_up_keys(settings[0])


	def run(self):
		self.running = True
		while self.running:
			self.clock.tick(pygame.display.get_current_refresh_rate())
			delta_time = (self.clock.get_time() / 1000)
			total_time = time.time()
			for event in pygame.event.get():
				self.handle_event(event)
				self.mods.handle_event(event)
			self.update(delta_time, total_time)
			self.draw()
		pygame.quit()

if __name__ == "__main__":
	logger.critical(f'Logging in {log_file}')
	game = Game()
	with open(log_file, 'a') as sys.stdout:
		cProfile.run('game.run()', sort='cumtime')
