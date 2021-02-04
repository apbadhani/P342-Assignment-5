import newlib as lib
import math
#Constants
h=6.626*10**(-34)
k=1.381*10**(-23)
c=3*10**8
p=10**(-4)                     #Precison
def f(x):
    return (x-5)*math.e**x+5
def b(x):
    return (h*c)/(x*k)
#printing the result of Newton-Raphson
#taking x = 4.965 (by plotting the graphs of this function)
print("\nWein's Constant = ",b(lib.newrap(4.965,f,200,"Q1",p)))


#Wein's Constant =  0.002899010322982113