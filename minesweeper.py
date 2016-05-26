import random
import time
from graphicalinterface import MSGraphicalInterface

class MSMineSweeper(object):
    def __init__(self):
        self.graphicalInterface = MSGraphicalInterface()
        self.play()

    def play(self):
        self.graphicalInterface.display()

if __name__ == "__main__":
    mineSweeper = MSMineSweeper()
    print("just testing something")
    mineSweeper.play()