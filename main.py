import sys
import pygame
from pygame.locals import *
import math
from classes.GameObject import GameObject
from classes.Player import Player

pygame.init()

size = width, height = 800, 600
fps = 30
pygame.display.set_caption('decay hook')
bg = pygame.image.load("images/wood_bg.jpg")


# Creates the screen/window
screen = pygame.display.set_mode(size)

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
            mouseAngle = math.degrees(math.atan2(mousePos[1]-Player.y(), mousePos[0]-Player.x()))
            print (mouseAngle)

    
    screen.blit(bg, [0, 0])
    pygame.display.flip()