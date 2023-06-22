#! python3 
# Snake and Ladder
import pygame as pyg
import sys, os
from pygame.locals import *
import random
import math

# variables
size = width,height = (800,650)
buttoncollide = False
# pygame setup
pyg.init()
pyg.display.set_caption("Snake and Ladder game - Amy Yang")
w = pyg.display.set_mode(size)
clock = pyg.time.Clock()
running = True

# images
background1 = pyg.image.load("seniorgame.png")
newbg1 = pyg.transform.scale(background1, (int(width/1.6), int(height/1.8)))
bg1 = background1.get_rect()
bg1.center = width/2.5, height/1.22

map = pyg.image.load("snake-and-ladder.png")
newmap = pyg.transform.scale(map, (int(width/1.6), int(height/1.4)))
maplocation = map.get_rect()
maplocation.center = width/2, height/1.4

font = pyg.font.SysFont('Georgia',40,bold=True)
surf = font.render('PLAY', True, 'white')
button = pyg.Rect(200,200,130,60)

playbutton = pyg.image.load("playbutton.png")
# texts
display_surface = pyg.display.set_mode((width, height)) 
font = pyg.font.SysFont('georgia', 80)
text = font.render('Snake and Ladder', True, "royalblue")
textRect = text.get_rect()
textRect.center = (width/2, height/7)

font1 = pyg.font.SysFont('calibri', 60)
text1 = font1.render('Best game ever', True, "darkorchid1")
textRect1 = text1.get_rect()
textRect1.center = (width/2, height/3.3)

font2 = pyg.font.SysFont('calibri', 32)
text2 = font2.render('By: Amy Yang', True, "mediumpurple1")
textRect2 = text.get_rect()
textRect2.center = (width/0.9, height/1)

# main program
while running:
    # background color
    w.fill("palegreen")
    # draw the screen elements
    w.blit(newbg1, bg1)
    w.blit(text,textRect)
    w.blit(text1,textRect1)
    w.blit(text2,textRect2)
    # update the screen
    pyg.display.flip()
    # loop through the events
    for event in pyg.event.get():
        if event.type == pyg.MOUSEBUTTONDOWN:
                if button.collidepoint(event.pos):
                    buttoncollide = True
                    
        # check if the event is the X button 
        if event.type == pyg.QUIT:
            running = False

    if buttoncollide == True:
        w.fill("paleturquoise1")
        w.blit(newmap, maplocation)
    a,b = pyg.mouse.get_pos()
    if button.x <= a <= button.x + 110 and button.y <= b <= button.y +60:
        pyg.draw.rect(w,(180,180,180),button )
    else:
        pyg.draw.rect(w, (110,110,110),button)
    w.blit(surf,(button.x +5, button.y+5))
    mouse = pyg.mouse.get_pos()
    w.blit(playbutton , (width/1.8,height/2,140,40))
 
    pyg.display.update()
    pyg.display.flip()

    clock.tick(60)  

pyg.quit()