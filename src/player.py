# import modules
import pygame
import os

# import const
from .const import *
from .location_func import *

class Player(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(img, (75, 75))
        self.image.set_colorkey(COLOR["BLACK"])
        self.rect = self.image.get_rect()
        self.speed = [8, 8]

        # player information variable
        self.location = "A1"
        self.health = 100    #TODO
        
        # center position
        self.rect.center = (GAME_BASE_SETUP["WIDTH"] / 2, GAME_BASE_SETUP["HEIGHT"] / 2)
    
    # getter and setter
    def getLocation(self): return self.location
    def setLocation(self, location: str): self.location = location

    # The ship moves to the next location or stops in place
    def location_change_or_stop(self, vector: tuple):
        if (can_move_nextArea((0, 1), self.location)):
            self.rect.left = 0
            self.location = location_change((0, 1), self.location)
        else:
            self.rect.right = GAME_BASE_SETUP["WIDTH"]
        
    def update(self):
        # get a class that store a list of bool that determine if any key was be clicked
        key_pressed = pygame.key.get_pressed()
        
        # control player to move
        if key_pressed[pygame.K_RIGHT]: self.rect.x += self.speed[0]
        if key_pressed[pygame.K_LEFT]: self.rect.x -= self.speed[0]
        if key_pressed[pygame.K_UP]: self.rect.y -= self.speed[1]
        if key_pressed[pygame.K_DOWN]: self.rect.y += self.speed[1]
            
        # setting border effect
        if self.rect.right > GAME_BASE_SETUP["WIDTH"]: 
            if (can_move_nextArea((0, 1), self.location)):
                self.rect.left = 0
                self.location = location_change((0, 1), self.location)
            else:
                self.rect.right = GAME_BASE_SETUP["WIDTH"]
        if self.rect.left < 0: 
            if (can_move_nextArea((0, -1), self.location)):
                self.rect.right = GAME_BASE_SETUP["WIDTH"]
                self.location = location_change((0, -1), self.location)
            else:
                self.rect.left = 0
        if self.rect.top < 0: 
            if (can_move_nextArea((-1, 0), self.location)):
                self.rect.bottom = GAME_BASE_SETUP["HEIGHT"]
                self.location = location_change((-1, 0), self.location)
            else:
                self.rect.top = 0
        if self.rect.bottom > GAME_BASE_SETUP["HEIGHT"]: 
            if (can_move_nextArea((1, 0), self.location)):
                self.rect.top = 0
                self.location = location_change((1, 0), self.location)
            else:
                self.rect.bottom = GAME_BASE_SETUP["HEIGHT"]