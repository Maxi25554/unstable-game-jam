import pygame
import GameObject

class Player(GameObject):
    def __init__(self, x, y):
        player = self.load_image('images/player.png')
        self.set_image(player, 25, 32)
        
        self.gravity = 0

        self.handle_key_events = True

        self.lives = 3

    def throw_grapple_hook(self):
        pass

    def check_lives(self):
        if lives <= 0:
            #Restart Level
            return
    
    def set_lives(self, lives):
        self.lives = lives
