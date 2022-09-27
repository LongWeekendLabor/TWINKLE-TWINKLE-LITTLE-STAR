from src.Const import *
import pygame
import random
import os


class Rocks(pygame.sprite.Sprite):
    def __init__(self):
        #Down load picture
        meteorite1_img = pygame.image.load(os.path.join("img","meteorite-1.png")).convert()
        meteorite2_img = pygame.image.load(os.path.join("img","meteorite-2.png")).convert()
        meteorite3_img = pygame.image.load(os.path.join("img","meteorite-3.png")).convert()
        meteorite4_img = pygame.image.load(os.path.join("img","meteorite-4.png")).convert()
        meteorite_img = [meteorite1_img,meteorite2_img,meteorite3_img,meteorite4_img]


        pygame.sprite.Sprite.__init__(self)

        #Using random to determine top or bottom orleft or right
        GAME_SETUP["RANDOMNUMBER"] = random.randrange(0,4)
        self.image = meteorite_img[GAME_SETUP["RANDOMNUMBER"]]
        self.image.set_colorkey(COLOR["BLACK"])
        self.rect = self.image.get_rect()

        #Top to bottom
        if GAME_SETUP["RANDOMNUMBER"] == 0:
            self.speedy = random.randrange(1,5)
            self.speedx = random.randrange(-1,1)
            self.rect.x = random.randrange(0, GAME_BASE_SETUP["WIDTH"] - self.rect.width)
            self.rect.y = random.randrange(-100,-40)
        #Left to right
        elif GAME_SETUP["RANDOMNUMBER"] == 1:
            self.speedx = random.randrange(1,3)
            self.speedy = random.randrange(-3,3)
            self.rect.x = random.randrange(-10, -5)
            self.rect.y = random.randrange(0,GAME_BASE_SETUP["HEIGHT"] - self.rect.height)
        #Bottom to top
        elif GAME_SETUP["RANDOMNUMBER"] == 2:
            self.speedx = random.randrange(-1,1)
            self.speedy = random.randrange(-3,-1)
            self.rect.x = random.randrange(0, GAME_BASE_SETUP["WIDTH"] - self.rect.width)
            self.rect.y = random.randrange(513,530)
        #Right to left
        elif GAME_SETUP["RANDOMNUMBER"] == 3:
            self.speedx = random.randrange(-8,-5)
            self.speedy = random.randrange(-3,3)
            self.rect.x = random.randrange(1025, 1030)
            self.rect.y = random.randrange(0,GAME_BASE_SETUP["HEIGHT"] - self.rect.height)


    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        #Top to bottom
        if self.rect.top > GAME_BASE_SETUP["HEIGHT"] or self.rect.right > GAME_BASE_SETUP["WIDTH"] or self.rect.left < 0 and GAME_SETUP["RANDOMNUMBER"] == 0:
            self.speedy = random.randrange(1,5)
            self.speedx = random.randrange(-1,1)
            self.rect.x = random.randrange(0, GAME_BASE_SETUP["WIDTH"] - self.rect.width)
            self.rect.y = random.randrange(-100,-40)
        #Left to right
        elif self.rect.top > GAME_BASE_SETUP["HEIGHT"] or self.rect.left > GAME_BASE_SETUP["WIDTH"] or self.rect.bottom < 0 and  GAME_SETUP["RANDOMNUMBER"] == 1:
            self.speedx = random.randrange(1,3)
            self.speedy = random.randrange(-3,3)
            self.rect.x = random.randrange(-10, -5)
            self.rect.y = random.randrange(0,GAME_BASE_SETUP["HEIGHT"] - self.rect.height)
        #Bottom to top
        elif self.rect.bottom < 0 or self.rect.right > GAME_BASE_SETUP["WIDTH"] or self.rect.left < 0 and GAME_SETUP["RANDOMNUMBER"] == 2:
            self.speedx = random.randrange(-1,1)
            self.speedy = random.randrange(-3,-1)
            self.rect.x = random.randrange(0, GAME_BASE_SETUP["WIDTH"] - self.rect.width)
            self.rect.y = random.randrange(513,530)
        #Right to left
        elif self.rect.top > GAME_BASE_SETUP["HEIGHT"] or self.rect.right < 0 or self.rect.bottom < 0 and GAME_SETUP["RANDOMNUMBER"] == 3:
            self.speedx = random.randrange(-8,-5)
            self.speedy = random.randrange(-3,3)
            self.rect.x = random.randrange(1025, 1030)
            self.rect.y = random.randrange(0,GAME_BASE_SETUP["HEIGHT"] - self.rect.height)