import pygame
from pygame.locals import *

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
class A44:
    def __init__(self):
        self.rect = pygame.draw.rect(screen, black, (80, 100, 40, 40))
        print("Curator Station")


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
    pygame.draw.rect(screen, (255, 0, 0), (70, 90, 40, 40))
    pygame.draw.rect(screen, (255, 0, 0), (295, 80, 40, 40))
    pygame.draw.rect(screen, (255, 0, 0), (525, 80, 40, 40))
    pygame.draw.rect(screen, (255, 0, 0), (700, 80, 40, 40))
    pygame.draw.rect(screen, (255, 0, 0), (415, 155, 40, 40))
    pygame.draw.rect(screen, (255, 0, 0), (525, 155, 40, 40))
    pygame.draw.rect(screen, (255, 0, 0), (620, 155, 40, 40))
    pygame.draw.rect(screen, (255, 0, 0), (230, 250, 40, 40))
    pygame.draw.rect(screen, (255, 0, 0), (320, 250, 40, 40))
    pygame.draw.rect(screen, (255, 0, 0), (500, 250, 40, 40))
    pygame.draw.rect(screen, (255, 0, 0), (670, 200, 40, 40))
    pygame.draw.rect(screen, (255, 0, 0), (60, 320, 40, 40))
    pygame.draw.rect(screen, (255, 0, 0), (240, 320, 40, 40))
    pygame.draw.rect(screen, (255, 0, 0), (505, 295, 60, 30))
    pygame.draw.rect(screen, (255, 0, 0), (750, 285, 40, 40))
    pygame.draw.rect(screen, (255, 0, 0), (320, 380, 40, 40))
    pygame.draw.rect(screen, (255, 0, 0), (395, 360, 40, 40))
    pygame.draw.rect(screen, (255, 0, 0), (505, 385, 60, 30))
    pygame.draw.rect(screen, (255, 0, 0), (620, 380, 40, 40))
    pygame.draw.rect(screen, (255, 0, 0), (250, 450, 60, 60))
    pygame.draw.rect(screen, (255, 0, 0), (395, 455, 40, 40))
    pygame.draw.rect(screen, (255, 0, 0), (525, 455, 40, 40))
    pygame.draw.rect(screen, (255, 0, 0), (150, 550, 60, 60))
    pygame.draw.rect(screen, (255, 0, 0), (395, 520, 40, 40))
    pygame.draw.rect(screen, (255, 0, 0), (635, 570, 40, 40))
    pygame.draw.rect(screen, (255, 0, 0), (60, 650, 60, 60))
    pygame.draw.rect(screen, (255, 0, 0), (525, 680, 40, 40))
    pygame.draw.rect(screen, (255, 0, 0), (695, 635, 40, 40))
    # Checks for stations
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if station1.rect.collidepoint(pygame.mouse.get_pos()):
                print("Mouse clicked on the Player")

        if event.type == pygame.MOUSEBUTTONUP:
            if station1.rect.collidepoint(pygame.mouse.get_pos()):
                print("Mouse released on the Player")

    pygame.display.update()
