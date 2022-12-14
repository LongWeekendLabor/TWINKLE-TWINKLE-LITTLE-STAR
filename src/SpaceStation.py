import random
from .LocationFunction import *
from .Const import * 

class SpaceStation(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # Loading image
        self.__pictrue = pygame.image.load(os.path.join('img', 'space_station.png')).convert()
        
        # public variables
        self.image = pygame.transform.scale(self.__pictrue,GAME_SETUP["STATION_SIZE"])
        self.image.set_colorkey(COLOR["BLACK"])
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(60, GAME_BASE_SETUP["WIDTH"] - 60)
        self.rect.centery = random.randrange(60, GAME_BASE_SETUP["HEIGHT"] - 60)
        
        # private variables
        self.__ori_image = self.image
        self.__location = self.__create_location()
        self.__isUsed = False
        self.__total_degree = 0
        self.__rot_degree = 0.05
        
    # public methods
    def update(self): self.__rotate()

    # Setters and Getters
    def setIsUsed(self, bool: bool): self.__isUsed = bool
    def getIsUsed(self): return self.__isUsed
    def getLocation(self): return self.__location

    def chuck_check(self, space_ship_location: str): return self.__location == space_ship_location
        
    # private methods
    def __create_location(self):
        size_x = GAME_SETUP["MAP_SIZE"][0]
        size_y = GAME_SETUP["MAP_SIZE"][1]
        x = random.randrange(0, size_x)
        y = random.randrange(0, size_y)
        input = (x, y)
        return tuple_to_location(input)
    
    def __rotate(self):
        self.__total_degree += self.__rot_degree
        self.__total_degree = self.__total_degree % 360
        self.image = pygame.transform.rotate(self.__ori_image, self.__total_degree)
        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center