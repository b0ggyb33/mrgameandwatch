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

        #for putting sprites on the main window
        self.mainWindowGroup = pygame.sprite.OrderedUpdates()

        #self.mainView = Viewport(width, height, self, b2Vec2(0, 0))

        #self.mainWindowGroup.add(self.mainView)


    def update(self):
        self.mainWindowGroup.update()
        #draw the scene
        dirty = self.mainWindowGroup.draw(self.screen)
        pygame.display.update(dirty)
        return True



    def renderScore(self,screen):
        fontSize=16
        font = pygame.font.Font(None,fontSize)
        position = (0,0)
        for player in self.world.players:
            string = "Player: "+str(player.getScore())
            position=(position[0],position[1]+fontSize)
            screen.blit(font.render(string,True,player.getColour()),position)


