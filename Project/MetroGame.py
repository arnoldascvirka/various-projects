import pygame
from pygame.locals import *
from stations import *

# Initializes pygame
pygame.init()
screen = pygame.display.set_mode((800, 800), 0, 32)
pygame.display.set_caption("Metro 20X3")

# Define colors / images / variables
bif = "assets/map.png"
mif = "assets/train.png"
metro = pygame.image.load(bif).convert()
train = pygame.image.load(mif).convert_alpha()
white = (255, 255, 255)
black = (255, 0, 0)
game_over = False

# Define stations
station1 = A44()

clock = pygame.time.Clock()

# Starts loop
while not game_over:
    clock.tick()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    # Draws stuff
    screen.fill(white)
    screen.blit(metro, (0, 0))
    # Checks for stations
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if station1.rect.collidepoint(pygame.mouse.get_pos()):
                print("Mouse clicked on the Player")

        if event.type == pygame.MOUSEBUTTONUP:
            if station1.rect.collidepoint(pygame.mouse.get_pos()):
                print("Mouse released on the Player")

quit()
