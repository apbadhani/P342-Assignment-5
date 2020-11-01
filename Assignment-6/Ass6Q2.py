import newlib as li
f=li.fu2
c=0
d=1
'''''
Max error = 0.0005 for good approx
N calculated:
for midpoint = 50
for trapezoid = 70
for simpson = 100
'''''
print("I value for Midpoint = ",li.midpoint(c,d,50,f))
print("I value for Trapezoid = ",li.trapezoid(c,d,70,f))
print("I value for Simpson = ",li.simpson(c,d,100,f))
'''''
I value for Midpoint =  0.7468363957465884
I value for Trapezoid =  0.7370225141840184
I value for Simpson =  0.7524525977629901
'''''