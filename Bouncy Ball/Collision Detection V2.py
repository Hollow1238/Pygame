

import pygame
pygame.init()

screen_width = 1600
screen_height = 1410
window = pygame.display.set_mode((screen_width , screen_height))



# Game Variables
White , Red , Green , Blue , Black = (255,255,255), (255,0,0), (0,255,0), (0,0,255), (0,0,0)  
FPS = 144


def get_background(name):
    image = pygame.image.load(name)
    _, _, width, height = image.get_rect()
    tiles = []
    for i in range(screen_width // width + 1):
        for j in range(((screen_height - height) // height + 1 ), (screen_height // height + 1)):
            pos = (i * width, j * height )
            tiles.append(pos)
    return tiles, image

def draw(window, background, bg_image):
    for tile in background:
        window.blit(bg_image, tile)
 
    pygame.display.update()


def main(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background('Bouncy Ball\Slime_Block_29_JE2_BE3.png')

    Running = True
    while Running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                Running = False

        draw(window, background, bg_image)

    mx, my = pygame.mouse.get_pos()
    offset = (mx - ox, my - oy)
    result = obstacle_mask.overlap()



    pygame.quit()
    quit()

if __name__ == "__main__":
    main(window)