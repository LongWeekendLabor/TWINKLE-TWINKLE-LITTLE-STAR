import pygame
import random

AZURE = (240, 255, 255)
WIDTH = 960
HEIGHT = 540

class SpaceJunk(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))
        self.image.fill(AZURE)
        self.rect = self.image.get_rect()
        self.speedy = random.randrange(1,5)
        self.speedx = random.randrange(-1,1)
        self.rect.x = random.randrange(0,WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100,-40)
        
    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > HEIGHT or self.rect.right > WIDTH or self.rect.left < 0:
            self.speedy = random.randrange(1,5)
            self.speedx = random.randrange(-1,1)
            self.rect.x = random.randrange(0,WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100,-40)

all_sprites = pygame.sprite.Group()
rockNumber = 3
for i in range(rockNumber):
    trash = SpaceJunk()
    all_sprites.add(trash)