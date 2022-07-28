# Importing libraries
import pygame
import pygame.font
from pygame.locals import *

pygame.font.init()
black = (0, 0, 0)
font = pygame.font.SysFont(None, 24)
gui_top = font.render("SimpleMetro - Arnoldas Cvirka", True, black)
gui_station = font.render("Station: ", True, black)
screen = pygame.display.set_mode((800, 800), 0, 32)

# Define Station locations
a44 = pygame.draw.rect(screen, (255, 0, 0), (70, 90, 40, 40))
a55 = pygame.draw.rect(screen, (255, 0, 0), (295, 80, 40, 40))
a77 = pygame.draw.rect(screen, (255, 0, 0), (525, 80, 40, 40))
a99 = pygame.draw.rect(screen, (255, 0, 0), (700, 80, 40, 40))
b11 = pygame.draw.rect(screen, (255, 0, 0), (415, 155, 40, 40))
b78 = pygame.draw.rect(screen, (255, 0, 0), (525, 155, 40, 40))
b86 = pygame.draw.rect(screen, (255, 0, 0), (620, 155, 40, 40))
c11 = pygame.draw.rect(screen, (255, 0, 0), (230, 250, 40, 40))
c91 = pygame.draw.rect(screen, (255, 0, 0), (320, 250, 40, 40))
c38 = pygame.draw.rect(screen, (255, 0, 0), (500, 250, 40, 40))
c25 = pygame.draw.rect(screen, (255, 0, 0), (670, 200, 40, 40))
d19 = pygame.draw.rect(screen, (255, 0, 0), (60, 320, 40, 40))
d34 = pygame.draw.rect(screen, (255, 0, 0), (240, 320, 40, 40))
d67 = pygame.draw.rect(screen, (255, 0, 0), (505, 295, 60, 30))
d89 = pygame.draw.rect(screen, (255, 0, 0), (750, 285, 40, 40))
e71 = pygame.draw.rect(screen, (255, 0, 0), (320, 380, 40, 40))
e94 = pygame.draw.rect(screen, (255, 0, 0), (395, 360, 40, 40))
e47 = pygame.draw.rect(screen, (255, 0, 0), (505, 385, 60, 30))
e85 = pygame.draw.rect(screen, (255, 0, 0), (620, 380, 40, 40))
f57 = pygame.draw.rect(screen, (255, 0, 0), (250, 450, 60, 60))
f64 = pygame.draw.rect(screen, (255, 0, 0), (395, 455, 40, 40))
f97 = pygame.draw.rect(screen, (255, 0, 0), (525, 455, 40, 40))
g58 = pygame.draw.rect(screen, (255, 0, 0), (150, 550, 60, 60))
g39 = pygame.draw.rect(screen, (255, 0, 0), (395, 520, 40, 40))
g12 = pygame.draw.rect(screen, (255, 0, 0), (635, 570, 40, 40))
h22 = pygame.draw.rect(screen, (255, 0, 0), (60, 650, 60, 60))
h82 = pygame.draw.rect(screen, (255, 0, 0), (525, 680, 40, 40))
h02 = pygame.draw.rect(screen, (255, 0, 0), (695, 635, 40, 40))


# list1 = [
#     a44,
#     a55,
#     a77,
#     a99,
#     b11,
#     b78,
#     b86,
#     c11,
#     c91,
#     c38,
#     c25,
#     d19,
#     d34,
#     d67,
#     d89,
#     e71,
#     e94,
#     e47,
#     e85,
#     f57,
#     f64,
#     f97,
#     g58,
#     g39,
#     g12,
#     h22,
#     h82,
#     h02,
# ]
