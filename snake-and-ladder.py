#! python3 
# Snake and Ladder
import pygame as pyg
from pygame.locals import *
import random
import math

# variables
size = width,height = (800,650)
buttoncollide = False
scene1 = 1
scene2 = 2
currentscene = 1

# pygame setup
pyg.init()
pyg.display.set_caption("Snake and Ladder game - Amy Yang")
display_surface = pyg.display.set_mode((width, height)) 
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

def scene1stuff():
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
    textRect2 = text2.get_rect()
    textRect2.center = (width/1.25, height/1.05)
    w.blit(text,textRect)
    w.blit(text1,textRect1)
    w.blit(text2,textRect2)

# playbutton
def playbutton():
    font = pyg.font.SysFont('Georgia',40,bold=True)
    surf = font.render('PLAY', True, 'white')
    global button
    button = pyg.Rect(width/1.4,height/1.7,130,60)
    a,b = pyg.mouse.get_pos()
    if button.x <= a <= button.x + 110 and button.y <= b <= button.y +60:
        pyg.draw.rect(w,(180,180,180),button)
    else:
        pyg.draw.rect(w, (110,110,110),button)
    w.blit(surf,(button.x+5, button.y+5))

# main program
while running:
    if currentscene == scene1:
        w.fill("palegreen")
        w.blit(newbg1,bg1)
        scene1stuff()
        playbutton()
    elif currentscene == scene2:
        w.fill("skyblue")
        w.blit(newmap,maplocation)

    for event in pyg.event.get():
        if event.type == pyg.MOUSEBUTTONDOWN:
                if button.collidepoint(event.pos):
                    if currentscene == scene1:
                        currentscene += 1
                    else:
                        currentscene == scene1
        if event.type == pyg.QUIT:
            running = False


    pyg.display.update()
    pyg.display.flip()

    clock.tick(60)  

pyg.quit()