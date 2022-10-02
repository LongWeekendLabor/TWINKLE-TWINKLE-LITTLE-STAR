import random
from .Const import *

class Star(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # Loading images
        self.__picture = []

        for i in range(3):
            self.__picture.append(pygame.image.load(os.path.join("img", f"star{i+1}.png")).convert())
            
        pygame.sprite.Sprite.__init__(self)
        
        # public variables
        self.image = pygame.transform.scale(random.choice(self.__picture), (60, 60))
        self.image.set_colorkey(COLOR["BLACK"])
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(60, GAME_BASE_SETUP["WIDTH"]-60)
        self.rect.centery = random.randrange(60, GAME_BASE_SETUP["HEIGHT"]-60)
        
        # private variables
        self.__location = "none"
        self.__isUsed = False

    # public methods
    def update(self):
        pass

    # Setters and Getters
    def setName(self, name: str): self.__name = name
    def setTemperture(self, temperture: float): self.__temperture = temperture
    def setColor(self, color: str): self.__color = color
    def setLocation(self, location: str): self.__location = location
    def setIsUsed(self, isUsed: bool): self.__isUsed = isUsed
    def getName(self): return self.__name
    def getTemperture(self): return self.__temperture
    def getColor(self): return self.__color
    def getLocation(self): return self.__location
    def getIsUser(self): return self.__isUsed
    
    # private methods