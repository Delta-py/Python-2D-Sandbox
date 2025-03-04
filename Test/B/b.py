print("In module products __package__, __name__ ==", __package__, __name__)
from B.C import c
# import math

# modules = ['.', 'Test.', 'B.', 'C.', 'c']

# def convert_to_base_n_recursive(number, base):
# 	if number < base:
# 		return str(number)
# 	else:
# 		return convert_to_base_n_recursive(number // base, base) + str(number % base)

# index = 0
# log_index = 0

# while True:
# 	module_string = ''
# 	module = convert_to_base_n_recursive(index, 5)
# 	for dight in module:
# 		module_string += modules[int(dight)]
# 	try:
# 		__import__(module_string)
# 		print(f'Successfully imported {module_string}')
# 	except Exception as e:
# 		pass
# 	if index != 0 and math.log(index, 5) > log_index + 1:
# 		log_index = int(math.log(index, 5))
# 		print(f'Reached base 5 logarithmic index {log_index}')
# 	index += 1