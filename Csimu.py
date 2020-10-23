import numpy as np
import time
import random
from threading import *
import math
from PyView import *

capacity = 132
rows = 23
cols = 7
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

    self.seated = False

    self.x = middle
    self.y = 0
    self.left = False
    self.right = False
    self.ent = False
    self.thisnum = thisnum
    self.sit = False
    self.age = float(int(np.random.normal(39, 19.5, 1)))
    self.numbags = self.setbags()
    # print(self.age)
    self.atime = self.agetime(self.age)
#        print(self.atime)
    self.Bags = []
    trackofbags = 0
    for k in range(0, self.numbags - 1):
      self.Bags.append(Bag())
#            print(self.Bags[k].volume)
      trackofbags = trackofbags + (float(self.Bags[k].volume) / Vmin)
    self.timestore = self.numbags * (trackofbags + self.atime)
    #print("For passenger")
    # print(self.thisnum)
    # print("bags")
    # print(self.numbags)
    # print("vol")
    # print(trackofbags)
    #print("age time")
    # print(self.atime)
    # print("tot")
    # print(self.timestore)

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
    self.y += 1
    seating[self.y][self.x] = self.thisnum
    seating[self.y - 1][self.x] = '_'

    processes.append([self.passNum, "down"])

    return processes

    # time.sleep(1)

  def moveLeft(self, seating, processes):
    self.x -= 1
    seating[self.y][self.x] = self.thisnum
    seating[self.y][self.x + 1] = '_'

    processes.append([self.passNum, "left"])

    return processes

    # time.sleep(1)

  def moveRight(self, seating, processes):
    self.x += 1
    seating[self.y][self.x] = self.thisnum
    seating[self.y][self.x - 1] = '_'

    processes.append([self.passNum, "right"])

    return processes

    # time.sleep(1)

  def sitDown(self, seating, processes):
    self.seated = True
    self.thisNum = 's'
    seating[self.y][self.x] = self.thisNum
    processes.append([self.passNum, "sit"])
    return processes

  def display(self, seating):
    print(seating)
    print("------------------")

  def update(self, seating, processes):
    # Enter plane from top middle one at a time:
    if self.ent == False and seating[0][middle] == '_':
      self.ent = True
      seating[0][middle] == self.thisnum
      self.y -= 1
      processes = self.moveDown(seating, processes)

    # For each standing passenger in plane
    elif self.ent == True and self.seated == False:

      # At correct seat -> sit down
      if self.y == self.rowNum and self.x == self.colNum:
        processes = self.sitDown(seating, processes)

      # At correct row -> move to correct seat
      elif self.y == self.rowNum:

        # Stow bags
        if self.timestore > 0:
          self.timestore -= 1
          if self.x > self.colNum:
            processes.append([self.passNum, "stowL"])
          else:
            processes.append([self.passNum, "stowR"])
        # Move left
        elif self.x > self.colNum and isEmpty(seating, self.x - 1, self.y):
          processes = self.moveLeft(seating, processes)
        # Move right
        elif self.x < self.colNum and isEmpty(seating, self.x + 1, self.y):
          processes = self.moveRight(seating, processes)

      # Incorrect row -> move down
      elif self.y < self.rowNum and isEmpty(seating, self.x, self.y + 1):
        processes = self.moveDown(seating, processes)

    return processes


def isEmpty(arr, x, y):
  if arr[y][x] == 's' or arr[y][x] == '_':
    return True
  else:
    return False


def allSeated(arr):
  for p in arr:
    if p.seated == False:
      return False
  return True


def initSeating(rows, cols):
  seating = []
  for i in range(0, rows):
    seating.append([])
    for j in range(0, cols):
      seating[i].append('_')
  return seating

def manyPassengers(num, plane, views):

  # creates list of (num) passengers
  # (plane) indicates the number of rows and columns
  # for 132 seats, plane = [23, 7]
  # views corresponds to v.passengers

  seating = []

  for i in range(0, plane[0]):
    for j in range(0, plane[1]):
      if((i == 0 or i == plane[0] - 1) and (j == 0 or j == 1 or j == plane[1] - 1)):
        pass
      elif j != middle:
        seating.append([i, j])

  passengers = []

  for i in range(0, num):
    index = random.randint(0, len(seating) - 1)
    coord = seating[index]
    passengers.append(Passenger(coord[0], coord[1], 'X', views[i], i))
    seating.remove(coord)

  return passengers

# 132 seats, 23 rows, 6 seats per row (rows 1 and 23 have only 3 seats)


#p1 = Passenger(4, 0, 2, v.passengers[0], 0)
#p2 = Passenger(3, 4, 3, v.passengers[1], 1)
#p3 = Passenger(2, 3, 4, v.passengers[2], 2)
#p4 = Passenger(1, 1, 5, v.passengers[3], 3)


def runProgram(processes):

  print("Initializing values...")

  processes = processes
  v = View()
  v.addSprite(capacity)
  planeDimensions = [rows, cols]
  passengers = manyPassengers(capacity, planeDimensions, v.spriteGroup.sprites())
  v.moveMultiple(processes)
  processes = []

  seating = initSeating(rows, cols)

  for p in passengers:
    p.timestore = 3
  ct = 0
  numpass = len(passengers)

  v.timer = 0

  print("\nClick to Start")

  start = False
  while start == False:
    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN:
        start = True

  finished = False

  while finished == False:
    pygame.event.pump()
    processes = []
    for passenger in passengers:
      processes = passenger.update(seating, processes)
    finished = allSeated(passengers)
    v.moveMultiple(processes)

    # if ct != numpass:
    #  for line in seating:
    #    print(line)
    #  print("-------------")

    processes = []

  running = True
  while running == True:
    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN:
        pygame.quit()
        running = False


runProgram(processes)
