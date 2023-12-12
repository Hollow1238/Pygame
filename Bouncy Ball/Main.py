import pygame
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

pos_x , pos_y = (SCREEN_x/2, 0)
gravity = 9.8/(framerate*2)
velocity_y = 1

RUNNING = True

def update():
    global pos_x
    global pos_y
    global velocity_y

    if pos_y < 1080:
        pos_y = pos_y + velocity_y
        velocity_y += gravity

    else:
        velocity_y = velocity_y * (-.75)
        pos_y -= 5

    if pos_y > 1078 and 0 < velocity_y < 1:
        velocity_y = 0
    print(f"velocity: {velocity_y}    Position: {pos_y}")


    
while RUNNING:
    timer.tick(framerate)
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
    update()

    screen.fill(black)

    pygame.draw.line(screen,white,(pos_x , pos_y),(pos_x - 5, pos_y),5)


    pygame.display.flip()

    pygame.display.flip()