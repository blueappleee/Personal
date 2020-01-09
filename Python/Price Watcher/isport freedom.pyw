import requests
from bs4 import BeautifulSoup

c = ('https://www.sportchek.ca/product/332261021.html')
r = requests.get(c)
soup = BeautifulSoup(r.content, 'html.parser')
e = soup.find_all('span',{'class':'product-detail__price-text'})
a = str(e)
b = (a[43:49])

if float(b) <= 154.98:
    file = open(r'C:\Users\Connor\Desktop\MONSTER ISPORT FREEDOMV2.0 SPORTCHEK.txt','w+')
    file.write('Price for Isport Freedom v2.0 is '+b)
    file.close()

##else:
##    file = open(r'C:\Users\Connor\Desktop\MONSTER ISPORT FREEDOMV2.0 SPORTCHEK.txt','w+')
##    file.write('Price for Isport Freedom v2.0 is '+b)
##    file.close()


