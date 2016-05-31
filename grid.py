from random import randint
import copy

def enum(**enums):
	return type('Enum', (), enums)

States = enum(UNDISCOVERED=-1,CLEAN=0,BOMB=9,FLAG=10,QUESTIONMARK=11)

class MSGrid(object):
	def __init__(self,heigth,width,mines):
		self.mapWithoutFog = []
		self.mapWithFog = []
		self.heigth = heigth
		self.width = width
		self.numberOfMines = mines
		self.numberOfMinesLeft = mines

	def generate(self):
		self.mapWithoutFog = [[States.CLEAN]*self.width for row in range(self.heigth)]
		for i in range(self.numberOfMines):
			self.addBomb()
		booleanMap = copy.deepcopy(self.mapWithoutFog)
		self.numerizeMap(booleanMap)

		self.mapWithFog = [[States.UNDISCOVERED]*self.width for row in range(self.heigth)]

	def addBomb(self):
		bombNotPlaced = True
		while bombNotPlaced:
			x = randint(0,self.width-1)
			y = randint(0,self.heigth-1)
			if self.mapWithoutFog[y][x] == States.CLEAN:
				self.mapWithoutFog[y][x] = States.BOMB
				bombNotPlaced = False

	def numerizeMap(self, booleanMap):
		for i in range(self.width):
			for j in range(self.heigth):
				if booleanMap[j][i] == States.BOMB:
					self.mapWithoutFog[j][i] = States.BOMB
				else:
					neighbourMines = 0
					for x in range(max(0, i-1), min(i+2, self.width)):
						for y in range(max(0, j-1), min(j+2, self.heigth)):
							if booleanMap[y][x] == States.BOMB:
								neighbourMines += 1
					self.mapWithoutFog[j][i] = neighbourMines

	# This function isn't used anymore, it served in the console interface
	def pickNextSquare(self):
		squareNotOkay = True
		while squareNotOkay:

			#We ask the user for the square he wants to check, and substract 1 because nobody is going to pick row 0
			try:
				x = int(raw_input("Column?: "))-1
			except ValueError:
				print("Incorrect column number")

			try:
				y = int(raw_input("Row?: "))-1
			except ValueError:
				print("Incorrect row number")

			if x <= self.width and y <= self.heigth:
				squareNotOkay = False

			self.intelligentReveal(x,y)

	def isBomb(self,x,y):
		return(self.mapWithoutFog[y][x] == States.BOMB)

	def flag(self,x,y):
		if self.mapWithFog[y][x] == States.FLAG:
			self.mapWithFog[y][x] = States.QUESTIONMARK
			self.numberOfMinesLeft += 1
		elif self.mapWithFog[y][x] == States.UNDISCOVERED:
			 self.mapWithFog[y][x] = States.FLAG
			 self.numberOfMinesLeft -= 1
		elif self.mapWithFog[y][x] == States.QUESTIONMARK:
			 self.mapWithFog[y][x] = States.UNDISCOVERED
		return self.mapWithFog[y][x]

	def isntFlag(self,x,y):
		return(self.mapWithFog[y][x] != States.FLAG)

	def reveal(self,x,y):
		self.mapWithFog[y][x] = self.mapWithoutFog[y][x]

	def intelligentReveal(self,x,y):
		self.mapWithFog[y][x] = self.mapWithoutFog[y][x]
		toUpdateCells = [[x,y,self.mapWithoutFog[y][x]]]
		if self.mapWithFog[y][x] == States.CLEAN:
			for i in range(max(0, x-1), min(x+2, self.width)):
				for j in range(max(0, y-1), min(y+2, self.heigth)):
					if self.mapWithFog[j][i] == -1:
						toUpdateCells= toUpdateCells + self.intelligentReveal(i,j)
		return toUpdateCells

	def hasEnoughAdjacentFlags(self,x,y):		
		numberOfFlags = 0
		for i in range(max(0, x-1), min(x+2, self.width)):
			for j in range(max(0, y-1), min(y+2, self.heigth)):
				if self.mapWithFog[j][i] == States.FLAG:
					numberOfFlags +=1
		return (numberOfFlags == self.mapWithoutFog[y][x])

	def flagReveal(self,x,y):
		hasLost = False
		toUpdateCells = []
		if self.hasEnoughAdjacentFlags(x,y):
			for i in range(max(0, x-1), min(x+2, self.width)):
				for j in range(max(0, y-1), min(y+2, self.heigth)):
					if self.isntFlag(i,j):
						if(self.isBomb(i,j)):
							hasLost = True
						toUpdateCells= toUpdateCells + self.intelligentReveal(i,j)
		return hasLost, toUpdateCells

	def isFinished(self):
		isFinished = True
		for i in range(self.width):
			for j in range(self.heigth):
				if self.mapWithoutFog[j][i] != States.BOMB and self.mapWithFog[j][i] == States.UNDISCOVERED:
					isFinished = False
		return isFinished

	def display(self):
		print(self.mapWithoutFog)
		print(self.mapWithFog)


