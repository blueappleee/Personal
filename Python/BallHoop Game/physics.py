#physics
import math

def angle(x,y): 
    y2 = y-85
    ytrue = 600 - y2 
    if x <= 50:
        xtrue = 1
    else:    
        xtrue = x - 50
    ratio = math.atan((ytrue / xtrue))
    theta = math.degrees(ratio)
    return(theta)

def power(slider):
    Vi = slider/3
    
    return(Vi)

def Vix(x, y, slider):
    theta = angle(x, y)
    Vi = power(slider)
    Vx = Vi * math.cos(math.radians(theta))
    
    return(Vx)

def Viy(x, y, slider):
    theta = angle(x, y)
    Vi = power(slider)
    Vy = Vi * math.sin(math.radians(theta))
    
    return(Vy)
     

def balllaunch(x, y, slider, distance, initialposx, initialposy):
    gravity = 10
    Vix2 = Vix(x, y, slider)
    Viy2 = Viy(x, y, slider)
    t = distance / Vix2
    
    positiony = Viy2 * t - 0.5 * gravity * t**2
    positionx = Vix2 * t
    ballposx = initialposx + positionx
    ballposy = initialposy - positiony
    
    return(ballposx, ballposy)








