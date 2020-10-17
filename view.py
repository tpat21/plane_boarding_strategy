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
stowR1 = 'Assets/stowR1.png'
stowR2 = 'Assets/stowR2.png'
stowR3 = 'Assets/stowR3.png'
stowR4 = 'Assets/stowR2.png'
stowL1 = 'Assets/stowL1.png'
stowL2 = 'Assets/stowL2.png'
stowL3 = 'Assets/stowL3.png'
stowL4 = 'Assets/stowL2.png'
walk = [walk1, walk2, walk3, walk4]
stowR = [stowR1, stowR2, stowR3, stowR4]
stowL = [stowL1, stowL2, stowL3, stowL4]
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
                elif processes[j][1] == 'stowR':
                    self.passengers[processes[j][0]].stow(i % 4, "r")
                elif processes[j][1] == 'stowL':
                    self.passengers[processes[j][0]].stow(i % 4, "l")
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

    def stow(self, frame, dir):
        self.sprite.undraw()
        if dir == 'r':
            self.sprite = self.drawPass(stowR[frame])
        else:
            self.sprite = self.drawPass(stowL[frame])

    def sitDown(self):
        if self.sitting == False:
            self.sprite.undraw()
            self.y += 60
            self.sprite = self.drawPass(sitting)
            self.sitting = True


# v.win.getMouse()  # Pause to view result
# v.win.close()    # Close window when done
