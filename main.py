import sys
import pygame
from pygame.locals import *


pygame.init()

# Initial variables
size = width, height = 800, 600
speed = [2, 2]
black = 0, 0, 0
fps = 30
pygame.mouse.set_visible(0)



# Background
bg = pygame.image.load("images/wood_bg.jpg")

# Creates the screen
screen = pygame.display.set_mode(size)

pygame.display.set_caption('decay hook')

# Main loop
x = 1
while True:
    screen.blit(bg, [0, 0])
    
    pygame.display.flip()