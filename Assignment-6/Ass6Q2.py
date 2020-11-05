import newlib as li
f=li.fu2
c=0
d=1
'''''
Max error = 0.001 for good approx
N calculated:
for midpoint = 10
for trapezoid = 13
for simpson = 4
'''''
print("I value for Midpoint = ",li.midpoint(c,d,10,f))
print("I value for Trapezoid = ",li.trapezoid(c,d,13,f))
print("I value for Simpson = ",li.simpson(c,d,4,f))
'''''
OUTPUT:
I value for Midpoint =  0.7471308777479975
I value for Trapezoid =  0.7464612610366896
I value for Simpson =  0.7468553797909872
'''''
