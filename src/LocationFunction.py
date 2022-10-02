# import model
import json
from .Const import *

# location (str) change to index
def location_index(location: str):
    return (ord(location[0]) - 65, (int(location[1]) - 1))

# can move to the next area
def can_move_nextArea(vector: tuple, location: str):
    location = location_index(location)
    move_index = (location[0] + vector[0], location[1] + vector[1])
    
    if (move_index[0] >= GAME_SETUP["MAP_SIZE"][0] or 
        move_index[1] >= GAME_SETUP["MAP_SIZE"][1] or
        move_index[0] < 0 or
        move_index[1] < 0):
        return False
    return True

# return the changed location
def location_change(vector: tuple, location: str):
    location = location_index(location)
    new_location = chr(location[0] + vector[0] + 65) + str(location[1] + vector[1] + 1)
    return new_location

def tuple_to_location(location: tuple):
     return chr(location[0]+65) + str(location[1]+1)

def read_txt(src):
    with open(src, mode='r', encoding='utf-8') as file:
        readLine = file.read().split("\n\n")
    textLine = []
    for i in readLine:
        line = []
        if len(i) > 34:
            line.append(i[:34])
            line.append(i[34:])
        else:
            line.append(i)
            line.append("")
        textLine.append(line)
    return textLine