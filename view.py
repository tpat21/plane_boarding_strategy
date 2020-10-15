from graphics import *
import numpy as np
import time
from threading import Timer
import math

walk1 = 'Assets/Sprite1.png'
walk2 = 'Assets/Sprite2.png'
walk3 = 'Assets/Sprite1.png'
walk4 = 'Assets/Sprite3.png'
nothing = 'Assets/Nothing.png'
walk = [walk1, walk2, walk3, walk4]
sitting = 'Assets/Sitting.png'

tileHeight = 80  # height of a tile (passenger, seat, etc) in pixels
speed = 1  # number of tiles a passenger can move through in 1 second without interference


class View():
    def __init__(self, columns, rows):
        self.col = columns
        self.row = rows
        self.width = tileHeight * columns
        self.height = tileHeight * columns + tileHeight
        self.win = self.createWindow()
        self.passengers = []

    def createWindow(self):
        win = GraphWin("Airplane Boarding", 80 * self.col, 80 * self.col + 80)
        for i in range(0, self.col + 1):
            for j in range(0, self.row):
                if j == math.floor(self.row / 2):
                    self.drawImg(win, j, i, 'Assets/Aisle2.png')
                elif i == 0:
                    self.drawImg(win, j, i, 'Assets/Empty.png')
                else:
                    self.drawImg(win, j, i, 'Assets/Seat2.png')
        return win

    def drawImg(self, win, x, y, name):
        img = Image(Point((tileHeight * x) + tileHeight / 2, (tileHeight * y) + tileHeight / 2), name)
        img.draw(win)

    def drawPass(self, win, p, name):
        img = Image(Point(p.x, p.y), name)
        img.draw(win)
        return img

    def addPass(self, num):
        for i in range(0, num):
            self.passengers.append(Passenger(self.width / 2, -1 * (tileHeight / 2) - 60, self.win))
            self.drawPass(self.win, self.passengers[-1], nothing)

    def moveMultiple(self, processes):
        print(len(processes))
        print(processes)
        for i in range(0, 8):
            for j in range(0, len(processes)):
                if processes[j][1] == 'down':
                    self.passengers[processes[j][0]].smallDown(i % 4)
                elif processes[j][1] == 'up':
                    self.passengers[processes[j][0]].smallUp(i % 4)
                elif processes[j][1] == 'right':
                    self.passengers[processes[j][0]].smallRight(i % 4)
                elif processes[j][1] == 'left':
                    self.passengers[processes[j][0]].smallLeft(i % 4)
                else:
                    self.passengers[processes[j][0]].sitDown()
            time.sleep(speed / 8)


class Passenger():
    def __init__(self, xPos, yPos, win):
        self.win = win
        self.x = xPos
        self.y = yPos
        self.sprite = Image(Point(self.x, self.y), nothing)
        self.sitting = False

    def drawPass(self, name):
        if(self.y <= -20):
            name = nothing
        img = Image(Point(self.x, self.y), name)
        img.draw(self.win)
        return img

    def walk(self, x, y):
        for i in range(0, 8):
            self.sprite.undraw()
            self.x += (tileHeight * x) / 8
            self.y += (tileHeight * y) / 8
            self.sprite = self.drawPass(walk[i % 4])
            time.sleep(speed / 8)

    def smallWalk(self, x, y, frame):
        self.sprite.undraw()
        self.x += (tileHeight * x) / 8
        self.y += (tileHeight * y) / 8
        self.sprite = self.drawPass(walk[frame])

    def smallDown(self, frame):
        self.smallWalk(0, 1, frame)

    def smallUp(self, frame):
        self.smallWalk(0, -1, frame)

    def smallRight(self, frame):
        self.smallWalk(1, 0, frame)

    def smallLeft(self, frame):
        self.smallWalk(-1, 0, frame)

    def moveDown(self):
        self.walk(0, 1)

    def moveUp(self):
        self.walk(0, -1)

    def moveRight(self):
        self.walk(1, 0)

    def moveLeft(self):
        self.walk(-1, 0)

    def sitDown(self):
        if self.sitting == False:
            self.sprite.undraw()
            self.y += 60
            self.sprite = self.drawPass(sitting)
            self.sitting = True


def main():
    v = View(5, 5)
    v.addPass(2)
    print(v.passengers)

    v.win.getMouse()  # Pause to view result
    v.win.close()    # Close window when done


