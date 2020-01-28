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
    angle = pygame.font.Font('freesansbold.ttf', 15)
    text = angle.render(('Angle: ' + str(round(degree, 3))), True, getblack())
    
    gamedisplay.blit(text,(display_width * 0.05, 20))
    pygame.display.update()

def powerdisp(slider):
    powerlevel = (slider / 297.5) * 100
    
    power = pygame.font.Font('freesansbold.ttf', 15)
    text = power.render(('Power: ' + str(round(powerlevel, 3)) + '%'), True, getblack())
    
    gamedisplay.blit(text,(display_width * 0.05, 45))
    pygame.display.update()
    

def launchrotate(x, y): ## switch to cannon and get rid of complexity
    angle = physics.angle(x, y)
    center = cannon.get_rect().center

    newcannon = pygame.transform.rotate(cannon, angle)
    newcannon.get_rect().center = center
    
        
    gamedisplay.blit(newcannon, (120, 450))

def guide(x, y, slider):
    distance = 80
    initialposx = 90 #these initial values are the back middle of the cannon
    initialposy = 545
    ballpositiony = 0
    ballpositionx = 0
    
    while ballpositiony < 570 and ballpositionx <= 500 :  #change parameters after testing so it doesnt give ball trajectory so easy
        position = physics.balllaunch(x, y, slider, distance, initialposx, initialposy)
        
        ballpositionx = position[0]
        ballpositiony = position[1]
        distance = distance + 50

        if ballpositiony <= display_height and ballpositiony >= 0:
            dotpos(ballpositionx, ballpositiony)
        
    pygame.display.update()

def powerslider(slider):
    level = 600 - ((slider * 2))

    slider = slider * 2
    
    disp = getheight()

    pygame.draw.line(gamedisplay, getblack(), (783, level - 5), (783, level), 32)

    for i in range(0, disp - int(level), 2):

        red = 0 + (i / 2)

        if red > 255:
            red = 255
        
        green = 255 - (i / 2)

        if green < 0:
            green = 0
        
        pygame.draw.line(gamedisplay, (red, green, 0), (783, disp - i), (783, disp - i - 2), 32) 
    

def target(linestarty, lineendy): 
    length = lineendy - linestarty

    interval = round(length / 5)

    blue = getblue()
    red = getred()

    pygame.draw.line(gamedisplay, getblack(), (765, getheight()), (765, 0), 5)#make black

    pygame.draw.line(gamedisplay, blue, (745, linestarty), (745, linestarty + interval), 15)
    pygame.draw.line(gamedisplay, red, (745, linestarty + interval + 1), (745, linestarty + (2 * interval)), 15)
    pygame.draw.line(gamedisplay, getyellow(), (745, linestarty + (2 * interval) + 1), (745, linestarty + (3 * interval)), 15)
    pygame.draw.line(gamedisplay, red, (745, linestarty + (3 * interval) + 1), (745, linestarty + (4 * interval)), 15)
    pygame.draw.line(gamedisplay, blue, (745, linestarty + (4 * interval) + 1), (745, linestarty + (5 * interval)), 15)

def text_objects(text, font):
    textSurface = font.render(text, True, getblack())
    return textSurface, textSurface.get_rect()
    

def message_display(text):
    Ltext = pygame.font.Font('freesansbold.ttf', 100)
    textsurf, textrect = text_objects(text, Ltext)
    textrect.center = (display_width * 0.48), (display_height * 0.48)
    
    gamedisplay.blit(textsurf, textrect)
    pygame.display.update()

def instruction():
    welcome = pygame.font.Font('freesansbold.ttf', 40)

    black = getblack()
    
    text = welcome.render(('Increase and Decrease Power on far right'), True, black)
    text2 = welcome.render(('Use Mouse to change launch angle'), True, black)
    text3 = welcome.render(('Click left mouse to shoot'), True, black)
    text4 = welcome.render(('Hit the target to score points'), True, black)
     
    gamedisplay.blit(text, (display_width * 0.003, display_height * 0.2))
    gamedisplay.blit(text2, (display_width * 0.08, display_height * 0.3))
    gamedisplay.blit(text3, (display_width * 0.2, display_height * 0.4))
    gamedisplay.blit(text4, (display_width * 0.18, display_height * 0.5))
     
    
def welcome():
    welcome = pygame.font.Font('freesansbold.ttf', 40)
    text = welcome.render(('Welcome to ----'), True, getblack())
    gamedisplay.blit(text,(display_width * 0.30, display_height * 0.3))
    

def startmessage():
    startmessage = pygame.font.Font('freesansbold.ttf', 40)
    text = startmessage.render(('Press Space to start'), True, getblack())
    
    gamedisplay.blit(text,(display_width * 0.25, display_height * 0.4))
      

def instructions():
    instructions = pygame.font.Font('freesansbold.ttf', 40)
    text = instructions.render(('Press i for instructions'), True, getblack())
    
    gamedisplay.blit(text,(display_width * 0.22, display_height * 0.5))

def Miss():
    message_display('You Missed')

def Hit():
    message_display('Hit')

def score(hit):
    score = pygame.font.Font('freesansbold.ttf', 50)
    text = score.render(('Your Score:' + str(hit)), True, getblack())
    
    gamedisplay.blit(text,(display_width * 0.31, display_height * 0.53))
    pygame.display.update()

    time.sleep(2)

    logic.game_loop() ### add value to game loop to get rid of second game loop

def displayBuild():
    gamedisplaybuild = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('ballgame')

    return gamedisplaybuild

def getwidth():
    return display_width

def getheight():
    return display_height

def getwhite():
    return (255,255,255)

def getblack():
    return (0,0,0)

def getred():
    return (255,0,0)

def getblue():
    return (0, 0, 255)

def getgreen():
    return (0, 255, 0)

def getyellow():
    return (255, 255, 0)

pygame.init()

display_width = 800
display_height = 600

dot = pygame.image.load('dot.png')
ball = pygame.image.load('dot.png')
cannon = pygame.image.load('cannon.png')
cannon_wheel = pygame.image.load('cannon wheel.png')

gamedisplay = displayBuild()

clock = pygame.time.Clock()

    
