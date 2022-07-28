# Importing libraries
from pickletools import ArgumentDescriptor
import pygame
import pygame.font
from pygame.locals import *

# Importing modules
from text import Station

pygame.font.init()
black = (0, 0, 0)
font = pygame.font.SysFont(None, 24)
gui_top = font.render("SimpleMetro - Arnoldas Cvirka", True, black)
gui_bottom = font.render("Use right click to navigate.", True, black)
gui_station = font.render("Station: ", True, black)
screen = pygame.display.set_mode((800, 800), 0, 32)

# Defines Station function
def draw_station(x, y, sizeX, sizeY):
    return pygame.draw.rect(screen, (255, 0, 0), (x, y, sizeX, sizeY))


# Define Station locations
a44 = draw_station(70, 90, 40, 40)
a55 = draw_station(295, 80, 40, 40)
a77 = draw_station(525, 80, 40, 40)
a99 = draw_station(700, 80, 40, 40)
b11 = draw_station(415, 155, 40, 40)
b78 = draw_station(525, 155, 40, 40)
b86 = draw_station(620, 155, 40, 40)
c11 = draw_station(230, 250, 40, 40)
c91 = draw_station(320, 250, 40, 40)
c38 = draw_station(500, 250, 40, 40)
c25 = draw_station(670, 200, 40, 40)
d19 = draw_station(60, 320, 40, 40)
d34 = draw_station(240, 320, 40, 40)
d67 = draw_station(505, 295, 60, 30)
d89 = draw_station(750, 285, 40, 40)
e71 = draw_station(320, 380, 40, 40)
e94 = draw_station(395, 360, 40, 40)
e47 = draw_station(505, 385, 60, 30)
e85 = draw_station(620, 380, 40, 40)
f57 = draw_station(250, 450, 60, 60)
f64 = draw_station(395, 455, 40, 40)
f97 = draw_station(525, 455, 40, 40)
g58 = draw_station(150, 550, 60, 60)
g39 = draw_station(395, 520, 40, 40)
g12 = draw_station(635, 570, 40, 40)
h22 = draw_station(60, 650, 60, 60)
h82 = draw_station(525, 680, 40, 40)
h02 = draw_station(695, 635, 40, 40)

# Draw all rectangles in an array
rects = [
    a44,
    a55,
    a77,
    a99,
    b11,
    b78,
    b86,
    c11,
    c91,
    c38,
    c25,
    d19,
    d34,
    d67,
    d89,
    e71,
    e94,
    e47,
    e85,
    f57,
    f64,
    f97,
    g58,
    g39,
    g12,
    h22,
    h82,
    h02,
]

# Define station classes
curator = Station("Curator Station", 1000, 2000, "Strider")
helios = Station("Helios Station", 2000, 4000, "Strider")
ark = Station("Ark Station", 4000, 6000, "Garuda")
origin = Station("Origin Station", 4000, 6000, "Garuda")
spire = Station("Spire Terminal", 1000, 2000, "Strider")
glory = Station("Glory", 6000, 8000, "Garuda")
ether = Station("Ether Station", 4000, 6000, "Garuda")
felicity = Station("Felicity Base", 2000, 4000, "Strider")
atlas = Station("Atlas", 6000, 8000, "Strider")
cendre = Station("Cendre Colony", 2000, 4000, "Strider")
astreaus = Station("Base Astreaus", 4000, 6000, "Garuda")
dream = Station("Dream Station", 1000, 2000, "9 Stripes")
vestige = Station("Vestige Station", 2000, 4000, "9 Stripes")
radiance = Station("Radiance", 10000, 15000, "Garuda")
arcadis = Station("Arcadis Terminal", 1000, 2000, "Garuda")
legacy = Station("Legacy Base", 1000, 2000, "Red Moon")
orbital = Station("Orbital Resupply", 2000, 4000, "Deltan")
serenity = Station("Serenity", 10000, 15000, "Garuda")
atmos = Station("Atmos Station", 4000, 6000, "Garuda")
escorte = Station("Escorte", 500, 1000, "Red Moon")
azura = Station("Azura Station", 4000, 6000, "Deltan")
voyage = Station("Voyage Station", 4000, 6000, "Deltan")
apollon = Station("Apollon", 100, 500, "Red Moon")
rogue = Station("Rogue Colony", 2000, 4000, "Deltan")
chronos = Station("Terminus Chronos", 1000, 2000, "Deltan")
valhalla = Station("Terminal Valhalla", 100, 200, "Red Moon")
prism = Station("Prism", 8000, 10000, "Deltan")
settler = Station("Settler Colony", 6000, 8000, "Deltan")
