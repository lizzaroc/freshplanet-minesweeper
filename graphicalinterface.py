from Tkinter import *
from tkMessageBox import *

class GraphicalInterface(object):
	def __init__(self, grid):
		self.grid = grid
		self.window = Tk()
		self.frame=Frame(self.window)

	def display(self):
		Grid.rowconfigure(self.window, 0, weight=1)
		Grid.columnconfigure(self.window, 0, weight=1)

		self.frame.grid(row=0, column=0, sticky=N+S+E+W)
		grid=Frame(self.frame)

		grid.grid(sticky=N+S+E+W, column=0, row=7, columnspan=2)
		Grid.rowconfigure(self.frame, 7, weight=1)
		Grid.columnconfigure(self.frame, 7, weight=1)

		self.update()
		self.window.mainloop()

	def update(self):
		for x in range(5):
			for y in range(5):
				button = Button(self.frame, text=str(self.grid.mapWithFog[y][x]), command= self.leftClickWrapper(x,y))
				button.grid(column=x, row=y, sticky=N+S+E+W)

	def leftClickWrapper(self,x,y):
		def hasLeftClicked(i=x,j=y):
			if self.grid.isBomb(x,y):
				if askretrycancel("You lost", "Wanna try again?"):
					print("To be implemented: try again")
				else:
					print("okay :(")

			self.grid.intelligentReveal(i,j)

			if self.grid.isFinished():
				if askyesno("Congratulations! You won!", "Wanna play again?"):
					print("to be implemented: play again")
				else:
					print("okay :(")

			self.update()
		return hasLeftClicked