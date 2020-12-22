import newlib as lib
def f(x,y,v):
    return 1-x-v
# RK4 method call for h=0.02
lib.rk4(f,0.02,2,1,5,0)
#xn=5 and step size h=0.5,0.1,0.01 are plotted in the graphs
#graph of 1+e^(-x)-(x^2)/2+2x over the range x ∈ [−5, 5] and y ∈ [−5, 5] is also plotted
