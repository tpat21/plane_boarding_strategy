from graphics import *
import numpy as np
import time
from threading import Timer
import math

walk1 = Image(Point(200, 60), 'Assets/Sprite1.png')
walk2 = Image(Point(200, 60), 'Assets/Sprite2.png')
walk3 = Image(Point(200, 60), 'Assets/Sprite1.png')
walk4 = Image(Point(200, 60), 'Assets/Sprite3.png')
walk = [walk1, walk2, walk3, walk4]
sitting = Image(Point(0, 0), 'Assets/Sitting.png')


def main():

    pass1 = [2, 0]

    win = GraphWin("Boarding", 400, 480)

    for i in range(0, 6):
        aisle = Image(Point(200, (80 * i) + 40), 'Assets/Aisle2.png')
        aisle.draw(win)

        for j in (0, 1, 3, 4):
            seat = Image(Point((80 * j) + 40, (80 * i) + 40), 'Assets/Seat2.png')
            seat.draw(win)

    for i in (0, 1, 3, 4):
        empty = Image(Point((80 * i) + 40, 40), 'Assets/Empty.png')
        empty.draw(win)

    walk[0].draw(win)
    win.getMouse()
    walk[0].undraw()

    pass1 = down(win, pass1, 1)
    pass1 = left(win, pass1, 2)
    sit(win, pass1)

    win.getMouse()

    move(win, pass1, [4, 4])

    win.getMouse()

    move(win, pass1, [3, 0])

    win.getMouse()  # Pause to view result
    win.close()    # Close window when done


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


def down(win, passenger, num):  # Moves 1 passenger down 1
    for x in range(0, num):
        step(win, [0, 1])

    passenger[1] += num
    return passenger


def right(win, passenger, num):  # Moves 1 passenger right 1
    for x in range(0, num):
        step(win, [1, 0])

    passenger[0] += num
    return passenger


def left(win, passenger, num):  # Moves 1 passenger left 1
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


main()
