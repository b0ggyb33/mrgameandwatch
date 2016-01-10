__author__ = 'b0ggyb33'

import unittest
import mock
from Actors import Ball,MrGameAndWatch
import World
positions={'LEFT':0,'RIGHT':7}


class testWorld(unittest.TestCase):

    def setUp(self):
        self.world=World.World()

    def updateWorld(self):
        self.world.update()

    def setMGWposition(self,position):
        self.world.mgw.position=position

    def test_timeUpdates(self):
        self.updateWorld()
        self.assertEqual(self.world.time,1)

    def test_BallUpdatesToRightInitially(self):
        self.assertEqual(self.world.balls[0].position,positions['RIGHT'])
        self.updateWorld()
        self.assertEqual(self.world.balls[0].position,positions['RIGHT']-1)

    def test_whenABallDiesGameEnds(self):
        self.world.triggerEndGame = mock.MagicMock(return_value=True)
        self.setMGWposition(positions['RIGHT'])
        for i in xrange(8):
            self.assertFalse(self.world.triggerEndGame.called)
            self.updateWorld()

        self.assertTrue(self.world.triggerEndGame.called)

    def test_whenABallAndMrGameAndWatchAtLEFTCollideBallTurnsRound(self):
        self.world.balls[0].position = self.world.balls[0].limits[0] #set to lower limit
        self.world.mgw.position = self.world.mgw.limits[1]
        self.world.handleCollision(self.world.balls[0])
        self.assertEqual(self.world.score,10)

    def test_whenABallAndMrGameAndWatchAtRIGHTCollideBallTurnsRound(self):
        self.world.balls[0].position = self.world.balls[0].limits[1]  #set to upper limit
        self.world.balls[0].velocity = World.directions['RIGHT']
        self.world.mgw.position = self.world.mgw.limits[0]
        self.world.handleCollision(self.world.balls[0])
        self.assertEqual(self.world.score,10)

