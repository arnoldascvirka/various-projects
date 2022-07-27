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
    if a55.collidepoint(pygame.mouse.get_pos()):
        message_display("Helios Station")
    if a77.collidepoint(pygame.mouse.get_pos()):
        message_display("Ark Station")
    if a99.collidepoint(pygame.mouse.get_pos()):
        message_display("Origin Station")
    if b11.collidepoint(pygame.mouse.get_pos()):
        message_display("Spire Terminal")
    if b78.collidepoint(pygame.mouse.get_pos()):
        message_display("Glory")
    if b86.collidepoint(pygame.mouse.get_pos()):
        message_display("Ether Station")
    if c11.collidepoint(pygame.mouse.get_pos()):
        message_display("Felicity Base")
    if c91.collidepoint(pygame.mouse.get_pos()):
        message_display("Atlas")
    if c38.collidepoint(pygame.mouse.get_pos()):
        message_display("Cendre Colony")
    if c25.collidepoint(pygame.mouse.get_pos()):
        message_display("Base Astraeus")
    if d19.collidepoint(pygame.mouse.get_pos()):
        message_display("Dream Station")
    if d34.collidepoint(pygame.mouse.get_pos()):
        message_display("Vestige Station")
    if d67.collidepoint(pygame.mouse.get_pos()):
        message_display("Radiance")
    if d89.collidepoint(pygame.mouse.get_pos()):
        message_display("Arcadis terminal")
    if e71.collidepoint(pygame.mouse.get_pos()):
        message_display("Legacy Base")
    if e94.collidepoint(pygame.mouse.get_pos()):
        message_display("Orbital resupply")
    if e47.collidepoint(pygame.mouse.get_pos()):
        message_display("Serenity")
    if e85.collidepoint(pygame.mouse.get_pos()):
        message_display("Atmos Station")
    if f57.collidepoint(pygame.mouse.get_pos()):
        message_display("Escorte")
    if f64.collidepoint(pygame.mouse.get_pos()):
        message_display("Azura Station")
    if f97.collidepoint(pygame.mouse.get_pos()):
        message_display("Voyage Station")
    if g58.collidepoint(pygame.mouse.get_pos()):
        message_display("Apollon")
    if g39.collidepoint(pygame.mouse.get_pos()):
        message_display("Rogue Colony")
    if g12.collidepoint(pygame.mouse.get_pos()):
        message_display("Terminus Chronos")
    if h22.collidepoint(pygame.mouse.get_pos()):
        message_display("Terminal Valhalla")
    if h82.collidepoint(pygame.mouse.get_pos()):
        message_display("Prism")
    if h02.collidepoint(pygame.mouse.get_pos()):
        message_display("Settler Colony")


def click():
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if a44.collidepoint(pygame.mouse.get_pos()):
                A44()
            if a55.collidepoint(pygame.mouse.get_pos()):
                A55()
            if a77.collidepoint(pygame.mouse.get_pos()):
                A77()
            if a99.collidepoint(pygame.mouse.get_pos()):
                A99()
            if b11.collidepoint(pygame.mouse.get_pos()):
                B11()
            if b78.collidepoint(pygame.mouse.get_pos()):
                B78()
            if b86.collidepoint(pygame.mouse.get_pos()):
                B86()
            if c11.collidepoint(pygame.mouse.get_pos()):
                C11()
            if c91.collidepoint(pygame.mouse.get_pos()):
                C91()
            if c38.collidepoint(pygame.mouse.get_pos()):
                C38()
            if c25.collidepoint(pygame.mouse.get_pos()):
                C25()
            if d19.collidepoint(pygame.mouse.get_pos()):
                D19()
            if d34.collidepoint(pygame.mouse.get_pos()):
                D34()
            if d67.collidepoint(pygame.mouse.get_pos()):
                D67()
            if d89.collidepoint(pygame.mouse.get_pos()):
                D89()
            if e71.collidepoint(pygame.mouse.get_pos()):
                E71()
            if e94.collidepoint(pygame.mouse.get_pos()):
                E94()
            if e47.collidepoint(pygame.mouse.get_pos()):
                E47()
            if e85.collidepoint(pygame.mouse.get_pos()):
                E85()
            if f57.collidepoint(pygame.mouse.get_pos()):
                F57()
            if f64.collidepoint(pygame.mouse.get_pos()):
                F64()
            if f97.collidepoint(pygame.mouse.get_pos()):
                F97()
            if g58.collidepoint(pygame.mouse.get_pos()):
                G58()
            if g39.collidepoint(pygame.mouse.get_pos()):
                G39()
            if g12.collidepoint(pygame.mouse.get_pos()):
                G12()
            if h22.collidepoint(pygame.mouse.get_pos()):
                H22()
            if h82.collidepoint(pygame.mouse.get_pos()):
                H82()
            if h02.collidepoint(pygame.mouse.get_pos()):
                H02()
