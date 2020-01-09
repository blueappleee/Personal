
#cap power at (555)
import pygame
import time
import random
import math



display_width = 800
display_height = 600
ball_diameter = 40
dot_diameter = 15

gamedisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('ballgame')
clock = pygame.time.Clock()

dot = pygame.image.load('dot.png')

ball = pygame.image.load('box.png')

cannon = pygame.image.load('conveyer.png')

cannon_wheel = pygame.image.load('launcher.png')

gravity = 10

white = (255,255,255)

black = (0,0,0)

red = (255,0,0)


def dotpos(dotpositionx,dotpositiony):
    gamedisplay.blit(dot,(dotpositionx,dotpositiony))

def cball(ballpositionx,ballpositiony):
    gamedisplay.blit(ball,(ballpositionx,ballpositiony))

def cannonb(cannonbx,cannonby):
    gamedisplay.blit(cannon,(cannonbx,cannonby))

def cannonw(cannonwx,cannonwy):
    gamedisplay.blit(cannon_wheel,(cannonwx,cannonwy))

def power(z):
    Vi = z/3
    return(Vi)

def Vix(x,y,z):
    theta = angle(x,y)
    Vi = power(z)
    Vx = Vi*math.cos(math.radians(theta))
    return(Vx)

def Viy(x,y,z):
    theta = angle(x,y)
    Vi = power(z)
    Vy = Vi*math.sin(math.radians(theta))
    return(Vy)
     

def balllaunch(x,y,z,distance,initialposx,initialposy):
    gravity = 10
    Vix2 = Vix(x,y,z)
    Viy2 = Viy(x,y,z)
    t = distance/Vix2
    positiony = Viy2*t - 0.5*gravity*t**2
    positionx = Vix2*t
    ballposx = initialposx+positionx
    ballposy = initialposy-positiony
    return(ballposx,ballposy)


def launchrotate(x,y):
    anglel = angle(x,y)
    subtract1 = anglel/3
    if anglel >= 80:
        ylaunch = 570 - subtract1
    elif anglel < 80 and anglel > 65:
        subtract2 = subtract1+3
        ylaunch = 570-subtract2 
    elif anglel < 65 and anglel >= 50:
        subtract2 = subtract1+4
        ylaunch = 570-subtract2
    elif anglel < 50 and anglel >= 25:
        subtract2 = subtract1 + 4
        ylaunch = 570 - subtract2
    elif anglel >= 15 and anglel <= 25:
        subtract2 = subtract1 + 3
        ylaunch = 570 - subtract2
    else:
        subtract2 = subtract1 + 1
        ylaunch = 570 - subtract2
        
    gamedisplay.blit((pygame.transform.rotate(cannon_wheel,anglel)),(120,ylaunch))
    
def angle(x,y): 
    y2 = y-85
    ytrue = 600 - y2 
    if x <= 50:
        xtrue = 1
    else:    
        xtrue = x-50
    ratio = math.atan((ytrue/xtrue))
    theta = math.degrees(ratio)
    return(theta)

def guide(x,y,z):
    ballpositiony = 0
    ballpositionx = 0
    distance = 80
    initialposx = 90
    initialposy = 545
    while ballpositiony < 570 and ballpositionx <= 500 :  #change parameters after testing so it doesnt give ball trajectory so easy
        position = balllaunch(x,y,z,distance,initialposx,initialposy)
        ballpositionx = position[0]
        ballpositiony = position[1]
        dotpositionx = ballpositionx-5
        dotpositiony = ballpositiony+15
        distance = distance+50
        dotpos(dotpositionx,dotpositiony)
    pygame.display.update()

def target(linestartx,linestarty,lineendx,lineendy): 
    pygame.draw.line(gamedisplay, red, (750,600),(750,0),20)
    bottomlinex = lineendx -15
    toplinex = linestartx - 15
    pygame.draw.line(gamedisplay, red, (linestartx,linestarty), (lineendx,lineendy),15)
    pygame.draw.line(gamedisplay, red, (linestartx + 7,linestarty), (toplinex,linestarty),10)
    pygame.draw.line(gamedisplay, red, (lineendx + 7,lineendy), (bottomlinex,lineendy),10) 


