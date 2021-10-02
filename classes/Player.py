import pygame
from classes.GameObject import GameObject
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent


class Player(GameObject):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        playersprite = self.load_image(PROJECT_ROOT / "images/player.png")
        self.set_image(playersprite, 25, 32)

        self.gravity = 0

        self.handle_key_events = True

        self.lives = 3

    def throw_grapple_hook(self):
        pass

    def check_lives(self, lives):
        if lives <= 0:
            #Restart Level
            return
    
    def set_lives(self, lives):
        self.lives = lives
