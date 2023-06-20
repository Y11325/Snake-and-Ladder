#! python3 
# Snake and Ladder
import pygame as pyg
import sys, os
from pygame.locals import *
import random
import math

# variables
size = width,height = (800,650)

# pygame setup
pyg.init()
pyg.display.set_caption("Snake and Ladder game - Amy Yang")
w = pyg.display.set_mode(size)
clock = pyg.time.Clock()
running = True

# images
background1 = pyg.image.load("ladder.png")

map = pyg.image.load("snake-and-ladder.png")
newmap = pyg.transform.scale(map, (int(width/1.6), int(height/1.4)))
maplocation = map.get_rect()
maplocation.center = width/2, height/1.4

playbutton = pyg.image.load("playbutton.png")
# texts
display_surface = pyg.display.set_mode((width, height)) 
font = pyg.font.SysFont('georgia', 55)
text = font.render('Snake and Ladder', True, "royalblue")
textRect = text.get_rect()
textRect.center = (width/1.5, height/3)
font2 = pyg.font.SysFont('calibri', 36)
text2 = font2.render('By: Amy Yang', True, "mediumslateblue")
textRect2 = text.get_rect()
textRect2.center = (width/1.2, height/2)

# main program
while running:
    # background color
    w.fill("palegreen")
    # draw the screen elements
    w.blit(background1, (0,0))
    w.blit(text,textRect)
    w.blit(text2,textRect2)
    # update the screen
    pyg.display.flip()
    # loop through the events
    for event in pyg.event.get():
        if event.type == pyg.MOUSEBUTTONDOWN:
            if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
                print("LOL")
                w.fill("SkyBlue")
                w.blit(newmap, maplocation)
        # check if the event is the X button 
        if event.type == pyg.QUIT:
            running = False

    mouse = pyg.mouse.get_pos()
    if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
        pyg.draw.rect(w,(170,170,170),[width/2,height/2,140,40])
          
    else:
        pyg.draw.rect(w,(100,100,100),[width/2,height/2,140,40])
      
    # superimposing the text onto our button
    w.blit(playbutton , (width/2+50,height/2))
    pyg.display.update()
    pyg.display.flip()

    clock.tick(60)  

pyg.quit()