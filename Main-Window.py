import pygame
from sys import exit
from copy import deepcopy
from math import floor

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True



def newQue():

	returnList = [
		"long",
		"square",
		"tee",
		"zeeL",
		"zeeR",
		"L",
		"J"
	]



class pieceClass():

	def __init__(self):

		self.blocks = []
		self.setup_pieceData(board.size)


	def setup_pieceData(self, size):
		# [y pos, x pos]
		pieceData = {}

		width = size[0]
		height = size[1] -1

		pieceData["long"] = [
			[height, floor(width/2)-2],
			[height, floor(width/2)-1],
			[height, floor(width/2)],
			[height, floor(width/2)+1]
		]

		pieceData["square"] = [
			[height, floor(width/2)-1],
			[height, floor(width/2)],
			[height-1, floor(width/2)-1],
			[height-1, floor(width/2)]
		]

		pieceData["tee"] = [
			[height, floor(width/2)-1],
			[height, floor(width/2)],
			[height-1, floor(width/2)],
			[height, floor(width/2)+1]
		]

		pieceData["zeeL"] = [
			[height, floor(width/2)-1],
			[height-1, floor(width/2)-1],
			[height-1, floor(width/2)],
			[height-1, floor(width/2)+1]
		]

		pieceData["zeeR"] = [
			[height, floor(width/2)-1],
			[height, floor(width/2)],
			[height-1, floor(width/2)],
			[height, floor(width/2)+1]
		]



class boardClass():

	def __init__(self, size):

		self.size = size

		tempList1 = []
		for i in range(size[0]):
			tempList1.append(0)
		
		tempList2 = []
		for i in range(size[1]):
			tempList2.append(deepcopy(tempList1))
		
		self.data = deepcopy(tempList2)



FPS = 60
currentFrame = 0
lastFrameDown = 0

board = boardClass([10, 20])


while running:

	currentFrame += 1



	for event in pygame.event.get():


		if event.type == pygame.QUIT:

			running = False
			exit()





	pygame.display.update()
	clock.tick(60)

