import pygame

from .Const import *

font_story = os.path.join("font/TaipeiSans.ttf")

class Dialogue(pygame.sprite.Sprite):
    def __init__(self, rect: tuple):
        pygame.sprite.Sprite.__init__(self)
        self.__text = ""

        self.font = pygame.font.Font(font_story, 25)
        self.image = self.font.render(self.__text, True, COLOR["WHITE"])
        self.rect = self.image.get_rect()
        self.rect.topleft = rect

    def update(self):
        self.image = self.font.render(self.__text, True, COLOR["WHITE"])
            
    def getText(self): return self.__text
    def setText(self, text): self.__text = text