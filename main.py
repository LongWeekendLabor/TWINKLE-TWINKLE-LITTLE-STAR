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
from src.Dialogue import *
from src.Explosion import *

# init & create a window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((GAME_BASE_SETUP["WIDTH"], GAME_BASE_SETUP["HEIGHT"]))
pygame.display.set_caption(GAME_BASE_SETUP["GAMENAME"])
pygame.display.set_icon(pygame.image.load(os.path.join('img', 'logo.png')))
clock = pygame.time.Clock()

# Loading Backgrounds
BGlist = []
for i in range(GAME_SETUP["MAP_SIZE"][0]):
    BGlist.append([ pygame.image.load(os.path.join('img', 'background', f'{random.randrange(1, GAME_SETUP["NUM_OF_BG"] + 1)}.jpg')).convert() for _ in range(GAME_SETUP["MAP_SIZE"][1])])

# loading imgs
init_background_img = pygame.image.load(os.path.join('img', 'init_background.jpg')).convert()
start_button_img = pygame.image.load(os.path.join('img', 'start_button.png')).convert()
start_button_img = pygame.transform.scale(start_button_img, GAME_SETUP["START_BUTTON_SIZE"])

# Loading effect sound
damage_sound = pygame.mixer.Sound(os.path.join('sound', 'effect', 'damage.mp3'))
heal_sound = pygame.mixer.Sound(os.path.join('sound', 'effect', 'heal.mp3'))
 
# Text font
font_name = os.path.join('font', 'voltergoldfish.ttf')

# json information
nameList, text_src, chuck = json_read()

# sprite group
all_sprites = pygame.sprite.Group()
rocks = pygame.sprite.Group()
stations = pygame.sprite.Group()
stars = pygame.sprite.Group()
story_text = pygame.sprite.Group()
blackholes = pygame.sprite.Group()

# create sprite
player = Player()
station = SpaceStation()
blackhole = BlackHole()
star = Star()

# define functions
def draw_init():
    playBGM('opening')
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
                playBGM('gaming')

def read_story(src, bg):
    textLine = read_txt(src)
    dialogue = Dialogue(textLine[0][0], (90, 350))
    dialogue_2 = Dialogue(textLine[0][1], (90, 380))
    story_text.add(dialogue)
    story_text.add(dialogue_2)

    dialogue_bg = pygame.Surface((GAME_BASE_SETUP["WIDTH"], GAME_BASE_SETUP["HEIGHT"]))
    dialogue_bg.fill((50, 50, 50))
    dialogue_bg.set_alpha(150)
    screen.blit(dialogue_bg, (0, 300))

    waiting = True
    Key_up_times = 1
    while waiting:
        clock.tick(GAME_BASE_SETUP["FPS"])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYUP:
                dialogue.setText(textLine[Key_up_times][0])
                dialogue_2.setText(textLine[Key_up_times][1])
                Key_up_times += 1
                screen.blit(bg, (0, 0))
                screen.blit(dialogue_bg, (0, 300))

        if Key_up_times >= len(textLine):
            waiting = False
        else:
            story_text.update()
            story_text.draw(screen)
            pygame.display.update()

def draw_plot():
    screen.fill(COLOR["BLACK"])
    pygame.display.update()
    pygame.time.delay(3000)
    
def createRock():
    rock = Rock()
    all_sprites.add(rock)
    rocks.add(rock)
    
def RecreateRock(rock: Rock, RandomMode = False):
    rock.kill()
    newRock = Rock(RandomMode)
    rocks.add(newRock)
    all_sprites.add(newRock)

def addStationIntoGroup():
    if station.alive() == False:
        all_sprites.add(station)
        stations.add(station)

def createBlackHole():
    all_sprites.add(blackhole)
    blackholes.add(blackhole)
    
    
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
    
def playBGM(BGM):
    pygame.mixer.music.load(os.path.join('sound', 'BGM', f'{BGM}.mp3'))
    pygame.mixer.music.set_volume(0.7)
    pygame.mixer.music.play(-1)

# add sprites into groups
all_sprites.add(player)
for i in range(GAME_SETUP["NUM_OF_ROCKS"]): createRock()
addStationIntoGroup()
createBlackHole()

# gaming loop
show_init = True
story = True
running = True
lastPlayerLocation = player.getLocation()
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
        player.setHealth(player.getHealth() - hit.radius)
        expl = Explosion(hit.rect.center, hit.rect.width * 1.5)
        all_sprites.add(expl)
        damage_sound.play()
        createRock()
        if player.getHealth() <= 0: running = False
        
    # Rock Zone
    rockList = rocks.sprites()
    for rock in rockList:
        if rock.isOutOfBoundary(): RecreateRock(rock)
    
    if lastPlayerLocation != player.getLocation():
        for rock in rockList: RecreateRock(rock, True)
        lastPlayerLocation = player.getLocation()
        
    if len(rockList) > GAME_SETUP["NUM_OF_ROCKS"]:
        for rock in rockList: rock.kill()
    elif len(rockList) < GAME_SETUP["NUM_OF_ROCKS"]:
        createRock()
    
    # Space Station Zone
    Heal = pygame.sprite.spritecollide(player, stations, False, pygame.sprite.collide_circle)
    if Heal:
        hp = player.getHealth()
        if not(station.getIsUsed()):
            if hp + GAME_SETUP["STATION_HEAL"] >= 100:
                player.setHealth(100)
            else:
                player.setHealth(hp + GAME_SETUP["STATION_HEAL"])
            heal_sound.play()
            station.setIsUsed(True)
    
    if not(station.chuck_check(player.getLocation())):
        station.kill()
        if station.getIsUsed():
            station = SpaceStation()
    else:
        addStationIntoGroup()

    if bool(chuck.count(player.getLocation())):
        if not(stars.has(star)):
            star = Star()
            star.setLocation(player.getLocation())
            stars.add(star)
        if star.getLocation() != player.getLocation() and star.getLocation() != "none":
            stars.empty()
    else:
        stars.empty()
        
    endGame = pygame.sprite.spritecollide(player, blackholes, False, pygame.sprite.collide_circle)
    if not(blackhole.chuck_check(player.getLocation())):
        blackhole.kill()

    # # Star Zone
    # Create = pygame.sprite.spritecollide(player, stars, False, pygame.sprite.collide_circle)
    # if Create:
    #     draw_plot()

    # display screen
    BGindex = location_index(player.getLocation())
    background_img = BGlist[BGindex[0]][BGindex[1]]
    screen.blit(background_img, (0, 0))

    # read story
    if story:
        read_story("./story/start.txt", background_img)
        story = False

    all_sprites.draw(screen)
    stars.draw(screen)
    draw_health(screen, player.getHealth(), 10, 10)
    draw_location_text(screen, player.getLocation())
    pygame.display.update()

pygame.quit()