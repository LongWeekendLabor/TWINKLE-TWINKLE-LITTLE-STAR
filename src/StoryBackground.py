# import modules
import pygame

# import const
from .Const import *

class StoryBackground(pygame.sprite.Sprite):
    def __init__(self, star_name, num_of_img, speed):
        pygame.sprite.Sprite.__init__(self)
        
        # Loading images
        bg_anim = []
        for i in range(num_of_img):
            bg_img = pygame.image.load(os.path.join('img', 'story_background', f'{star_name}', f'{i + 1}.jpg')).convert()
            bg_img.set_colorkey(COLOR["BLACK"])
            bg_anim.append(pygame.transform.scale(bg_img, (GAME_BASE_SETUP["WIDTH"], GAME_BASE_SETUP["HEIGHT"])))
        
        # public variables
        
        self.image = bg_anim[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)
        
        # private variables
        self.__bg_anim = bg_anim
        self.__frame = 0
        self.__last_update = pygame.time.get_ticks()
        self.__frame_rate = speed
        
    # public methods
    def update(self):
        now = pygame.time.get_ticks()
        if now - self.__last_update > self.__frame_rate:
            self.__last_update = now
            self.__frame += 1
            if self.__frame == len(self.__bg_anim):
                self.__frame = -1
            else:
                self.image = self.__bg_anim[self.__frame]
                center = self.rect.center
                self.rect = self.image.get_rect()
                self.rect.center = center
