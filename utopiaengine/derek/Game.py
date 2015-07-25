'''
@author: adm
'''
import pygame

from sys import exit

# screen = pygame.display.set_mode((735, 951), 0, 32);
# background = pygame.Surface

def initGame():
    pass


def initScreen():
    global screen 
    global background 
    background_image_filename = '../1_m.png';
    pygame.display.set_caption("Hello, World!")
    screen = pygame.display.set_mode((735, 951), 0, 32);
    background = pygame.image.load(background_image_filename).convert()
    pass


if __name__ == '__main__':
    
    
    initGame();
    
    initScreen();
    
#     main loop
    while True:
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
    
                exit()
     
        screen.blit(background, (0,0))
    
     
    #     x, y = pygame.mouse.get_pos()
    
    #     x-= mouse_cursor.get_width() / 2
    #     y-= mouse_cursor.get_height() / 2
    # 
    #     screen.blit(mouse_cursor, (x, y))
    
     
        pygame.display.update()
    