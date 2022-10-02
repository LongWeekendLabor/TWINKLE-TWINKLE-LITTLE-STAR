# import modules
import pygame

# import const
from .Const import *

class StarCoin(pygame.sprite.Sprite):
    def __init__(self, nth):
        pygame.sprite.Sprite.__init__(self)
        
        # Loading images
        star_coin_anim = []
        for i in range(13):
            star_coin_img = pygame.image.load(os.path.join('img', 'StarCoin', f'{i + 1}.png')).convert()
            star_coin_img.set_colorkey(COLOR["BLACK"])
            star_coin_anim.append(pygame.transform.scale(star_coin_img, (30, 30)))
        
        # public variables
        self.image = star_coin_anim[0]
        self.rect = self.image.get_rect()
        self.rect.top = 25
        self.rect.left = 7 + 10 * (nth - 1)
        
        # private variables
        self.__star_coin_anim = star_coin_anim
        self.__frame = 0
        self.__last_update = pygame.time.get_ticks()
        self.__frame_rate = 50
        
    # public methods
    def update(self):
        now = pygame.time.get_ticks()
        if now - self.__last_update > self.__frame_rate:
            self.__last_update = now
            self.__frame += 1
            if self.__frame == len(self.__star_coin_anim):
                self.__frame = 0
            else:
                self.image = self.__star_coin_anim[self.__frame]
                center = self.rect.center
                self.rect = self.image.get_rect()
                self.rect.center = center
