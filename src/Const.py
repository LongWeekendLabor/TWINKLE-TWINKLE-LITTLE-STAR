# import models
import pygame
import os

# define const
GAME_BASE_SETUP = {
    "FPS" : 60, 
    "WIDTH" : 1024,
    "HEIGHT" : 512,
    "GAMENAME" : 'UNTITLED'
}

GAME_SETUP = {
    "MAP_SIZE" : (2, 2),
    "NUM_OF_ROCKS" : 5,
    "HP_BAR_LENGTH" : 150,
    "HP_BAR_HEIGHT" : 15, 
    "LOCATION_TEXT_CENTER" : (45, GAME_BASE_SETUP["HEIGHT"] - 28),
    "LOCATION_TEXT_SIZE" : 50,
<<<<<<< HEAD
    "LOCATION_ARRAY" : ("A1", "A2", "B1", "B2")
=======
    "RANDOMNUMBER" : 0
>>>>>>> Rock
}

# define color area
COLOR = {
    "BLACK" : (0, 0, 0),
    "RED" : (255, 0, 0),
    "AZURE" : (240, 255, 255),
    "WHITE" : (255, 255, 255)
}
