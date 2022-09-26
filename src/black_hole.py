import pygame
from .const import *

black_hole_setup = {
    "image_size" : (50, 50),
}

class black_hole(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(black_hole_setup["image_size"])
        self.image.fill(game_base_setup["BLACK"])
        self.rect = self.image.get_rect()
        # self.rect.x = 
        # self.rect.y = 


