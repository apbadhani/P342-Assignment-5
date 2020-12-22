import newlib as lib
def f(x,y):
    return 6-2*y/x
print('Enter final point:')
xn = int(input('end point, xn = '))
#given conditions- x0=3, y(3)=1

# h is taken 0.5,0.2,0.1,0.02

# Euler method call for h=0.01
lib.foeu(f,3,1,0.01,xn)

#the values of 0.01 is shown.for other values graph is plotted
#for the graphs xn=7