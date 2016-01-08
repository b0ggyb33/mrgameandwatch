import pygame
import pygame.gfxdraw,pygame.rect


class Renderer(object):
    """Handles all GUI related stuff"""
    is_event_handler = True

    def __init__(self,gameWorld, width, height):
        '''
        Constructor -
        sets up pygame
        creates the pygame window of the width and height
        '''

        self.world=gameWorld

        self.width = width
        self.height = height

        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("MrGameAndWatch")

        self.surface = pygame.Surface(self.screen.get_size())


    def update(self):
        #draw the scene
        self.draw()
        pygame.display.update()

        return True

    def draw(self):
        self.renderScore()

        self.screen.blit(self.surface,(0,0))

    def renderScore(self):
        fontSize=16
        font = pygame.font.Font(None,fontSize)
        position = (0,0)

        string = str(self.world.score)
        position=(position[0],position[1]+fontSize)
        self.surface.blit(font.render(string,True,(255,0,0)),position)


