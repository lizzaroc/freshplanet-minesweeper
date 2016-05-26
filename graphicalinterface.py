from Tkinter import *
from tkMessageBox import *
from grid import MSGrid

class MSGraphicalInterface(object):
	def __init__(self):
		self.grid = MSGrid(20,20,30)
		self.window = Tk()
		self.frame=Frame(self.window)
		self.askGridFormat()

	def askGridFormat(self):
		heigthLabel = Label(self.window, text="Heigth?")
		heigthSpinbox = Spinbox(self.window, from_=10, to=50)
		heigthLabel.pack()
		heigthSpinbox.pack()

		widthLabel = Label(self.window, text="Width?")
		widthSpinbox = Spinbox(self.window, from_=10, to=50)
		widthLabel.pack()
		widthSpinbox.pack()

		minesLabel = Label(self.window, text="Number of mines?")
		minesSpinbox = Spinbox(self.window, from_=10, to=99)
		minesLabel.pack()
		minesSpinbox.pack()

		def okButtonClicked():
			heigth = int(heigthSpinbox.get())
			width = int(widthSpinbox.get())
			mines = int(minesSpinbox.get())
			self.setGrid(heigth, width, mines)

		okButton = Button(text='Ok', command=okButtonClicked)
		okButton.pack()

		self.window.mainloop()

	def setGrid(self,heigth,width,mines):
		self.window.destroy()
		self.window = Tk()
		self.frame=Frame(self.window)
		self.grid = MSGrid(heigth, width, mines)
		self.grid.generate()
		self.display()
		
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
		for x in range(self.grid.heigth):
			for y in range(self.grid.width):
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