import pygame, sys, time
from pygame.locals import *

pygame.init()

# set window
DISPLAYSURF = pygame.display.set_mode((400,300))
pygame.display.set_caption('Beep!')

# set colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# load sound
sound = pygame.mixer.Sound('assets/audio/beeps.wav')

while True: # game loop
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	sound.play()
	time.sleep(1) # wait one second
	sound.stop()
	pygame.display.update()