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
        self.location = random.choice(GAME_SETUP["LOCATION_ARRAY"])
        print(self.location)

    def update(self):
            pass

    # Setters and Getters
    def getLocation(self):
        return self.location