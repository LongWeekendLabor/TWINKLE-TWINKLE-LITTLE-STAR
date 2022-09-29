import pygame
import random
import os

# import sources
from src.Const import *
from src.Player import *
from src.Rock import *
from src.Star import *
from src.BlackHole import *
from src.SpaceStation import *

# init & create a window
pygame.init()
screen = pygame.display.set_mode((GAME_BASE_SETUP["WIDTH"], GAME_BASE_SETUP["HEIGHT"]))
pygame.display.set_caption(GAME_BASE_SETUP["GAMENAME"])
clock = pygame.time.Clock()

# loading imgs
init_background_img = pygame.image.load(os.path.join('img', 'init_background.jpg')).convert()
spaceship = pygame.image.load(os.path.join('img', 'spaceship.png')).convert()
space_station_img = pygame.image.load(os.path.join('img', 'space_station.png'))
start_button_img = pygame.image.load(os.path.join('img', 'start_button.png')).convert()
start_button_img = pygame.transform.scale(start_button_img, GAME_SETUP["START_BUTTON_SIZE"])
 
# Text font
font_name = pygame.font.match_font("arial")

# sprite group
all_sprites = pygame.sprite.Group()
rocks = pygame.sprite.Group()
stations = pygame.sprite.Group()
stars = pygame.sprite.Group()

# create sprite
player = Player(spaceship)
station = SpaceStation(space_station_img)

# define functions
def draw_init():
    start_button_img.set_colorkey(COLOR["BLACK"])
    screen.blit(init_background_img, (0, 0))
    screen.blit(start_button_img, GAME_SETUP["START_BUTTON_TOPLEFT"])

    pygame.display.update()
    waiting = True
    while waiting:
        clock.tick(GAME_BASE_SETUP["FPS"])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYUP:
                waiting = False
    
def createRock():
    rock = Rock()
    all_sprites.add(rock)
    rocks.add(rock)

def addStationIntoGroup():
    if station.alive() == False:
        all_sprites.add(station)
        stations.add(station)
    
def draw_health(surf, hp, x, y):
    if hp < 0:
        hp = 0
    fill = (hp / 100) * GAME_SETUP["HP_BAR_LENGTH"]
    outline_rect = pygame.Rect(x, y, GAME_SETUP["HP_BAR_LENGTH"], GAME_SETUP["HP_BAR_HEIGHT"])
    fill_rect = pygame.Rect(x, y, fill, GAME_SETUP["HP_BAR_HEIGHT"])
    pygame.draw.rect(surf, COLOR["RED"], fill_rect)
    pygame.draw.rect(surf, COLOR["WHITE"], outline_rect, 2)

def draw_location_text(surf, text):
    font = pygame.font.Font(font_name, GAME_SETUP["LOCATION_TEXT_SIZE"])
    text_surface = font.render(text, True, COLOR["WHITE"])
    text_rect = text_surface.get_rect()
    text_rect.center = GAME_SETUP["LOCATION_TEXT_CENTER"]
    surf.blit(text_surface, text_rect)

# add sprites into groups
all_sprites.add(player)
for i in range(GAME_SETUP["NUM_OF_ROCKS"]): createRock()
addStationIntoGroup()

# gaming loop
show_init = True
running = True
while running:
    # show the game init screen
    if show_init:
        draw_init()
        show_init = False
    
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
        player.setHealth(player.getHealth() - 20) #TODO
        createRock()
        if player.getHealth() <= 0: running = False
    
    # Space Station Zone
    Heal = pygame.sprite.spritecollide(player, stations, False, pygame.sprite.collide_circle)
    for heal in Heal:
        hp = player.getHealth()
        if not(station.getIsUsed()):
            if hp + 15 >= 100:
                player.setHealth(100)
            else:
                player.setHealth(hp + 15)
            station.setIsUsed(True)
    
    if not(station.chuck_check(player.getLocation())):
        station.kill()
        if station.getIsUsed():
            station = SpaceStation(space_station_img)
    else:
        addStationIntoGroup()
    
    # display screen
    background_img = pygame.image.load(os.path.join('img', f'background_{player.getLocation()}.jpg')).convert()
    screen.blit(background_img, (0, 0))
    all_sprites.draw(screen)
    draw_health(screen, player.getHealth(), 10, 10)
    draw_location_text(screen, player.getLocation())
    pygame.display.update()

pygame.quit()