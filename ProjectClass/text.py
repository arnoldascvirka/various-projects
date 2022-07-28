# Importing libraries
import pygame
import pygame.font
from pygame.locals import *
import time
import random

# Importing Modules
from stationsTime import *

# Method to print any text, pygame creates an image with given text and returns it.
pygame.font.init()
font = pygame.font.SysFont(None, 24)
black = (0, 0, 0)
screen = pygame.display.set_mode((1200, 800), 0, 32)


def message_display(text):
    message = font.render(text, True, black)
    screen.blit(message, (950, 180))
    pygame.display.update()


# Class for stations.
# fmt: off
class Station:
    def __init__(self, station, popR1, popR2, zone):
        self.station = station
        self.pop = random.randint(popR1, popR2)
        self.zone = zone
        self.black = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 24)

    def print_station(self):
        stationwelcome = self.font.render(f"Welcome to: {self.station}", True, self.black)
        screen.blit(stationwelcome, (880, 220))
        pygame.display.update()
        time.sleep(0.2)

    def print_population(self):
        population = self.font.render(f"Population: {self.pop}", True, self.black)
        screen.blit(population, (880, 260))
        pygame.display.update()
        time.sleep(0.2)
        
    def print_zone(self):
        zone = self.font.render(f"Zone: {self.zone}", True, self.black)
        screen.blit(zone, (880, 300))
        pygame.display.update()
        time.sleep(2)
# fmt: on
