import unittest
from World import directions
import Actors
positions={'LEFT':0,'RIGHT':7}

class testActor(unittest.TestCase):

    def setUp(self):
        self.actor = Actors.Actor((positions['LEFT'],positions['RIGHT']))

    def getPosition(self):
        return self.actor.position

    def move(self,direction):
        self.actor.move(direction)

    def setPosition(self,newPosition):
        self.actor.position = newPosition

    def testMgwPositionIsCentre(self):
        self.assertEqual(self.getPosition(),positions['LEFT']+positions['RIGHT']/2)

    def testMgwPositionIsLeftWhenMoved(self):
        self.setPosition(5)
        self.move(directions['LEFT'])
        self.assertEqual(self.getPosition(),4)

    def testMgwPositionIsFarLeftWhenMovedFromLeft(self):
        self.setPosition(positions['LEFT']+1)
        self.move(directions['LEFT'])
        self.assertEqual(self.getPosition(),positions['LEFT'])

    def testMgwPositionCannotGoFurtherThanFLEFTWhenMovingLeft(self):
        self.setPosition(positions['LEFT'])
        self.move(directions['LEFT'])
        self.assertEqual(self.getPosition(),positions['LEFT'])

    def testMgwCanMoveRightFromMiddle(self):
        initialPosition = self.getPosition()
        self.move(directions['RIGHT'])
        self.assertEqual(self.getPosition(),initialPosition+1)

    def testMgwCannotMoveBeyondFarRight(self):
        self.setPosition(positions['RIGHT'])
        self.move(directions['RIGHT'])
        self.assertEqual(self.getPosition(),positions['RIGHT'])

    def testWhenInitialisedWithALEFTDirectionThenActorStartsAtLeftLimit(self):
        actor = Actors.Actor((positions['LEFT'],positions['RIGHT']),directions['LEFT'])
        self.assertEqual(actor.position,positions['LEFT'])

    def testWhenInitialsedWithARIGHTDirectionThenActorStartsRight(self):
        actor = Actors.Actor((positions['LEFT'],positions['RIGHT']),directions['RIGHT'])
        self.assertEqual(actor.position,positions['RIGHT'])

class testBall(testActor):
    def setUp(self):
        self.actor = Actors.Ball((positions['LEFT'],positions['RIGHT']))

    def test_updateMovesBallRight(self):
        self.setPosition(4)
        self.actor.update()
        self.assertEqual(5,self.actor.position)

    def test_updateMovesBallLeftWhenVelocityIsLeft(self):
        self.setPosition(4)
        self.actor.velocity=directions['LEFT']
        self.actor.update()
        self.assertEqual(3,self.actor.position)

    def test_updateFromLEFTToTheLeftMovesBallAndSetsStatusToFalse(self):
        self.actor.velocity=directions['LEFT']
        self.actor.position=positions['LEFT']
        self.actor.update()
        self.assertEqual(self.actor.live,False)

    def test_updateFromMiddleToLeftMovesBallAndStatusRemainsTrue(self):
        self.actor.velocity=directions['LEFT']
        self.actor.update()
        self.assertEqual(self.actor.live,True)

    def test_velocityIsSetProperlyWhenBallInitialisesAtRightLimit(self):
        ball = Actors.Ball((positions['LEFT'],positions['RIGHT']),directions['RIGHT'])
        self.assertEqual(ball.velocity,directions['LEFT'])

    def atLimitsReturnsTrueWhenPositionIsRIGHT(self):
        ball = Actors.Ball((positions['LEFT'],positions['RIGHT']),directions['RIGHT'])
        self.assertTrue(ball.atLimit())

    def atLimitsReturnsFalseWhenPositionIsRIGHTAndUpdate(self):
        ball = Actors.Ball((positions['LEFT'],positions['RIGHT']),directions['RIGHT'])
        ball.update()
        self.assertFalse(ball.atLimit())
