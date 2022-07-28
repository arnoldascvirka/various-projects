# Importing libraries
from cgitb import text
from email import message
from mailbox import linesep
import pygame
import pygame.font
from pygame.locals import *
import random

# Importing Modules
from text import message_display_xy, message_display_station_text

# Creates random number in range for the station population
num100_200 = random.randint(100, 200)
num100_500 = random.randint(100, 500)
num500_1k = random.randint(500, 1000)
num1k_2k = random.randint(1000, 2000)
num2k_4k = random.randint(2000, 4000)
num4k_6k = random.randint(4000, 6000)
num6k_8k = random.randint(6000, 8000)
num8k_10k = random.randint(8000, 10000)
num10k_15k = random.randint(10000, 15000)

# Prints Territory on screen if their station is called.
# if A44() or A55() or B11() or C11() or C91() or C38() is True:
#     message_display_territory("Teritory: Strider")

# if (
#     A77()
#     or A99()
#     or B78()
#     or B86()
#     or C25()
#     or D67()
#     or D89()
#     or E47()
#     or E85() is True
# ):
#     message_display_territory("Teritory: Garuda")

# if E94() or F64() or F97() or G39() or G12() or H82() or H02() is True:
#     message_display_territory("Territory: Deltan")

# if D19() or D34() is True:
#     message_display_territory("Territory: 9 Stripes")

# if E71() or F57() or G58() or H22() is True:
#     message_display_territory("Territory: Red Moon")


def A44():
    # A44"
    message_display_xy("Welcome to Curator Station", 880, 260)
    message_display_xy(f"Population: {num1k_2k}", 880, 300)


def A55():
    # A55
    message_display_xy("Welcome to Curator Station", 880, 260)
    message_display_xy(f"Population: {num2k_4k}", 880, 300)


def A77():
    # A77
    message_display_xy("Welcome to Curator Station", 880, 260)
    message_display_xy(f"Population: {num4k_6k}", 880, 300)


def A99():
    # A99
    message_display_xy("Welcome to Curator Station", 880, 260)
    message_display_xy(f"Population: {num4k_6k}", 880, 300)


def B11():
    # B11
    message_display_xy("Welcome to Curator Station", 880, 260)
    message_display_xy(f"Population: {num1k_2k}", 880, 300)


def B78():
    # B78
    message_display_xy("Welcome to Curator Station", 880, 260)
    message_display_xy(f"Population: {num6k_8k}", 880, 300)


def B86():
    # B86
    message_display_xy("Welcome to Curator Station", 880, 260)
    message_display_xy(f"Population: {num4k_6k}", 880, 300)


def C11():
    # C11
    message_display_xy("Welcome to Curator Station", 880, 260)
    message_display_xy(f"Population: {num2k_4k}", 880, 300)


def C91():
    # C91
    message_display_xy("Welcome to Curator Station", 880, 260)
    message_display_xy(f"Population: {num6k_8k}", 880, 300)


def C38():
    # C38
    message_display_xy("Welcome to Curator Station", 880, 260)
    message_display_xy(f"Population: {num2k_4k}", 880, 300)


def C25():
    # C25
    message_display_xy("Welcome to Curator Station", 880, 260)
    message_display_xy(f"Population: {num4k_6k}", 880, 300)


def D19():
    # D19
    message_display_xy("Welcome to Curator Station", 880, 260)
    message_display_xy(f"Population: {num1k_2k}", 880, 300)


def D34():
    # D34
    message_display_xy("Welcome to Curator Station", 880, 260)
    message_display_xy(f"Population: {num2k_4k}", 880, 300)


def D67():
    # D67
    message_display_xy("Welcome to Curator Station", 880, 260)
    message_display_xy(f"Population: {num10k_15k}", 880, 300)


def D89():
    # D89
    message_display_xy("Welcome to Curator Station", 880, 260)
    message_display_xy(f"Population: {num1k_2k}", 880, 300)


def E71():
    # E71
    message_display_xy("Welcome to Curator Station", 880, 260)
    message_display_xy(f"Population: {num1k_2k}", 880, 300)


def E94():
    # E94
    message_display_xy("Welcome to Curator Station", 880, 260)
    message_display_xy(f"Population: {num2k_4k}", 880, 300)


def E47():
    # E47
    message_display_xy("Welcome to Curator Station", 880, 260)
    message_display_xy(f"Population: {num10k_15k}", 880, 300)


def E85():
    # E85
    message_display_xy("Welcome to Curator Station", 880, 260)
    message_display_xy(f"Population: {num4k_6k}", 880, 300)


def F57():
    # F57
    message_display_xy("Welcome to Curator Station", 880, 260)
    message_display_xy(f"Population: {num500_1k}", 880, 300)


def F64():
    # F64
    message_display_xy("Welcome to Curator Station", 880, 260)
    message_display_xy(f"Population: {num4k_6k}", 880, 300)


def F97():
    # F97
    message_display_xy("Welcome to Curator Station", 880, 260)
    message_display_xy(f"Population: {num4k_6k}", 880, 300)


def G58():
    # G58
    message_display_xy("Welcome to Curator Station", 880, 260)
    message_display_xy(f"Population: {num100_500}", 880, 300)


def G39():
    # G39
    message_display_xy("Welcome to Curator Station", 880, 260)
    message_display_xy(f"Population: {num2k_4k}", 880, 300)


def G12():
    # G12
    message_display_xy("Welcome to Curator Station", 880, 260)
    message_display_xy(f"Population: {num1k_2k}", 880, 300)


def H22():
    # H22
    message_display_xy("Welcome to Curator Station", 880, 260)
    message_display_xy(f"Population: {num100_200}", 880, 300)


def H82():
    # H82
    message_display_xy("Welcome to Curator Station", 880, 260)
    message_display_xy(f"Population: {num8k_10k}", 880, 300)


def H02():
    # H02
    message_display_xy("Welcome to Curator Station", 880, 260)
    message_display_xy(f"Population: {num6k_8k}", 880, 300)


0
