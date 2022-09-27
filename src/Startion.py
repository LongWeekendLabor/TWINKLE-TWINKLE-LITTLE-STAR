import random
from .Const import * 

location_array = ["A1", "A2", "B1", "B2"]

class Station(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,50))
        self.image.fill((0,200,200))
        self.image.set_colorkey(COLOR["BLACK"])
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(10,1014)
        self.rect.y = random.randrange(10,502)
        self.location = random.choice(location_array)

    def update(self):
            pass

    # Setters and Getters
    def getLocation(self):
        return self.location