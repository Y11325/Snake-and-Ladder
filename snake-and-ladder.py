#! python3 
# Snake and Ladder
import pygame as pyg
from pygame.locals import *
import random
import time
import math

# variables
size = width,height = (900,750)
buttoncollide = False
scene1 = 1
scene2 = 2
scene3 = 3
currentscene = 1

# pygame setup
pyg.init()
pyg.display.set_caption("Snake and Ladder game - Amy Yang")
display_surface = pyg.display.set_mode((width, height)) 
w = pyg.display.set_mode(size)
clock = pyg.time.Clock()
running = True

def scene1stuff():
    w.fill("palegreen")
    font = pyg.font.SysFont('impact', 80)
    text = font.render('Snake and Ladder', True, "royalblue")
    textRect = text.get_rect()
    textRect.center = (width/2, height/6)
    font1 = pyg.font.SysFont('opensans', 60)
    text1 = font1.render('Best game ever', True, "darkorchid1")
    textRect1 = text1.get_rect()
    textRect1.center = (width/2, height/3.3)
    font2 = pyg.font.SysFont('calibribold', 42)
    text2 = font2.render('By: Amy Yang', True, "mediumpurple1")
    textRect2 = text2.get_rect()
    textRect2.center = (width/1.25, height/1.1)
    w.blit(text,textRect)
    w.blit(text1,textRect1)
    w.blit(text2,textRect2)
    background1 = pyg.image.load("seniorgame.png")
    newbg1 = pyg.transform.scale(background1, (int(width/1.6), int(height/1.8)))
    bg1 = background1.get_rect()
    bg1.center = width/2.5, height/1.38
    w.blit(newbg1,bg1)

def scene2stuff():
    w.fill(0)
    font = pyg.font.SysFont('opensans', 80)
    text = font.render('CHOOSE # of players', False, "royalblue")
    textRect = text.get_rect()
    textRect.center = (width/2, height/5)
    w.blit(text,textRect)

def scene3stuff():
    w.fill("skyblue")
    map = pyg.image.load("snake-and-ladder.png")
    newmap = pyg.transform.scale(map, (int(width/1.4), int(height/1.2)))
    maplocation = map.get_rect()
    maplocation.center = width/2.5, height/2.1
    w.blit(newmap,maplocation)
    gd = pyg.image.load("gamedie.png")
    newgd = pyg.transform.scale(gd, (int(width/5), int(height/4.1)))
    gdlocation = gd.get_rect()
    gdlocation.center = width/1.08, height/2
    w.blit(newgd,gdlocation)

def playbutton():
    font = pyg.font.SysFont('roboto',65,bold=True)
    surf = font.render('PLAY', True, 'white')
    global button
    button = pyg.Rect(width/1.4,height/1.7,150,150)
    a,b = pyg.mouse.get_pos()
    if button.x <= a <= button.x + 150 and button.y <= b <= button.y +150:
        pyg.draw.rect(w,(255,182,193),button,border_radius=12)
    else:
        pyg.draw.rect(w,(230,100,250),button,border_radius=12)
    w.blit(surf,(button.x+15, button.y+50))

def twoPB():
    font = pyg.font.SysFont('roboto',65,bold=True)
    surf = font.render('2 players', True, 'white')
    global twopb
    twopb = pyg.Rect(width/2.5,height/3,210,60)
    a,b = pyg.mouse.get_pos()
    if twopb.x <= a <= twopb.x + 210 and twopb.y <= b <= twopb.y +60:
        pyg.draw.rect(w,(255,200,130),twopb,border_radius=10)
    else:
        pyg.draw.rect(w,(135,206,250),twopb,border_radius=10)
    w.blit(surf,(twopb.x+5, twopb.y+5))
    
def threePB():
    font = pyg.font.SysFont('roboto',65,bold=True)
    surf = font.render('3 players', True, 'white')
    global threepb
    threepb = pyg.Rect(width/2.5,height/2,210,60)
    a,b = pyg.mouse.get_pos()
    if threepb.x <= a <= threepb.x + 210 and threepb.y <= b <= threepb.y +60:
        pyg.draw.rect(w,(189,252,201),threepb,border_radius=10)
    else:
        pyg.draw.rect(w,(171,130,255),threepb,border_radius=10)
    w.blit(surf,(threepb.x+5, threepb.y+5))

