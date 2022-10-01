import random
from .Const import * 

class Star(pygame.sprite.Sprite):
    def __init__(self, name: str, temperture: float, color: str, location: str, size: tuple):

        # Loading images
        image = []
        for i in range(3):
            image.append(pygame.image.load(os.path.join("img", f"star{i+1}.png")).convert())

        pygame.sprite.Sprite.__init__(self)
        
        # public variables
        self.image = pygame.Surface(size)
        self.image.set_colorkey(COLOR["BLACK"])
        self.rect = self.image.get_rect()
        
        # private variables
        self.__name = name
        self.__temperture = temperture
        self.__color = color
        self.__location = location
        self.__chuck_array = ["A1"]

    # public methods
    def update(self):
        pass

    # Setters and Getters
    def setName(self, name: str): self.__name = name
    def setTemperture(self, temperture: float): self.__temperture = temperture
    def setColor(self, color: str): self.__color = color
    def setLocation(self, location: str): self.__location = location
    def getName(self): return self.__name
    def getTemperture(self): return self.__temperture
    def getColor(self): return self.__color
    def getLocation(self): return self.__location
    
    def is_create_stars(self, chuck: str):
        if self.__chuck_array.count(chuck) == 0:
            self.__chuck_array.append(chuck)
        else:
            star_number = random.randrange(0, 4)
            location = []
            for i in range(star_number):
                x = random.randrange(60, GAME_BASE_SETUP["WIDTH"]-60)
                y = random.randrange(60, GAME_BASE_SETUP["LENGTH"]-60)
                location.append((x, y))
        return star_number, location
    
    # private methods
    