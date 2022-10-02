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
    "MAP_SIZE" : (3, 3),
    "NUM_OF_BG" : 36,
    "NUM_OF_ROCKS" : 5,
    "HP_BAR_LENGTH" : 150,
    "HP_BAR_HEIGHT" : 15,
    "STATION_SIZE" : (198, 120),
    "STATION_HEAL" : 25,
    "LOCATION_TEXT_CENTER" : (5, GAME_BASE_SETUP["HEIGHT"] - 50),
    "LOCATION_TEXT_SIZE" : 50,
    "START_BUTTON_TOPLEFT" : (GAME_BASE_SETUP["WIDTH"] - 140, GAME_BASE_SETUP["HEIGHT"] - 68),
    "START_BUTTON_SIZE" : (128,66),
    "TARGET" : 5
}

# define color area
COLOR = {
    "BLACK" : (0, 0, 0),
    "RED" : (255, 0, 0),
    "AZURE" : (240, 255, 255),
    "WHITE" : (255, 255, 255)
}
