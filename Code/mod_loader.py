import settings
import inspect
import os
import sys
from settings import *
import importlib.util
import importlib._bootstrap
import importlib._bootstrap_external

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)

from Mods.API.template import ModTemplate

def importfile(path):
	"""Import a Python source file or compiled file given its path."""
	magic = importlib.util.MAGIC_NUMBER
	with open(path, 'rb') as file:
		is_bytecode = magic == file.read(len(magic))
	filename = os.path.basename(path)
	name, ext = os.path.splitext(filename)
	if is_bytecode:
		loader = importlib._bootstrap_external.SourcelessFileLoader(name, path)
	else:
		loader = importlib._bootstrap_external.SourceFileLoader(name, path)
	# XXX We probably don't need to pass in the loader here.
	spec = importlib.util.spec_from_file_location(name, path, loader=loader)
	try:
		return importlib._bootstrap._load(spec)
	except Exception as err:
		print(f"Error importing {filename}: {err}")


class Mods(ModTemplate):
	def __init__(self, settings, mods, mod_names):
		super().__init__(settings)
		self.mods = {}
		self.mod_names = mod_names
		mods = mods
		for index, mod in enumerate(mods):
			self.mods[f'{index}_{mod_names[index]}'] = mod(settings)

	def on_init(self, app):
		super().on_init(app)
		for mod in self.mods.keys():
			self.mods[mod].on_init(app)

	def handle_event(self, event):
		super().handle_event(event)
		for mod in self.mods.keys():
			self.mods[mod].handle_event(event)

	def update(self, delta_time, total_time):
		super().update(delta_time, total_time)
		for mod in self.mods.keys():
			self.mods[mod].update(delta_time, total_time)

	def draw(self):
		super().draw()
		for mod in self.mods.keys():
			self.mods[mod].draw()
		print('Mods drawing finished')

def load_mods() -> Mods:
	mods = []
	mod_names = []
	for file in os.scandir(get_file_path('Mods')):
		if file.is_file() and file.name.split('.')[1] =='py':
			mod_module = importfile(file.path)
			for member_name, member in inspect.getmembers(mod_module):
				print(member_name)
				if inspect.isclass(member) and member.__bases__.__contains__(ModTemplate):
					mods.append(member)
					mod_names.append(member_name)
					print('Module loaded')
	return Mods(settings, mods, mod_names) if mods else ModTemplate(settings)
