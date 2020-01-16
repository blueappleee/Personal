import graphics
import pygame

pygame.init()

def intro_loop():
    play = False
    Space = False
    Instruct = False
    
    while not play:
        while not Space:
            graphics.gamedisplay.fill(graphics.getwhite())
            
            if Instruct == True:
                graphics.instruction()
                
            else:
                graphics.welcome()
                graphics.startmessage()
                graphics.instructions()
                
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
            graphics.clock.tick(60)
                                    
 
  
