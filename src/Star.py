import random
from .Const import * 

class Star(pygame.sprite.Sprite):
    def __init__(self, name: str, temperture: float, color: str, location: str, size: tuple):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.temperture = temperture
        self.color = color
        self.location = location
        self.image = pygame.Surface(size)
        self.image.set_colorkey(COLOR["BLACK"])
        self.rect = self.image.get_rect()
        self.chuck_array = ["A1"]

    def update(self):
            pass

    # Setters and Getters
    def setName(self, name: str):
        self.name = name

    def setTemperture(self, temperture: float):
        self.temperture = temperture

    def setColor(self, color: str):
        self.color = color

    def setLocation(self, location: str):
        self.location = location

    def getName(self):
        return self.name

    def getTemperture(self):
        return self.temperture

    def getColor(self):
        return self.color

    def getLocation(self):
        return self.location
    
    def is_create_stars(self, chuck: str):
        if self.chuck_array.count(chuck) == 0:
            self.chuck_array.append(chuck)
        else:
            star_number = random.randrange(0, 4)
            location = []
            for i in range(star_number):
                x = random.randrange(60, GAME_BASE_SETUP["WIDTH"]-60)
                y = random.randrange(60, GAME_BASE_SETUP["LENGTH"]-60)
                location.append((x, y))
        return star_number, location
            