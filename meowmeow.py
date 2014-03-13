import pygame, sys, time 
from pygame.locals import *

pygame.init()

FPS = 30 # frames per second
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((400,300), 0, 32)
pygame.display.set_caption('Beeping Animation')

# set up vars
WHITE = (255,255,255)
catImg = pygame.image.load('assets/img/cat.png')
sound = pygame.mixer.Sound('assets/audio/cat.wav')
catx = 0
caty = 0
direction = 'right'

while True: # game loop
	DISPLAYSURF.fill(WHITE)

	if (catx == -5 and caty == 0) or \
	   (catx == -5 and caty == 225) or \
	   (catx == 280 and caty == 0) or \
	   (catx == 280 and caty == 225):
		sound.play()
		# time.sleep(1) # wait one second
		# sound.stop()

	if catx < 280 and caty == 0:
		catx += 5

	elif catx == 280 and caty < 225:
		caty += 5

	elif catx > -5 and caty == 225:
		catx -= 5

	elif catx == -5 and caty > 0:
		caty -= 5

	DISPLAYSURF.blit(catImg, (catx,caty))
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	pygame.display.update()
	fpsClock.tick(FPS)