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
        