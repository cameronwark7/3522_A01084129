# initialize with random values
import math
import random
import datetime
import time

'''
Asteroid class for creating asteroid objects
'''
class Asteroid:
    id = 1

    def __init__(self):
        self._ccmf = self.randCcmf()
        self._pos = (random.randint(0, 100), random.randint(0, 100), random.randint(0, 100))
        self._oldPos = ()
        self._vel = (random.randint(1, 5), random.randint(1, 5), random.randint(1, 5))
        self._id = self.addID()

    def move(self):
        curPos = self.getPos()
        curVel = self.getVel()
        newPos = (curPos[0] + curVel[0], curPos[1] + curVel[1], curPos[2] + curVel[2])
        self.setPos(newPos)
        self.__str__()

    def randCcmf(self):
        rad = random.randint(0, 4000)/1000
        ccmf = (2*math.pi*rad)
        return ccmf

    def addID(self):
        val = Asteroid.id
        Asteroid.id = Asteroid.id + 1
        return val

    def __str__(self):
        myString = 'Asteroid {0} has moved! Old Pos: {1}, {2}, {3} -> '\
                    'New Pos: {4}, {5}, {6}\nAsteroid {0} is currently at {4}, {5}, {6}' \
                   ' and is moving at {7}, {8}, {9} meters per second. ' \
                   'It has a circumference of {10}'\
                    .format(self._id, self._oldPos[0], self._oldPos[1], self._oldPos[2],
                            self._pos[0], self._pos[1], self._pos[2],
                            self._vel[0], self._vel[1], self._vel[2],
                            self._ccmf)
        print(myString)

    def getPos(self):
        return self._pos

    def getVel(self):
        return self._vel

    def setPos(self, new):
        self._oldPos = self._pos
        self._pos = new

class Controller:
    def __init__(self, i):
        self._asteroids = self.createAList(i)
        self._numAsteroids = i

    def createAList(self, i):
        aList = []
        for x in range(i - 1):
            aList.append(Asteroid())
        return aList

    def simulate(self, seconds):
        endTime = datetime.datetime.now() + datetime.timedelta(seconds=seconds)

        while datetime.datetime.now() < endTime:
            self.aggrMove()
            time.sleep(1)

    def aggrMove(self):
        for x in self._asteroids:
            x.move()

c = Controller(10)
c.simulate(4)