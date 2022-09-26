# import models
import pygame
import os

# define const
game_base_setup = {
    "FPS" : 60, 
    "WIDTH" : 1024,
    "HEIGHT" : 512,
    "GAMENAME" : 'UNTITLED', 
    "MAP_SIZE" : (2, 2)
}

game_setup = {
    "NumOfRocks" : 5,
    "HP_BAR_LENGTH" : 150,
    "HP_BAR_HEIGHT" : 15
}

# define color area
COLOR = {
    "BLACK" : (0, 0, 0),
    "RED" : (255, 0, 0),
    "AZURE" : (240, 255, 255),
    "WHITE" : (255, 255, 255)
}
