import sys
import pygame
from pygame.locals import *
import math

pygame.init()

bg = pygame.image.load("images/wood_bg.jpg")
size = width, height = 800, 600
fps = 30
pygame.display.set_caption('decay hook')

# Creates the screen/window
screen = pygame.display.set_mode(size)

# Load classes
from classes.GameObject import GameObject
from classes.Player import Player

# Player
player = Player(400, 300)


# Main loop
while True:
    ev = pygame.event.get()
    for event in ev:

        # Close Game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Handle click
        elif event.type == pygame.MOUSEBUTTONUP:
            mousePos = pygame.mouse.get_pos()
            print (mousePos)
            mouseAngle = math.degrees(math.atan2(mousePos[1]-100, mousePos[0]-100))
            print (mouseAngle)

    
    screen.blit(bg, [0, 0])
    pygame.display.flip()