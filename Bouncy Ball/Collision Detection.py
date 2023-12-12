import pygame
import math

pygame.init()

SCREEN_x , SCREEN_y = (1920 , 1080)
screen = pygame.display.set_mode((SCREEN_x , SCREEN_y))
pygame.display.set_caption('Snake Game')
timer = pygame.time.Clock()
framerate = 144

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)

square_1_pos_x , square_1_pos_y = SCREEN_x/2 , SCREEN_y/2
square_2_pos_x , square_2_pos_y = SCREEN_x/2 + 25, SCREEN_y/2 + 25

RUNNING = True

def distance_calc():
    global square_1_pos_x
    global square_1_pos_y
    global square_2_pos_x
    global square_2_pos_y
    dist_1_2 = math.sqrt(((square_2_pos_x - square_1_pos_x) ** 2) + ((square_2_pos_y - square_1_pos_y ) ** 2))
    print(dist_1_2)
                

    
while RUNNING:
    timer.tick(framerate)
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
    distance_calc()

    screen.fill(black)

    squre_1 = pygame.draw.line(screen,white,(square_1_pos_x , square_1_pos_y),(square_1_pos_x - 5, square_1_pos_y),5)
    square_2 = pygame.draw.line(screen,white,(square_2_pos_x , square_2_pos_y),(square_2_pos_x - 5, square_2_pos_y),5)

    pygame.display.flip()