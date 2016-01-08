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
        while True:
            clock.tick(self.fps)
            self.update()
            #if we leave the loop tidy up all the shizzle

    def update(self):
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                pygame.quit()

if __name__ == "__main__":
    pygameInterface()