import newlib as lib
import math
g=9.8
def dzdx(x,y,v):
    return -g
def dydx(x):
    return -g*x
#Given boundary conditions are -
#y(0)=2     y(5)=45
#v(5)=0
#Calculate v(0)

z = lib.ShootingMethod(dydx,dzdx,0, 5, 2, 45, 0, 1.5, 10**(-4))
