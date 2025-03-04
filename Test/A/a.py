import importlib.util
import sys
import os
print(__file__)
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)
print(__file__)
from B import b
print(b.__name__, b.__package__)

def importfile(module_name, file_path):
	spec = importlib.util.spec_from_file_location(module_name, file_path)
	module = importlib.util.module_from_spec(spec)
	sys.modules[module_name] = module
	spec.loader.exec_module(module)
	return module

b_ = importlib.import_module('B.b')