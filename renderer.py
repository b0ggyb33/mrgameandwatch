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
        mgwRight = pygame.image.load(os.path.join("art","mgw_right.png"))
        mgwLeft = pygame.image.load(os.path.join("art","mgw_left.png"))
        mgwMiddle = pygame.image.load(os.path.join("art","mgw_middle.png"))
        self.mgwPositions = [mgwLeft, mgwMiddle, mgwRight]
        self.mgwImageLocation = (self.width/2 - self.mgwImage.get_width()/2,self.height - self.mgwImage.get_height())

        self.crashLeft = pygame.image.load(os.path.join("art","crash_left.png"))
        self.crashRight = pygame.image.load(os.path.join("art","crash_right.png"))

        self.surface = pygame.Surface(self.screen.get_size())

        self.positions={0:[],1:[],2:[]}
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
        self.renderCrash()

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

    def renderCrash(self):
        if self.world.crash != 0:
            #crash has occured
            if self.world.crash>0: #RHS
                self.surface.blit(self.crashRight,self.mgwImageLocation)
            else:
                self.surface.blit(self.crashLeft,self.mgwImageLocation)

    def renderMGW(self):
        mgw = self.world.mgw
        mgwImageCopy = self.mgwImage.copy()
        mgwImageCopy.blit(self.mgwPositions[mgw.position],(0,0))

        self.surface.blit(mgwImageCopy,self.mgwImageLocation)
