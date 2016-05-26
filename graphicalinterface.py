from Tkinter import *
from tkMessageBox import *
from grid import MSGrid

class MSGraphicalInterface(object):
	def __init__(self):
		self.grid = MSGrid(20,20,30)
		self.buttonsGrid = [[0 for i in range(self.grid.width)] for j in range(self.grid.heigth)]
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
		self.buttonsGrid = [[0 for i in range(width)] for j in range(heigth)]
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

		changingButtons = []
		for x in range(self.grid.width):
			for y in range(self.grid.heigth):
				self.buttonsGrid[y][x] = Button(self.frame, text="", command=self.leftClickWrapper(x,y))
				self.buttonsGrid[y][x].config(height = 1, width = 1)
				self.buttonsGrid[y][x].grid(column=x, row=y, sticky=N+S+E+W)

		self.update(changingButtons)
		self.window.mainloop()

	def update(self,changingButtons):
		for toUpdateButton in changingButtons:
			x = toUpdateButton[0]
			y = toUpdateButton[1]
			value = toUpdateButton[2]
			self.buttonsGrid[y][x].config(text=	str(self.grid.mapWithFog[y][x]))

	def leftClickWrapper(self,x,y):
		def hasLeftClicked(i=x,j=y):
			if self.grid.isBomb(x,y):
				if askretrycancel("You lost", "Wanna try again?"):
					print("To be implemented: try again")
				else:
					print("okay :(")

			changingButtons = self.grid.intelligentReveal(i,j)

			if self.grid.isFinished():
				if askyesno("Congratulations! You won!", "Wanna play again?"):
					print("to be implemented: play again")
				else:
					print("okay :(")

			self.update(changingButtons)
		return hasLeftClicked