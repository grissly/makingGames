import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30 # frames per second
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((400,300), 0, 32)
pygame.display.set_caption('Animation')

# set up vars
WHITE = (255,255,255)
catImg = pygame.image.load('assets/img/cat.png')
sound = pygame.mixer.Sound('assets/audio/cat.wav')
catx = 0
caty = 0
direction = 'right'

while True: # game loop
	DISPLAYSURF.fill(WHITE)

	if direction == 'right':
		catx += 5
		if catx == 280:
			direction = 'down'
			sound.play()
	
	elif direction == 'down':
		caty += 5
		if caty == 225:
			direction = 'left'
			sound.play()

	elif direction == 'left':
		catx -= 5
		if catx < 0:
			direction = 'up'
			sound.play()

	elif direction == 'up':
		caty -= 5
		if caty == 0:
			direction = 'right'
			sound.play()

	DISPLAYSURF.blit(catImg, (catx,caty))

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	pygame.display.update()
	fpsClock.tick(FPS)