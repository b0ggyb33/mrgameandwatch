__author__ = 'b0ggyb33'

positions={'LEFT':0,'MIDDLE':4,'RIGHT':7}
directions={'LEFT':-1, 'RIGHT':1}

import Actors

class World(object):
    def __init__(self):
        self.time = 0
        self.balls=[Actors.Ball((positions['LEFT'],positions['RIGHT']),directions['RIGHT']) for i in xrange(1)]
        self.mgw = Actors.MrGameAndWatch((0,2),directions['LEFT'])
        self.score=0
        self.speed=30

    def tick(self):
        self.time+=1

    def increaseScore(self):
        self.score+=10

    def update(self,keyPress=None):
        self.tick()

        if keyPress:
            self.mgw.move(keyPress)

        if self.time%self.speed==0:
            [actor.update() for actor in self.balls]
            [self.handleCollision(ball) for ball in self.balls]

        return self.checkBallStatus()

    def handleCollision(self,ball):
        if ball.atLimit():
                if ball.position == ball.limits[1]:
                    if self.mgw.position == self.mgw.limits[0]:
                        self.increaseScore()
                        ball.changeDirection()
                else: #lower
                    if self.mgw.position == self.mgw.limits[1]:
                        self.increaseScore()
                        ball.changeDirection()



    def triggerEndGame(self):
        self.score = 0

    def checkBallStatus(self):
        if not all([ball.live for ball in self.balls]):
           self.triggerEndGame()
           return True
        return False