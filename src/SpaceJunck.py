from src.const import *
import pygame
import random

class SpaceJunk(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))
        self.image.fill(COLOR["AZURE"])
        self.rect = self.image.get_rect()
        self.speedy = random.randrange(1,5)
        self.speedx = random.randrange(-1,1)
        self.rect.x = random.randrange(0, game_base_setup["WIDTH"] - self.rect.width)
        self.rect.y = random.randrange(-100,-40)
        
    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > game_base_setup["HEIGHT"] or self.rect.right > game_base_setup["WIDTH"] or self.rect.left < 0:
            self.speedy = random.randrange(1,5)
            self.speedx = random.randrange(-1,1)
            self.rect.x = random.randrange(0, game_base_setup["WIDTH"] - self.rect.width)
            self.rect.y = random.randrange(-100,-40)