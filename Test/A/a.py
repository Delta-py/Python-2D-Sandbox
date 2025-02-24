import importlib.util
import importlib._bootstrap
import importlib._bootstrap_external
import os

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

b = importfile(os.path.join('C:\\', *((__file__.split(':')[1]).split('\\')[:-2]), 'B', 'b.py'))