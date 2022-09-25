from black_hole import black_hole
import pygame
import random
import os

# import sources
from src.const import *
from src.player import *

# init & create a window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(GAMENAME)
clock = pygame.time.Clock()

# loading imgs
# example...
background_img = pygame.image.load(os.path.join('img', 'sample_bg.png')).convert()
spaceship = pygame.image.load(os.path.join('img', 'sample.png')).convert()
        

# sprite group
all_sprites = pygame.sprite.Group()
player = Player(spaceship)
all_sprites.add(player)

    
# gaming loop
running = True
while running:
    
    # execute at most <FPS> times in 1 sec
    clock.tick(FPS)
    
    # get input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # refresh game
    all_sprites.update()    # execute update function of every sprite in group
    
    
    # display screen
    screen.blit(background_img, (0, 0))
    all_sprites.draw(screen)
    pygame.display.update()

pygame.quit()