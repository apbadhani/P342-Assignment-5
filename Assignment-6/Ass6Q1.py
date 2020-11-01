import newlib as li
f=li.fu1
c=1
d=3
#Values here are calculated for N=1000 for better approximation
print("I value for Midpoint = ",li.midpoint(c,d,1000,f))
print("I value for Trapezoid = ",li.trapezoid(c,d,1000,f))
print("I value for Simpson = ",li.simpson(c,d,1000,f))
'''''
ANALYTICAL VALUE = 1.30685281944

For N=10
I value for Midpoint =  1.3071646395900398
I value for Trapezoid =  1.180424712850113
I value for Simpson =  1.3833605594602516

For N=25
I value for Midpoint =  1.3069028019555275
I value for Trapezoid =  1.2566116551937927
I value for Simpson =  1.3570998943226809

For N=50
I value for Midpoint =  1.306865318346547
I value for Trapezoid =  1.2817914340736978
I value for Simpson =  1.3219148660338558
'''''

