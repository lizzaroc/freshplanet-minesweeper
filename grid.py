from random import randint

class Grid(object):
	def __init__(self):
		self.mapWithoutFog = []
		self.mapWithFog = []
		self.heigth = 5
		self.width = 5
		self.numberOfMines = 3

	def generate(self):
		self.mapWithoutFog = [[0]*self.width for i in range(self.heigth)]
		print("map generated:")
		print(self.mapWithoutFog)
		for i in range(self.numberOfMines):
			self.addBomb()

	def addBomb(self):
		bombNotPlaced = True
		while bombNotPlaced:
			x = randint(0,self.width-1)
			y = randint(0,self.heigth-1)
			print(x)
			print(y)
			if self.mapWithoutFog[y][x] == 0:
				self.mapWithoutFog[y][x] = 1
				bombNotPlaced = False

	def display(self):
		print(self.mapWithoutFog)
		print(self.mapWithFog)


