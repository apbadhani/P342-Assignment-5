import newlib as lib
def f1(y1,y2,x):                      #first derivative
    dy1dx=y2
    return dy1dx
def f2(y1,y2,x):                       #second derivative
    dy2dx=1-y2-x
    return dy2dx
# RK4 method call for h=0.02
lib.rk4(f1,f2,0.02,1,2,5,0)
#xn=5 and step size h=0.5,0.1,0.01 are plotted in the graphs
#graph of 1+e^(-x)-(x^2)/2+2x over the range x ∈ [−5, 5] and y ∈ [−5, 5] is also plotted
