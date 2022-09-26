import pygame
from .Const import * 

class star(pygame.sprite.Sprite):
    def __init__(self, name: str, temperture: float, color: str, location: list, size: tuple):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.temperture = temperture
        self.color = color
        self.location = location
        self.image = pygame.Surface(size)
        self.image.set_colorkey(COLOR["BLACK"])
        self.rect = self.image.get_rect()

    def update(self):
        # get a class that store a list of bool that determine if any key was be clicked
        key_pressed = pygame.mouse.get_pressed()
        if key_pressed:
            0

    def set_name(self, name: str):
        self.name = name

    def set_temperture(self, temperture: float):
        self.temperture = temperture

    def set_color(self, color: str):
        self.color = color

    def set_location(self, location: str):
        self.location = location

    def get_name(self):
        return self.name

    def get_temperture(self):
        return self.temperture

    def get_color(self):
        return self.color

    def get_location(self):
        return self.location