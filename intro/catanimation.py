import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30 # frames per second
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((400,300), 0, 32)
pygame.display.set_caption('Animation')

# set up vars
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
catImg = pygame.image.load('assets/img/cat.png')
catx = 0
caty = 0
direction = 'right'

while True: # game loop
	DISPLAYSURF.fill(WHITE)

	if direction == 'right':
		catx += 5
		if catx == 280:
			direction = 'down'
	
	elif direction == 'down':
		caty += 5
		if caty == 225:
			direction = 'left'

	elif direction == 'left':
		catx -= 5
		if catx < 0:
			direction = 'up'

	elif direction == 'up':
		caty -= 5
		if caty == 0:
			direction = 'right'

	DISPLAYSURF.blit(catImg, (catx,caty))

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	pygame.display.update()
	fpsClock.tick(FPS)