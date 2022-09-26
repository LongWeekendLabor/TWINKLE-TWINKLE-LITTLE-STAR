import pygame
import random
import os

# import sources
from src.const import *
from src.player import *
from src.SpaceJunck import *
from src.star_class import *
from  src.black_hole import *

# init & create a window
pygame.init()
screen = pygame.display.set_mode((game_base_setup["WIDTH"], game_base_setup["HEIGHT"]))
pygame.display.set_caption(game_base_setup["GAMENAME"])
clock = pygame.time.Clock()

# loading imgs
# example...
background_img = pygame.image.load(os.path.join('img', 'background_A1.jpg')).convert()
spaceship = pygame.image.load(os.path.join('img', 'spaceship.png')).convert()

# sprite group
all_sprites = pygame.sprite.Group()
player = Player(spaceship)
all_sprites.add(player)

rockNumber = 3
for i in range(rockNumber):
    trash = SpaceJunk()
    all_sprites.add(trash)
    
# gaming loop
running = True
while running:
    
    # execute at most <FPS> times in 1 sec
    clock.tick(game_base_setup["FPS"])
    
    # get input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # refresh game
    all_sprites.update()    # execute update function of every sprite in group
    
    # display screen
    background_img = pygame.image.load(os.path.join('img', f'background_{player.getLocation()}.jpg')).convert()
    screen.blit(background_img, (0, 0))
    all_sprites.draw(screen)
    pygame.display.update()

pygame.quit()