def text_objects(text,font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
    

def message_display(text):
    Ltext = pygame.font.Font('freesansbold.ttf',100)
    textsurf, textrect = text_objects(text, Ltext)
    textrect.center = (display_width*0.48),(display_height*0.48)
    gamedisplay.blit(textsurf, textrect)
    pygame.display.update()

def instruction():
    welcome = pygame.font.Font('freesansbold.ttf',40)
    text = welcome.render(('Increase and Decrease Power on far right'),True,black)
    text2 = welcome.render(('Use Mouse to change launch angle'),True,black)
    text3 = welcome.render(('Get the box onto the shelf'),True,black)
     
    gamedisplay.blit(text,(display_width*0.003,display_height*0.3))
    gamedisplay.blit(text2,(display_width*0.08,display_height*0.4))
    gamedisplay.blit(text3,(display_width*0.18,display_height*0.5)) 
     
    
def welcome():
    welcome = pygame.font.Font('freesansbold.ttf',40)
    text = welcome.render(('Welcome to ----'),True,black)
    gamedisplay.blit(text,(display_width*0.30,display_height*0.3))
    

def startmessage():
    startmessage = pygame.font.Font('freesansbold.ttf',40)
    text = startmessage.render(('Press Space to start'),True,black)
    gamedisplay.blit(text,(display_width*0.25,display_height*0.4))
      

def instructions():
    instructions = pygame.font.Font('freesansbold.ttf',40)
    text = instructions.render(('Press i for instructions'),True,black)
    gamedisplay.blit(text,(display_width*0.22,display_height*0.5))
    


def Miss():
    message_display('You Missed')

def score(hit):
    score = pygame.font.Font('freesansbold.ttf',50)
    text = score.render(('Your Score:'+str(hit)),True,black)
    gamedisplay.blit(text,(display_width*0.31,display_height*0.53))
    pygame.display.update()

    time.sleep(2)

    game_loop()


def game_loophit(z,hit): #when it hits the back board hit = hit+1 and then game_loophit(z,hit) eventually add level to conditions
    miss = False
    GameExit = False
    Space = False
    x = 0
    y = 0
    distance = 0
    z = 275
    x2 = 0
    y2 = 0
    initialposx = 94
    initialposy = 545
    ballpositionx = 0
    ballpositiony = 0
    ballend = 668
    ballpos3x = 40
    ballpos3y = 530

    line1 = random.randint(50,500)
    line2 = line1 + random.randint(60,75)
    
    
    linestartx = 725 
    linestarty = line1
    lineendx = 725
    lineendy = line2
    
    while not GameExit:
        while not miss: 
            while  ballpositiony < 570 and ballpositionx < ballend:
                gamedisplay.fill(white)
                
                while not Space:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                        else:
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_SPACE:
                                    
                                    Space = True

                            
                                    
                            pos = pygame.mouse.get_pos()
                            x = pos[0]
                            y = pos[1]
                            guide(x,y,z)
                            
                            
                            print(angle(x,y))
                            if x >= 750 and x <= 800:
                                ytruep = 600 - y
                                if ytruep >= 350:
                                    z = 350
                                else:
                                    z = ytruep
                                power(z)
                                print(z)

                            gamedisplay.fill(white)
                            cannonb(40,570)
                            launchrotate(x,y)
                            cball(40,530) 
                            target(linestartx,linestarty,lineendx,lineendy)


                            pygame.display.update()

                            clock.tick(60)


                    if x2 == x and y2 == y:
                        x2 = x
                        y2 = y
                        guide(x,y,z)
                    else:
                        x2 = x
                        y2 = y
                
                
                distance = distance+4
                
                    
                    
                if Space == True:
                    if ballpos3x < 88:
                        ballpos3x = ballpos3x+3
                        ballpositionx = ballpos3x
                        ballpositiony = ballpos3y
                        cball(ballpositionx,ballpositiony)
                            
                    else:    
                        position = balllaunch(x,y,z,distance,initialposx,initialposy)
                        ballpositionx = position[0]
                        ballpositiony = position[1]
                        cball(ballpositionx,ballpositiony)
                        ballposy2 = ballpositiony+40 
                    
                    
                target(linestartx,linestarty,lineendx,lineendy)
                cannonb(40,570)
                launchrotate(x,y)
                
              
                

                if ballpositionx <= 670 and ballpositionx >= 666:
                    if ballpositiony >= lineendy + 15 or ballpositiony + 40 <= linestarty -15:
                        ballend = 680
                    elif ballpositiony > linestarty and ballpositiony + 40 < lineendy:
                        ballend = 680
                    
                    elif ballpositiony >= lineendy and ballpositiony <= lineendy + 10:
                        ballend = ballend
                    elif ballpositiony + 40 >= lineendy and ballpositiony + 40 <= lineendy + 10:
                        ballend = ballend
                    elif ballpositiony >= linestarty and ballpositiony <= linestarty - 10:
                        ballend = ballend
                    elif ballpositiony + 40 >= linestarty and ballpositiony + 40 <= linestarty + 10:
                        ballend = ballend
                
                if ballpositionx <= 682 and ballpositionx >= 680: ## change ball variable  ### change to a box and make game launching box onto shelf
                    if ballpositiony < lineendy and ballpositiony + 40 > linestarty:
                        time.sleep(0.5)
                        hit = hit+1
                        game_loophit(z,hit)
                    elif ballpositiony > lineendy or ballpositiony + 40 < linestarty:
                        ballend = 700
                 
                 
                

                    
                pygame.display.update()
                clock.tick(144)

            target(linestartx,linestarty,lineendx,lineendy) 
            cball(ballpositionx,ballpositiony)
            cannonb(40,570)
            launchrotate(x,y)

            
            

            Miss()
            score(hit)
            
                                
                            
            pygame.display.update()
            clock.tick(144)  





def game_loop():

    miss = False
    GameExit = False
    Space = False
    x = 0
    hit = 0
    z = 275
    y = 0
    distance = 0
    x2 = 0
    y2 = 0
    initialposx = 94
    initialposy = 545
    ballpositionx = 0
    ballpositiony = 0
    ballend = 668
    ballpos3x = 40
    ballpos3y = 530

    line1 = random.randint(50,500)
    line2 = line1 + random.randint(60,75)
    
    
    linestartx = 725 
    linestarty = line1
    lineendx = 725
    lineendy = line2
    
    while not GameExit:
        while not miss: 
            while  ballpositiony < 570 and ballpositionx <= ballend :
                gamedisplay.fill(white)
                
                while not Space:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                        else:
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_SPACE:
                                    
                                    Space = True

                            
                                    
                            pos = pygame.mouse.get_pos()
                            x = pos[0]
                            y = pos[1]
                            guide(x,y,z)
                            
                            
                            print(angle(x,y))
                            if x >= 750 and x <= 800:
                                ytruep = 600 - y
                                if ytruep >= 350:
                                    z = 350
                                else:
                                    z = ytruep
                                power(z)
                                print(z)

                            gamedisplay.fill(white)
                            cannonb(40,570)
                            launchrotate(x,y)
                            cball(40,530)
                            target(linestartx,linestarty,lineendx,lineendy)


                            pygame.display.update()

                            clock.tick(144)


                    if x2 == x and y2 == y:
                        x2 = x
                        y2 = y
                        guide(x,y,z)
                    else:
                        x2 = x
                        y2 = y
                
                
                distance = distance+4
                
                    
                if Space == True:
                    if ballpos3x < 88:
                        ballpos3x = ballpos3x+3
                        ballpositionx = ballpos3x
                        ballpositiony = ballpos3y
                        cball(ballpositionx,ballpositiony)
                            
                    else:    
                        position = balllaunch(x,y,z,distance,initialposx,initialposy)
                        ballpositionx = position[0]
                        ballpositiony = position[1]
                        cball(ballpositionx,ballpositiony)
                        ballposy2 = ballpositiony+40 
                        
               
                     
                    
                target(linestartx,linestarty,lineendx,lineendy)
                cannonb(40,570)
                launchrotate(x,y) 
                                
                print(ballpositionx)
                if ballpositionx <= 670 and ballpositionx >= 666:
                    if ballpositiony >= lineendy + 15 or ballpositiony + 40 <= linestarty -15:
                        ballend = 680
                    elif ballpositiony > linestarty and ballpositiony + 40 < lineendy:
                        ballend = 680
                    
                    elif ballpositiony >= lineendy and ballpositiony <= lineendy + 10:
                        ballend = ballend
                    elif ballpositiony + 40 >= lineendy and ballpositiony + 40 <= lineendy + 10:
                        ballend = ballend
                    elif ballpositiony >= linestarty and ballpositiony <= linestarty - 10:
                        ballend = ballend
                    elif ballpositiony + 40 >= linestarty and ballpositiony + 40 <= linestarty + 10:
                        ballend = ballend
                
                if ballpositionx <= 682 and ballpositionx >= 680: 
                    if ballpositiony < lineendy and ballpositiony + 40 > linestarty:
                        time.sleep(0.5)
                        hit = hit+1
                        game_loophit(z,hit)
                    elif ballpositiony > lineendy or ballpositiony + 40 < linestarty:
                        ballend = 700
                
                
                    
                pygame.display.update()
                clock.tick(144)

            target(linestartx,linestarty,lineendx,lineendy) 
            cball(ballpositionx,ballpositiony)
            cannonb(40,570)

            launchrotate(x,y) 

            
            

            Miss()
            score(hit)
            
                                
                            
            pygame.display.update()
            clock.tick(144)
            



def intro_loop():
    play = False
    Space = False
    Instruct = False
    while not play:
        while not Space:
            gamedisplay.fill(white)
            if Instruct == True:
                instruction()
            else:
                welcome()
                startmessage()
                instructions()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                else:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                                    
                            Space = True
                            play = True

                        elif event.key == pygame.K_i:
                            
                            Instruct = True


            pygame.display.update()
            clock.tick(144)
                                    
 
        
        
        
    
pygame.init()
intro_loop()
game_loop()

    








