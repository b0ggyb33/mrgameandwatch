__author__ = 'b0ggyb33'
import pygame
import renderer
import World

class MrGameAndWatch(object):
    def __init__(self):

        self.fps=30

        pygame.init()

        self.world = World.World()
        self.renderer = renderer.Renderer(self.world,272, 208)

        clock = pygame.time.Clock()
        done=False
        while not done:
            clock.tick(self.fps)
            done = self.update()
        pygame.quit()

    def update(self):

        keyPress=None

        for event in pygame.event.get(): # User did something
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    keyPress = World.directions['LEFT']
                elif event.key == pygame.K_RIGHT:
                    keyPress = World.directions['RIGHT']
            if event.type == pygame.QUIT: # If user clicked close
                return True

        status = self.world.update(keyPress)
        self.renderer.update()

        return status

if __name__ == "__main__":
    game=MrGameAndWatch()