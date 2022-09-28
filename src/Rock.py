from src.Const import *
import pygame
import random
import os

class Rock(pygame.sprite.Sprite):

    def __init__(self):
        #Down load picture
        meteorite1_img = pygame.image.load(os.path.join("img","meteorite-1.png")).convert()
        meteorite2_img = pygame.image.load(os.path.join("img","meteorite-2.png")).convert()
        meteorite3_img = pygame.image.load(os.path.join("img","meteorite-3.png")).convert()
        meteorite4_img = pygame.image.load(os.path.join("img","meteorite-4.png")).convert()
        meteorite_img = [meteorite1_img,meteorite2_img,meteorite3_img,meteorite4_img]
        pygame.sprite.Sprite.__init__(self)

        #Using random to determine top or bottom orleft or right
        self.randomNumber = self.Random()
        self.image_ori = meteorite_img[self.randomNumber]
        self.image = self.image_ori.copy()
        self.image_ori.set_colorkey(COLOR["BLACK"])
        self.rect = self.image.get_rect()

        #Top to bottom
        if self.randomNumber == 0:
            self.speedANDlocation(self.randomNumber)
        #Left to right
        elif self.randomNumber == 1:
            self.speedANDlocation(self.randomNumber)
        #Bottom to top
        elif self.randomNumber == 2:
            self.speedANDlocation(self.randomNumber)
        #Right to left
        elif self.randomNumber == 3:
            self.speedANDlocation(self.randomNumber)

        self.total_degree = 0
        self.rot_degree = random.randrange(-3,3)

    def Random(self):
        number = random.randrange(0,4)
        return number

    def speedANDlocation(self,direction):
        if direction == 0:
            self.speedx = random.randrange(-1,1)
            self.speedy = random.randrange(1,3)
            self.rect.x = random.randrange(0, GAME_BASE_SETUP["WIDTH"] - self.rect.width)
            self.rect.y = random.randrange(-100,-40)
        elif direction == 1:
            self.speedx = random.randrange(1,3)
            self.speedy = random.randrange(-1,1)
            self.rect.x = random.randrange(-100, -40)
            self.rect.y = random.randrange(0,GAME_BASE_SETUP["HEIGHT"] - self.rect.height)
        elif direction == 2:
            self.speedx = random.randrange(-1,3)
            self.speedy = random.randrange(-3,-1)
            self.rect.x = random.randrange(0, GAME_BASE_SETUP["WIDTH"] - self.rect.width)
            self.rect.y = random.randrange(513,530)
        elif direction == 3:
            self.speedx = random.randrange(-3,-1)
            self.speedy = random.randrange(-1,1)
            self.rect.x = random.randrange(1025, 1034)
            self.rect.y = random.randrange(0,GAME_BASE_SETUP["HEIGHT"] - self.rect.height)


    def rotate(self):
        self.total_degree += self.rot_degree
        self.total_degree = self.total_degree % 360
        self.image = pygame.transform.rotate(self.image_ori, self.total_degree)
        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center


    def update(self):
        self.rotate()
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        #Top to bottom
        if self.rect.top > GAME_BASE_SETUP["HEIGHT"] or self.rect.right > GAME_BASE_SETUP["WIDTH"] or self.rect.left < 0 and self.randomNumber == 0:
            self.speedANDlocation(self.randomNumber)
        #Left to right
        elif self.rect.top > GAME_BASE_SETUP["HEIGHT"] or self.rect.left > GAME_BASE_SETUP["WIDTH"] or self.rect.bottom < 0 and  self.randomNumber == 1:
            self.speedANDlocation(self.randomNumber)
        #Bottom to top
        elif self.rect.bottom < 0 or self.rect.right > GAME_BASE_SETUP["WIDTH"] or self.rect.left < 0 and self.randomNumber == 2:
            self.speedANDlocation(self.randomNumber)
        #Right to left
        elif self.rect.top > GAME_BASE_SETUP["HEIGHT"] or self.rect.right < 0 or self.rect.bottom < 0 and self.randomNumber == 3:
            self.speedANDlocation(self.randomNumber)