### calculates the x value in the fibonacci sequence
x = int(input())
e = x - 2
a = 1
b = 0
d = 0


while d <= e:
    c = a + b
    b = a
    a = c
    d = d+1

print(c)
    

