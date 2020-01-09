import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import math

x2 = []
y2 = []
e = []
begin = 0
tanx2 = False
dvd = False

def equation(t,e):
    y = 0
    y1 = 0
    y2 = 0
    if dvd == True:
        for i in range(len(e)):
            inx = False
            sinx = False
            cosx = False
            tanx = False
            w = e[i]
            for j in range(len(e[i])):
                if w[j] == 'x':
                    inx = True
                    break
                elif w[j:j+3] == 'sin' or w[j:j+3] == 'cos' or w[j:j+3] == 'tan':
                    if w[j:j+3] == 'sin':
                        sinx = True
                    elif w[j:j+3] == 'cos':
                        cosx = True
                    elif w[j:j+3] == 'tan':
                        tanx = True
            
            try:
                if i < middle:
                    if sinx == True:
                        if len(w) == 4:
                            y = y + math.sin(t)
                        else:
                            w2 = w.split('sin')
                            e2 = w.split('x')
                            try:
                                t1 = t**(int(e2[1]))
                            except:
                                t1 = t
                            try:
                                t1_1 = int(e2[0][3])*t1
                            except:
                                t1_1 = t1
                            try:    
                                t2 = int(w2[0])*(math.sin(t1_1))
                            except:
                                t2 = math.sin(t1_1)
                            y = y + t2 

                    elif cosx == True:
                        if len(w) == 4:
                            y = y + math.cos(t)
                        else:
                            w2 = w.split('cos')
                            e2 = w.split('x')
                            try:
                                t1 = t**(int(e2[1]))
                            except:
                                t1 = t
                            try:
                                t1_1 = int(e2[0][3])*t1
                            except:
                                t1_1 = t1    
                            try:    
                                t2 = int(w2[0])*(math.cos(t1_1))
                            except:
                                t2 = math.cos(t1_1)
                            y = y + t2
                    elif tanx == True:
                        if len(w) == 4:
                            y = y + math.tan(t)
                        else:
                            w2 = w.split('tan')
                            e2 = w.split('x')
                            try:
                                t1 = t**(int(e2[1]))
                            except:
                                t1 = t
                            try:
                                t1_1 = int(e2[0][3])*t1
                            except:
                                t1_1 = t1
                            try:    
                                t2 = int(w2[0])*(math.tan(t1_1))
                            except:
                                t2 = math.tan(t1_1)
                            y = y + t2      
                    else:
                        t2 = 0
                        try:
                            t2 = int(w)
                            y1 = y1+t2
                        except:
                            if w == '+x':
                                t2 = x
                            elif w == '-x':
                                t2 = -x
                            else:
                                if inx == True:
                                    e2 = w.split('x')
                                    try:
                                        t1 = t**(int(e2[1]))
                                    except:
                                        t1 = t
                                    try:
                                        t2 = int(e2[0])*t1
                                    except:
                                        t2 = t1
                                else:
                                    try:
                                        t2 = int(w)
                                    except:
                                        t2 = 0
                            if inx == False:
                                try:
                                    if w[0] == '-':
                                        y1 = y1 + int(e[i])
                                    elif w[0] == '+':
                                        y1 = y1 + int(w[1])
                                except:
                                    t2 = 0
                                    y1 = y1
                            else:
                                y1 = y1+t2
                else:
                    if sinx == True:
                        if len(w) == 4:
                            y = y + math.sin(t)
                        else:
                            w2 = w.split('sin')
                            e2 = w.split('x')
                            try:
                                t1 = t**(int(e2[1]))
                            except:
                                t1 = t
                            try:
                                t1_1 = int(e2[0][3])*t1
                            except:
                                t1_1 = t1
                            try:    
                                t2 = int(w2[0])*(math.sin(t1_1))
                            except:
                                t2 = math.sin(t1_1)
                            y = y + t2 

                    elif cosx == True:
                        if len(w) == 4:
                            y = y + math.cos(t)
                        else:
                            w2 = w.split('cos')
                            e2 = w.split('x')
                            try:
                                t1 = t**(int(e2[1]))
                            except:
                                t1 = t
                            try:
                                t1_1 = int(e2[0][3])*t1
                            except:
                                t1_1 = t1    
                            try:    
                                t2 = int(w2[0])*(math.cos(t1_1))
                            except:
                                t2 = math.cos(t1_1)
                            y = y + t2
                    elif tanx == True:
                        if len(w) == 4:
                            y = y + math.tan(t)
                        else:
                            w2 = w.split('tan')
                            e2 = w.split('x')
                            try:
                                t1 = t**(int(e2[1]))
                            except:
                                t1 = t
                            try:
                                t1_1 = int(e2[0][3])*t1
                            except:
                                t1_1 = t1
                            try:    
                                t2 = int(w2[0])*(math.tan(t1_1))
                            except:
                                t2 = math.tan(t1_1)
                            y = y + t2    
                    else:
                        t2 = 0
                        try:
                            t2 = int(w)
                            y2 = y2+t2
                        except:
                            if w == '+x':
                                t2 = x
                            elif w == '-x':
                                t2 = -x
                            else:
                                if inx == True:
                                    e2 = w.split('x')
                                    try:
                                        t1 = t**(int(e2[1]))
                                    except:
                                        t1 = t
                                    try:
                                        t2 = int(e2[0])*t1
                                    except:
                                        t2 = t1
                                else:
                                    try:
                                        t2 = int(w)
                                    except:
                                        t2 = 0
                            if inx == False:
                                try:
                                    if w[0] == '-':
                                        y2 = y2 + int(e[i])
                                    elif w[0] == '+':
                                        y2 = y2 + int(w[1])
                                except:
                                    t2 = 0
                                    y2 = y2
                            else:
                                y2 = y2+t2
                            
                
                y = y1/y2
            except:
                Y = 0

    else:###
        for i in range(len(e)):
            inx = False
            sinx = False
            cosx = False
            tanx = False
            w = e[i]
            for j in range(len(e[i])):
                if w[j] == 'x':
                    inx = True
                    break
                elif w[j:j+3] == 'sin' or w[j:j+3] == 'cos' or w[j:j+3] == 'tan':
                    if w[j:j+3] == 'sin':
                        sinx = True
                    elif w[j:j+3] == 'cos':
                        cosx = True
                    elif w[j:j+3] == 'tan':
                        tanx = True
            
            if sinx == True:
                if len(w) == 4:
                    y = y + math.sin(t)
                else:
                    w2 = w.split('sin')
                    e2 = w.split('x')
                    try:
                        t1 = t**(int(e2[1]))
                    except:
                        t1 = t
                    try:
                        t1_1 = int(e2[0][3])*t1
                    except:
                        t1_1 = t1
                    try:    
                        t2 = int(w2[0])*(math.sin(t1_1))
                    except:
                        t2 = math.sin(t1_1)
                    y = y + t2 

            elif cosx == True:
                if len(w) == 4:
                    y = y + math.cos(t)
                else:
                    w2 = w.split('cos')
                    e2 = w.split('x')
                    try:
                        t1 = t**(int(e2[1]))
                    except:
                        t1 = t
                    try:
                        t1_1 = int(e2[0][3])*t1
                    except:
                        t1_1 = t1    
                    try:    
                        t2 = int(w2[0])*(math.cos(t1_1))
                    except:
                        t2 = math.cos(t1_1)
                    y = y + t2
            elif tanx == True:
                if len(w) == 4:
                    y = y + math.tan(t)
                else:
                    w2 = w.split('tan')
                    e2 = w.split('x')
                    try:
                        t1 = t**(int(e2[1]))
                    except:
                        t1 = t
                    try:
                        t1_1 = int(e2[0][3])*t1
                    except:
                        t1_1 = t1
                    try:    
                        t2 = int(w2[0])*(math.tan(t1_1))
                    except:
                        t2 = math.tan(t1_1)
                    y = y + t2    
            else:
                t2 = 0
                try:
                    t2 = int(w)
                    y = y+t2
                except:
                    if w == '+x':
                        t2 = x
                    elif w == '-x':
                        t2 = -x
                    else:
                        if inx == True:
                            e2 = w.split('x')
                            try:
                                t1 = t**(int(e2[1]))
                            except:
                                t1 = t
                            try:
                                t2 = int(e2[0])*t1
                            except:
                                t2 = t1
                        else:
                            t2 = 0
                    if inx == False:
                        try:
                            if w[0] == '-':
                                y = y + int(e[i])
                            elif w[0] == '+':
                                y = y + int(w[1])
                        except:
                            t2 = 0
                            y = y
                    else:
                        y = y+t2
            
    #print(y1,y2,y)                
    return(y)
        

