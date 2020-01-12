import sys
import random
print('Welcome to Tic Tack Toe')
print('Enter your names')
d = input()
e = input()
x = ['-','-','-','-','-','-','-','-','-']
q = [0,1,2,3,4,5,6,7,8]
c = 0
k = 2
y = random.randint(0,1)
if y == 0:
    print(d, ' you are player one',sep = '')
    print(e, ' you are player two',sep = '')
else:
    print(e, ' you are player one',sep = '')
    print(d, ' you are player two',sep = '')

print(x[0],x[1],x[2])
print(x[3],x[4],x[5])
print(x[6],x[7],x[8])
    
for i in range(8):
    print('Available spaces are:', q)
    if k%2 == 0:
        print('Player ones turn, enter a coordinate')
        w = int(input())
        f = 'X'
    else:
        print('Player twos turn, enter a coordinate')
        w = int(input())
        f = 'O'
    q.remove(w)
    x[w] = f
    a = 0
    b = 0
    
    for j in range(3):
        if x[a] == x[a+1] and x[a] == x[a+2] and x[a] != '-' and x[a+1] != '-':
            if x[a] == 'X':
                print('Winner is: player one')
                sys.exit()
            elif x[a] == 'O':
                print('Winner is player two')
                sys.exit()
            break
        a = a+3
        if x[b] == x[b+3] and x[b] == x[b+6] and x[b] != '-' and x[b+3] != '-':
            if x[b] == 'X':
                print('Winner is: player one')
                sys.exit()
            elif x[b] == 'O':
                print('Winner is player two')
                sys.exit()
            break
            
        b = b+1
    if x[0] == x[4] and x[0] == x[8] and x[0] != '-':
        if x[0] == 'X':
            print('Winner is: player one')
            sys.exit()
        elif x[0] == 'O':
            print('Winner is player two')
            sys.exit()
        
    if x[2] == x[4] and x[2] == x[6] and x[2] != '-':
        if x[2] == 'X':
            print('Winner is: player one')
            sys.exit()
        elif x[2] == 'O':
            print('Winner is player two')
            sys.exit() 
    
    print(x[0],x[1],x[2])
    print(x[3],x[4],x[5])
    print(x[6],x[7],x[8])
    k = k+1

print('Final space is:',q)
print('Final Turn, player one choose a coordinate')
w = int(input())
f = 'x'
x[w] = f

print(x[0],x[1],x[2])
print(x[3],x[4],x[5])
print(x[6],x[7],x[8])
a = 0
b = 0


for j in range(3):
    if x[a] == x[a+1] and x[a] == x[a+2] and x[a] != '-':
        c = c+1
        if x[a] == 'X':
            print('Winner is: player one')
            sys.exit()
        elif x[a] == 'O':
            print('Winner is player two')
            sys.exit()
    a = a+3
    if x[b] == x[b+3] and x[b] == x[b+6] and x[b] != '-':
        c = c+1
        if x[a] == 'X':
            print('Winner is: player one')
            sys.exit()
        elif x[a] == 'O':
            print('Winner is player two')
            sys.exit()
    b = b+1
if x[0] == x[4] and x[0] == x[8] and x[0] != '-':
    c = c+1
    if x[a] == 'X':
        print('Winner is: player one')
        sys.exit()
    elif x[a] == 'O':
        print('Winner is player two')
        sys.exit() 
if x[2] == x[4] and x[2] == x[6] and x[2] != '-':
    print('Winner is: player',x[4])
    c = c+1
    if x[a] == 'X':
        print('Winner is: player one')
        sys.exit()
    elif x[a] == 'O':
        print('Winner is player two')
        sys.exit() 
if c == 0:
    print('There is no winner')

       
