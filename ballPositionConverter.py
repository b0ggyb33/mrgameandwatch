track0={0:(51,128),1:(56,101),2:(60,81),3:(68,61),4:(77,61),5:(85,81),6:(88,101),7:(93,128)}

track1={0:(41,128),1:(42,103),2:(48,76),3:(55,53),4:(68,43),5:(78,43),6:(86,53), 7:(94,76),8:(98,103),9:(102,128)}

track2={0:(32,128),1:(32,100),2:(36,78),3:(42,54),4:(53,35),5:(66,28),6:(77,28), 7:(88,35),8:(98,54),9:(105,78),10:(110,100),11:(113,128)}

import cv2
import numpy as np

balls=np.ones((168,144,3))*255
balls[1:-1,1:-1]=(0,0,0)

def drawBalls(ballPositions):
    for x,y in ballPositions.values():
        try:
            balls[y,x] = (255,255,255)
        except IndexError:
            pass

drawBalls(track0)
drawBalls(track1)
drawBalls(track2)

    
cv2.imwrite("balls.png",balls)

def printOutPositions(ballPositions):
    xString = "positions0x[8] = {"
    yString = "positions0y[8] = {"
    for x,y in ballPositions.values():
        xString+=str(x)+","
        yString+=str(y)+","
    xString = xString[:-1]+"};"
    yString = yString[:-1]+"};"
    print xString
    print yString

printOutPositions(track0)
printOutPositions(track1)
printOutPositions(track2)


