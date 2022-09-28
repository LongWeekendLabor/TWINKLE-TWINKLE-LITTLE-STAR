import random
from .LocationFunction import *
from .Const import * 

class SpaceStation(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(image, (90, 80))
        self.image.set_colorkey(COLOR["BLACK"])
        self.ori_image = self.image
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(60, GAME_BASE_SETUP["WIDTH"] - 60)
        self.rect.centery = random.randrange(60, GAME_BASE_SETUP["HEIGHT"] - 60)
        self.location = self.create_location()
        self.isUsed = False
        self.total_degree = 0
        self.rot_degree = random.randrange(-3, 3)
        print(self.getLocation())

    def update(self):
            # self.rotate()
            pass

    # Setters and Getters
    def setIsUsed(self, bool: bool):
        self.isUsed = bool

    def getLocation(self):
        return self.location

    def getIsUsed(self):
        return self.isUsed

    def create_location(self):
        size_x = GAME_SETUP["MAP_SIZE"][0]
        size_y = GAME_SETUP["MAP_SIZE"][1]
        x = random.randrange(0, size_x)
        y = random.randrange(0, size_y)
        input = (x, y)
        return tuple_to_location(input)

    def chuck_check(self, space_ship_location: str):
        return self.location == space_ship_location

    def rotate(self):
        self.total_degree += self.rot_degree
        self.total_degree = self.total_degree % 360
        self.image = pygame.transform.rotate(self.image, self.total_degree)
        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center