import pygame
from classes.GameObject import GameObject
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent


class Player(GameObject):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_speed = 0
        self.y_speed = 0
        playersprite = self.load_image(PROJECT_ROOT / "images/player.png")
        self.set_image(playersprite, 50, 64)

        self.gravity = 0

        self.handle_key_events = True

        self.lives = 3

        offimage = pygame.image.load(PROJECT_ROOT / "images/player.png")
        self.xoffset = (offimage.get_width()/2)
        self.yoffset = (offimage.get_height()/2)

        self.gpoint = [0,0]
        self.grapple = False


    def throw_grapple_hook(self):
        pass

    def check_lives(self, lives):
        if lives <= 0:
            #Restart Level
            return
    
    def set_lives(self, lives):
        self.lives = 3