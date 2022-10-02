import pygame
import random
from .LocationFunction import *
from .Const import *

class BlackHole(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # Loading image
        image = pygame.image.load(os.path.join('img', 'black_hole.png')).convert()
        self.image = pygame.transform.scale(image, (200, 200))
        self.image.set_colorkey(COLOR["BLACK"])
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(60, GAME_BASE_SETUP["WIDTH"] - 60)
        self.rect.centery = random.randrange(60, GAME_BASE_SETUP["HEIGHT"] - 60)
        self.radius = self.rect.width * 0.7 / 2
        
        # private methods
        self.__image_ori = self.image
        self.__total_degree = 0
        self.__rot_degree = 0.6
        self.__location = self.__create_location()
        print(self.__location)

    # public methods
    def getLocation(self): return self.__location
    
    def update(self):
        self.__rotate()

    # private methods
    def __rotate(self):
        self.__total_degree += self.__rot_degree
        self.__total_degree = self.__total_degree % 360
        self.image = pygame.transform.rotate(self.__image_ori, self.__total_degree)
        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center
    
    def __create_location(self):
        size_x = GAME_SETUP["MAP_SIZE"][0]
        size_y = GAME_SETUP["MAP_SIZE"][1]
        x = random.randrange(0, size_x)
        y = random.randrange(0, size_y)
        input = (x, y)
        return tuple_to_location(input)

    def chuck_check(self, space_ship_location: str): return self.__location == space_ship_location