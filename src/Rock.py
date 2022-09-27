from src.Const import *
import pygame
import random


class Rock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))
        self.image.fill(COLOR["AZURE"])
        self.rect = self.image.get_rect()
        #Using random to determine top or bottom orleft or right
        GAME_SETUP["RANDOMNUMBER"] = random.randrange(0,4)
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