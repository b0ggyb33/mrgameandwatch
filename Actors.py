__author__ = 'b0ggyb33'
from World import positions,directions

class Actor(object):
    def __init__(self,limits,initialPosition=None):
        self.limits=limits
        if initialPosition == directions['LEFT']:
            self.position = self.limits[0]
        elif initialPosition == directions['RIGHT']:
            self.position = self.limits[1]
        else:
            self.position=int((self.limits[0]+self.limits[1]) / 2)
        self.live=True

    def move(self,direction):
        newPosition = self.position+direction
        if self.limits[0] <= newPosition <= self.limits[1]:
            self.position = newPosition
            return True
        else:
            return False

class Ball(Actor):
    def __init__(self,limits,initialPosition=None,track=0):
        super(Ball,self).__init__(limits,initialPosition)
        if initialPosition == directions['RIGHT']:
            self.velocity = directions['LEFT']
        else:
            self.velocity = directions['RIGHT']

        self.track=track
        self.hasBeenScored=True

    def atLimit(self):
        if self.position in self.limits:
            return True
        else:
            return False

    def update(self):
        self.hasBeenScored=False
        self.live = self.move(self.velocity)

    def changeDirection(self):
        if self.velocity == directions['LEFT']:
            self.velocity = directions['RIGHT']
        else:
            self.velocity = directions['LEFT']


class MrGameAndWatch(Actor):
    def __init__(self,limits,initialPosition=None):
        super(MrGameAndWatch,self).__init__(limits,initialPosition)

    def update(self):
        pass