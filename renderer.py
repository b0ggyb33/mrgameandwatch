import pygame
import pygame.gfxdraw,pygame.rect
import os
import World
BLACK = (0,0,0)
BCKGRND = (196,211,130)

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

        self.ballColour=BLACK
        self.ballRadius=5
        self.mgwColour=BLACK

        self.mgwImage = pygame.image.load(os.path.join("art","mrGameAndWatch.png"))

        self.surface = pygame.Surface(self.screen.get_size())

        self.positions={}
        for name,value in World.positions.items():
            self.positions[name]=value*self.width/float(len(World.positions))



    def update(self):
        #draw the scene
        self.draw()
        pygame.display.update()

        return True

    def draw(self):
        self.surface.fill(BCKGRND)
        self.renderScore()
        self.renderBalls()
        self.renderMGW()

        self.screen.blit(self.surface,(0,0))

    def renderScore(self):
        fontSize=16
        font = pygame.font.Font(None,fontSize)
        position = (0,0)

        string = str(self.world.score)
        position=(position[0],position[1]+fontSize)
        self.surface.blit(font.render(string,True,BLACK),position)

    def renderBalls(self):
        for ball in self.world.balls:
            location=int(ball.position *self.width/float(World.positions['RIGHT']+1)) , self.height/2
            pygame.draw.circle(self.surface,self.ballColour,location,self.ballRadius)


    def renderMGW(self):
        mgw = self.world.mgw

        self.surface.blit(self.mgwImage,(self.width/2 - self.mgwImage.get_width()/2,self.height - self.mgwImage.get_height()))
