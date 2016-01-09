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

        self.ballRadius=5

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
        track0={0:(103,140),1:(108,110),2:(114,85),3:(126,70),4:(139,70),5:(152,85),6:(162,110),7:(171,140)}
        track1={0:(88,140),1:(92,110),2:(100,85),3:(110,60),4:(127,50),5:(145,50),6:(162,60), 7:(173,85),8:(182,110),9:(185,140)}
        track2={0:(68,140),1:(72,120),2:(80,100),3:(88,80),4:(102,60),5:(122,50),6:(149,50), 7:(168,60),8:(184,80),9:(192,100),10:(200,120),11:(204,140)}

        self.ballPositions=[track0,track1,track2]



    def update(self):
        #draw the scene
        self.draw()
        pygame.display.update()

        return True

    def draw(self):
        self.surface.fill(BCKGRND)
        self.renderScore()
        self.renderMGW()
        self.renderBalls()
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
            #location=int(ball.position *self.width/float(World.positions['RIGHT']+1)) , self.mgwImageLocation[1] + 26 - self.ballRadius - 100 + (abs(5-ball.position))*40
            track = self.ballPositions[ball.track]
            pygame.draw.circle(self.surface,BLACK,track[ball.position],self.ballRadius)

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
