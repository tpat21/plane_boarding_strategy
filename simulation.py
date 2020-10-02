import numpy as np
import time
from threading import Timer
import math


rows = 5
cols = 5
middle =  math.ceil(cols/2) -1
seating = np.zeros([rows, cols])


class Passenger:
    def __init__(self, rowNum, colNum, carryOn):
        self.carryOn = carryOn
        self.rowNum = rowNum
        self.colNum = colNum

        self.x = middle
        self.y = 0
        self.ticker = 0
        self.isSeated = False
        self.left = False
        self.right = False

    def sit(self):
        pass

    def putCarryOn(self):
        pass

    def collide(self):
        pass

    def moveDown(self):
        seating[self.y, self.x] = 7
        self.display()
        self.y += 1
        seating[self.y - 1, self.x] = 0

        time.sleep(1)

    def moveLeft(self):
        seating[self.y, self.x] = 7
        self.display()
        self.x -= 1
        seating[self.y, self.x + 1] = 0
        time.sleep(1)

    def moveRight(self):
        seating[self.y, self.x] = 7
        self.display()
        self.x += 1
        seating[self.y, self.x - 1] = 0
        time.sleep(1)

    def wait(self):
        pass

    def display(self):
        print(seating)


p1 = Passenger(4, 0, False)



def runProgram():
    passengers = [p1]

    for passenger in passengers:
        while passenger.rowNum != passenger.y:
            passenger.moveDown()

        if passenger.colNum < middle:
            while passenger.x != -1:
                passenger.moveLeft()

        else:
            while passenger.x != cols:
                passenger.moveRight()





runProgram()
