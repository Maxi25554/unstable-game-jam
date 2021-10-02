import sys
import pygame


pygame.init()

# Initial variables
size = width, height = 800, 600
speed = [2, 2]
black = 0, 0, 0
fps = 30

# Background
bg = pygame.image.load("images/wood_bg.jpg")

# Creates the screen
screen = pygame.display.set_mode(size)

# Main loop
x = 1
while True:
    x = x + 1
