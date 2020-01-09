
def gcf(a,b):          # defining a function that finds gcf of two numbers ( a and b)
    

    if a % b == 0:     # if a/b is a number without remainder than the gcf is the smaller number which in this case would be b
        return(b)      # returning b since it is the smaller number and therefore the gcf 


    elif b % a == 0:   # if b/a is a number without remainder than the gcf is the smaller number which in this case would be b
        return(a)      # returning a since it is the smaller number and therefore the gcf


    elif a > b:        # in the case that the first number is larger than the second
        e = a % b      # defining what e will be in order to give parameters to loop
        while e != 0:  # loop will continue until remainder is 0 because when remainder is 0 you have the gcf in the most recent calculation
            e = a % b  # e is the remainder of a/b
            a = b      # a becomes the value of b in the previous calculation in preperation for the next calculation
            b = e      # b becomes the value of e from the latest calculation in preperation for the next calculation

        return(a)      # gcf is equal to the value of b in calculation were the remainder becomes 0
                       # Since a becomes b in the process after the calculation you return a since b at that point has become the value of e from the latest calculation
        

    else:              # in the case that the second number is larger than the first
        e = b % a      # defining what e will be in order to give parameters to the loop 
        while e != 0:  # loop will continue until remainder is 0 because when remainder is 0 you have gcf in most recent calculation
            e = b % a  # e is the remainder of b/a
            b = a      # b becomes the value of a in the previous calculation in preperation for the next calculation
            a = e      # a becomes the value of e from the latest calculation in preperation for the next calculation
                        
        return(b)      # gcf is equal to the value of a in the calculation were the remainder was 0
                       # Since b becomes a in the process after the calculation you return b since a at that point has become the value of e from the latest calculation

    

    
def lcm(a,b):               # defining program to find LCM of two numbers 

    if a == b:              # if the first and second number are the same then the LCM is the value of either of those numbers since they are the same
        return(a)           # return the first number since it is the same as the LCM

    else:                   # in the case that the two numbers are not the same 
        l = (a*b)/gcf(a,b)  # l will multiply the two numbers a and b, it will then call the gcf program to find the greatest common factor of a and b,
                            # it will then divide the product of a and b by the greatest common factor of a and b making the variable l the lowest common multiple between a and b
        return(l)           # since l is the Lowest Common Multiple between a and b return 'l'          

 

                

   
   
