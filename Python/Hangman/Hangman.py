import sys  #7 attempts
print('Welcome to Hangman')
print('Enter word/s')
d = input()
x = []
y = []
a = 0
for i in range(len(d)):
    x.append('_')
for i in range(len(d)):
    y.append(d[a])
    a = a+1
h = ''.join(map(str,y))
print('Current Guess:',''.join(map(str,x)))    
c = 0
while c < 7:
    if c == 0:
        print('  -----')
        print('  |   |')
        print('      |')
        print('      |')
        print('      |')
        print('      |')
        print('      |')
        print('      |')
        print('      |')
        print(' ------')
    elif c == 1:
        print('  -----')
        print('  |   |')
        print('  0   |')
        print('      |')
        print('      |')
        print('      |')
        print('      |')
        print('      |')
        print('      |')
        print(' ------')
    elif c == 2:
        print('  -----')
        print('  |   |')
        print('  0   |')
        print('  |   |')
        print('      |')
        print('      |')
        print('      |')
        print('      |')
        print('      |')
        print(' ------')
    elif c == 3:
        print('  -----')
        print('  |   |')
        print('  0   |')
        print('  |   |')
        print(' /    |')
        print('      |')
        print('      |')
        print('      |')
        print('      |')
        print(' ------')
    elif c == 4:
        print('  -----')
        print('  |   |')
        print('  0   |')
        print('  |   |')
        print(' / \  |')
        print('      |')
        print('      |')
        print('      |')
        print('      |')
        print(' ------')
    elif c == 5:
        print('  -----')
        print('  |   |')
        print('  0   |')
        print('  |   |')
        print(' / \  |')
        print('  |   |')
        print('      |')
        print('      |')
        print('      |')
        print(' ------')
    elif c == 6:
        print('  -----')
        print('  |   |')
        print('  0   |')
        print('  |   |')
        print(' / \  |')
        print('  |   |')
        print(' /    |')
        print('      |')
        print('      |')
        print(' ------')
        
    a = 0
    d = 0
    print('Enter a letter')
    b = input()
    for i in range(len(y)):
        if y[a] == b:
            x[a] = b
            d = d+1
        a = a+1
    if d == 0:
        c = c+1
    g = ''.join(map(str,x))
    print('Current Guess:',g)
    if g == h:
        print('Congrats you win')
        print('Enter e to end')
        while 1:
            x = input()
            if x == 'e':
                sys.exit()
    print('Attempt Guess word? (yes/no)')
    e = input()
    if e == 'Yes' or e == 'yes':
        print('Guess word/s')
        f = input()
        if f == h:
            print('Congrats you win')
            print('Enter e to end')
            while 1:
                x = input()
                if x == 'e':
                    sys.exit()


print('  -----')
print('  |   |')
print('  0   |')
print('  |   |')
print(' / \  |')
print('  |   |')
print(' / \  |')
print('      |')
print('      |')
print(' ------')
print('You Lose')
print('You Guessed:', ''.join(map(str,x)))
print('Answer was:', ''.join(map(str,y)))
    
            
    
    
    
            

    
