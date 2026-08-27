import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True


FPS = 60
currentFrame = 0

while running:

	currentFrame += 1



	for event in pygame.event.get():


		if event.type == pygame.QUIT:

			running = False
			exit()






	clock.tick(60)