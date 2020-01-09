list1 = ["‘","’",' ','!','"','#','$','%','&',"'",'(',')','*','+',',','-','.','/','0','1','2','3','4','5','6','7','8','9',':',';','<','=','>','?','@','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','[','\\',']','^','_','`','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','{','|','}']

import sys

print('Enter Message')
x = input()
print('Encrypt or decrypt?')
f = input()
print('Enter positive shift value')
s = int(input())

y = []
if f == 'Encrypt' or f == 'e':
    for i in range(len(x)):
        a = x[i]
        b = list1.index(a)
        c = b + s
        if c >= 96:
            if s > 96:
                g = s//96
                h = s - g*96
                if h > (96-b):
                    j = h - (93-b)
                    s1 = 0 + j
                    c = b + s1
                else:
                    s1 = h
                    c = b + s1
            else:
                s1 = 96-b
                s2 = s - s1
                c = s2
        d = list1[c]
        
        y.append(d)

elif f == 'Decrypt' or f == 'd':
    for i in range(len(x)):
        a = x[i]
        b = list1.index(a)
        c = b - s
        if c <= 0:
            g = s//93
            h = s - g*93
            if h > (b):
                j = h - (b)
                s1 = 0 + j
                c = b - s1
            else:
                s1 = h
                c = b - s1
        d = list1[c]
        
        y.append(d)
        
print(''.join(map(str,y)))
print('Enter e to exit')
while 1>0:
    x = input()
    if x == 'e' or x == 'E':
        sys.exit()
    else:
        continue
    
