import pygame
from .Const import * 

class Star(pygame.sprite.Sprite):
    def __init__(self, name: str, temperture: float, color: str, location: str, size: tuple):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.temperture = temperture
        self.color = color
        self.location = location
        self.image = pygame.Surface(size)
        self.image.set_colorkey(COLOR["BLACK"])
        self.rect = self.image.get_rect()

    def update(self):
            pass

    # Setters and Getters
    def setName(self, name: str):
        self.name = name

    def setTemperture(self, temperture: float):
        self.temperture = temperture

    def setColor(self, color: str):
        self.color = color

    def setLocation(self, location: str):
        self.location = location

    def getName(self):
        return self.name

    def getTemperture(self):
        return self.temperture

    def getColor(self):
        return self.color

    def getLocation(self):
        return self.location