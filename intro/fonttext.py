import pygame, sys
from pygame.locals import *

pygame.init()

# set window
DISPLAYSURF = pygame.display.set_mode((400,300))
pygame.display.set_caption('Hello World!')

# set colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# define font and render text
fontObj = pygame.font.Font('freesansbold.ttf',32)
textSurfaceObj = fontObj.render('Hello World!',True,GREEN,BLUE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200,150)

while True: # game loop
	DISPLAYSURF.fill(WHITE)
	DISPLAYSURF.blit(textSurfaceObj,textRectObj)
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()