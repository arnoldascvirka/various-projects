# Importing libraries
import pygame
import pygame.font
from pygame.locals import *

# Importing Modules
from stationsTime import *
from text import *

# Initialize font
pygame.font.init()
# Gets mouse position every frame and displays the Station information on hover.
def hover():
    for r in rects:
        if r.collidepoint(pygame.mouse.get_pos()):
            clicked = 1
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
        if event.type == pygame.MOUSEBUTTONUP:
            if a44.collidepoint(pygame.mouse.get_pos()):
                curator.print_station()
                curator.print_population()
                curator.print_zone()
            elif a55.collidepoint(pygame.mouse.get_pos()):
                helios.print_station()
            elif a77.collidepoint(pygame.mouse.get_pos()):
                ark.print_station()
            elif a99.collidepoint(pygame.mouse.get_pos()):
                origin.print_station()
            elif b11.collidepoint(pygame.mouse.get_pos()):
                spire.print_station()
            elif b78.collidepoint(pygame.mouse.get_pos()):
                glory.print_station()
            elif b86.collidepoint(pygame.mouse.get_pos()):
                ether.print_station()
            elif c11.collidepoint(pygame.mouse.get_pos()):
                felicity.print_station()
            elif c91.collidepoint(pygame.mouse.get_pos()):
                atlas.print_station()
            elif c38.collidepoint(pygame.mouse.get_pos()):
                cendre.print_station()
            elif c25.collidepoint(pygame.mouse.get_pos()):
                astreaus.print_station()
            elif d19.collidepoint(pygame.mouse.get_pos()):
                dream.print_station()
            elif d34.collidepoint(pygame.mouse.get_pos()):
                vestige.print_station()
            elif d67.collidepoint(pygame.mouse.get_pos()):
                radiance.print_station()
            elif d89.collidepoint(pygame.mouse.get_pos()):
                arcadis.print_station()
            elif e71.collidepoint(pygame.mouse.get_pos()):
                legacy.print_station()
            elif e94.collidepoint(pygame.mouse.get_pos()):
                orbital.print_station()
            elif e47.collidepoint(pygame.mouse.get_pos()):
                serenity.print_station()
            elif e85.collidepoint(pygame.mouse.get_pos()):
                atmos.print_station()
            elif f57.collidepoint(pygame.mouse.get_pos()):
                escorte.print_station()
            elif f64.collidepoint(pygame.mouse.get_pos()):
                azura.print_station()
            elif f97.collidepoint(pygame.mouse.get_pos()):
                voyage.print_station()
            elif g58.collidepoint(pygame.mouse.get_pos()):
                apollon.print_station()
            elif g39.collidepoint(pygame.mouse.get_pos()):
                rogue.print_station()
            elif g12.collidepoint(pygame.mouse.get_pos()):
                chronos.print_station()
            elif h22.collidepoint(pygame.mouse.get_pos()):
                valhalla.print_station()
            elif h82.collidepoint(pygame.mouse.get_pos()):
                prism.print_station()
            elif h02.collidepoint(pygame.mouse.get_pos()):
                settler.print_station()
