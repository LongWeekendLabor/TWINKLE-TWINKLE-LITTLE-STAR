from src.Const import *
import pygame
import random
import os

class Rock(pygame.sprite.Sprite):

    def __init__(self):
        
       # Loading image
        meteorite_img = [ pygame.image.load(os.path.join("img", "meteorite", f"meteorite-{ _ + 1 }.png")).convert() for _ in range(4)]

        pygame.sprite.Sprite.__init__(self)

        # Using random to determine top or bottom or left or right
        self.__direction = self.__Random()
        self.__image_ori = meteorite_img[self.__Random()]
        self.image = self.__image_ori.copy()
        self.__image_ori.set_colorkey(COLOR["BLACK"])
        self.rect = self.image.get_rect()
        self.radius = self.rect.width * 0.7 / 2
        self.__decideLocation()
        self.__total_degree = 0
        self.__rot_degree = random.randrange(-3,3)


    # public methods
    def update(self):
        self.__rotate()
        self.rect.x += self.__speedx
        self.rect.y += self.__speedy

 
    # Setters and Getters
    def getDamage(self): return self.__damage
    
            
    def isOutOfBoundary(self):
        if self.rect.top > GAME_BASE_SETUP["HEIGHT"] or self.rect.bottom < 0 or self.rect.left > GAME_BASE_SETUP["WIDTH"] or self.rect.right < 0:
            return True
        else: return False
    
    # private methods
    def __Random(self): return random.randrange(0,4)
    
    def __rotate(self):
        self.__total_degree += self.__rot_degree
        self.__total_degree = self.__total_degree % 360
        self.image = pygame.transform.rotate(self.__image_ori, self.__total_degree)
        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center
        
    def __decideLocation(self):
        if self.__direction == 0:
            self.__speedx = random.randrange(-1,1)
            self.__speedy = random.randrange(1,3)
            self.rect.x = random.randrange(0, GAME_BASE_SETUP["WIDTH"] - self.rect.width)
            self.rect.y = random.randrange(-100,-40)
        elif self.__direction == 1:
            self.__speedx = random.randrange(1,3)
            self.__speedy = random.randrange(-1,1)
            self.rect.x = random.randrange(-100, -40)
            self.rect.y = random.randrange(0,GAME_BASE_SETUP["HEIGHT"] - self.rect.height)
        elif self.__direction == 2:
            self.__speedx = random.randrange(-1,3)
            self.__speedy = random.randrange(-3,-1)
            self.rect.x = random.randrange(0, GAME_BASE_SETUP["WIDTH"] - self.rect.width)
            self.rect.y = random.randrange(513,530)
        else:
            self.__speedx = random.randrange(-3,-1)
            self.__speedy = random.randrange(-1,1)
            self.rect.x = random.randrange(1025, 1034)
            self.rect.y = random.randrange(0,GAME_BASE_SETUP["HEIGHT"] - self.rect.height)