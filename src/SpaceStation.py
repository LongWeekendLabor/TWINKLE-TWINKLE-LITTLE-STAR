import random
from .LocationFunction import *
from .Const import * 

class SpaceStation(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(image, (61, 80))
        self.ori_image = self.image
        self.image.set_colorkey(COLOR["BLACK"])
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(60, GAME_BASE_SETUP["WIDTH"] - 60)
        self.rect.centery = random.randrange(60, GAME_BASE_SETUP["HEIGHT"] - 60)
        self.location = self.create_location()
        print(self.getLocation())

    def update(self):
            pass

    # Setters and Getters
    def getLocation(self):
        return self.location

    def create_location(self):
        size = GAME_SETUP["MAP_SIZE"][0]
        x = random.randrange(0, size)
        y = random.randrange(0, size)
        input = (x, y)
        return tuple_to_location(input)

    def chuck_check(self, space_ship_location: str):
        return self.location == space_ship_location