# def main():
#
#    pass1 = [2, 0]
#
#    win = createWindow(5)
#
#    for i in range(0, 6):
#        aisle = Image(Point(200, (80 * i) + 40), 'Assets/Aisle2.png')
#        aisle.draw(win)
#
#        for j in (0, 1, 3, 4):
#            seat = Image(Point((80 * j) + 40, (80 * i) + 40), 'Assets/Seat2.png')
#            seat.draw(win)
#
#    for i in (0, 1, 3, 4):
#        empty = Image(Point((80 * i) + 40, 40), 'Assets/Empty.png')
#        empty.draw(win)
#
#    walk[0].draw(win)
#    win.getMouse()
#    walk[0].undraw()
#
#    pass1 = down(win, pass1, 1)
#    pass1 = left(win, pass1, 2)
#    sit(win, pass1)
#
#    win.getMouse()
#
#    move(win, pass1, [4, 4])
#
#    win.getMouse()
#
#    move(win, pass1, [3, 0])
#
#    win.getMouse()  # Pause to view result
#    win.close()    # Close window when done

# def createWindow(columns):

    # Columns is the number of seats in both rows plus the aisle
    # 2 seats in a row on either side of the aisle would be columns=5

#    win = GraphWin("Airplane Boarding", 80 * columns, 80 * columns + 80)
#    for i in range(0, columns + 1):
#        aisle = Image(Point(200, (80 * i) + 40), 'Assets/Aisle2.png')
#        aisle.draw(win)

#        for j in (0, 1, 3, 4):
#            seat = Image(Point((80 * j) + 40, (80 * i) + 40), 'Assets/Seat2.png')
#            seat.draw(win)

#    for i in (0, 1, 3, 4):
#        empty = Image(Point((80 * i) + 40, 40), 'Assets/Empty.png')
#        empty.draw(win)
#    return win


def main2():
    start = [0, 0, 2, 0]
    end = [1, 3, 2, 4]
    runSim(start, end)


def step(win, dir):

    for x in range(0, 8):

        for w in walk:  # Moves location of all walking sprites
            w.move(10 * dir[0], 10 * dir[1])
        walk[x % 4].draw(win)

        time.sleep(0.125)  # 8 frames per second
        walk[x % 4].undraw()


def down(win, passenger, num):

        # Moves 1 passenger down 1

    for x in range(0, num):
        step(win, [0, 1])

    passenger[1] += num
    return passenger


def right(win, passenger, num):

        # Moves 1 passenger right 1

    for x in range(0, num):
        step(win, [1, 0])

    passenger[0] += num
    return passenger


def left(win, passenger, num):

        # Moves 1 passenger left 1

    for x in range(0, num):
        step(win, [-1, 0])

    passenger[0] -= num
    return passenger


def up(win, passenger, num):  # Moves 1 passenger up 1
    for x in range(0, num):
        step(win, [0, -1])

    passenger[1] -= num
    return passenger

def move(win, passenger, seat):

    # Moves a passenger from one place to another

    sitting.undraw()
    sitting.move(-1 * sitting.anchor.getX(), -1 * sitting.anchor.getY())

    while walk[0].anchor.getX() > 200:
        left(win, passenger, 1)

    while walk[0].anchor.getX() < 200:
        right(win, passenger, 1)

    current = [int((walk[0].anchor.getX() - 40) / 80), int(((walk[0].anchor.getY()) + 20) / 80) - 1]

    xdif = seat[0] - current[0]
    ydif = seat[1] - current[1]

    if ydif > 0:
        down(win, passenger, ydif)
    elif ydif < 0:
        up(win, passenger, -1 * ydif)

    if xdif > 0:
        right(win, passenger, xdif)
    elif xdif < 0:
        left(win, passenger, -1 * xdif)

    sit(win, passenger)


def sit(win, passenger):

    # Changes sprite to sitting

    coords = [walk[0].anchor.getX(), walk[0].anchor.getY()]
    sitting.move(coords[0], coords[1] + 60)
    sitting.draw(win)


def clear(win):

    # clears window

    for item in win.items[:]:
        item.undraw()
    win.update()


def runSim(arr1, arr2):

    # TODO
    # Working with multiple passengers

    passengers = len(arr1) / 2


# main()
