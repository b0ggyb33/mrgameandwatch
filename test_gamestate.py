__author__ = 'b0ggyb33'

import unittest
import mock
from Actors import Ball
import World



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
        self.assertEqual(self.world.balls[0].position,World.positions['MIDDLE'])
        self.updateWorld()
        self.assertEqual(self.world.balls[0].position,World.positions['RIGHT'])

    def test_whenABallAndMrGameAndWatchCollideScoreIncreases(self):
        self.setMGWposition(World.positions['FRIGHT'])
        self.updateWorld()
        self.updateWorld()
        self.assertEqual(self.world.score,10)

    def test_whenABallDiesGameEnds(self):
        self.world.triggerEndGame = mock.MagicMock(return_value=True)

        self.updateWorld() #middle -> right
        self.assertFalse(self.world.triggerEndGame.called)
        self.updateWorld() #right ->far right
        self.assertFalse(self.world.triggerEndGame.called)
        self.updateWorld() #out of game
        self.assertTrue(self.world.triggerEndGame.called)

    def test_whenBallCollidesItTurnsRound(self):
        self.world.balls[0].position=World.positions['RIGHT']
        self.setMGWposition(World.positions['FRIGHT'])
        self.updateWorld()
        self.assertEqual(self.world.balls[0].velocity,World.directions['LEFT'])
        self.updateWorld()
        self.assertEqual(self.world.balls[0].position,World.positions['RIGHT'])