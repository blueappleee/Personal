import sys
import random

def checkwinner(x):
    global c
    c = 0
    a = 0
    b = 0

    for j in range(3):
            if x[a] == x[a+1] and x[a] == x[a+2] and x[a] != '-':
                if x[a] == 'X':
                    print('Winner is: player one')
                elif x[a] == 'O':
                    print('Winner is player two')
                c = c+1
                break
            a = a+3
            if x[b] == x[b+3] and x[b] == x[b+6] and x[b] != '-':
                if x[b] == 'X':
                    print('Winner is: player one')
                elif x[b] == 'O':
                    print('Winner is player two')
                c = c+1
                break
                
            b = b+1
        
    if x[0] == x[4] and x[0] == x[8] and x[0] != '-':
        if x[0] == 'X':
            print('Winner is: player one')
        elif x[0] == 'O':
            print('Winner is player two')
        c = c+1
        
    if x[2] == x[4] and x[2] == x[6] and x[2] != '-':
        if x[2] == 'X':
            print('Winner is: player one')
        elif x[2] == 'O':
            print('Winner is player two')
        c = c+1
        

def space(q,i,x):
    corner = [0,2,6,8]
    corner2 = []
    middle = 4
    a = 0
    b = 0
    choice = ''
    global choicep

    if first == True:
        symb = 'X'
        osymb = 'O'
    else:
        symb = 'O'
        osymb = 'X'

    if i <= 2:
        if i <= 1:
            if first == True:
                choice = 0
            else:
                if x[4] == '-':
                    choice = 4
                else:
                    for p in range(2):
                        check1 = corner[p]
                        if x[check1] == '-':
                            choice = int(check1)
                            break           
                
        else:
            if x[0] == x[2] and x[0] == osymb:
                choice = a+2
                
            elif x[0] == x[6] and x[0] == osymb:
                choice = a+2
                
            elif x[6] == x[8] and x[6] == osymb:
                choice = a+2
                
            elif x[2] == x[8] and x[2] == osymb:
                choice = a+2
                
            elif x[0] == x[8] and x[0] == osymb:
                choice = a+2
                
            elif x[2] == x[6] and x[2] == osymb:
                choice = a+2
                    
            if choice == '':
                if choicep == 0 or choicep == 8:
                    corner2 = [2,6]
                    
                elif choicep == 2:
                    corner2 = [0,6]
                    
                elif choicep == 6:
                    corner2 = [0,8]
                    
                for o in range(2):
                    check1 = corner2[o]
                    if x[check1] == '-':
                        choice = int(check1)
                        break
                    
    
    else:
        for j in range(3):
            if x[a] == x[a+1] and x[a] != '-':
                if x[a+2] == '-':
                    choice = a+2
                    
            
            elif x[a] == x[a+2] and x[a] != '-':
                if x[a+1] == '-':
                    choice = a+1
            elif x[a+1] == x[a+2] and x[a] != '-':
                if x[a] == '-':
                    choice = a
        
            a = a+3
            
            if x[b] == x[b+6] and x[b] != '-':
                if x[b+3] == '-':
                    choice = b+3
                    
            elif x[b+3] == x[b+6] and x[b+3] != '-':
                if x[b] == '-':
                    choice = b       
            
            elif x[b] == x[b+3]and x[b] != '-':
                if x[b+6] == '-':
                    choice = b+6
      
            b = b+1
            
        if x[0] == x[4] and x[0] != '-':
            if x[8] == '-':        
                choice = 8

        elif x[4] == x[6] and x[4] != '-':
            if x[2] == '-':
                choice = 2

        elif x[4] == x[8] and x[4] != '-':
            if x[0] == '-':
                choice = 0
                
        elif x[0] == x[8] and x[0] != '-':
            if x[0] == symb:
                if x[4] == '-':
                    choice = 4
            else:
                if x[3] == '-':
                    choice = 3
                elif x[5] == '-':
                    choice = 5
            
        elif x[2] == x[4] and x[2] != '-':
            if x[6] == '-':
                choice = 6
                
        elif x[2] == x[6] and x[2] != '-':
            if x[2] == symb:
                if x[4] == '-':
                    choice = 4
            else:
                if x[7] == '-':
                    choice = 7
                elif x[5] == '-':
                    choice = 5

    if choice == '':
        for v in range(len(q)):
            if q[v] == 0 or q[v] == 2 or q[v] == 6 or q[v] == 8:
                choice = q[v]
                break
            
        if choice == '':
            choicet = random.randint(0,len(q)-1)
            choice = q[choicet] 
            

    choicep = choice
    return(choice)

    

print('Welcome to Tic Tack Toe')
print('Enter your name')
d = input()
while 1:
    x = ['-','-','-','-','-','-','-','-','-']
    q = [0,1,2,3,4,5,6,7,8]
    k = 2
    y = random.randint(0,1)
    if y == 0:
        print(d, ' you are player one (X)',sep = '')
        print('Computer is player two (O)',sep = '')
        first = False
    else:
        print('Computer is player one (X)',sep = '')
        print(d, ' you are player two (O)',sep = '')
        first = True

    for i in range(9):
        if y == 0:
            if k%2 == 0:
                print('Player ones turn, enter a coordinate')
                w = int(input()) -1
                f = 'X'
            else:
                print('Player twos turn')
                w = space(q,i,x)
                f = 'O'
        else:
            if k%2 == 0:
                print('Player ones turn')
                w = space(q,i,x)
                f = 'X'
            else:
                print('Player twos turn, enter a coordinate')
                w = int(input()) - 1
                f = 'O' 
        t = q.index(w)
        del q[t]
        x[w] = f

        print(x[0],x[1],x[2])
        print(x[3],x[4],x[5])
        print(x[6],x[7],x[8])

        checkwinner(x)

        if c > 0:
            break
        
        k += 1

    if c == 0:
        print('There is no winner')
        
    print('Would you like to restart?')
    question = input()
    
    if question == 'no' or question == 'No':
        sys.exit()



       

