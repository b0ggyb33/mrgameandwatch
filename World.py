__author__ = 'b0ggyb33'

positions={'LEFT':0,'MIDDLE':4,'RIGHT':7}
directions={'LEFT':-1, 'RIGHT':1}

import Actors

class World(object):
    def __init__(self):
        self.time = 0
        self.balls=[Actors.Ball() for i in xrange(1)]
        self.mgw = Actors.MrGameAndWatch()
        self.score=0

    def tick(self):
        self.time+=1

    def increaseScore(self):
        self.score+=10

    def update(self):
        self.tick()
        [actor.update() for actor in self.balls]
        for ball in self.balls:
            if ball.position == self.mgw.position:
                self.handleCollision(ball)

        self.checkBallStatus()

    def handleCollision(self,ball):
        self.increaseScore()
        if ball.velocity == directions['LEFT']:
            ball.velocity = directions['RIGHT']
        else:
            ball.velocity = directions['LEFT']

    def triggerEndGame(self):
        pass

    def checkBallStatus(self):
        if not all([ball.live for ball in self.balls]):
           self.triggerEndGame()