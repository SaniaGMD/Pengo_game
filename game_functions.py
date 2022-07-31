import sys
import pygame

def check_events():
    ""Respond to keypress and mouse events""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        elif event.type == pygame.KEYDOWN:
             if event.type == pygame.K_RIGHT:
                ship.moving_right= True
            elif event.type == pygame.K_LEFT:
                ship.moving_left= True

                
        elif event.type == pygame.KEYUP:
             if event.type == pygame.K_RIGHT:
                ship.moving_right= False
            elif event.type == pygame.K_LEFT:
                ship.moving_leftt= False
                
def update_screen(ai_settings, screen, ship):
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        
        pygame.display.flip()
        
        
