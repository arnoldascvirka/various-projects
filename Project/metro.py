import pygame
from pygame.locals import *

pygame.init()

blue = (0, 0, 255)
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)

img = pygame.image.load("map.png")
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Metro")

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
    screen.blit(img, (0, 0))
    milli = clock.tick()
    seconds = milli / 1000
    dmx = seconds * speedx
    dmy = seconds * speedy
    x += dmx
    y += dmy

    pygame.draw.rect(screen, blue, [x, y, 10, 10])

    pygame.display.update()

    clock.tick(15)

quit()
