import random
import time
from grid import Grid
from graphicalinterface import GraphicalInterface

class MineSweeper(object):
    def __init__(self):
        self.isPlaying = True
        self.grid = Grid()
        self.graphicalInterface = GraphicalInterface(self.grid)
        self.play()

    def play(self):
        while True:
            self.grid.generate()
            self.graphicalInterface.display()

if __name__ == "__main__":
    mineSweeper = MineSweeper()
    mineSweeper.play()