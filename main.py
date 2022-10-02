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
from src.Explosion import *
from src.StarCoin import *
from src.LocationFunction import *
from src.StoryBackground import *

# init & create a window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((GAME_BASE_SETUP["WIDTH"], GAME_BASE_SETUP["HEIGHT"]))
pygame.display.set_caption(GAME_BASE_SETUP["GAMENAME"])
pygame.display.set_icon(pygame.image.load(os.path.join('img', 'logo.png')))
clock = pygame.time.Clock()

# load json file
readed_star = []
with open('./story/star.json', mode='r', encoding='utf-8') as file:
    location_star = json.load(file)
with open('./story/script.json', mode='r', encoding='utf-8') as file:
    script = json.load(file)
with open("./story/star.json", mode="r", encoding="utf-8") as file:
    data = json.load(file)
chuck = list(data.keys())

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
zhFont = os.path.join('font', 'TaipeiSans.ttf')
enFont = os.path.join('font', 'voltergoldfish.ttf')

# sprite group
all_sprites = pygame.sprite.Group()
rocks = pygame.sprite.Group()
stations = pygame.sprite.Group()
stars = pygame.sprite.Group()
story_text = pygame.sprite.Group()
blackholes = pygame.sprite.Group()
bg = pygame.sprite.Group()

# create sprite
player = Player()
station = SpaceStation()
blackhole = BlackHole()

def draw_text(text: str, text_size: int, topleft: tuple, font=enFont, background:tuple=None):
    font = pygame.font.Font(font, text_size)
    text_surface = font.render(text, True, COLOR["WHITE"], background)
    screen.blit(text_surface, topleft)

# define functions
def draw_init():
    playBGM('opening')
    screen.blit(init_background_img, (0, 0))
    draw_text("Enter to start", 20, (1024 - 150, 516 - 30), background=(0, 0, 0))

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

def show_story_bg(star_name: str):
    story_image = pygame.image.load(os.path.join('img', 'story_background', f'{star_name}.jpg')).convert()
    story_image = pygame.transform.scale(story_image, (GAME_BASE_SETUP["WIDTH"], GAME_BASE_SETUP["HEIGHT"]))
    screen.blit(story_image, (0, 0))
    return story_image

def get_gray_mask():
    gray_mask = pygame.Surface((GAME_BASE_SETUP["WIDTH"], GAME_BASE_SETUP["HEIGHT"]))
    gray_mask.fill((50, 50, 50))
    gray_mask.set_alpha(150)
    return gray_mask

def show_question(star_name: str):
    with open(os.path.join('story', f'{star_name}', 'question.json'), mode='r', encoding='utf-8') as file:
        data = json.load(file)
    show_story_bg(star_name)
    gray_mask = get_gray_mask()
    screen.blit(gray_mask, (0, 0))
    draw_text("Q:", 30, (95, 70))
    questionList = split_text(data["question"], 10)
    show_dialogue(questionList, 28, (95, 110))
    for i in range(len(data["options"])):
        optionList = split_text(f'{i + 1}. {data["options"][i]}', 10)
        show_dialogue(optionList, 24, (130, 250 + 30 * (i + 1)))
    pygame.display.update()

    waiting = True
    while waiting:
        clock.tick(GAME_BASE_SETUP["FPS"])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1: ans = 0
                elif event.key == pygame.K_2: ans = 1
                elif event.key == pygame.K_3: ans = 2
                elif event.key == pygame.K_4: ans = 3
                else: ans = -1
                
                if ans != -1: 
                    if ans == data["answer"]: 
                        player.addEarnedStars()
                        createStarCoin()
                    waiting = False

# split text
def split_text(text: str, long: int): # return text list
    textList = []
    char_list = list(text.split(" "))
    text = ""
    while len(char_list) > long:
        for i in range(0, long):
            text += char_list[i] + " "
        print(text)
        textList.append(text)
        char_list = char_list[long - 1: len(char_list)]
        text = ""
        
    for i in range(0, len(char_list)):
        text += char_list[i] + " "
    if (len(char_list) != 0):
        textList.append(text)
    print(textList)
    return textList

def show_dialogue(textList: list, size, topleft: tuple):
    for i in range(0, len(textList)):
        draw_text(textList[i], size, (topleft[0], topleft[1] + ((i) * 30)))

