from os import times
import pygame
from pygame import (
    K_UP, 
    K_DOWN, 
    K_LEFT, 
    K_RIGHT, 
    K_ESCAPE, 
    KEYDOWN, 
    QUIT,
    Rect,
)
from time import sleep 
import random

from pygame.sprite import collide_rect

pygame.init()
win = pygame.display.set_mode((1500, 800))
# Sets loop variable 
pygame.display.set_caption("Plinko")

setupcomplete = False

# Variables 

x = 745
y = 175
width = 20
height = 20
xvel = 40
yvel = -40
xvel1 = 1 
yvel1 = 1
gamend = {0:False}

timesplayed = 0

rectcolour = (0, 255, 0)

boxpositions = {0: 11, 1: 21, 2: 30, 3: 38, 4: 45, 5: 51, 6: 56, 7: 60, 8: 63, 9: 65, 10: 66}
boxpositioncords1 = {0: 1150, 1: 1070, 2: 990, 3: 910, 4: 830, 5: 750}
boxpositioncords2 = {0: 670, 1: 590, 2: 510, 3: 430, 4: 350}
positions = {}
score = {}
xx = x + 5

class GamePiece():
    def gp(x, y, w, h):  
          pygame.draw.rect(win, (0, 255, 0), (x, y, w, h))         
            
def Prize2(): 
    if y >= 600:
        gamend[0]=True
        if x == 1150 + 5: 
            score[timesplayed] = "Lost"
                     
                     
                     
        elif x == 1070 + 35:
            score[timesplayed] = "Lost"  
                     
                     
        elif x == 990 + 35:
            score[timesplayed] = "Lost"
                     
                 
                     
        elif x == 910 + 35:
            score[timesplayed] = "Lost"
                    
                     
        elif x == 830 + 35:
            score[timesplayed] = "Lost" 
                     
                     
        elif x == 750 + 35:
            score[timesplayed] = "Won"
                         
                     
                         
        elif x == 670 + 35:
            score[timesplayed] = "Won"
                   
                  
                     
        elif x == 590 + 35:
            score[timesplayed] = "Lost"
                 
                   
                     
        elif x == 510 + 35:
            score[timesplayed] = "Lost" 
                    
                
                     
        elif x == 430 + 35:
            score[timesplayed] = "Lost"
                        
                        
                         
        elif x == 350 + 35:
            score[timesplayed] = "Lost" 
                  
            
def yourscore(num): 
    template = pygame.font.SysFont('monospace', 70)
    template2 = template.render(f"You {num}!", True, (255, 255, 255))
    win.blit(template2,(575, 700))
    
        

class PlayAgain:
    def playagain():
        playagain = text.render("Press SPACE to play again", True, (191, 54, 54))
        win.blit(playagain, (377, 850))
     
 
