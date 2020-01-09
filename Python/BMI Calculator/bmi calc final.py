print('Enter height in meters')
h = float(input())
print('Enter weight in kilograms')
w = float(input())
x = w/(h*h)
if x >25:
    print('Overweight')
elif x <=25 and x > 18.5:
    print('Normal Weight')
else:
    print('Underweight')
