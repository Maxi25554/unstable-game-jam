import pygame

class GameObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 0
        self.height = 0
        self.x_speed = 0
        self.y_speed = 0
        self.image = 0
        self.velocity = [self.x_speed, self.y_speed]
        self.gravity = 0
        self.angle = 0

    def update(self):
        self.y_speed = self.y_speed + self.gravity
        self.x += self.x_speed
        self.y += self.y_speed
        self.rect.x = self.x
        self.rect.y = self.y