import pygame
import pygame.gfxdraw,pygame.rect
import World

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

        self.ballColour=(0,255,0)
        self.ballRadius=5
        self.mgwColour=(0,0,255)
        self.mgwWidth=16
        self.mgwHeight=8
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
        self.surface.fill((0,0,0))
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
        self.surface.blit(font.render(string,True,(255,0,0)),position)

    def renderBalls(self):
        for ball in self.world.balls:
            location=int(ball.position *self.width/float(len(World.positions))) , self.height/2
            pygame.draw.circle(self.surface,self.ballColour,location,self.ballRadius)


    def renderMGW(self):
        mgw = self.world.mgw
        location=pygame.rect.Rect(int(mgw.position *self.width/float(len(World.positions))) - self.mgwWidth/2 , 3*self.height/4 - self.mgwHeight/2,self.mgwHeight,self.mgwWidth)
        pygame.draw.ellipse(self.surface,self.mgwColour,location)