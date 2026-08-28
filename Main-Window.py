import pygame
from sys import exit
from copy import deepcopy
from math import floor
import random

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()


class queClass():
	def __init__(self):
		self.newQue()
	

	def newQue(self):

		returnList = [
			"long",
			"square",
			"tee",
			"zeeL",
			"zeeR",
			"L",
			"J"
		]
		self.que = returnList
	

	def shuffle(self):
		self.que = random.shuffle(self.que)

que = queClass()



class pieceClass():

	def __init__(self, typeInput=None):

		self.pieceData = self.setup_pieceData(boardSize)

		if typeInput == None:
			self.type = self.takeFromQue()
		else:
			self.type = typeInput
		self.blocks = self.setup_pieceData(board.size)[type]


	def setup_pieceData(self, size):
		# [y pos, x pos]
		pieceData = {}

		width = size[0]
		height = size[1] -1
		mid = floor(width/2)

		pieceData["long"] = [
			[height, mid-2],
			[height, mid-1],
			[height, mid],
			[height, mid+1]
		]

		pieceData["square"] = [
			[height, mid],
			[height-1, mid],
			[height, mid+1],
			[height-1, mid+1]
		]

		pieceData["tee"] = [
			[height, mid-1],
			[height, mid],
			[height-1, mid],
			[height, mid+1]
		]

		pieceData["zeeL"] = [
			[height, mid-1],
			[height, mid],
			[height-1, mid],
			[height-1, mid+1]
		]

		pieceData["zeeR"] = [
			[height-1, mid-1],
			[height-1, mid],
			[height, mid],
			[height, mid+1]
		]

		pieceData["L"] = [
			[height-1, mid-1],
			[height, mid-1],
			[height, mid],
			[height, mid+1]
		]

		pieceData["J"] = [
			[height, mid-1],
			[height, mid],
			[height, mid+1],
			[height-1, mid+1]
		]

		return pieceData
	

	def takeFromQue(self):
		if len(que.que) == 0:
			que.newQue()
		type = que.que.pop(0)
		if len(que.que) == 0:
			que.newQue()
		return type



class boardClass():

	def __init__(self, size):
		self.newBoard(size)

	def newBoard(self, size):

		self.size = size

		tempList1 = []
		for i in range(size[0]):
			tempList1.append(0)
		
		tempList2 = []
		for i in range(size[1]):
			tempList2.append(deepcopy(tempList1))
		
		self.data = deepcopy(tempList2)



boardSize = [10, 20]
board = boardClass(boardSize)

totalInputList = []
playerInputs = {
	"up": pygame.K_UP,
	"left": pygame.K_LEFT,
	"right": pygame.K_RIGHT,
	"down": pygame.K_DOWN,
	"rotLeft": pygame.K_q,
	"rotRight": pygame.K_e,
	"hold": pygame.K_SPACE,
	"enter": pygame.K_RETURN,
	"escape": pygame.K_ESCAPE,
}

FPS = 60
running = True
TAS = False
currentFrame = 0
lastFrameDown = 0
gameState = 0

while running:

	currentFrame += 1

	inputValues = []
	for i in range(7):
		inputValues.append(0)



	for event in pygame.event.get():


		if event.type == pygame.QUIT:

			running = False
			exit()
		

		if event.type == pygame.KEYDOWN:
			
			if event.key == pygame.K_ESCAPE:
				print("ya")





	pygame.display.update()
	clock.tick(60)

