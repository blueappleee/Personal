### finds and prints all factors of a number and outputs total factor amount
x = int(input())
e = 0

for i in range(x+1):
    try:
        if x % i == 0:
            print(i)
            e = e+1
            
    except:
        pass
    
print('Total number:', e)
               
               
                
