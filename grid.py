from random import randint
import copy

class MSGrid(object):
	def __init__(self,heigth,width,mines):
		self.mapWithoutFog = []
		self.mapWithFog = []
		self.heigth = heigth
		self.width = width
		self.numberOfMines = mines

	def generate(self):
		self.mapWithoutFog = [[0]*self.width for row in range(self.heigth)]
		for i in range(self.numberOfMines):
			self.addBomb()
		booleanMap = copy.deepcopy(self.mapWithoutFog)
		self.numerizeMap(booleanMap)

		self.mapWithFog = [[-1]*self.width for row in range(self.heigth)]

	def addBomb(self):
		bombNotPlaced = True
		while bombNotPlaced:
			x = randint(0,self.width-1)
			y = randint(0,self.heigth-1)
			if self.mapWithoutFog[y][x] == 0:
				self.mapWithoutFog[y][x] = 1
				bombNotPlaced = False

	def numerizeMap(self, booleanMap):
		for i in range(self.width):
			for j in range(self.heigth):
				if booleanMap[j][i] == 1:
					self.mapWithoutFog[j][i] = 9
				else:
					neighbourMines = 0
					for x in range(max(0, i-1), min(i+2, self.width)):
						for y in range(max(0, j-1), min(j+2, self.heigth)):
							if booleanMap[y][x] == 1:
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
		return(self.mapWithoutFog[y][x] == 9)

	def reveal(self,x,y):
		self.mapWithFog[y][x] = self.mapWithoutFog[y][x]

	def intelligentReveal(self,x,y):
		self.mapWithFog[y][x] = self.mapWithoutFog[y][x]
		if self.mapWithFog[y][x] == 0:
			for i in range(max(0, x-1), min(x+2, self.width)):
				for j in range(max(0, y-1), min(y+2, self.heigth)):
					if self.mapWithFog[j][i] == -1:
						self.intelligentReveal(i,j)

	def isFinished(self):
		isFinished = True
		for i in range(self.width):
			for j in range(self.heigth):
				if self.mapWithoutFog[j][i] != 9 and self.mapWithFog[j][i] == -1:
					isFinished = False
		return isFinished

	def display(self):
		print(self.mapWithoutFog)
		print(self.mapWithFog)


