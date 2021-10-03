import pygame
import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent

AIR = 0
BARRIER = 1
STONE = 2
GRASS = 3
DIRT = 4
WATER = 5


class TileMap:
    def __init__(self, tile_size):
        self.tile_size = tile_size
        self.mapwidth = 0
        self.mapheight = 0
        self.textures = {
            AIR : 0,
            BARRIER : 0,
            STONE : self.load_image(PROJECT_ROOT / "images/stone.png"),
            GRASS : self.load_image(PROJECT_ROOT / "images/grass.png"),
            DIRT : self.load_image(PROJECT_ROOT / "images/dirt.png"),
            WATER : self.load_image(PROJECT_ROOT / "images/water.png")
        }
        self.tilemap = []
        self.highest_tile_index = WATER
        self.lowest_tile_index = AIR
        self.render = True

    def load_image(self, file_name):
        return os.path.join('images', file_name)

    def set_image(self, image, x, y, width, height):
        self.image_orig = pygame.image.load(image).convert_alpha()
        self.image_orig = pygame.transform.scale(self.image_orig, (width, height))
        self.width = width
        self.height = height
        self.image = self.image_orig.copy()
        self.rect = pygame.Rect(x, y, width, height)

    def create_tilemap(self):
        #create the lists for the tilemap positions
        for i in range(self.mapwidth):
            self.tilemap.append([])
        
        #add zeros as placeholders for each tile
        for i in range(self.mapwidth):
            list = self.tilemap[i]
            for y in range(self.mapheight):
                list.append(0)
                self.tilemap[i] = list

    def add_tile(self, x_pos, y_pos, tile):
        #Check if tile variable is a valid tile
        if tile > self.highest_tile_index or tile < self.lowest_tile_index:
            print(f"Error: Tile cannot be bigger than index {self.highest_tile_index} or lower than index {self.lowest_tile_index}")
            return

        #If tile is valid, find specified tile position and change it accordingly
        pos_x = 0
        pos_y = 0
        for x in range(self.mapwidth):
            if x == x_pos:
                pos_x = x
        
        for y in range(self.mapheight):
            if y == y_pos:
                pos_y = y
        
        self.tilemap[pos_y][pos_x] = tile #finds the list (the y value) and goes to the position in that list (the x value) and 

    def remove_tile(self, x_pos, y_pos):
        #Find specified tile position and change it accordingly
        pos_x = 0
        pos_y = 0
        for x in range(self.mapwidth):
            if x == x_pos:
                pos_x = x
        
        for y in range(self.mapheight):
            if y == y_pos:
                pos_y = y
        
        self.tilemap[pos_y][pos_x] = 0 #Change tile back to air(essentially destroying whatever was there)

    def render_tilemap(self):
        #this is just if we want to have multiple tilemaps for different levels
        if not self.render:
            return
        
        #I honestly don't know what I'm doing with this code much
        for x in range(self.mapwidth):
            for y in range(self.mapheight):
                tile_index = self.tilemap[y][x]
                tile_texture = None
                tile_texture = self.set_tile_texture(tile_index)
                tile = self.set_image(tile_texture, x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size)
        pass

    def set_tile_texture(self, tile_index):
        if tile_index == 0:
            return self.textures[AIR]
        elif tile_index == 1:
            return self.textures[BARRIER]
        elif tile_index == 2:
            return self.textures[STONE]
        elif tile_index == 3:
            return self.textures[GRASS]
        elif tile_index == 4:
            return self.textures[DIRT]
        elif tile_index == 5:
            return self.textures[WATER]

    def check_collisions(self):
        pass