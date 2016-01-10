__author__ = 'b0ggyb33'

positions={'LEFT':0,'MIDDLE':4,'RIGHT':7}
directions={'LEFT':-1, 'RIGHT':1}

import Actors

class World(object):
    def __init__(self):
        self.time = 0
        track0Ball = Actors.Ball((positions['LEFT'],positions['RIGHT']),directions['RIGHT'],0)
        track1Ball = Actors.Ball((positions['LEFT'],9),directions['LEFT'],1)
        track2Ball = Actors.Ball((positions['LEFT'],11),directions['RIGHT'],2)
        self.balls=[track0Ball,track1Ball,track2Ball]
        self.mgw = Actors.MrGameAndWatch((0,2),directions['LEFT'])
        self.score=0
        self.speed=30
        self.crash=0
        self.timeOfLastUpdate=0

        #controls 'difficulty'
        self.updateSpeedFrequency=200

    def tick(self):
        self.time+=1

    def increaseScore(self):
        self.score+=10

    def update(self,keyPress=None):
        self.tick()

        if keyPress:
            self.mgw.move(keyPress)

        if self.time - self.timeOfLastUpdate >= self.speed:
            [actor.update() for actor in self.balls]
            self.timeOfLastUpdate = self.time

        [self.handleCollision(ball) for ball in self.balls]

        if (self.time%self.updateSpeedFrequency == 0)  and self.speed >= 1:
            self.speed -= 1

        return self.checkBallStatus()

    def handleCollision(self,ball):
        if not ball.hasBeenScored and ball.atLimit():
                if ball.track == 0:
                    if ball.position == ball.limits[1]:
                        if self.mgw.position == self.mgw.limits[0]:
                            self.collisionEvents(ball)
                    else: #lower
                        if self.mgw.position == self.mgw.limits[1]:
                            self.collisionEvents(ball)
                elif ball.track ==1:
                    if self.mgw.position not in self.mgw.limits:
                        self.collisionEvents(ball)
                elif ball.track == 2:
                    if ball.position == ball.limits[1]:
                        if self.mgw.position == self.mgw.limits[1]:
                            self.collisionEvents(ball)
                    else: #lower
                        if self.mgw.position == self.mgw.limits[0]:
                            self.collisionEvents(ball)

    def collisionEvents(self, ball):
        self.increaseScore()
        ball.changeDirection()
        ball.hasBeenScored = True

    def triggerEndGame(self,direction):
        self.crash = direction

    def checkBallStatus(self):
        for ball in self.balls:
            if not ball.live:
                self.triggerEndGame(ball.velocity)
                return True
        return False