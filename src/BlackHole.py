import pygame
import random
from .LocationFunction import *
from .Const import *

black_hole_setup = {
    "image_size" : (50, 50),
}

class BlackHole(pygame.sprite.Sprite):
    def __init__(self):
        # Loading image
        image = pygame.image.load(os.path.join('img', 'black_hole.png')).convert()
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(black_hole_setup["image_size"])
        self.image = image
        self.image.set_colorkey(COLOR["BLACK"])
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(60, GAME_BASE_SETUP["WIDTH"] - 60)
        self.rect.centery = random.randrange(60, GAME_BASE_SETUP["HEIGHT"] - 60)
        self.radius = self.rect.width * 0.7 / 2
        self.__location = self.__create_location()
        print(self.__location)

    # public methods
    def getLocation(self): return self.__location

    # private methods
    def __create_location(self):
        size_x = GAME_SETUP["MAP_SIZE"][0]
        size_y = GAME_SETUP["MAP_SIZE"][1]
        x = random.randrange(0, size_x)
        y = random.randrange(0, size_y)
        input = (x, y)
        return tuple_to_location(input)

    def chuck_check(self, space_ship_location: str): return self.__location == space_ship_location