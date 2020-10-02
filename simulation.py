import numpy as np
import time
from threading import Timer


class Passenger:
    def __init__(self, rowNum, colNum, carryOn):
        self.carryOn = carryOn
        self.rowNum = rowNum
        self.colNum = colNum

        self.x = 2
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
        # seating[self.y, self.x + 1] = 0
        time.sleep(1)

    def wait(self):
        pass

    def display(self):
        print(seating)


p1 = Passenger(3, 3, False)

rows = 5
cols = 5
seating = np.zeros([rows, cols])


def runProgram():
    passengers = [p1]

    for passenger in passengers:
        while passenger.rowNum != passenger.y:
            passenger.moveDown()

        # while passenger.colNum != passenger.x:
        #     if passenger.colNum == 1 or 2:
        #         passenger.moveLeft()
        #         print("e")


runProgram()
