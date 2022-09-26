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
screen = pygame.display.set_mode((GAME_BASE_SETUP["WIDTH"], GAME_BASE_SETUP["HEIGHT"]))
pygame.display.set_caption(GAME_BASE_SETUP["GAMENAME"])
clock = pygame.time.Clock()

# loading imgs
background_img = pygame.image.load(os.path.join('img', 'background_A1.jpg')).convert()
spaceship = pygame.image.load(os.path.join('img', 'spaceship.png')).convert()

# sprite group
all_sprites = pygame.sprite.Group()
rocks = pygame.sprite.Group()
player = Player(spaceship)

# define functions
def createRock():
    rock = SpaceJunk()
    all_sprites.add(rock)
    rocks.add(rock)
    
def draw_health(surf, hp, x, y):
    if hp < 0:
        hp = 0
    fill = (hp / 100) * GAME_SETUP["HP_BAR_LENGTH"]
    outline_rect = pygame.Rect(x, y, GAME_SETUP["HP_BAR_LENGTH"], GAME_SETUP["HP_BAR_HEIGHT"])
    fill_rect = pygame.Rect(x, y, fill, GAME_SETUP["HP_BAR_HEIGHT"])
    pygame.draw.rect(surf, COLOR["RED"], fill_rect)
    pygame.draw.rect(surf, COLOR["WHITE"], outline_rect, 2)

# add sprites into groups
all_sprites.add(player)
for i in range(GAME_SETUP["NUM_OF_ROCKS"]): createRock()
    
# gaming loop
running = True
while running:
    
    # execute at most <FPS> times in 1 sec
    clock.tick(GAME_BASE_SETUP["FPS"])
    
    # get input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # refresh game
    all_sprites.update()    # execute update function of every sprite in group
    hits = pygame.sprite.spritecollide(player, rocks, True, pygame.sprite.collide_circle)
    for hit in hits:
        player.health -= 20 #TODO
        createRock()
        if player.health <= 0: running = False
    
    # display screen
    background_img = pygame.image.load(os.path.join('img', f'background_{player.getLocation()}.jpg')).convert()
    screen.blit(background_img, (0, 0))
    all_sprites.draw(screen)
    draw_health(screen, player.health, 10, 10)
    pygame.display.update()

pygame.quit()