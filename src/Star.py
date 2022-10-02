import random
from .Const import *

class Star(pygame.sprite.Sprite):
    def __init__(self, center, size, cycle):

        # Loading images
        star_anim = []
        for i in range(4):
            star_img = pygame.image.load(os.path.join('img', 'star', f'{i + 1}.png')).convert()
            star_img.set_colorkey(COLOR["BLACK"])
            star_anim.append(pygame.transform.scale(star_img, (size, size)))
            
        pygame.sprite.Sprite.__init__(self)
        
        # public variables
        # self.image = pygame.transform.scale(random.choice(self.__picture), (60, 60))
        # self.image.set_colorkey(COLOR["BLACK"])
        self.image = star_anim[0]
        self.rect = self.image.get_rect()
        # self.rect.centerx = random.randrange(60, GAME_BASE_SETUP["WIDTH"] - 60)
        # self.rect.centery = random.randrange(60, GAME_BASE_SETUP["HEIGHT"] - 60)
        self.rect.center = center
        self.radius = self.rect.width * 0.7 / 2
        
        # private variables
        self.__location = "none"
        self.__isUsed = False
        self.__star_anim = star_anim
        self.__frame = 0
        self.__last_update = pygame.time.get_ticks()
        self.__frame_rate = cycle

    # public methods
    def update(self):
        now = pygame.time.get_ticks()
        if now - self.__last_update > self.__frame_rate:
            self.__last_update = now
            self.__frame += 1
            if self.__frame == len(self.__star_anim):
                self.__frame = -1
            else:
                self.image = self.__star_anim[self.__frame]
                center = self.rect.center
                self.rect = self.image.get_rect()
                self.rect.center = center

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