import imp
from pickle import TRUE
from random import random
import pygame
import time
import random
pygame.init()
d_width,d_height=800,600
c_width= 80
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
gamedisplay=pygame.display.set_mode((d_width,d_height))
pygame.display.set_caption('first game in python')
clock=pygame.time.Clock()
carImg=pygame.image.load('XX.png')
carImg=pygame.transform.scale(pygame.image.load('XX.png'),(80,150))
def crash():
    message_display('You Crashed')
def message_display(text):
    largeText=pygame.font.Font('freesansbold.ttf',100)
    Textsurf,TextRec=text_objects(text,largeText)
    TextRec.center=(d_width/2,d_height/2)
    gamedisplay.blit(Textsurf,TextRec)
    pygame.display.update()
    time.sleep(2)
    game_loop()
def text_objects(text,font):
    textSurface=font.render(text,True,black)
    return textSurface, textSurface.get_rect()
def car(x,y):
    gamedisplay.blit(carImg,(x,y))
def things(thingx,thingy,thingw,thingh,color):
    pygame.draw.rect(gamedisplay,color,[thingx,thingy,thingw,thingh])

def game_loop():
    x=d_width*0.46
    y=d_height*0.75
    thing_startx=random.randrange(0,d_width)
    thing_starty=-500
    thing_speed=10

    thing_height,thing_width=(100,100)
    x_change=0
    gameExit=False
    while not gameExit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_change=-5
                if event.key==pygame.K_RIGHT:
                    x_change=5
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    x_change=0
        x+=x_change

        gamedisplay.fill(white)
        things(thing_startx,thing_starty,thing_width,thing_height,black)
        thing_starty+=thing_speed
        car(x,y)
        if x>d_width-c_width or x<0:
            crash()
        if thing_starty > d_height:
            thing_starty=-thing_height
            thing_startx=random.randrange(0,d_width-100)
        if thing_starty+thing_height>y:
            if thing_startx+thing_width<x:
                crash()
        pygame.display.update()
        clock.tick(60)
game_loop()
pygame.quit()
quit()