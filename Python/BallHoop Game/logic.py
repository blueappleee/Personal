#logic loop
import graphics
import physics
import pygame
import random
import time
import sys

pygame.init()

def intersects(ball, object2):
    pass

def game_loop(slider = 297.5, hit = 0, x = 45, y = 45):
    miss = False
    GameExit = False
    Click = False
    LEFT = 1
    distance = 0
    initialposx = 94
    initialposy = 545
    ballpositionx = 0
    ballpositiony = 0
    ballend = 668
    ballpos3x = 40
    ballpos3y = 530

    targetstarty = random.randint(25, 520)

    if hit <= 20:
        targetendy = targetstarty + 60 - (hit * 2)

    else:
        targetendy = targetstarty + 20
    
    while not GameExit:
        while not miss: 
            while  ballpositiony < graphics.getheight() and ballpositionx < ballend:
                graphics.gamedisplay.fill(graphics.getwhite())
                
                while not Click:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                            
                        else:
                            pos = pygame.mouse.get_pos()
                            x = pos[0]
                            y = pos[1]

                            if x < 760:
                                if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                                    Click = True

                                else:
                                    graphics.guide(x, y, slider)  
                                
                            if x >= 760 and x <= 800:
                                ytruep = 600 - y

                                if ytruep > 595:
                                    ytruep = 595

                                if ytruep < 5:
                                    ytruep = 5
                                
                                slider = ytruep / 2

                            graphics.gamedisplay.fill(graphics.getwhite())
                            graphics.cannonw(40, 400) 
                            graphics.target(targetstarty, targetendy)
                            graphics.launchrotate(x, y)
                            graphics.angledisp(physics.angle(x, y))
                            graphics.powerdisp(slider)
                            graphics.guide(x, y, slider)
                            graphics.powerslider(slider)

                            pygame.display.update()

                            graphics.clock.tick(60)
                    
                distance = distance + 4
                    
                if Click == True:
                    if ballpos3x < 88:
                        ballpos3x = ballpos3x+3
                        ballpositionx = ballpos3x
                        ballpositiony = ballpos3y
                        
                        graphics.cball(ballpositionx, ballpositiony)
                            
                    else:    
                        position = physics.balllaunch(x, y, slider, distance, initialposx, initialposy)
                        ballpositionx = position[0]
                        ballpositiony = position[1]
                        
                        graphics.cball(ballpositionx, ballpositiony)
                        
                        ballposy2 = ballpositiony + 15       
                    
                graphics.target(targetstarty, targetendy)
                graphics.cannonw(40, 400)
                graphics.launchrotate(x, y)
                graphics.angledisp(physics.angle(x, y))
                graphics.powerdisp(slider)
                graphics.powerslider(slider)

                if ballpositionx <= 670 and ballpositionx >= 666:
                    if ballpositiony >= targetendy + 15 or ballpositiony + 40 <= targetstarty - 15:
                        ballend = 680
                        
                    elif ballpositiony > targetstarty and ballpositiony + 40 < targetendy:
                        ballend = 680
                    
                    elif ballpositiony >= targetendy and ballpositiony <= targetendy + 10:
                        ballend = ballend
                        
                    elif ballpositiony + 40 >= targetendy and ballpositiony + 40 <= targetendy + 10:
                        ballend = ballend
                        
                    elif ballpositiony >= targetstarty and ballpositiony <= targetstarty - 10:
                        ballend = ballend
                        
                    elif ballpositiony + 40 >= targetstarty and ballpositiony + 40 <= targetstarty + 10:
                        ballend = ballend
                
                if ballpositionx <= 682 and ballpositionx >= 680: ## change ball variable  ### change to a box and make game launching box onto shelf
                    if ballpositiony < targetendy and ballpositiony + 40 > targetstarty:
                        graphics.Hit()
                        
                        time.sleep(0.5)
                        hit = hit + 1
                        
                        game_loop(slider, hit, x, y)
                        
                    elif ballpositiony > targetendy or ballpositiony + 40 < targetstarty:
                        ballend = 700
                 
                pygame.display.update()
                graphics.clock.tick(60)

            graphics.target(targetstarty, targetendy) 
            graphics.cball(ballpositionx, ballpositiony)
            graphics.cannonw(40, 400)
            graphics.launchrotate(x, y)
            graphics.angledisp(physics.angle(x, y))
            graphics.powerdisp(slider)
            graphics.powerslider(slider)

            graphics.Miss()
            graphics.score(hit)                    
                            
            pygame.display.update()
            graphics.clock.tick(60)  
