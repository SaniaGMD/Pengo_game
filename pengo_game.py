import pygame
import sys
import os

'''
Variables
'''

worldx = 1050
worldy = 630
fps = 40
ani = 4
dis = pygame.display.set_mode([worldx, worldy])

BLUE = (25, 25, 200)
BLACK = (23, 23, 23)
WHITE = (254, 254, 254)
ALPHA = (0, 255, 0)
jump= False
vel_x=10
vel_y=10


'''
Objects
'''


class Player(pygame.sprite.Sprite):
    """
    Spawn a player
    """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.health = 10
        self.images = []
        for i in range(1, 5):
            img = pygame.image.load(os.path.join('images', 'walk-' + str(i) + '.png')).convert()
            img.convert_alpha()
            
            self.images.append(img)
            self.image = self.images[0]
            img.set_colorkey(ALPHA)
            self.rect = self.image.get_rect()
            
        
    def control(self, x, y):
        """
        control player movement
        """
        self.movex += x
        self.movey += y

    def update(self):
        """
        Update sprite position
        """

        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey

        # moving left
        if self.movex < 0:
            self.frame += 1
            if self.frame > 3*ani:
                self.frame = 0
            self.image = pygame.transform.flip(self.images[self.frame // ani], True, False)

        # moving right
        if self.movex > 0:
            self.frame += 1
            if self.frame > 3*ani:
                self.frame = 0
            self.image = self.images[self.frame//ani]

        hit_list = pygame.sprite.spritecollide(self, enemy_list, False)
        for enemy in hit_list:
            self.health -= 1
            print(self.health)


class Enemy(pygame.sprite.Sprite):
    """
    Spawn an enemy
    """
    def __init__(self, x, y, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('images', img))
        self.image.convert_alpha()
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.counter = 0

    def move(self):
        """
        enemy movement
        """
        distance = 40
        speed = 3

        if self.counter >= 0 and self.counter <= distance:
            self.rect.x += speed
        elif self.counter >= distance and self.counter <= distance*2:
            self.rect.x -= speed
        else:
            self.counter = 0

        self.counter += 1


class Level():
    def bad(lvl, eloc):
        if lvl == 1:
            enemy = Enemy(eloc[0], eloc[1], 'walk-1.png')
            enemy_list = pygame.sprite.Group()
            enemy_list.add(enemy)
        if lvl == 2:
            print("Level " + str(lvl) )

        return enemy_list


'''
Setup
'''

backdrop = pygame.image.load(os.path.join('images', 'BG.png'))
clock = pygame.time.Clock()
pygame.init()
#backdropbox = world.get_rect()
main = True

player = Player()  # spawn player
player.rect.x = 100  # go to x
player.rect.y = 510  # go to y
player_list = pygame.sprite.Group()
player_list.add(player)
steps = 10

eloc = []
eloc = [340, 430]
eloc1 = []
eloc1 = [0,0]
enemy_list = Level.bad(1, eloc )
enemy_list1 = Level.bad(1, eloc1 )
#e2=Enemy(200, 100, 'walk-1.png')

a1=pygame.image.load("1.png")
a2=pygame.image.load("2.png")
a3=pygame.image.load("3.png")
a17=pygame.image.load("17.png")
a13=pygame.image.load("13.png")
a14=pygame.image.load("14.png")
a15=pygame.image.load("15.png")
a4=pygame.image.load("4.png")
a5=pygame.image.load("5.png")
a6=pygame.image.load("6.png")
t1=pygame.image.load("Tree_2.png")
t1 = pygame.transform.scale(t1, (100, 75+50))
t2=pygame.image.load("Tree_3.png")
t2 = pygame.transform.scale(t2, (100, 75+50))
b3=pygame.image.load("Bush (3).png")
b4=pygame.image.load("Bush (4).png")
c1=pygame.image.load("Crate.png")
background_image =pygame.image.load("BG.png")

#adding_tiles
#dis.blit(background_image, [0, 0])


        
'''
Main Loop
'''
gravity= -1
while main:
    dis.blit(background_image, [0, 0])
    dis.blit(a1, [0, 550])
    dis.blit(a2, [80, 550])
    dis.blit(a3, [160, 550])
    dis.blit(a17, [160+80, 575])

    dis.blit(a13, [160, 150])
    dis.blit(a14, [160+80, 150])
    dis.blit(a15, [160+80+80, 150])

    dis.blit(a4, [240+80, 550])
    dis.blit(a5, [240+80+80, 550])
    dis.blit(a6, [240+80+80+80, 550])

    dis.blit(a1, [240+80, 550-80])
    dis.blit(a2, [240+80+80, 550-80])
    dis.blit(a3, [240+80+80+80,550-80])

    #adding_trees
    dis.blit(b3, [60, 550-40])
    dis.blit(b4, [140, 550-40])
    dis.blit(t1, [90, 550-120])
    dis.blit(c1, [250, 120])
    dis.blit(c1, [250+30, 120])
    dis.blit(c1, [265, 90])
    
    
    
    #key_pressed = pygame.key.get_pressed()
    #if key_pressed[pygame.K_SPACE]:
     #   jump=True
    #if jump:
     #   player.movey -= vel_y
      #  vel_y -= gravity
       # if vel_y <- 10:
        #    jump = False
         #   player.movey = 10
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            try:
                sys.exit()
            finally:
                main = False

        if event.type == pygame.KEYDOWN:
            if event.key == ord('q'):
                pygame.quit()
                try:
                    sys.exit()
                finally:
                    main = False
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(-steps, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(steps, 0)
            
            
            
            
            if event.key == pygame.K_UP or event.key == ord('w'):
                print('jump')
                jump = True
                
            if jump is True:
                player.movey -= vel_y
                vel_y -= 1
                #if player.movey < -10:          #any free move in the screen
                if vel_y < -10:                  #only straight up
                    jump = False
                    vel_y = 10
                    player.movey += 20
             
            
            
            
            
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(steps, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(-steps, 0)
                
            if event.key == pygame.K_UP or event.key == ord('w'):
                print('jump')
                jump = True
            if jump is True:
                player.movey -= vel_y
                vel_y -= 1
                if vel_y < 10:
                    jump = False
                    vel_y = 10
                player.movey += 20
                    

    #world.blit(backdrop, backdropbox)
    player.update()
    player_list.draw(dis)
    enemy_list.draw(dis)
    for e in enemy_list:
        e.move()
    pygame.display.flip()
    clock.tick(fps)