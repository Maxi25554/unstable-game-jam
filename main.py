import sys
import pygame
from pygame.locals import *


pygame.init()

size = width, height = 800, 600
fps = 30
pygame.display.set_caption('decay hook')
bg = pygame.image.load("images/wood_bg.jpg")


# Creates the screen/window
screen = pygame.display.set_mode(size)

# Main loop
while True:
    for event in pygame.event.get():
        
    
    screen.blit(bg, [0, 0])
    pygame.display.flip()