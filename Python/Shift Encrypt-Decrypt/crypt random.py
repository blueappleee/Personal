import random

string1 = input()
x = len(string1)
fact = []
shift = []
y = []
string = []
list1 = ["‘","’",' ','!','"','#','$','%','&',"'",'(',')','*','+',',','-','.','/','0','1','2','3','4','5','6','7','8','9',':',';','<','=','>','?','@','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','[','\\',']','^','_','`','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','{','|','}']

for i in range(x):
    string.append(string1[i])

number = x

for i in range(number):
    key = random.randint(0,96)
    shift.append(key)

for num1 in range(int(x/number)):
    for i in range(number):
        s = shift[i]
        a = string[((number*num1) + i)]
        print(a,end='')
        b = list1.index(a)
        s2 = b + s
        if s2 >= 96:
                s1 = 96-b
                s2 = s - s1
        d = list1[s2]
        y.append(d)
print('\n')
print(''.join(map(str,y)))
print(','.join(map(str,shift)))
#print(len(shift),len(string))




