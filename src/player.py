# import modules
import pygame
import os

# import const
from .const import *

class Player(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(img, (38, 38))
        self.image.set_colorkey(COLOR["BLACK"])
        self.rect = self.image.get_rect()
        self.speed = [8, 8]
        
        # absolute position
        # self.rect.x = 200
        # self.rect.y = 200
        
        # center position
        self.rect.center = (game_base_setup["WIDTH"] / 2, game_base_setup["HEIGHT"] / 2)
        
    def update(self):
        # get a class that store a list of bool that determine if any key was be clicked
        key_pressed = pygame.key.get_pressed()
        
        # control player to move
        if key_pressed[pygame.K_RIGHT]: self.rect.x += self.speed[0]
        if key_pressed[pygame.K_LEFT]: self.rect.x -= self.speed[0]
        if key_pressed[pygame.K_UP]: self.rect.y -= self.speed[1]
        if key_pressed[pygame.K_DOWN]: self.rect.y += self.speed[1]
            
        # setting border effect
        if self.rect.right > game_base_setup["WIDTH"]: self.rect.right = game_base_setup["WIDTH"]
        if self.rect.left < 0: self.rect.left = 0
        if self.rect.top < 0: self.rect.top = 0
        if self.rect.bottom > game_base_setup["HEIGHT"]: self.rect.bottom = game_base_setup["HEIGHT"]