class Board():
    setupcomplete = False
    basex = 750
    basey = 200
    positionnum = 1
    def create(x, y):
        
        base = pygame.Rect(x, y, 10, 10)
        pygame.draw.rect(win, (255, 255, 255), base)
        positions[Board.positionnum] = base.topleft

        Board.positionnum = Board.positionnum + 1
    
    def PrizeBox(value, px, py):
        text = pygame.font.SysFont('monospace', 50)
        renderer = text.render(value, True, (213, 16, 235))
        win.blit(renderer, (px, py))
        
    
    def PrizeBox2(colour, px, py): 
        base = pygame.Rect(px, py, 50, 50)
        if colour == 'red':
            pygame.draw.rect(win, (255, 0, 0), base)
        elif colour == 'green': 
            pygame.draw.rect(win, (0, 255, 0), base)
        elif colour == 'blue': 
            pygame.draw.rect(win, (0, 0, 255), base)
        else: 
            print('no colour selected')
        
    
    def loop(pnum, rx, ry, sp): 
        for i in range(pnum): 
            Board.create(Board.basex, Board.basey) 
            Board.basex += 40
            Board.basey += 40
            pygame.display.update()
            sleep(sp)
        Board.basex = rx
        Board.basey = ry
        #print(Board.basex, Board.basey)
    
    def looper(pnumnum, spsp):
        if Board.setupcomplete == False:
            for i in range(10):
                #print(Board.basex - newbasex)
                Board.loop(pnumnum,Board.basex - 40, Board.basey + 40, spsp)
                pnumnum -= 1
            Board.loop(pnumnum,Board.basex - 40, Board.basey + 40, spsp)
        else: 
            Board.basex = 750 
            Board.basey = 100
            for i in range(10):
                Board.loop(pnumnum,Board.basex - 40, Board.basey + 40, spsp)
                pnumnum -= 1
            Board.loop(pnumnum,Board.basex - 40, Board.basey + 40, spsp)
    
    def board(): 
        for i in range(1, 67): 
          
            num = i
            x, y = positions[num]
            if y == 600:
                 Board.PrizeBox('L', 350 - 60, y)
                
                 
                 if x == 1150:
                     Board.PrizeBox('L', x + 30, y)
                     
                     
                 elif x == 1070:
                     Board.PrizeBox('L', x + 30, y)
                     
                     
                 elif x == 990:
                     Board.PrizeBox('L', x + 30, y)
                 
                     
                 elif x == 910:
                     Board.PrizeBox('L', x + 30, y)
                    
                     
                 elif x == 830: 
                     Board.PrizeBox('L', x + 30, y)
                 
                     
                 elif x == 750:
                         Board.PrizeBox('W', x + 30, y)
                     
                         
                 elif x == 670:
                     Board.PrizeBox('W', x + 30, y)
                  
                     
                 elif x == 590:
                     Board.PrizeBox('L', x + 30, y)
                   
                     
                 elif x == 510: 
                     Board.PrizeBox('L', x + 30, y)
                
                     
                 elif x == 430:
                         Board.PrizeBox('L', x + 30, y)
                        
                         
                 elif x == 350: 
                     Board.PrizeBox('L', x + 30, y)
                   
                     
                     
            else: 
                pass
            base = pygame.Rect(x, y, 10, 10)   
            pygame.draw.rect(win, (255, 255, 255), base)  
               
def setup():    
    score.clear() 
    positions.clear()
    Board.looper(11, 0.02)
    #print(positions)
    Board.setupcomplete = True
    pygame.display.update()

running = True
gamerun = True
# Run the setup for the game
setup()

# Main loop (processes user input)
while running:
    for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                running = False
    sq = GamePiece.gp(x, y, width, height) 
    
# Looks at every event in the queue
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 
    keys = pygame.key.get_pressed() #Gives Dictionary of keys and whether they are pressed or not
        
    directions = ['left', 'right']
        
    Board.board()
    
    if keys[pygame.K_UP]: 
        print(score)
      
        
    Prize2()
        
    if y == 460:
            gamerun = False
            y += 40
            currentx = x 
            x = currentx
        
    dir = random.choice(directions)
    sleep(0.01)
    #print(dir)
    if gamend[0] == False:
        if keys[pygame.K_RETURN]: 
            if dir == 'left':
                x += xvel
                y -= yvel
                pygame.display.update(piece)
                sleep(0.1)
            elif dir == 'right':
                x -= xvel
                pygame.display.update(piece)
                y -= yvel
                pygame.display.update(piece)
                sleep(0.1)
    else:
        Prize2()
        PlayAgain.playagain()
        
        currentscore = score[timesplayed]
        yourscore(currentscore)
        pygame.display.update()
        if keys[pygame.K_SPACE]: 
            x = 745
            y = 175
            gamend[0] = False
            timesplayed += 1
    
    pygame.display.update()
    win.fill((0, 0, 0))
        
    # Draw the game piece
    text = pygame.font.SysFont('monospace', 50)
    piece = pygame.draw.rect(win, (0, 255, 0), (x, y, width, height)) 
    plinko = text.render("Plinko!", True, (191, 54, 54))
    instructions1 = text.render("Press the ENTER key to move the green ball", True, (191, 54, 54))
    win.blit(plinko,(652, 20))
    win.blit(instructions1,(100, 80))
pygame.quit()