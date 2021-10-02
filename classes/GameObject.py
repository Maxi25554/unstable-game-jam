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

    def set_image(self, image, width, height):
        self.image_orig = pygame.image.load(image).convert_alpha()
        self.image_orig = pygame.transform.scale(self.image_orig, (width, height))
        self.width = width
        self.height = height
        self.image = self.image_orig.copy()
        self.rect = pygame.Rect(self.x, self.y, width, height)

    def update(self):
        self.y_speed = self.y_speed + self.gravity
        self.x += self.x_speed
        self.y += self.y_speed
        self.rect.x = self.x
        self.rect.y = self.y