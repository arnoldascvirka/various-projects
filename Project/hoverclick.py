# Importing libraries
import pygame
import pygame.font
from pygame.locals import *

# Importing Modules
from stationsTime import *
from text import *
from stationmethods import *


# Gets mouse position every frame and displays the Station information on hover.


def hover():
    if a44.collidepoint(pygame.mouse.get_pos()):
        message_display("Curator Station")
    elif a55.collidepoint(pygame.mouse.get_pos()):
        message_display("Helios Station")
    elif a77.collidepoint(pygame.mouse.get_pos()):
        message_display("Ark Station")
    elif a99.collidepoint(pygame.mouse.get_pos()):
        message_display("Origin Station")
    elif b11.collidepoint(pygame.mouse.get_pos()):
        message_display("Spire Terminal")
    elif b78.collidepoint(pygame.mouse.get_pos()):
        message_display("Glory")
    elif b86.collidepoint(pygame.mouse.get_pos()):
        message_display("Ether Station")
    elif c11.collidepoint(pygame.mouse.get_pos()):
        message_display("Felicity Base")
    elif c91.collidepoint(pygame.mouse.get_pos()):
        message_display("Atlas")
    elif c38.collidepoint(pygame.mouse.get_pos()):
        message_display("Cendre Colony")
    elif c25.collidepoint(pygame.mouse.get_pos()):
        message_display("Base Astraeus")
    elif d19.collidepoint(pygame.mouse.get_pos()):
        message_display("Dream Station")
    elif d34.collidepoint(pygame.mouse.get_pos()):
        message_display("Vestige Station")
    elif d67.collidepoint(pygame.mouse.get_pos()):
        message_display("Radiance")
    elif d89.collidepoint(pygame.mouse.get_pos()):
        message_display("Arcadis terminal")
    elif e71.collidepoint(pygame.mouse.get_pos()):
        message_display("Legacy Base")
    elif e94.collidepoint(pygame.mouse.get_pos()):
        message_display("Orbital resupply")
    elif e47.collidepoint(pygame.mouse.get_pos()):
        message_display("Serenity")
    elif e85.collidepoint(pygame.mouse.get_pos()):
        message_display("Atmos Station")
    elif f57.collidepoint(pygame.mouse.get_pos()):
        message_display("Escorte")
    elif f64.collidepoint(pygame.mouse.get_pos()):
        message_display("Azura Station")
    elif f97.collidepoint(pygame.mouse.get_pos()):
        message_display("Voyage Station")
    elif g58.collidepoint(pygame.mouse.get_pos()):
        message_display("Apollon")
    elif g39.collidepoint(pygame.mouse.get_pos()):
        message_display("Rogue Colony")
    elif g12.collidepoint(pygame.mouse.get_pos()):
        message_display("Terminus Chronos")
    elif h22.collidepoint(pygame.mouse.get_pos()):
        message_display("Terminal Valhalla")
    elif h82.collidepoint(pygame.mouse.get_pos()):
        message_display("Prism")
    elif h02.collidepoint(pygame.mouse.get_pos()):
        message_display("Settler Colony")


def click():
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if a44.collidepoint(pygame.mouse.get_pos()):
                A44()
            elif a55.collidepoint(pygame.mouse.get_pos()):
                A55()
            elif a77.collidepoint(pygame.mouse.get_pos()):
                A77()
            elif a99.collidepoint(pygame.mouse.get_pos()):
                A99()
            elif b11.collidepoint(pygame.mouse.get_pos()):
                B11()
            elif b78.collidepoint(pygame.mouse.get_pos()):
                B78()
            elif b86.collidepoint(pygame.mouse.get_pos()):
                B86()
            elif c11.collidepoint(pygame.mouse.get_pos()):
                C11()
            elif c91.collidepoint(pygame.mouse.get_pos()):
                C91()
            elif c38.collidepoint(pygame.mouse.get_pos()):
                C38()
            elif c25.collidepoint(pygame.mouse.get_pos()):
                C25()
            elif d19.collidepoint(pygame.mouse.get_pos()):
                D19()
            elif d34.collidepoint(pygame.mouse.get_pos()):
                D34()
            elif d67.collidepoint(pygame.mouse.get_pos()):
                D67()
            elif d89.collidepoint(pygame.mouse.get_pos()):
                D89()
            elif e71.collidepoint(pygame.mouse.get_pos()):
                E71()
            elif e94.collidepoint(pygame.mouse.get_pos()):
                E94()
            elif e47.collidepoint(pygame.mouse.get_pos()):
                E47()
            elif e85.collidepoint(pygame.mouse.get_pos()):
                E85()
            elif f57.collidepoint(pygame.mouse.get_pos()):
                F57()
            elif f64.collidepoint(pygame.mouse.get_pos()):
                F64()
            elif f97.collidepoint(pygame.mouse.get_pos()):
                F97()
            elif g58.collidepoint(pygame.mouse.get_pos()):
                G58()
            elif g39.collidepoint(pygame.mouse.get_pos()):
                G39()
            elif g12.collidepoint(pygame.mouse.get_pos()):
                G12()
            elif h22.collidepoint(pygame.mouse.get_pos()):
                H22()
            elif h82.collidepoint(pygame.mouse.get_pos()):
                H82()
            elif h02.collidepoint(pygame.mouse.get_pos()):
                H02()
