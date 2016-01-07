__author__ = 'b0ggyb33'
from World import positions,directions

class Actor(object):
    def __init__(self):
        self.position=positions['MIDDLE']
        self.live=True

    def move(self,direction):
        newPosition = self.position+direction
        if positions['FLEFT'] <= newPosition <= positions['FRIGHT']:
            self.position = newPosition
            return True
        else:
            return False


class Ball(Actor):
    def __init__(self):
        super(Ball,self).__init__()
        self.velocity=directions['RIGHT']

    def update(self):
        self.live = self.move(self.velocity)

class MrGameAndWatch(Actor):
    def __init__(self):
        super(MrGameAndWatch,self).__init__()

    def update(self):
        pass