# Memory Puzzle 
# Originally By Al Sweigart al@inventwithpython.com
# http://inventwithpython.com/pygame
# Released under a "Simplified BSD" license

import random, pygame, sys
from pygame.locals import *

FPS = 30 # frames per second
WINDOWWIDTH = 640 # window size in pixels
WINDOWHEIGHT = 480 # window size in pixels
REVEALSPEED = 8 # slide animation speed
TILESIZE = 40 # height and width of tiles in pixels
GAPSIZE = 10 # padding between tiles in pixels
BOARDWIDTH = 10 # number of tile columns
BOARDHEIGHT = 7 # number of tile rows
assert (BOARDHEIGHT * BOARDWIDTH) % 2 == 0, "Board needs to have an even amount of tiles for pairs of matches."
XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (TILESIZE + GAPSIZE))) / 2)
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * (TILESIZE + GAPSIZE))) / 2)

#            R    G    B
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)

BGCOLOR = NAVYBLUE
LIGHTBGCOLOR = GRAY
TILECOLOR = WHITE
HIGHLIGHTCOLOR = BLUE

DONUT = 'donut'
SQUARE = 'square'
DIAMOND = 'diamond'
LINES = 'lines'
OVAL = 'oval'

ALLCOLORS = (RED,GREEN,BLUE,YELLOW,ORANGE,PURPLE,CYAN)
ALLSHAPES = (DONUT,SQUARE,DIAMOND,LINES,OVAL)
assert len(ALLCOLORS) * len(ALLSHAPES) * 2 >= BOARDWIDTH * BOARDHEIGHT, "Board is too big for the number of shapes/colors defined."

def main():
	global FPSCLOCK, DISPLAYSURF
	pygame.init()
	FPSCLOCK = pygame.time.Clock()
	DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))

	mousex = 0 # stores x coordinate of mouse event
	mousey = 0 # stores y coordinate of mouse event
	pygame.display.set_caption('Memory Game')

	mainBoard = getRandomizedBoard()
	revealedTiles = generateRevealedTilesData(False)
	firstSelection = None # stores the (x,y) of first tile selected
	startGameAnimation(mainBoard)

	while True: # game loop
		mouseClicked = False

		DISPLAYSURF.fill(BGCOLOR) # drawing the window
		drawBoard(mainBoard, revealedTiles)

		for event in pygame.event.get(): # event handling loop
			if event.type == QUIT or \
			  (event.type == KEYUP and event.key == K_ESCAPE):
				pygame.quit()
				sys.exit()

			elif event.type == MOUSEMOTION:
				mousex, mousey = event.pos

			elif event.type == MOUSEBUTTONUP:
				mousex, mousey = event.pos
				mouseClicked = True

		tilex, tiley = getTileAtPixel(mousex,mousey)
		if tilex != None and tiley != None:
			# mouse is on a tile
			if not revealedTiles[tilex][tiley]:
				drawHighlightTile(tilex,tiley)
			if not revealedTiles[tilex][tiley] and mouseClicked:
				revealTilesAnimation(mainBoard, [(tilex,tiley)])
				revealedTiles[tilex][tiley] = True # set the tile as revealed
				if firstSelection == None: # the current tile was first clicked
					firstSelection = (tilex,tiley) # set current tile as first
				else:
					#check if there is a match between two icons
					icon1shape, icon1color = getShapeAndColor(mainBoard, firstSelection[0], firstSelection[1])
					icon2shape, icon2color = getShapeAndColor(mainBoard, tilex, tiley)

					if icon1shape != icon2shape or icon1color != icon2color:
						# icons don't match. Cover both selections
						pygame.time.wait(1000) # wait one second
						coverTilesAnimation(mainBoard, [(firstSelection[0],firstSelection[1]),(tilex,tiley)])
						revealedTiles[firstSelection[0]][firstSelection[1]] = False
						revealedTiles[tilex][tiley]

					elif hasWon(revealedTiles): # check if all pairs found
						gameWonAnimation(mainBoard)
						pygame.time.wait(2000) # wait two seconds

						# Reset Board
						mainBoard = getRandomizedBoard()
						revealedTiles = generateRevealedTilesData(False)

						# Show fully unrevealed board for a second
						drawBoard(mainBoard, revealedTiles)
						pygame.display.update()
						pygame.time.wait(1000) # one second

						# Replay the start of game animation
						startGameAnimation(mainBoard)
					firstSelection = None # reset selection

		# Redraw screen and wait a clock tick
		pygame.display.update()
		FPSCLOCK.tick(FPS)


def getRandomizedBoard():
	# get list of every shape/color permutation
	icons = []
	for color in ALLCOLORS:
		for shape in ALLSHAPES:
			icons.append((shape,color))

	# randomize order of icons and
	# calculate how many icons are needed
	random.shuffle(icons) 
	numIconsUsed = int(BOARDWIDTH * BOARDHEIGHT / 2)
	icons = icons[:numIconsUsed] * 2 # make a pair of each icon
	random.shuffle(icons)

	# create the board data structure, with randomly placed icons
	board = []
	for x in range(BOARDWIDTH):
		column = []
		for y in range(BOARDHEIGHT):
			column.append(icons[0])
			del icons[0] # remove icons as we place them on board
		board.append(column)
	return board

def generateRevealedTilesData(val):
	revealedTiles = []
	for i in range(BOARDWIDTH):
		revealedTiles.append([val] * BOARDHEIGHT)
		return revealedTiles

def drawBoard():
	# implement

def startGameAnimation():
	# implement

def getTileAtPixel():
	# implement

def drawHighlightTile():
	# implement

def revealTilesAnimation():
	# implement

def getShapeAndColor():
	# implement

def coverTilesAnimation():
	# implement

def hasWon():
	# implement

def gameWonAnimation():
	# implement