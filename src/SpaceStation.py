import random
from .Const import * 

class SpaceStation(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(image, (61, 80))
        self.ori_image = self.image
        self.image.set_colorkey(COLOR["BLACK"])
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(60,964)
        self.rect.centery = random.randrange(60,452)
        self.location = self.create_location()
        self.radius = 29
        pygame.draw.circle(self.image, (255,0,0), self.rect.center, self.radius)
        print(self.getLocation())

    def update(self):
            pass

    # Setters and Getters
    def setRadius(self, radius):
        self.radius = radius

    def getLocation(self):
        return self.location

    def getRadius(self):
        return self.radius

    def create_location(self):
        size = GAME_SETUP["MAP_SIZE"][0]
        first = random.randrange(0,size)
        second = random.randrange(0,size)
        return chr(first+65) + str(second+1)

    def chuck_check(self, space_ship_location: str):
        return self.location == space_ship_location