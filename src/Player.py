# import modules
import pygame

# import const
from .Const import *
from .LocationFunction import *

class Player(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(img, (75, 75))
        self.ori_img = self.image
        self.image.set_colorkey(COLOR["BLACK"])
        self.rect = self.image.get_rect()
        self.speed = [8, 8]
        self.last = 0
        
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
    
    # let img rotate "degree" degree
    def rotate(self, degree):
        self.image = pygame.transform.rotate(self.ori_img, degree)
        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center
        
    def update(self):
        # get a class that store a list of bool that determine if any key was be clicked
        key_pressed = pygame.key.get_pressed()
        
        # assign key_pressed to variable
        RIGHT = key_pressed[pygame.K_RIGHT]
        LEFT = key_pressed[pygame.K_LEFT]
        UP = key_pressed[pygame.K_UP]
        DOWN = key_pressed[pygame.K_DOWN]
        
        # control player to move
        if RIGHT: self.rect.x += self.speed[0]
        if LEFT: self.rect.x -= self.speed[0]
        if UP: self.rect.y -= self.speed[1]
        if DOWN: self.rect.y += self.speed[1]
        
        # decide the direction of img
        if RIGHT and UP: self.rotate(315)
        elif RIGHT and DOWN: self.rotate(225)
        elif LEFT and UP: self.rotate(45)
        elif LEFT and DOWN: self.rotate(135)
        elif RIGHT: self.rotate(270)
        elif LEFT: self.rotate(90)
        elif UP: self.rotate(0)
        elif DOWN: self.rotate(180)
            
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
        
        now = []
        now.append(UP)
        now.append(DOWN)
        now.append(LEFT)
        now.append(RIGHT)
        if now != self.last:
            print(now)
        self.last = now