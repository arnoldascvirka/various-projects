# Importing libraries
import pygame
import pygame.font
from pygame.locals import *

# Importing Modules
from hoverclick import *
from stationsTime import *
from text import *


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
    clicked = 0
    looptwo = 0
    # Define methods and classes
    def startgame():
        font = pygame.font.SysFont(None, 24)
        gui_start = font.render("Double click starting station.", True, black)
        screen.blit(gui_start, (880, 220))

    # Starts loop
    while not game_over:
        clock.tick()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            for r in rects:
                if event.type == pygame.MOUSEBUTTONUP:
                    if r.collidepoint(pygame.mouse.get_pos()):
                        clicked = 1
                        looptwo = 1
        # Draws stuff
        screen.fill(white)
        screen.blit(metro, (0, 0))
        screen.blit(gui_top, (880, 80))
        screen.blit(gui_bottom, (900, 700))
        screen.blit(gui_station, (880, 180))

        # Shows start game text and removes it when chosen
        if clicked == 0:
            startgame()

        # Checks station selection
        hover()
        if looptwo == 1:
            click()
        # Updates the game screen
        pygame.display.update()


Main()
