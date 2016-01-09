import unittest
from World import positions,directions
import Actors

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
        self.assertEqual(self.getPosition(),positions['MIDDLE'])

    def testMgwPositionIsLeftWhenMoved(self):
        self.move(directions['LEFT'])
        self.assertEqual(self.getPosition(),positions['MIDDLE']-1)

    def testMgwPositionIsFarLeftWhenMovedFromLeft(self):
        self.setPosition(positions['LEFT']+1)
        self.move(directions['LEFT'])
        self.assertEqual(self.getPosition(),positions['LEFT'])

    def testMgwPositionCannotGoFurtherThanFLEFTWhenMovingLeft(self):
        self.setPosition(positions['LEFT'])
        self.move(directions['LEFT'])
        self.assertEqual(self.getPosition(),positions['LEFT'])

    def testMgwCanMoveRightFromMiddle(self):
        self.move(directions['RIGHT'])
        self.assertEqual(self.getPosition(),positions['MIDDLE']+1)

    def testMgwCannotMoveBeyondFarRight(self):
        self.setPosition(positions['RIGHT'])
        self.move(directions['RIGHT'])
        self.assertEqual(self.getPosition(),positions['RIGHT'])

class testBall(testActor):
    def setUp(self):
        self.actor = Actors.Ball((positions['LEFT'],positions['RIGHT']))

    def test_updateMovesBallRight(self):
        self.actor.update()
        self.assertEqual(positions['MIDDLE']+1,self.actor.position)

    def test_updateMovesBallLeftWhenVelocityIsLeft(self):
        self.actor.velocity=directions['LEFT']
        self.actor.update()
        self.assertEqual(positions['MIDDLE']-1,self.actor.position)

    def test_updateFromLEFTToTheLeftMovesBallAndSetsStatusToFalse(self):
        self.actor.velocity=directions['LEFT']
        self.actor.position=positions['LEFT']
        self.actor.update()
        self.assertEqual(self.actor.live,False)

    def test_updateFromMiddleToLeftMovesBallAndStatusRemainsTrue(self):
        self.actor.velocity=directions['LEFT']
        self.actor.update()
        self.assertEqual(self.actor.live,True)

