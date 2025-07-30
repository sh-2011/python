import math
def myfunction(a,b,c):
     m = (b**2)-(4*a*c) 
     if m>0: 
        global x 
        x = (-b) / (2*a)
        return ((-b + (math.sqrt(m)))/(2*a)),((-b - (math.sqrt(m)))/(2*a)),x,a * x ** 2 + b * x + c
     elif m == 0:
        return  x
     elif m < 0:
        print('not found')
print(myfunction(7,4,-3))