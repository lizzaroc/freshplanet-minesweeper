from Tkinter import *
from tkMessageBox import *
from grid import MSGrid
import sys

from PIL import ImageTk

def enum(**enums):
	return type('Enum', (), enums)

States = enum(UNDISCOVERED=-1,CLEAN=0,BOMB=9,FLAG=10,QUESTIONMARK=11)

class MSGraphicalInterface(object):
	def __init__(self):
		self.grid = MSGrid(20,20,30)
		self.buttonsGrid = [[0 for i in range(self.grid.width)] for j in range(self.grid.heigth)]
		NoDefaultRoot()
		self.window = Tk()
		self.askGridCanvas = Canvas(self.window)
		self.gridCanvas=Canvas(self.window)
		self.loadImages()
		self.askGridFormat()

	def askGridFormat(self):
		heigthLabel = Label(self.askGridCanvas, text="Heigth?")
		heigthSpinbox = Spinbox(self.askGridCanvas, from_=10, to=30)
		heigthLabel.pack()
		heigthSpinbox.pack()

		widthLabel = Label(self.askGridCanvas, text="Width?")
		widthSpinbox = Spinbox(self.askGridCanvas, from_=10, to=30)
		widthLabel.pack()
		widthSpinbox.pack()

		minesLabel = Label(self.askGridCanvas, text="Number of mines?")
		minesSpinbox = Spinbox(self.askGridCanvas, from_=10, to=300)
		minesLabel.pack()
		minesSpinbox.pack()

		def okButtonClicked():
			heigth = int(heigthSpinbox.get())
			width = int(widthSpinbox.get())
			mines = int(minesSpinbox.get())
			self.setGrid(heigth, width, mines)

		okButton = Button(self.askGridCanvas,text='Ok', command=okButtonClicked)
		okButton.pack()

		self.askGridCanvas.pack()

		self.window.mainloop()

	def setGrid(self,heigth,width,mines):
		self.askGridCanvas.destroy()
		self.gridCanvas.destroy()
		try:
			self.minesLeftLabel1.destroy()
		except:
			pass
		self.gridCanvas=Canvas(self.window)
		self.grid = MSGrid(heigth, width, mines)
		self.minesLeftLabel1 = Label(self.window, text="Number of mines left: " + str(self.grid.numberOfMines))
		self.minesLeftLabel1.pack()

		self.gridCanvas=Frame(self.window)
		self.buttonsGrid = [[0 for i in range(width)] for j in range(heigth)]
		self.grid.generate()
		self.display()
		
	def display(self):
		Grid.rowconfigure(self.gridCanvas, 0, weight=1)
		Grid.columnconfigure(self.gridCanvas, 0, weight=1)

		self.gridCanvas.grid(row=0, column=0, sticky=N+S+E+W)
		grid=Frame(self.gridCanvas)

		grid.grid(sticky=N+S+E+W, column=0, row=7, columnspan=2)
		Grid.rowconfigure(self.gridCanvas, 7, weight=1)
		Grid.columnconfigure(self.gridCanvas, 7, weight=1)

		self.gridCanvas.pack()

		changingButtons = []
		for x in range(self.grid.width):
			for y in range(self.grid.heigth):
				self.buttonsGrid[y][x] = Button(self.gridCanvas,command=self.leftClickWrapper(x,y))
				self.buttonsGrid[y][x].config(image = self.undiscoveredImage, width=30, height=22)
				self.buttonsGrid[y][x].bind("<Button-2>", self.rightClickWrapper(0,x,y))
				self.buttonsGrid[y][x].bind("<Button-3>", self.doubleClickWrapper(0,x,y))
				self.buttonsGrid[y][x].grid(column=x, row=y, sticky=N+S+E+W)

		self.update(changingButtons)

	def loadImages(self):
		self.undiscoveredImage = ImageTk.PhotoImage(master = self.gridCanvas, file= "undiscovered.gif")
		self.discoveredImage = ImageTk.PhotoImage(master = self.gridCanvas, file= "discovered.gif")
		self.oneMineImage = ImageTk.PhotoImage(master = self.gridCanvas, file = "1.gif")
		self.twoMinesImage = ImageTk.PhotoImage(master= self.gridCanvas, file = "2.gif")
		self.threeMineImage = ImageTk.PhotoImage(master = self.gridCanvas, file = "3.gif")
		self.fourMinesImage = ImageTk.PhotoImage(master= self.gridCanvas, file = "4.gif")
		self.fiveMineImage = ImageTk.PhotoImage(master = self.gridCanvas, file = "5.gif")
		self.sixMinesImage = ImageTk.PhotoImage(master= self.gridCanvas, file = "6.gif")
		self.sevenMineImage = ImageTk.PhotoImage(master = self.gridCanvas, file = "7.gif")
		self.eightMinesImage = ImageTk.PhotoImage(master= self.gridCanvas, file = "8.gif")
		self.bombImage =ImageTk.PhotoImage(master = self.gridCanvas, file = "bomb.gif")
		self.flagImage = ImageTk.PhotoImage(master= self.gridCanvas, file = "flag.gif")
		self.questionMarkImage = ImageTk.PhotoImage(master = self.gridCanvas, file = "questionMark.gif")

	def imageForValue(self,value):
		if value == States.UNDISCOVERED:
			return self.undiscoveredImage
		elif value == States.CLEAN:
			return self.discoveredImage
		elif value == 1:
			return self.oneMineImage
		elif value == 2:
			return self.twoMinesImage
		elif value == 3:
			return self.threeMineImage
		elif value == 4:
			return self.fourMinesImage
		elif value == 5:
			return self.fiveMineImage
		elif value == 6:
			return self.sixMinesImage
		elif value == 7:
			return self.sevenMineImage
		elif value == 8:
			return self.eightMinesImage
		elif value == States.BOMB:
			return self.bombImage
		elif value == States.FLAG:
			return self.flagImage
		elif value == States.QUESTIONMARK:
			return self.questionMarkImage

	def update(self,changingButtons):
		for toUpdateButton in changingButtons:
			x = toUpdateButton[0]
			y = toUpdateButton[1]
			value = toUpdateButton[2]
			self.buttonsGrid[y][x].config(image = self.imageForValue(value), width=30, height=22)

	def leftClickWrapper(self,x,y):
		def hasLeftClicked(i=x,j=y):
			if self.grid.isBomb(x,y):
				self.hasLost()
			else:
				changingButtons = self.grid.intelligentReveal(i,j)
				self.update(changingButtons)

			if self.grid.isFinished():
				if askyesno("Congratulations! You won!", "Wanna play again?",master=self.gridCanvas):
					self.setGrid(self.grid.heigth,self.grid.width,self.grid.numberOfMines)
				else:
					showinfo("Okay :(", "See you next time!",master=self.gridCanvas)
					self.quit()

		return hasLeftClicked

	def rightClickWrapper(self,event,x,y):
		def hasRightClicked(Event=None,i=x,j=y):
			self.update([[i,j,self.grid.flag(i,j)]])
			self.minesLeftLabel1.config(text="Number of mines left: " + str(self.grid.numberOfMinesLeft))
		return hasRightClicked

	def doubleClickWrapper(self,event,x,y):
		def hasDoubleClicked(Event=None,i=x,j=y):
			print("double clic")
			hasFailed,toUpdate = self.grid.flagReveal(i,j)
			self.update(toUpdate)
			if hasFailed:
				self.hasLost()
		return hasDoubleClicked

	def hasLost(self):
		if askretrycancel("You lost", "Wanna try again?",master=self.gridCanvas):
			self.setGrid(self.grid.heigth,self.grid.width,self.grid.numberOfMines)
		else:
			showinfo("Okay :(", "See you next time!",master=self.gridCanvas)
			self.quit()

	def quit(self):
		self.window.destroy()
		sys.exit()

