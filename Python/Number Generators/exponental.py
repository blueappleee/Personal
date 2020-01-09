### shows exponential growth of a number (a) by a value (b) for c iterations
def exponental(a,b,c):
    d = 0
    
    while d < c:
        e = a**b
        print('-',e)
        a = e
        d = d + 1
        
        
    