def fourPB():
    font = pyg.font.SysFont('roboto',65,bold=True)
    surf = font.render('4 players', True, 'white')
    global fourpb
    fourpb = pyg.Rect(width/2.5,height/1.5 ,210,60)
    a,b = pyg.mouse.get_pos()
    if fourpb.x <= a <= fourpb.x + 210 and fourpb.y <= b <= fourpb.y +60:
        pyg.draw.rect(w,(255,165,79),fourpb,border_radius=10)
    else:
        pyg.draw.rect(w,(230,100,250),fourpb,border_radius=10)
    w.blit(surf,(fourpb.x+5, fourpb.y+5))

def characters():
    global players
    if players == 2:
        capybara()
        cat()
    elif players == 3:
        capybara()
        cat()
        dog()
    elif players == 4:
        capybara()
        cat()
        dog()
        duck()

def capybara():
    cb = pyg.image.load("capybara.png")
    cblocation = cb.get_rect()
    cblocation.center = width/18, height/1.1
    w.blit(cb,cblocation)

def cat():
    cat = pyg.image.load("cat.png")
    catlocation = cat.get_rect()
    catlocation.center = width/6, height/1.1
    w.blit(cat,catlocation)

def dog():
    dog = pyg.image.load("dog.png")
    doglocation = dog.get_rect()
    doglocation.center = width/3.5, height/1.1
    w.blit(dog,doglocation)

def duck():
    duck = pyg.image.load("duck.png")
    ducklocation = duck.get_rect()
    ducklocation.center = width/2.5, height/1.1
    w.blit(duck,ducklocation)

def gamedie():
    font = pyg.font.SysFont('impact',65)
    surf = font.render('ROLL', True, 'white')
    global roll
    roll = pyg.Rect(width/1.3,height/1.5 ,140,100)
    a,b = pyg.mouse.get_pos()
    if roll.x <= a <= roll.x + 140 and roll.y <= b <= roll.y +100:
        pyg.draw.rect(w,(150,150,150),roll,border_radius=10)
    else:
        pyg.draw.rect(w,(100,100,100),roll,border_radius=10)
    w.blit(surf,(roll.x+5, roll.y+5))

def rollgd():
    global players
    if players == 2:
        player1 = random.randint(1,6)
        player2 = random.randint(1,6)
        print(player1,player2)
    elif players == 3:
        player1 = random.randint(1,6)
        player2 = random.randint(1,6)
        player3 = random.randint(1,6)
        print(player1,player2,player3)
    elif players == 4:
        player1 = random.randint(1,6)
        player2 = random.randint(1,6)
        player3 = random.randint(1,6)
        player4 = random.randint(1,6)
        print(player1,player2,player3,player4)

# main program
while running:
    if currentscene == scene1:
        scene1stuff()
        playbutton()
    elif currentscene == scene2:
        scene2stuff()
        twoPB()
        threePB()
        fourPB()
    elif currentscene == scene3:
        scene3stuff()
        characters()
        gamedie()

    if currentscene == scene1:
        for event in pyg.event.get():
            if event.type == pyg.MOUSEBUTTONDOWN:
                if button.collidepoint(event.pos):
                    currentscene += 1
            elif event.type == pyg.QUIT:
                running = False
    elif currentscene == scene2:
        for event in pyg.event.get():
            if event.type == pyg.MOUSEBUTTONDOWN:
                if twopb.collidepoint(event.pos):
                    currentscene += 1
                    players = 2
                elif threepb.collidepoint(event.pos):
                    currentscene += 1
                    players = 3
                elif fourpb.collidepoint(event.pos):
                    currentscene += 1
                    players = 4
            elif event.type == pyg.QUIT:
                running = False
    elif currentscene == scene3:
        for event in pyg.event.get():
            if event.type == pyg.MOUSEBUTTONDOWN:
                if roll.collidepoint(event.pos):
                    rollgd()
            elif event.type == pyg.QUIT:
                running = False

    pyg.display.update()
    pyg.display.flip()

    clock.tick(60)  

pyg.quit()