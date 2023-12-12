import pygame
pygame.init()

SCREEN_x , SCREEN_y = (1920 , 1080)
screen = pygame.display.set_mode((SCREEN_x , SCREEN_y))
pygame.display.set_caption('Snake Game')

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)

pos_x , pos_y = (30, SCREEN_y/2)
dir_x , dir_y = (3.44 , 0)
speed = 3.44

RUNNING = True

timer = pygame.time.Clock()
framerate = 20

def update():
    global pos_x
    global pos_y
    global dir_x
    global dir_y
    if pos_x < SCREEN_x-30:
        pos_x += dir_x
    else:
        dir_x = dir_x * -1
        pos_x -= 5
    if pos_x > 35:
        pos_x += dir_x
    else:
        dir_x = dir_x * -1
        pos_x += 5
    if pos_y < SCREEN_y-5:
        pos_x += dir_x
    else:
        dir_y = dir_y * -1
        pos_y -= 5
    if pos_y > 5:
        pos_y += dir_y
    else:
        dir_y = dir_y * -1
        pos_y += 5

while RUNNING:
    timer.tick(framerate)
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        
        #Controls Movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                dir_x = 0
                dir_y = -speed
            if event.key == pygame.K_a:
                dir_x = -speed
                dir_y = 0
            if event.key == pygame.K_s:
                dir_x = 0
                dir_y = speed
            if event.key == pygame.K_d:
                dir_x = speed
                dir_y = 0
    update()

    screen.fill(black)

    pygame.draw.line(screen,white,(pos_x , pos_y),(pos_x - 5, pos_y),5)
    pygame.draw.line(screen,red,(15 , 0),(15, SCREEN_y),30)
    pygame.draw.line(screen,red,(1905 , 0),(1905, SCREEN_y),30)

    pygame.display.flip()

    pygame.display.flip()