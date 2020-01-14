#logic loop
import graphics
import physics
import pygame
import random

pygame.init()

def game_loop(slider = 275, hit = 0): #when it hits the back board hit = hit+1 and then game_loophit(z,hit) eventually add level to conditions
    miss = False
    GameExit = False
    Space = False
    x = 0
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

    line1 = random.randint(50, 500)
    line2 = line1 + random.randint(60, 75)
    
    linestartx = 725 
    linestarty = line1
    lineendx = 725
    lineendy = line2
    
    while not GameExit:
        while not miss: 
            while  ballpositiony < 570 and ballpositionx < ballend:
                graphics.gamedisplay.fill(graphics.white)
                
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
                            
                            #limits slider
                            print(physics.angle(x,y))

                            if x < 750:
                                graphics.guide(x, y, slider)
                                graphics.launchrotate(x, y)
                                
                            
                            if x >= 750 and x <= 800:
                                ytruep = 600 - y
                                
                                if ytruep >= 350:
                                    slider = 350
                                else:
                                    slider = ytruep
                                    
                                physics.power(slider)
                                print(slider)

                            graphics.gamedisplay.fill(graphics.white)
                            graphics.cannonb(40, 570)
                            graphics.launchrotate(x, y)
                            graphics.cball(40, 530) 
                            graphics.target(linestartx, linestarty, lineendx, lineendy)


                            pygame.display.update()

                            graphics.clock.tick(60)


                    if x2 == x and y2 == y:
                        x2 = x
                        y2 = y
                        graphics.guide(x, y, slider)
                        
                    else:
                        x2 = x
                        y2 = y
                
                distance = distance + 4
                    
                if Space == True:
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
                        
                        ballposy2 = ballpositiony + 40       
                    
                graphics.target(linestartx, linestarty, lineendx, lineendy)
                graphics.cannonb(40, 570)
                graphics.launchrotate(x, y)

                if ballpositionx <= 670 and ballpositionx >= 666:
                    if ballpositiony >= lineendy + 15 or ballpositiony + 40 <= linestarty - 15:
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
                        hit = hit + 1
                        
                        game_loop(slider, hit)
                        
                    elif ballpositiony > lineendy or ballpositiony + 40 < linestarty:
                        ballend = 700
                 
                pygame.display.update()
                graphics.clock.tick(60)

            graphics.target(linestartx, linestarty, lineendx, lineendy) 
            graphics.cball(ballpositionx, ballpositiony)
            graphics.cannonb(40, 570)
            graphics.launchrotate(x, y)

            Miss()
            score(hit)                    
                            
            pygame.display.update()
            graphics.clock.tick(60)  