# dialog read and display
def read_story(src, bg):
    with open(src, mode='r', encoding='utf-8') as file:
        readLine = file.read().split("\n\n")
    textList = []
    for i in readLine:
        textList.append(split_text(i, 13))
    dialogue_bg = get_gray_mask()
    key_up_times = 1
    waiting = True
    while waiting:
        clock.tick(GAME_BASE_SETUP["FPS"])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYUP and key_up_times > len(textList):
                waiting = False
            elif event.type == pygame.KEYUP:
                screen.blit(bg, (0, 0))
                screen.blit(dialogue_bg, (0, 350))
                show_dialogue(textList[key_up_times - 1], 25, (50, 370))
                pygame.display.update()
                key_up_times += 1

def draw_story_scenes(star_name: str, file_name: str = None):
    with open(os.path.join('story', f'{star_name}', 'question.json'), mode='r', encoding='utf-8') as file:
        data = json.load(file)
    playBGM('WatchingStar')
    if file_name == None: file_name = star_name
    story_image = show_story_bg(star_name)
    bgggg = StoryBackground(star_name, 31)
    bg.add(bgggg)
    pygame.display.update()
    waiting = True
    while waiting:
        bg.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting = False
        bg.draw(screen)
        show_dialogue(split_text(data["info"], 10), 20, (20, 20))
        # draw_text(f'{data["info"]}', 20, (20, 20))
        draw_text("Enter to continue", 20, (1024 - 210, 512 - 30), font=enFont)
        pygame.display.update()
    read_story(os.path.join('story', f'{star_name}', f'{file_name}.txt'), story_image)

def createStarCoin():
    starcoin = StarCoin(player.getEarnedStars())
    all_sprites.add(starcoin)
    
def createRock():
    rock = Rock()
    all_sprites.add(rock)
    rocks.add(rock)
    
def RecreateRock(rock: Rock, RandomMode = False):
    rock.kill()
    newRock = Rock(RandomMode)
    rocks.add(newRock)
    all_sprites.add(newRock)
    
def createStar(center: tuple, size: int, cycle: int):
    star = Star(center, size, cycle)
    star.setLocation(player.getLocation())
    stars.add(star)
    all_sprites.add(star)    

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

def playBGM(BGM):
    pygame.mixer.music.load(os.path.join('sound', 'BGM', f'{BGM}.mp3'))
    pygame.mixer.music.set_volume(0.7)
    pygame.mixer.music.play(-1)

# add sprites into groups
all_sprites.add(player)
for i in range(GAME_SETUP["NUM_OF_ROCKS"]): createRock()
addStationIntoGroup()

# gaming loop
show_init = True
story_init = True
running = True
lastPlayerLocation = player.getLocation()
while running:
    # execute at most <FPS> times in 1 sec
    clock.tick(GAME_BASE_SETUP["FPS"])
    
    # show the game init screen
    if show_init:
        draw_init()
        show_init = False
   
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

    # Star Zone
    Create = pygame.sprite.spritecollide(player, stars, False, pygame.sprite.collide_circle)
    if Create and (not player.getLocation() in readed_star):
        readed_star.append(player.getLocation())
        star_name = location_star[player.getLocation()]
        draw_story_scenes(star_name)
        show_question(star_name)
        read_story(os.path.join('story', 'doge', f'{len(readed_star) - 1}.txt'), background_img)
        playBGM('gaming')
        
    if player.getLocation() in chuck:
        if stars.__len__() == 0: createStar((512, 256), 100, 200)
    else:
        for star in stars.sprites(): star.kill()
        
    # Blackhole Zone
    absorb = pygame.sprite.groupcollide(blackholes, rocks, True, pygame.sprite.collide_circle)
    endGame = pygame.sprite.spritecollide(player, blackholes, False, pygame.sprite.collide_circle)
    if player.getEarnedStars() >= GAME_SETUP["TARGET"]:
        if blackhole.chuck_check(player.getLocation()):
            createBlackHole()
        else:
            blackhole.kill()
        if endGame:
            draw_story_scenes("Earth")
            running = False

    # display screen
    BGindex = location_index(player.getLocation())
    background_img = BGlist[BGindex[0]][BGindex[1]]
    screen.blit(background_img, (0, 0))

    # read story
    if story_init:
        pygame.display.update()
        read_story("./story/start.txt", background_img)
        story_init = False

    all_sprites.draw(screen)
    stars.draw(screen)
    draw_health(screen, player.getHealth(), 10, 10)
    draw_text(player.getLocation(), GAME_SETUP["LOCATION_TEXT_SIZE"], GAME_SETUP["LOCATION_TEXT_CENTER"], font=enFont)
    pygame.display.update()

pygame.quit()
