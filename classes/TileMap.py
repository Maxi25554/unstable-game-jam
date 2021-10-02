import pygame

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
            AIR : None,
            BARRIER : None,
            STONE : None,
            GRASS : None,
            DIRT : None,
            WATER : None
        }
        self.tilemap = []
        self.highest_tile_index = WATER
        self.lowest_tile_index = AIR

    def create_tilemap(self):
        for i in range(self.mapwidth):
            self.tilemap.append([])
        
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
        
        self.tilemap[pos_y][pos_x] = tile

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

    def display_tile_map(self):
        pass

    def check_collisions(self):
        pass