import pygame
from sys import exit
from copy import deepcopy
from math import floor
import random

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()



def findIndex(toFind, list):
	for i in range(len(list)):
		if list[i] == toFind:
			return i
	print("fuckall, didn't find shit in this list")


# toFind is value, function returns index of key in list of keys
def findIndex_dict(toFind, dict):
	keys = list(dict.keys())
	for i in range(len(keys)):
		
		if dict[keys[i]] == toFind:
			return i
	
	print("findIndex_dict returns nothing")



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
TASon = False
currentFrame = 0
lastFrameDown = 0
gameState = 0

while running:
	frameEvents = pygame.event.get()
	if pygame.QUIT in frameEvents:
		exit()

	currentFrame += 1



	if TASon and currentFrame <= len(totalInputList):
		pass

	# turn player inputs into input values
	else:

		tempList1 = [0]*len(list(playerInputs.keys()))
		for event in frameEvents:
			if event.type == pygame.KEYDOWN:
				
				if event.key in list(playerInputs.values()):
					# tempList1[index of event.key's player input dict key] = 1
					tempList1[findIndex_dict(event.key, playerInputs)] = 1
				else:
					print("event key not in inputs")
		
		totalInputList.append(tempList1)
		
	# inputValues index
	ivi = currentFrame - 1
	inputValues = totalInputList[ivi]








	pygame.display.update()
	clock.tick(60)

