import pygame
from pygame.locals import *

pygame.init()

blue = (0, 0, 255)
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)

mif = "assets/map.png"
bif = "assets/train.png"

screen = pygame.display.set_mode((800, 800), 0, 32)
metro = pygame.image.load(mif).convert()
train = pygame.image.load(bif).convert_alpha()
pygame.display.set_caption("Metro 20X3")

game_over = False

x = 342
y = 266

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()
speedx = 150
speedy = 150

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                y1_change = -10
                x1_change = 0
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                y1_change = 10
                x1_change = 0
    screen.fill(white)
    screen.blit(metro, (0, 0))
    screen.blit(train, (x, y))

    ######################################
    # Was supposed to be diagonal movement
    ######################################
    # milli = clock.tick()
    # seconds = milli / 10000
    # dmx = seconds * speedx + (x1_change / 100)
    # dmy = seconds * speedy + (y1_change / 100)
    # x += dmx
    # y += dmy

    pygame.display.update()

quit()
