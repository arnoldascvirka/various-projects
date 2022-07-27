# Importing libraries
import pygame
import pygame.font
from pygame.locals import *
import time

# Importing Modules
from stationsTime import *


# Method to print any text, pygame creates an image with given text and returns it.

font = pygame.font.SysFont(None, 24)


def message_display(text):
    message = font.render(text, True, black)
    screen.blit(message, (950, 180))
    pygame.display.update()
    time.sleep(0.2)


def message_display_xy(text, x, y):
    message = font.render(text, True, black)
    screen.blit(message, (x, y))
    pygame.display.update()
    time.sleep(0.2)


def message_display_territory(text):
    message = font.render(text, True, black)
    screen.blit(message, (950, 250))
    pygame.display.update()
    time.sleep(0.2)


def message_display_station_text(text):
    lines = text.splitlines()
    for l in lines:
        screen.blit(font.render(l, True, black), (880, 250))
