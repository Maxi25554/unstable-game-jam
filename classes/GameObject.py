import math
import os
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

        self.collision_object_types = set()
        self.collision_objects = []

    def load_image(self, file_name):
        return os.path.join('Images', file_name)

    def set_image(self, image, width, height):
        self.image_orig = pygame.image.load(image).convert_alpha()
        self.image_orig = pygame.transform.scale(self.image_orig, (width, height))
        self.width = width
        self.height = height
        self.image = self.image_orig.copy()
        self.rect = pygame.Rect(self.x, self.y, width, height)

    def register_collision_object(self, collision_object):
        self.collision_object_types.add(collision_object)

    def update(self):
        self.y_speed = self.y_speed + self.gravity
        self.x += self.x_speed
        self.y += self.y_speed
        self.rect.x = self.x
        self.rect.y = self.y

    def delete_object(self, obj):
        self.room.delete_object(obj)

    def remove_object(self, obj):
        for index, list_obj in enumerate(self.collision_objects):
            if list_obj is obj:
                self.collision_objects.pop(index)

    def check_collisions(self):
        for item in self.collision_objects:
            if self.rect.colliderect(item.rect):
                self.handle_collision(item)

    def collides_at(self, obj, x, y, collision_type):
        check_rect = obj.rect.move(x, y)
        collision_found = False
        for item in self.collision_objects:
            if check_rect.colliderect(item.rect):
                if type(item).__name__ == collision_type:
                    collision_found = True
                    break
        return collision_found