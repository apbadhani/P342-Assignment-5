import newlib as lib
import math
a=math.sin(math.pi/8)
#Defining the function
def f(x):
    return 1/math.sqrt(1-(a*math.sin(x))**2)
#Constants
l=1
g=9.8
print("\nValue of T = ",4*math.sqrt(l/g)*lib.simpson(0,math.pi/2,10,f))

#Value of T =  2.0873200174795916
