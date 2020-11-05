import newlib as li
f=li.fu1
c=1
d=3
print("I value for Midpoint = ",li.midpoint(c,d,52,f))
print("I value for Trapezoid = ",li.trapezoid(c,d,52,f))
print("I value for Simpson = ",li.simpson(c,d,52,f))
'''''
ANALYTICAL VALUE = 1.30685281944

For N=10
I value for Midpoint =  1.3071646395900398
I value for Trapezoid =  1.306228596824572
I value for Simpson =  1.3068497693110697

For N=24
I value for Midpoint =  1.3069070523279667
I value for Trapezoid =  1.306744336022721
I value for Simpson =  1.306852725655682

For N=52
I value for Midpoint =  1.3068643754579667
I value for Trapezoid =  1.3068297066030374
I value for Simpson =  1.306852815169979

'''''

