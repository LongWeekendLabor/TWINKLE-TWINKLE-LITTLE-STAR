# import modules
import pygame

# import const
from .Const import *

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        
        # Loading images
        expl_anim = []
        for i in range(6):
            expl_img = pygame.image.load(os.path.join('img', 'explosion', f'{i + 1}.png')).convert()
            expl_img.set_colorkey(COLOR["BLACK"])
            expl_anim.append(pygame.transform.scale(expl_img, (size, size)))
        
        # public variables
        
        self.image = expl_anim[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        
        # private variables
        self.__expl_anim = expl_anim
        self.__frame = 0
        self.__last_update = pygame.time.get_ticks()
        self.__frame_rate = 50
        
    # public methods
    def update(self):
        now = pygame.time.get_ticks()
        if now - self.__last_update > self.__frame_rate:
            self.__last_update = now
            self.__frame += 1
            if self.__frame == len(self.__expl_anim):
                self.kill()
            else:
                self.image = self.__expl_anim[self.__frame]
                center = self.rect.center
                self.rect = self.image.get_rect()
                self.rect.center = center
