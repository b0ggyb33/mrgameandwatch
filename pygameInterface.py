__author__ = 'b0ggyb33'
import pygame
import renderer
import World

class pygameInterface(object):
    def __init__(self):


        self.fps=1/30.

        pygame.init()
        # Input handling
        self.keys_pressed = set()

        self.world = World.World()

        self.renderer = renderer.Renderer(self.world,600, 800)

        clock = pygame.time.Clock()
        done=False
        while not done:
            clock.tick(30)
            done = self.update()
            #if we leave the loop tidy up all the shizzle
        pygame.quit()

    def update(self):

        self.renderer.update()
        self.world.update()

        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                return True
        return False

if __name__ == "__main__":
    p=pygameInterface()