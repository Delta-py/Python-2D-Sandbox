class ModTemplate:
	def __init__(self, settings, tools):
		self.settings = settings
		self.tools = tools
		self.debug: bool

	def on_init(self, app):
		self.app = app

	def handle_event(self, event):
		pass

	def update(self, delta_time, total_time, debug):
		self.debug = debug

	def draw(self, displacement):
		pass
