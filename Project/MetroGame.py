# Importing libraries
import pygame
import pygame.font
from pygame.locals import *

# Importing Modules
from stationsTime import *
from text import *
from hoverclick import *


def Main():
    # Initializes pygame
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((1200, 800), 0, 32)
    pygame.display.set_caption("Metro 20X3")

    # Define colors / images / variables
    bif = "assets/map.png"
    mif = "assets/train.png"
    metro = pygame.image.load(bif).convert()
    train = pygame.image.load(mif).convert_alpha()
    white = (255, 255, 255)
    black = (0, 0, 0)
    game_over = False
    clock = pygame.time.Clock()
    run_once = 0

    # Define methods and classes
    def startgame():
        font = pygame.font.SysFont(None, 24)
        gui_start = font.render("Choose starting station.", True, black)
        screen.blit(gui_start, (880, 220))

    # Starts loop
    while not game_over:
        clock.tick()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        # Draws stuff
        screen.fill(white)
        screen.blit(metro, (0, 0))
        screen.blit(gui_top, (880, 80))
        screen.blit(gui_station, (880, 180))

        # Checks station selection
        if run_once == 0:
            startgame()
            run_once == 1
        hover()
        click()
        # Updates the game screen
        pygame.display.update()


Main()
