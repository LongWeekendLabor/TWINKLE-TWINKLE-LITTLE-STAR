import pygame

set_up = {
    "image_size" : (50, 50),
    "image_color" : (0, 0, 0)
}

class black_hole(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(set_up["image_size"])
        self.image.fill(set_up["image_color"])
        self.rect = self.image.get_rect()
        # self.rect.x = 
        # self.rect.y = 


