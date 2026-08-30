import pygame
from sys import exit
from copy import deepcopy
from math import floor
import random

pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()





def findIndex(toFind, list):
	for i in range(len(list)):
		if list[i] == toFind:
			return i
	print("debug (findIndex): fuckall, didn't find shit in this list")



# toFind is value, function returns index of key in list of keys
def findIndex_dict(toFind, dict):
	keys = list(dict.keys())
	for i in range(len(keys)):
		
		if dict[keys[i]] == toFind:
			return i
	
	print("debug (findIndex_dict): findIndex_dict returns nothing")




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
		self.blocks = self.setup_pieceData(boardSize)[type]


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



class buttonClass():

	def __init__(self, buttonType, pos, dud=None):
		self.type = buttonType
		self.pos = pos
		if dud == None:
			self.active = True
		else:
			self.active = False

		self.mm_size = [80, 50]

		if buttonType[:2] == "mm":
			self.size = self.mm_size


	def drawButton_surf(self, pos, size, color):
		surface = pygame.Surface(size)
		surface.fill(color)
		rect = surface.get_rect(center=pos)
		screen.blit(surface, rect)


	def drawButton_text(self, text, pos, AA=True, size=36, color='black'):
			font = pygame.font.Font(None, size)
			surface = font.render(text, AA, color)
			rect = surface.get_rect(center=pos)
			screen.blit(surface, rect)


	def drawButton(self, specificPos=None):
		buttonBorderSize = {
			"mm": 10,
		}
		mm_size_1 = self.mm_size
		mm_size_2 = [mm_size_1[0]-buttonBorderSize["mm"], mm_size_1[1]-buttonBorderSize["mm"]]

		if specificPos == None:
			pos = self.pos
		else:
			pos = specificPos

		# for easier offset when drawing on screen
		x = pos[0]
		y = pos[1]

		if self.type[:2] == "mm":
			# base
			self.drawButton_surf(pos, mm_size_1, "cyan")
			self.drawButton_surf(pos, mm_size_2, "cornflowerblue")

			# text
			if self.type[-1:] == "1":
				self.drawButton_text("play", pos)
			if self.type[-1:] == "2":
				self.drawButton_text("exit", pos)


	def function(self):

		if self.type == "mm_1":
			pass

		if self.type == "mm_2":
			exit()




def createButtonList(gs, ss, scrn):
	# gs: gameState
	# ss: subState
	# scrn: screen

	# buttonList contains sub lists, each sub list contains bool of whether you can select that button at that point, and actual button
	buttonList = []
	
	# gs 10s
	if floor(gs/10) == 1:
		buttonList.append([True, buttonClass(buttonType="mm_1", pos=[scrn.get_width()/2, scrn.get_height()/2-40])])
		buttonList.append([True, buttonClass(buttonType="mm_2", pos=[scrn.get_width()/2, scrn.get_height()/2+40])])


	# gs 20s
	if floor(gs/10) == 2:

		if int(str(gs)[-1]) == 0 and ss == 0:
			buttonList.append([True, buttonClass(buttonType="dud", pos=[scrn.get_width()/2, scrn.get_height()/2], dud=True)])


	return buttonList




###### GAME SETUP ######

# board
boardSize = [10, 20]
board = boardClass(boardSize)

# inputs
totalInputList = []

playerInputs = {
	"up": pygame.K_UP,
	"down": pygame.K_DOWN,
	"left": pygame.K_LEFT,
	"right": pygame.K_RIGHT,
	"rotLeft": pygame.K_q,
	"rotRight": pygame.K_e,
	"hold": pygame.K_SPACE,
	"enter": pygame.K_RETURN,
	"escape": pygame.K_ESCAPE,
	"f4": pygame.K_F4,
}

# game
FPS = 60
running = True
TAS = False
currentFrame = 0
lastFrameDown = 0
# ones place: section of main game state
# 10: main menu
# 20: gameplay
gameState = 10
# for deeper sub-menus and such
subState = 0

# buttons
buttonListIndicator = 0
buttonList = createButtonList(gs=gameState, ss=subState, scrn=screen)



###### GAME START ######
while running:
	# frame setup
	frameEvents = pygame.event.get()
	for event in frameEvents:
		if event.type == pygame.QUIT:
			running = False
			exit()

	currentFrame += 1


	# inputValues setup
	if TAS and currentFrame <= len(totalInputList):
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
					print("debug: event key not in inputs")
		
		totalInputList.append(tempList1)
		
	# inputValues index
	ivi = currentFrame - 1
	inputValues = totalInputList[ivi]




	##### MAIN MENU #####

	lastBLIpos = buttonListIndicator

	if inputValues[0] == 1:
		if buttonListIndicator <= 0:
			buttonListIndicator = len(buttonList)-1
		else:
			buttonListIndicator -= 1

	if inputValues[1] == 1:
		if buttonListIndicator >= len(buttonList)-1:
			buttonListIndicator = 0
		else:
			buttonListIndicator += 1






	##### RENDERING #####
	
	# main menu
	if floor(gameState/10) == 1:

		# darkblue
		# darkslateblue
		screen.fill("darkslateblue")

		for button in buttonList:
			button[1].drawButton()

		## buttonListIndicator
		button = buttonList[buttonListIndicator][1]
		# ref spacing
		rs = button.pos[0] - (button.size[0]/2+50)
		BLIsize = [50, 40]
		BLIpos = [(rs, button.pos[1]), (rs-BLIsize[0], button.pos[1]+(BLIsize[1]/2)), (rs-BLIsize[0], button.pos[1]-(BLIsize[1]/2))]
		pygame.draw.polygon(screen, "red", BLIpos)





	pygame.display.update()
	clock.tick(60)

