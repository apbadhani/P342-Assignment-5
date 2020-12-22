import newlib as lib
import math
def f1(x,y):
    return math.log(y)*y/x
print('Enter final point:')
xn = int(input('end point, xn = '))
#given conditions- x0=2, y(2)=e

# h is taken 0.5,0.2,0.1,0.02

# Euler method call for h=0.01
lib.foeu(f1,2,2.71828,0.01,xn)

#the values of 0.01 is shown.for other values graph is plotted
#for the graphs xn=6
