from newlib import*
from math import log,sin,cos
f1=lambda x: log(x)-sin(x)
f=lambda x:-x-cos(x)
a=1.5
b=2.5
A= [1,-3,-7,27,-18]
B=[]
print("Q1")
print("solution by Bisection method=",bisection(a,b,f1))
print("solution Regula_falsi method =",regfal(a,b,f1))
print("solution by Newton Raphson method=",newrap(a,f1))
print("Q2")
print("solution by Bisection method=",bisection(-2,b,f))
print("solution Regula_falsi method =",regfal(a,b,f))
print("solution by Newton Raphson method=",newrap(-2,f))
#Q1(a) solution
# solution by Bisection method= 2.25
# solution by Regula_falsi method = 2.2191070451360577
# solution by Newton Raphson method= 2.219107148913746
#Q1(b) solution
#solution by Bisection method= -0.875
#solution Regula_falsi method = -0.7390850953790912
#solution by Newton Raphson method= -0.7390851332151607