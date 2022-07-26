import pygame
from pygame.locals import *
from stations import *

# Initializes pygame
pygame.init()
screen = pygame.display.set_mode((800, 800), 0, 32)
pygame.display.set_caption("Metro 20X3")

# Define colors / images / variables
white = [255, 255, 255]
game_over = False

# Starts loop


station1 = A44()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if station1.rect.collidepoint(pygame.mouse.get_pos()):
                print("Mouse clicked on the Player")

        if event.type == pygame.MOUSEBUTTONUP:
            if station1.rect.collidepoint(pygame.mouse.get_pos()):
                print("Mouse released on the Player")
