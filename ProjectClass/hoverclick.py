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


def call_station(station):
    station.print_station()
    station.print_population()
    station.print_zone()


def click():
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            if a44.collidepoint(pygame.mouse.get_pos()):
                call_station(curator)
            elif a55.collidepoint(pygame.mouse.get_pos()):
                call_station(helios)
            elif a77.collidepoint(pygame.mouse.get_pos()):
                call_station(ark)
            elif a99.collidepoint(pygame.mouse.get_pos()):
                call_station(origin)
            elif b11.collidepoint(pygame.mouse.get_pos()):
                call_station(spire)
            elif b78.collidepoint(pygame.mouse.get_pos()):
                call_station(glory)
            elif b86.collidepoint(pygame.mouse.get_pos()):
                call_station(ether)
            elif c11.collidepoint(pygame.mouse.get_pos()):
                call_station(felicity)
            elif c91.collidepoint(pygame.mouse.get_pos()):
                call_station(atlas)
            elif c38.collidepoint(pygame.mouse.get_pos()):
                call_station(cendre)
            elif c25.collidepoint(pygame.mouse.get_pos()):
                call_station(astreaus)
            elif d19.collidepoint(pygame.mouse.get_pos()):
                call_station(dream)
            elif d34.collidepoint(pygame.mouse.get_pos()):
                call_station(vestige)
            elif d67.collidepoint(pygame.mouse.get_pos()):
                call_station(radiance)
            elif d89.collidepoint(pygame.mouse.get_pos()):
                call_station(arcadis)
            elif e71.collidepoint(pygame.mouse.get_pos()):
                call_station(legacy)
            elif e94.collidepoint(pygame.mouse.get_pos()):
                call_station(orbital)
            elif e47.collidepoint(pygame.mouse.get_pos()):
                call_station(serenity)
            elif e85.collidepoint(pygame.mouse.get_pos()):
                call_station(atmos)
            elif f57.collidepoint(pygame.mouse.get_pos()):
                call_station(escorte)
            elif f64.collidepoint(pygame.mouse.get_pos()):
                call_station(azura)
            elif f97.collidepoint(pygame.mouse.get_pos()):
                call_station(voyage)
            elif g58.collidepoint(pygame.mouse.get_pos()):
                call_station(apollon)
            elif g39.collidepoint(pygame.mouse.get_pos()):
                call_station(rogue)
            elif g12.collidepoint(pygame.mouse.get_pos()):
                call_station(chronos)
            elif h22.collidepoint(pygame.mouse.get_pos()):
                call_station(valhalla)
            elif h82.collidepoint(pygame.mouse.get_pos()):
                call_station(prism)
            elif h02.collidepoint(pygame.mouse.get_pos()):
                call_station(settler)
