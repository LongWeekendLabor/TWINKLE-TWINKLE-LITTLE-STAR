# import modules
import pygame

# import const
from .Const import *

class StarCoin(pygame.sprite.Sprite):
    def __init__(self, center, size):
        # Loading images
        SC_anim = []
        for i in range(13):
            SC_img = pygame.image.load(os.path.join('img', 'countStar', f'{i + 1}.png')).convert()
            SC_img.set_colorkey(COLOR["BLACK"])
            SC_anim.append(pygame.transform.scale(SC_img, (size, size)))
        
        pygame.sprite.Sprite.__init__(self)
        
        # public variables
        
        self.image = SC_anim[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        
        # private variables
        self.__SC_anim = SC_anim
        self.__frame = 0
        self.__last_update = pygame.time.get_ticks()
        self.__frame_rate = 50
        self.__count = 0
    
    # public methods
    def update(self):
        now = pygame.time.get_ticks()
        if now - self.__last_update > self.__frame_rate:
            self.__last_update = now
            self.__frame += 1
            if self.__frame == len(self.__SC_anim):
                self.kill()
            else:
                self.image = self.__SC_anim[self.__frame]
                center = self.rect.center
                self.rect = self.image.get_rect()
                self.rect.center = center

    def setCount(self):
        self.__count += 1

    def getCount(self):
        return self.__count
        