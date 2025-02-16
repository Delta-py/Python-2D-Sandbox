import enum
import pygame
import tkinter.simpledialog

class Key(enum.Enum):
	w = 0
	a = 1
	s = 2
	d = 3

class Keyboard:
	def __init__(self):
		wasd = tkinter.simpledialog.askstring('Pygame window', 'Type wasd or your preferred controls.')
		self.w = pygame.key.key_code(wasd[int(Key.w.value)])
		self.a = pygame.key.key_code(wasd[int(Key.a.value)])
		self.s = pygame.key.key_code(wasd[int(Key.s.value)])
		self.d = pygame.key.key_code(wasd[int(Key.d.value)])

	def __getitem__(self, index):
		if index == Key.w:
			return self.w
		elif index == Key.a:
			return self.a
		elif index == Key.s:
			return self.s
		elif index == Key.d:
			return self.d
		return None
