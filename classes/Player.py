import pygame
import GameObject

class Player(GameObject):
    def __init__(self, x, y):
        player = self.load_image('images/player.png')
        self.set_image(player, 25, 32)
        
        self.gravity = 0

        self.handle_key_events = True