e1 = input()
c = int(input('Range \n'))
e3 = e1.strip()

for i in range(len(e3)-3):
    if e1[i:i+3] == 'tan':
        tanx2 = True
for i in range(len(e3)):
    if e3[i] == '/':
        dvd = True
        break
#print(dvd)


for i in range(len(e3)):
    if e3[i] == '+' or e3[i] == '-':
        e.append(e3[begin:(i)])
        begin = i
    elif e3[i] == '/':
            e.append(e3[begin:i])
            begin = i+1
            middle = len(e)

e.append(e3[begin:len(e3)])

if len(e) == 0:
    e.append(e3)

#print(e)
    
if tanx2 == True:
    interval = c/100000
elif dvd == True:
    interval = c/(c*100)
else:
    interval = c/10000
down = -c
up = interval

if dvd == True or tanx2 == True:   
    while down < 0:
        x = down
        y = equation(down,e)
        if dvd == True:
            if y <= c*10 and y >= -c*10:
                x2.append(x)
                y2.append(y)
        else:
            x2.append(x)
            y2.append(y)
        down +=interval
        

    y = equation(0,e)
    x2.append(0)
    y2.append(y)


    while up <= c:
        x = up
        y = equation(up,e)
        if dvd == True:
            if y <= c*10 and y >= -c*10:
                x2.append(x)
                y2.append(y)
        else:
            x2.append(x)
            y2.append(y)
        up +=interval
else:
    while down < 0:
        x = down
        y = equation(down,e)
        x2.append(x)
        y2.append(y)
        down +=interval
        

    y = equation(0,e)
    x2.append(0)
    y2.append(y)


    while up <= c:
        x = up
        y = equation(up,e)    
        x2.append(x)
        y2.append(y)
        up +=interval
    


tick_spacing = c/5

fig, ax = plt.subplots(1,1)
ax.plot(x2,y2)
ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
ax.set_xlim((min(x2)-0.00000000000001),(max(x2)+1))
plt.ticklabel_format(axis='y',style = 'sci',scilimits=(-7,7))
if tanx2 == True:
    ax.set_ylim([-c*10,c*10])
    
plt.grid()
plt.show()
