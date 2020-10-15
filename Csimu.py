import numpy as np
import time
import random
from threading import *
import math
from view import *


rows = 5
cols = 5
middle = int(math.ceil(cols / 2)) - 1
#seating = np.zeros([rows, cols])
Vmin = 17 * 11 * 7
processes = []


class Bag:
  def __init__(self):
    self.volume = self.bagvol()

  def bagvol(self):
    l = random.randrange(17, 22, 1)
    w = random.randrange(11, 14, 1)
    h = random.randrange(7, 9, 1)
    return(l * w * h)


class Passenger:
  def __init__(self, rowNum, colNum, thisnum, sprite, passNum):
    self.passNum = passNum

    self.rowNum = rowNum
    self.colNum = colNum

    self.sprite = sprite
    processes.append([self.passNum, "down"])

    self.x = middle
    self.y = 0
    self.left = False
    self.right = False
    self.ent = False
    self.thisnum = thisnum
    self.sit = False
    self.age = float(int(np.random.normal(39, 19.5, 1)))
    self.numbags = self.setbags()
    print(self.age)
    self.atime = self.agetime(self.age)
#        print(self.atime)
    self.Bags = []
    trackofbags = 0
    for k in range(0, self.numbags - 1):
      self.Bags.append(Bag())
#            print(self.Bags[k].volume)
      trackofbags = trackofbags + (float(self.Bags[k].volume) / Vmin)
    self.timestore = self.numbags * (trackofbags + self.atime)
    print("For passenger")
    print(self.thisnum)
    print("bags")
    print(self.numbags)
    print("vol")
    print(trackofbags)
    print("age time")
    print(self.atime)
    print("tot")
    print(self.timestore)

  def agetime(self, a):
    if a < 25:
      a = (((a / 2.5) - 10)**2) + 3
    else:
      a = (((a / 10) - 2.5)**2) + 3
    return(a)

  def setbags(self):
    j = np.random.normal(2, 1.5, 1)
    if self.age <= 10:
      if j < 1.5:
        j = 0
      else:
        j = 1
    elif self.age >= 65:
      if j < 2:
        j = 1
      else:
        j = 2
    else:
      if j < 1:
        j = 1
      elif j > 3:
        j = 3
      else:
        j = 2
    return(j)

  def moveDown(self, seating, processes):
    seating[self.y, self.x] = self.thisnum
    # self.display()
    self.y += 1
    seating[self.y - 1, self.x] = 0

    processes.append([self.passNum, "down"])

    # time.sleep(1)

  def moveLeft(self, seating, processes):
    seating[self.y, self.x] = self.thisnum
    # self.display()
    self.x -= 1
    seating[self.y, self.x + 1] = 0

    processes.append([self.passNum, "left"])

    # time.sleep(1)

  def moveRight(self, seating, processes):
    seating[self.y, self.x] = self.thisnum
    # self.display()
    self.x += 1
    seating[self.y, self.x - 1] = 0

    processes.append([self.passNum, "right"])

    # time.sleep(1)

  def sitDown(self, seating, processes):
    seating[self.y, self.x + 1] = self.thisnum
    self.seated = True

    processes.append([self.passNum, "sit"])

  def display(self, seating):
    print(seating)
    print("------------------")


v = View(cols, rows)
v.addPass(4)

p1 = Passenger(4, 0, 2, v.passengers[0], 0)
p2 = Passenger(3, 4, 3, v.passengers[1], 1)
p3 = Passenger(2, 3, 4, v.passengers[2], 2)
p4 = Passenger(1, 1, 5, v.passengers[3], 3)


def runProgram(processes):
  processes = processes
  seating = np.zeros([rows, cols])
  p1.timestore = 3
  p2.timestore = 3
  p3.timestore = 3
  p4.timestore = 3
  passengers = [p2, p1, p4, p3]
  ct = 0
  numpass = len(passengers)
  while ct < numpass:
    for passenger in passengers:
      if passenger.ent == False and seating[passenger.y, passenger.x] == 0:
        seating[passenger.y, passenger.x] = passenger.thisnum
        passenger.ent = True
        processes.append([passenger.passNum, "down"])
      elif passenger.ent == True:
        if passenger.colNum == passenger.x and passenger.rowNum == passenger.y:
          # passenger.sitDown(seating)
          if passenger.sit == False:
            processes.append([passenger.passNum, "sit"])
            passenger.sit = True
          tmp = 0
          for passenger in passengers:
            if passenger.sit == True:
              tmp += 1
          if tmp == numpass:
            ct = numpass
        elif passenger.rowNum != passenger.y and seating[passenger.y + 1, passenger.x] == 0:
          passenger.moveDown(seating, processes)
          seating[passenger.y - 1, passenger.x] = 0
          seating[passenger.y, passenger.x] = passenger.thisnum
        elif passenger.rowNum == passenger.y and passenger.timestore > 0:
          passenger.timestore = passenger.timestore - 1
          processes.append([passenger.passNum, "stow"])
        if passenger.timestore <= 0:
          if passenger.colNum < middle and seating[passenger.y, passenger.x - 1] == 0:
            if passenger.x != -1:
              passenger.moveLeft(seating, processes)
              seating[passenger.y, passenger.x + 1] = 0
              seating[passenger.y, passenger.x] = passenger.thisnum

          elif passenger.colNum != passenger.x and seating[passenger.y, passenger.x + 1] == 0:
            passenger.moveRight(seating, processes)
            seating[passenger.y, passenger.x - 1] = 0
            seating[passenger.y, passenger.x] = passenger.thisnum
    if ct != numpass:
      print(seating)
      print("-------------")
      # time.sleep(1)
    v.moveMultiple(processes)
    processes = []


runProgram(processes)
