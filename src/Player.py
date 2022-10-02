# import modules
import pygame

# import const
from .Const import *
from .LocationFunction import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
    
        # Loading image
        image = pygame.image.load(os.path.join('img', 'spaceship.png')).convert()
        
        # public variables
        self.image = pygame.transform.scale(image, (75, 75))
        self.image.set_colorkey(COLOR["BLACK"])
        self.rect = self.image.get_rect()
        self.radius = 20
        
        # center position
        self.rect.center = (GAME_BASE_SETUP["WIDTH"] / 2, GAME_BASE_SETUP["HEIGHT"] / 2)
        
        # private variables
        self.__ori_img = self.image
        self.__speed = [2, 2]
        self.__last = 0
        self.__earnedStars = 0
        
        # player information variables
        self.__location = tuple_to_location((GAME_SETUP["MAP_SIZE"][0] // 2, GAME_SETUP["MAP_SIZE"][1] // 2))
        self.__health = 100    #TODO
    
    # public methods
    # getter and setter
    def getLocation(self): return self.__location
    def getHealth(self): return self.__health
    def getEarnedStars(self): return self.__earnedStars
    def setLocation(self, location: str): self.__location = location
    def setHealth(self, health: int): self.__health = health
    def setEarnedStars(self, earnedStars): self.__earnedStars = earnedStars
       
    def addEarnedStars(self): self.__earnedStars += 1    
        
    def update(self):
        # get a class that store a list of bool that determine if any key was be clicked
        key_pressed = pygame.key.get_pressed()
        
        # assign key_pressed to variable
        RIGHT = key_pressed[pygame.K_RIGHT]
        LEFT = key_pressed[pygame.K_LEFT]
        UP = key_pressed[pygame.K_UP]
        DOWN = key_pressed[pygame.K_DOWN]
        
        # control player to move
        if RIGHT: self.rect.x += self.__speed[0]
        if LEFT: self.rect.x -= self.__speed[0]
        if UP: self.rect.y -= self.__speed[1]
        if DOWN: self.rect.y += self.__speed[1]
        
        # decide the direction of img
        if RIGHT and UP: self.__rotate(315)
        elif RIGHT and DOWN: self.__rotate(225)
        elif LEFT and UP: self.__rotate(45)
        elif LEFT and DOWN: self.__rotate(135)
        elif RIGHT: self.__rotate(270)
        elif LEFT: self.__rotate(90)
        elif UP: self.__rotate(0)
        elif DOWN: self.__rotate(180)
            
        # setting border effect
        if self.rect.right > GAME_BASE_SETUP["WIDTH"]: 
            if (can_move_nextArea((0, 1), self.__location)):
                self.rect.left = 0
                self.__location = location_change((0, 1), self.__location)
            else:
                self.rect.right = GAME_BASE_SETUP["WIDTH"]
        if self.rect.left < 0: 
            if (can_move_nextArea((0, -1), self.__location)):
                self.rect.right = GAME_BASE_SETUP["WIDTH"]
                self.__location = location_change((0, -1), self.__location)
            else:
                self.rect.left = 0
        if self.rect.top < 0: 
            if (can_move_nextArea((-1, 0), self.__location)):
                self.rect.bottom = GAME_BASE_SETUP["HEIGHT"]
                self.__location = location_change((-1, 0), self.__location)
            else:
                self.rect.top = 0
        if self.rect.bottom > GAME_BASE_SETUP["HEIGHT"]: 
            if (can_move_nextArea((1, 0), self.__location)):
                self.rect.top = 0
                self.__location = location_change((1, 0), self.__location)
            else:
                self.rect.bottom = GAME_BASE_SETUP["HEIGHT"]
    
    # private methods
    # let img rotate "degree" degree
    def __rotate(self, degree):
        self.image = pygame.transform.rotate(self.__ori_img, degree)
        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center
