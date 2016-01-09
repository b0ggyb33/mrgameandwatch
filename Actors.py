__author__ = 'b0ggyb33'
from World import positions,directions

class Actor(object):
    def __init__(self,limits):
        self.limits=limits
        self.position=positions['MIDDLE']
        self.live=True

    def move(self,direction):
        newPosition = self.position+direction
        if self.limits[0] <= newPosition <= self.limits[1]:
            self.position = newPosition
            return True
        else:
            return False

class Ball(Actor):
    def __init__(self,limits):
        super(Ball,self).__init__(limits)
        self.velocity=directions['RIGHT']

    def update(self):
        self.live = self.move(self.velocity)


class MrGameAndWatch(Actor):
    def __init__(self,limits):
        super(MrGameAndWatch,self).__init__(limits)

    def update(self):
        pass