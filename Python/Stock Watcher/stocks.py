import re
import decimal
import requests
from bs4 import BeautifulSoup

def allstocks(path):
    try:
        y = []

        with open(path,'r') as file:
            line = file.readline()
            y.append(line.replace('\n',''))
            for line in file:
                x = line.replace('\n','')
                y.append(x)
        #print(y)

        for i in range(len(y)):
            try:
                a = y[i].strip()
                c = ('https://www.bloomberg.com/quote/',a)
                d =(''.join(map(str,c)))
                #print(d)
                
                r = requests.get(d)
                soup = BeautifulSoup(r.content, 'html.parser')
                try:
                    s = soup.find_all('div',{'class':'basic-quote'})
                except:
                    print(a,':No price')
                for s in s:
                    p = s.find_all('div',{'class':'price'})
                #print(s)
                #print(p)
                sp = str(p)
                np = re.sub('[^0-9]','',sp) 
                f = len(np)-2
                h = len(np)
                print(a,': $',np[0:f],'.',np[f:h],sep='',end='')
                print('\n')
            except:
                a = y[i]
                print(a,'error with ticker check in stocks file to ensure all characters are correct')
            
    except:
        print('error with path request recall function and ensure to include the entire path with the r infront of the path to indicate raw')
        
    print('enter e to exit')
    while 1>0:
        key = input()
        if key == 'e':
            break
        else:
            continue

def stock(ticker):
    try:
        a = ticker
        c = ('https://www.bloomberg.com/quote/',a)
        d =(''.join(map(str,c)))
        #print(d)
        
        r = requests.get(d)
        soup = BeautifulSoup(r.content, 'html.parser')
        try:
            s = soup.find_all('div',{'class':'basic-quote'})
        except:
            print(a,':No price')
        for s in s:
            p = s.find_all('div',{'class':'price'})
        #print(s)
        #print(p)
        sp = str(p)
        np = re.sub('[^0-9]','',sp) 
        f = len(np)-2
        h = len(np)
        print(a,': $',np[0:f],'.',np[f:h],sep='',end='')
        print('\n')
    except:
        print('error with ticker request recall function and ensure to include the entire ticker')
        
    print('enter e to exit')
    while 1>0:
        key = input()
        if key == 'e':
            break
        else:
            continue
    
