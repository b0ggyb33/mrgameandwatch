import unittest
from World import positions,directions
import Actors

class testActor(unittest.TestCase):

    def setUp(self):
        self.actor = Actors.Actor()

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
        self.assertEqual(self.getPosition(),positions['LEFT'])

    def testMgwPositionIsFarLeftWhenMovedFromLeft(self):
        self.setPosition(positions['LEFT'])
        self.move(directions['LEFT'])
        self.assertEqual(self.getPosition(),positions['FLEFT'])

    def testMgwPositionCannotGoFurtherThanFLEFTWhenMovingLeft(self):
        self.setPosition(positions['FLEFT'])
        self.move(directions['LEFT'])
        self.assertEqual(self.getPosition(),positions['FLEFT'])

    def testMgwCanMoveRightFromMiddle(self):
        self.move(directions['RIGHT'])
        self.assertEqual(self.getPosition(),positions['RIGHT'])

    def testMgwCannotMoveBeyondFarRight(self):
        self.setPosition(positions['FRIGHT'])
        self.move(directions['RIGHT'])
        self.assertEqual(self.getPosition(),positions['FRIGHT'])

class testBall(testActor):
    def setUp(self):
        self.actor = Actors.Ball()

    def test_updateMovesBallRight(self):
        self.actor.update()
        self.assertEqual(positions['RIGHT'],self.actor.position)

    def test_updateMovesBallLeftWhenVelocityIsLeft(self):
        self.actor.velocity=directions['LEFT']
        self.actor.update()
        self.assertEqual(positions['LEFT'],self.actor.position)

    def test_updateFromFLEFTToTheLeftMovesBallAndSetsStatusToFalse(self):
        self.actor.velocity=directions['LEFT']
        self.actor.position=positions['FLEFT']
        self.actor.update()
        self.assertEqual(self.actor.live,False)

    def test_updateFromMiddleToLeftMovesBallAndSetsStatusToTrue(self):
        self.actor.velocity=directions['LEFT']
        self.actor.update()
        self.assertEqual(self.actor.live,True)