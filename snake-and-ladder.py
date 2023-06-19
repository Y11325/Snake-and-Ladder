#! python3 
# Snake and Ladder
import pygame as pyg
import sys, os
from pygame.locals import *
import random
import math

# variables
size = width,height = (800,650)

# images
map = pyg.image.load("snake-and-ladder.png")
newmap = pyg.transform.scale(map, (int(width/1.6), int(height/1.4)))
maplocation = map.get_rect()
maplocation.center = width/2, height/1.4


# pygame setup
pyg.init()
w = pyg.display.set_mode(size)
clock = pyg.time.Clock()
running = True

# decoration
w.fill("purple")
pyg.display.set_caption("Snake and Ladder game - Amy Yang")

# main program
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window

    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    w.fill("SkyBlue")

    # RENDER YOUR GAME HERE
    w.blit(newmap, maplocation)
    pyg.display.update()
    # flip() the display to put your work on screen
    pyg.display.flip()

    clock.tick(60)  # limits FPS to 60

pyg.quit()