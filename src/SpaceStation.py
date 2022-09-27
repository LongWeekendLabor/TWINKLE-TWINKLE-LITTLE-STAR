import random
from .Const import * 

class SpaceStation(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(image, (105, 105))
        self.ori_image = self.image
        self.image.set_colorkey(COLOR["BLACK"])
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(60,964)
        self.rect.centery = random.randrange(60,452)
        self.location = self.create_location()
        print(self.location)

    def update(self):
            pass

    # Setters and Getters
    def getLocation(self):
        return self.location

    def create_location(self):
        size = GAME_SETUP["MAP_SIZE"][0]
        first = random.randrange(0,size)
        second = random.randrange(0,size)
        return chr(first+65) + str(second+1)

    def chuck_check(self, space_ship_location: str):
        return self.location == space_ship_location