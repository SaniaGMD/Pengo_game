import pygame  # load pygame keywords
import sys     # let  python use your file system
import os      # help python identify your OS
import time
import random
from plyaer1 import Player
from enemy import Enemy
pygame.init()

steps = 10  # how many pixels to move

#basic_screen_settings
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 1050
dis_height = 630
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

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Game')

clock = pygame.time.Clock()
snake_block=10
#text_display
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3]) 
    
    
def gameLoop():
    game_over = False
    game_close = False
    player = Player()  # spawn player
    player.rect.x = 0  # go to x
    player.rect.y = 30  # go to y
    player_list = pygame.sprite.Group()
    player_list.add(player)
    steps = 10

 
    #foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    #foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
 
    while not game_over:
        #adding_tiles
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
        
        
        
        while game_close == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    try:
                        sys.exit()
                    finally:
                        game_over = False

                if event.type == pygame.KEYDOWN:
                    if event.key == ord('q'):
                        pygame.quit()
                        try:
                            sys.exit()
                        finally:
                            game_over = False
                    if event.key == pygame.K_LEFT or event.key == ord('a'):
                        player.control(-steps, 0)
                    if event.key == pygame.K_RIGHT or event.key == ord('d'):
                        player.control(steps, 0)
                    if event.key == pygame.K_UP or event.key == ord('w'):
                        print('jump')

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == ord('a'):
                        player.control(steps, 0)
                    if event.key == pygame.K_RIGHT or event.key == ord('d'):
                        player.control(-steps, 0)

 
        
 
        pygame.display.update()
        player.update()
        player_list.draw(dis)
        enemy_list.draw(dis)
        for e in enemy_list:
            e.move()
        pygame.display.flip()
        clock.tick(fps)

       
    pygame.quit()
    quit()
 
 
gameLoop()  
