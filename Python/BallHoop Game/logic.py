#logic loop
import graphics
import physics
import pygame
import random
import time
import sys

pygame.init()

def ballintersects(ballx, bally, object2y, object2x, object2len, object2width):
    ballcentx = ballx + 7
    ballcenty = bally + 7

    if ballcentx + 7 >= object2x:
        ## intersects on middle edge of ball

        print(ballcenty, object2y, object2y + object2len)
        if ballcenty >= object2y and ballcenty <= (object2y + object2len):
            return True

    #use pythagrian theorem 
    #if ballcentx + 7 >= (object2x):
     #   diffx = ballcentx - object2x
      #  diffy = ballcenty - object2y
        
        #if ballcentx + 7 >= (object2x + ):
        
    else:
        return False

def game_loop(slider = 297.5, hit = 0, launchx = 45, launchy = 45):
    miss = False
    GameExit = False
    Click = False
    collide = False
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

    targetlen = targetendy - targetstarty
    
    while not GameExit:
        while not miss: 
            while  ballpositiony < graphics.getheight() - 10 and not collide:
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
                                    launchx = x
                                    launchy = y
                                    graphics.guide(launchx, launchy, slider)  
                                
                            if x >= 765 and x <= 800:
                                mouse = pygame.mouse.get_pressed() 
                                if mouse[0] == True:
                                    ytruep = 600 - y

                                    if ytruep > 595:
                                        ytruep = 595

                                    if ytruep < 5:
                                        ytruep = 5
                                
                                    slider = ytruep / 2

                            graphics.gamedisplay.fill(graphics.getwhite())
                            graphics.cannonw(40, 400) 
                            graphics.target(targetstarty, targetendy)
                            graphics.launchrotate(launchx, launchy)
                            graphics.angledisp(physics.angle(launchx, launchy))
                            graphics.guide(launchx, launchy, slider)
                            graphics.powerdisp(slider)
                            graphics.powerslider(slider)

                            pygame.display.update()

                            graphics.clock.tick(60)
                    
                distance = distance + 3
                    
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
                graphics.launchrotate(launchx, launchy)
                graphics.angledisp(physics.angle(launchx, launchy))
                graphics.powerdisp(slider)
                graphics.powerslider(slider)
                
                if ballpositionx >= 722: ## change ball variable  ### change to a box and make game launching box onto shelf
                    hittarget = ballintersects(ballpositionx, ballpositiony, targetstarty, 738, targetlen, 15)
                    print(hittarget)
                    if hittarget:
                        collide = True
                        
                        graphics.Hit()
                        
                        time.sleep(0.5)
                        hit = hit + 1
                        
                        game_loop(slider, hit, launchx, launchy)
                        
                    elif ballpositionx >= 747:
                        collide = True
                 
                pygame.display.update()
                graphics.clock.tick(60)

            graphics.target(targetstarty, targetendy) 
            graphics.cball(ballpositionx, ballpositiony)
            graphics.cannonw(40, 400)
            graphics.launchrotate(launchx, launchy)
            graphics.angledisp(physics.angle(launchx, launchy))
            graphics.powerdisp(slider)
            graphics.powerslider(slider)

            graphics.Miss()
            graphics.score(hit)                    
                            
            pygame.display.update()
            graphics.clock.tick(60)  
