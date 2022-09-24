import pygame

# define const
FPS = 60
WIDTH = 960
HEIGHT = 540
GAMENAME = 'UNTITLED'

# init & create a window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(GAMENAME)
clock = pygame.time.Clock()

# sprite
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.speed = [8, 8]
        
        # absolute position
        # self.rect.x = 200
        # self.rect.y = 200
        
        # center position
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        
    def update(self):
        # get a class that store a list of bool that determine if any key was be clicked
        key_pressed = pygame.key.get_pressed()
        
        # control player to move
        if key_pressed[pygame.K_RIGHT]: self.rect.x += self.speed[0]
        if key_pressed[pygame.K_LEFT]: self.rect.x -= self.speed[0]
        if key_pressed[pygame.K_UP]: self.rect.y -= self.speed[1]
        if key_pressed[pygame.K_DOWN]: self.rect.y += self.speed[1]
            
        # setting border effect
        if self.rect.right > WIDTH: self.rect.right = WIDTH
        if self.rect.left < 0: self.rect.left = 0
        if self.rect.top < 0: self.rect.top = 0
        if self.rect.bottom > HEIGHT: self.rect.bottom = HEIGHT
        
# sprite group
all_sprites = pygame.sprite.Group()
player = Player()
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
    screen.fill((183, 224, 243))
    all_sprites.draw(screen)
    pygame.display.update()