import tkinter.simpledialog
from settings import *
import tkinter
import tkinter.ttk

class Setting_Menu(tkinter.Tk):
	def __init__(self, pickle_world, unpickle_world, baseName = None, className = "Tk", useTk = True, sync = False, use = None):
		super().__init__('Settings', baseName, className, useTk, sync, use)

		self.style = tkinter.ttk.Style(self)
		self.style.configure('TSeparator', background='black')

		self.left_frame = tkinter.ttk.Frame(self)
		self.left_frame.pack(side=tkinter.LEFT, fill=tkinter.BOTH)

		self.separator = tkinter.ttk.Separator(self, orient=tkinter.HORIZONTAL)
		self.separator.pack(side=tkinter.LEFT, fill=tkinter.Y, padx=5)

		self.right_frame = tkinter.ttk.Frame(self)
		self.right_frame.pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=True)

		self.group = tkinter.Listbox(self.left_frame)
		self.group.pack(expand=True, fill='both', padx=4, pady=4)

		self.label_1 = tkinter.ttk.Label(self.right_frame, font=('Segoe UI', 32), text='Settings')
		self.label_1.grid(pady=4, columnspan=2, sticky='W')

		self.label_2 = tkinter.ttk.Label(self.right_frame, text='Controls:')
		self.label_2.grid(pady=4, row=1, sticky='W')

		self.text = tkinter.StringVar(self.right_frame, value='WASD')
		self.text_input = tkinter.ttk.Entry(self.right_frame, textvariable=self.text)
		self.text_input.grid(pady=4, column=1, row=1, sticky='W')

		self.button_save_game = tkinter.ttk.Button(self.right_frame, text='Pickle World', command=lambda: self.pickle_world(pickle_world))
		self.button_save_game.grid(pady=4, row=2, sticky='W')

		self.button_save_game = tkinter.ttk.Button(self.right_frame, text='Unpickle World', command=lambda: self.unpickle_world(unpickle_world))
		self.button_save_game.grid(pady=4, column=1, row=2, sticky='W')

		self.button_quit = tkinter.ttk.Button(self.right_frame, text="Quit", command=self.destroy)
		self.button_quit.grid(pady=4, padx=2, column=0, row=3, sticky='EW')

		self.saved_settings = False
		self.button_save = tkinter.ttk.Button(self.right_frame, text="Save Settings", command=self.save_settings)

		self.button_save.grid(pady=4, padx=2, column=1, row=3, sticky='EW')

	def pickle_world(self, pickle_world):
		pickle_world(tkinter.simpledialog.askstring('World Name', 'World Name:'))

	def unpickle_world(self, unpickle_world):
		unpickle_world(tkinter.simpledialog.askstring('World Name', 'World Name:'))

	def save_settings(self):
		self.saved_settings = True
		self.destroy()

	def run(self):
		self.mainloop()
		return [self.text.get()] if self.saved_settings else None

if __name__ == "__main__":
	menu = Setting_Menu()
	print(menu.run())
