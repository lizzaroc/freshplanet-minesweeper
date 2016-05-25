import random
import time
from grid import Grid

class MineSweeper(object):
    def __init__(self):
        self.isPlaying = True
        self.grid = Grid()
        self.play()

    def play(self):
        while True:
            self.grid.generate()
            print("ok")

            while self.isPlaying:
                self.grid.pickNextSquare()
                #self.isPlaying = self.grid.hasFinished()
                self.grid.display()
                time.sleep(5)

if __name__ == "__main__":
    mineSweeper = MineSweeper()
    mineSweeper.play()