#graphics
import pygame
import time
import physics
import logic

def dotpos(dotpositionx, dotpositiony):
    gamedisplay.blit(dot,(dotpositionx, dotpositiony))

def cball(ballpositionx, ballpositiony):
    gamedisplay.blit(ball, (ballpositionx, ballpositiony))

def cannonw(cannonwx, cannonwy):
    gamedisplay.blit(cannon_wheel, (cannonwx, cannonwy))

def angledisp(degree):
    angle = pygame.font.Font('freesansbold.ttf', 20)
    text = angle.render(('Angle: ' + str(round(degree, 3))), True, black)
    
    gamedisplay.blit(text,(display_width * 0.05, 20))
    pygame.display.update()

def powerdisp(slider):
    powerlevel = (slider / 297.5) * 100
    
    power = pygame.font.Font('freesansbold.ttf', 20)
    text = power.render(('Power: ' + str(round(powerlevel, 3)) + '%'), True, black)
    
    gamedisplay.blit(text,(display_width * 0.05, 50))
    pygame.display.update()
    

def launchrotate(x, y): ## switch to cannon and get rid of complexity
    angle = physics.angle(x, y)
    center = cannon.get_rect().center

    newcannon = pygame.transform.rotate(cannon, angle)
    newcannon.get_rect().center = center
    
        
    gamedisplay.blit(newcannon, (120, 450))

def guide(x, y, slider):
    ballpositiony = 0
    ballpositionx = 0
    distance = 80
    initialposx = 90
    initialposy = 545
    
    while ballpositiony < 570 and ballpositionx <= 500 :  #change parameters after testing so it doesnt give ball trajectory so easy
        position = physics.balllaunch(x, y, slider, distance, initialposx, initialposy)
        
        ballpositionx = position[0]
        ballpositiony = position[1]
        dotpositionx = ballpositionx - 5
        dotpositiony = ballpositiony + 15
        distance = distance + 50

        if dotpositiony <= display_height and dotpositiony >= 0:
            dotpos(dotpositionx, dotpositiony)
        
    pygame.display.update()

def target(linestartx, linestarty, lineendx, lineendy): 
    pygame.draw.line(gamedisplay, red, (750, 600), (750, 0), 20)
    
    bottomlinex = lineendx - 15
    toplinex = linestartx - 15
    
    pygame.draw.line(gamedisplay, red, (linestartx, linestarty), (lineendx, lineendy), 15)
    pygame.draw.line(gamedisplay, red, (linestartx + 7, linestarty), (toplinex, linestarty), 10)
    pygame.draw.line(gamedisplay, red, (lineendx + 7, lineendy), (bottomlinex, lineendy), 10) 

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
    

def message_display(text):
    Ltext = pygame.font.Font('freesansbold.ttf', 100)
    textsurf, textrect = text_objects(text, Ltext)
    textrect.center = (display_width * 0.48), (display_height * 0.48)
    
    gamedisplay.blit(textsurf, textrect)
    pygame.display.update()

def instruction():
    welcome = pygame.font.Font('freesansbold.ttf', 40)
    
    text = welcome.render(('Increase and Decrease Power on far right'), True, black)
    text2 = welcome.render(('Use Mouse to change launch angle'), True, black)
    text3 = welcome.render(('Get the box onto the shelf'), True, black)
     
    gamedisplay.blit(text, (display_width * 0.003, display_height * 0.3))
    gamedisplay.blit(text2, (display_width * 0.08, display_height * 0.4))
    gamedisplay.blit(text3, (display_width * 0.18, display_height * 0.5)) 
     
    
def welcome():
    welcome = pygame.font.Font('freesansbold.ttf',40)
    text = welcome.render(('Welcome to ----'),True,black)
    gamedisplay.blit(text,(display_width*0.30,display_height*0.3))
    

def startmessage():
    startmessage = pygame.font.Font('freesansbold.ttf', 40)
    text = startmessage.render(('Press Space to start'), True, black)
    
    gamedisplay.blit(text,(display_width * 0.25, display_height * 0.4))
      

def instructions():
    instructions = pygame.font.Font('freesansbold.ttf', 40)
    text = instructions.render(('Press i for instructions'), True, black)
    
    gamedisplay.blit(text,(display_width * 0.22, display_height * 0.5))

def Miss():
    message_display('You Missed')

def score(hit):
    score = pygame.font.Font('freesansbold.ttf', 50)
    text = score.render(('Your Score:' + str(hit)), True, black)
    
    gamedisplay.blit(text,(display_width * 0.31, display_height * 0.53))
    pygame.display.update()

    time.sleep(2)

    logic.game_loop() ### add value to game loop to get rid of second game loop

def displayBuild():
    gamedisplaybuild = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('ballgame')

    return gamedisplaybuild

pygame.init()

display_width = 800
display_height = 600

dot = pygame.image.load('dot.png')
ball = pygame.image.load('dot.png')
cannon = pygame.image.load('cannon.png')
cannon_wheel = pygame.image.load('cannon wheel.png')

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

gamedisplay = displayBuild()

clock = pygame.time.Clock()

    
