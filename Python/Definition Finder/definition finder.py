import requests
from bs4 import BeautifulSoup
y = []
b = 0
with open('w.txt','r') as file:
    line = file.readline()
    y.append(line.replace('\n',''))
    for line in file:
        x = line.replace('\n','')
        y.append(x)
for i in range(len(y)):
    a = y[b]
    c = ('http://www.dictionary.com/browse/',a)
    d =(''.join(map(str,c)))
    
    r = requests.get(d)
    soup = BeautifulSoup(r.content, 'html.parser')
    t = soup.find_all('div',{'class':'def-content'})
    
    for t in t:
        w = t.find_all('span',{'class','def-number','1'})
    
        

    try:
        e = t.text.replace('\n','')
        print(y[b],': ',e.strip(), sep ='')
        print('\n')
        b = b+1
    except:
        print(y[b],': No definition')
        b = b+1
        


    
    
