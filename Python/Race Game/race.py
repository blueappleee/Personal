#once done edit car to follow mouse

import pygame
import sys
import time
import random
pygame.init()

display_width = 800
display_height = 600
car_width = 40
car_height = 80

gamedisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Race')
clock = pygame.time.Clock()

f1car = pygame.image.load('car3.png')

explode = pygame.image.load('explode.png')

border = pygame.image.load('line.png')




black = (0,0,0)
white = (255,255,255)

def borderline(x,y):
    gamedisplay.blit(border,(x,y))

def car(x,y):
    gamedisplay.blit(f1car,(x,y))

def explosion(x,y):
    gamedisplay.blit(explode,(x-15,y))

def explosion2(x,y):
    gamedisplay.blit(explode,((x-40),y))
    

def text_objects(text,font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
    

def message_display(text):
    Ltext = pygame.font.Font('freesansbold.ttf',100)
    textsurf, textrect = text_objects(text, Ltext)
    textrect.center = (display_width*0.48),(display_height*0.48)
    gamedisplay.blit(textsurf, textrect)
    pygame.display.update()

    

def score(passed):
    score = pygame.font.Font('freesansbold.ttf',50)
    text = score.render(('Your Score:'+str(passed)),True,black)
    gamedisplay.blit(text,(display_width*0.31,display_height*0.53))
    pygame.display.update()

    time.sleep(2)

    game_loop() 
    

def crash():
    message_display('You Crashed')


def objects(object_x,object_y):
    car(object_x,object_y)

def objectspassed(passed):
    stext = pygame.font.Font('freesansbold.ttf',25)
    text = stext.render(str(passed),True,black)
    gamedisplay.blit(text,(16,0))
    
    


def game_loop():

    difficult = 0
    passed = 0
    x_change = 0
    z = 2 + difficult
    xborder1 = 0
    xborder2 = 785
    yborder = 0
    objectchance = 0
    count = 0

    x = (display_width * 0.44)
    y = (display_height * 0.80)

    GameExit = False
    passedfinish = False
    crashed = False
 
    
    while not GameExit:


        while not crashed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and event.key == pygame.K_RIGHT:
                        x_change = 0 
                    elif event.key == pygame.K_LEFT:
                        x_change = -5
                    elif event.key == pygame.K_RIGHT:
                        x_change = 5
                    if event.key == pygame.K_UP and event.key == pygame.K_DOWN:
                        if z > 2 + difficult:
                            z = z - 0.5
                        elif z < 2 + difficult:
                            z = z - 0.5
                        else:
                            z == 2 + difficult
                    elif event.key == pygame.K_DOWN:
                        if z > 2 + diffucult:
                            z = z - 1
                        else:
                            z = 2 + difficult
                    elif event.key == pygame.K_UP:
                        if z < 8 + difficult:
                            z = z + 0.5
                        else:
                            z == 8 + difficult
                    

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0
                    if event.key == pygame.K_UP:
                        if z > 2 + difficult:
                            z = z - 0.1
                        elif z < 2 + difficult:
                            z = z - 0.1
                        else:
                            z == 2 + difficult
                    elif event.key == pygame.K_DOWN:
                        if z < 2 + difficult:
                            z = z + 0.1
                        elif z > 2 + difficult:
                            z = z - 0.1
                        else:
                            z == 2 + difficult
                
                
            x += x_change

            
                
            gamedisplay.fill(white)

            speed = 20*z
            
            if count == 0:
                object_y = 0
                object_x = random.randrange(15,display_width-55)
                objects(object_x,object_y)
                count = count+1
                
            elif object_y > display_height:
                passed = passed+1
                count = 0
                difficult = difficult+5
            else:
                object_y = object_y + speed
                objects(object_x,object_y)
                count = count+1

            if object_y > display_height*0.8-80 and object_y <= display_height*0.8+80 and x >= object_x and x <= object_x+40:
                explosion(x,y)
                crash()
                score((str(passed)))
            elif object_y > display_height*0.8-80 and object_y <= display_height*0.8+80 and x+40 >= object_x and x +40 <= object_x+40:
                explosion2(x,y)
                crash()
                score((str(passed)))
            
            

            borderline(xborder1,yborder)
            borderline(xborder2,yborder)

            objectspassed((str(passed)))
            

            if x < 15:
                explosion(x,y)
                
                crash()
                score((str(passed)))
                
            elif x > 755:
                explosion2(x,y)
                
                crash()
                score((str(passed)))
            else:
                car(x,y)
        
            pygame.display.update()
            clock.tick(60)
            

game_loop()
#edit accel and decel values to fit game better
    

