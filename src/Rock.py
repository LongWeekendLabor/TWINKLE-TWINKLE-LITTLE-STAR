from src.Const import *
import pygame
import random
import os

class Rock(pygame.sprite.Sprite):

    def __init__(self):
        # Down load picture
        meteorite_img = [ pygame.image.load(os.path.join("img", "meteorite", f"meteorite-{ _ + 1 }.png")).convert() for _ in range(4)]
        pygame.sprite.Sprite.__init__(self)

        # Using random to determine top or bottom or left or right
        self.__randomNumber = self.__Random()
        self.__image_ori = meteorite_img[self.__randomNumber]
        self.image = self.__image_ori.copy()
        self.__image_ori.set_colorkey(COLOR["BLACK"])
        self.rect = self.image.get_rect()
        self.radius = self.rect.width * 0.7 / 2

        # Top to bottom
        if self.__randomNumber == 0:
            self.__speedANDlocation(self.__randomNumber)
        # Left to right
        elif self.__randomNumber == 1:
            self.__speedANDlocation(self.__randomNumber)
        # Bottom to top
        elif self.__randomNumber == 2:
            self.__speedANDlocation(self.__randomNumber)
        # Right to left
        elif self.__randomNumber == 3:
            self.__speedANDlocation(self.__randomNumber)

        self.__total_degree = 0
        self.__rot_degree = random.randrange(-3,3)


    def update(self):
        self.__rotate()
        self.rect.x += self.__speedx
        self.rect.y += self.__speedy
        
        # Top to bottom
        if self.rect.top > GAME_BASE_SETUP["HEIGHT"] or self.rect.right > GAME_BASE_SETUP["WIDTH"] or self.rect.left < 0 and self.__randomNumber == 0:
            self.__speedANDlocation(self.__randomNumber)
        # Left to right
        elif self.rect.top > GAME_BASE_SETUP["HEIGHT"] or self.rect.left > GAME_BASE_SETUP["WIDTH"] or self.rect.bottom < 0 and  self.__randomNumber == 1:
            self.__speedANDlocation(self.__randomNumber)
        # Bottom to top
        elif self.rect.bottom < 0 or self.rect.right > GAME_BASE_SETUP["WIDTH"] or self.rect.left < 0 and self.__randomNumber == 2:
            self.__speedANDlocation(self.__randomNumber)
        # Right to left
        elif self.rect.top > GAME_BASE_SETUP["HEIGHT"] or self.rect.right < 0 or self.rect.bottom < 0 and self.__randomNumber == 3:
            self.__speedANDlocation(self.__randomNumber)
            
    
    # private methods
    def __Random(self):
        number = random.randrange(0,4)
        return number
    
    def __rotate(self):
        self.__total_degree += self.__rot_degree
        self.__total_degree = self.__total_degree % 360
        self.image = pygame.transform.rotate(self.__image_ori, self.__total_degree)
        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center
        
    def __speedANDlocation(self, direction):
        if direction == 0:
            self.__speedx = random.randrange(-1,1)
            self.__speedy = random.randrange(1,3)
            self.rect.x = random.randrange(0, GAME_BASE_SETUP["WIDTH"] - self.rect.width)
            self.rect.y = random.randrange(-100,-40)
        elif direction == 1:
            self.__speedx = random.randrange(1,3)
            self.__speedy = random.randrange(-1,1)
            self.rect.x = random.randrange(-100, -40)
            self.rect.y = random.randrange(0,GAME_BASE_SETUP["HEIGHT"] - self.rect.height)
        elif direction == 2:
            self.__speedx = random.randrange(-1,3)
            self.__speedy = random.randrange(-3,-1)
            self.rect.x = random.randrange(0, GAME_BASE_SETUP["WIDTH"] - self.rect.width)
            self.rect.y = random.randrange(513,530)
        elif direction == 3:
            self.__speedx = random.randrange(-3,-1)
            self.__speedy = random.randrange(-1,1)
            self.rect.x = random.randrange(1025, 1034)
            self.rect.y = random.randrange(0,GAME_BASE_SETUP["HEIGHT"] - self.rect.height)