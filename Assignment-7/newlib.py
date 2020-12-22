import math                                     #for base e
import random                                   #for random function
def f1(x):
    return math.log(x)-math.sin(x)
def f2(x):
    return -x-math.cos(x)
def der1(f,x,h=0.0002):
    return ((f(x + h) - f(x - h))/(2*h))
def bracket_root(f, a, b, beta=1.5):
    for i in range(12):
        if f(a) * f(b) > 0:
            if abs(f(a)) < abs(f(b)):
                a = a - beta * (b - a)
            else:
                b = b + beta * (b - a)
    if f(a) * f(b) > 0:
        print('Try different range')
    return a, b
def bisection(a,b,f):
    n = 0
    file1 = open("File1.txt", "w+")
    while(abs(b-a) > 0.000001) and (n<200):
        c = (a + b)/2
        file1.write("%f\r\n" % abs(a-b))
        m=(a + b)/2
        n = n + 1
        f_m_n = f(m)
        if f(a)*f_m_n < 0:
            b = m
        elif f(b)*f_m_n < 0:
            a = m
        file1.close()
        return float((a + b)/2)
def regfal(x0,x1,f):
    file1=open("file2.txt","w+")
    n=0
    condition=abs(x0-x1)
    while condition> 0.000001:
        x2=x0-(x1-x0)*f(x0)/(f(x1)-f(x0))
        file1.write("%f\r\n" % condition)
        if f(x0)*f(x2)<0:
            x1=x2
            n=n+1
        elif f(x1)*f(x2)<0:
            x0=x2
            n=n+1
        elif f(c)==0:
            print("exact solution")
            return c
        else:
            return None
        condition=abs(f(x2))
    file1.close()
    return x2
def newrap(x,f,max=118):
    errors = []
    file1=open("file3.txt","w+")
    for i in range(max):
        if der1(f, x) == 0.0:
            print('Divide by zero error!')
            return
        x_prev = x
        # update x as per newton-raphson formula
        x = x - f(x) / der1(f,x)
        file1.write("%f\r\n" % abs((x - x_prev)))
        # append the absolute error in list
        errors.append(abs(x - x_prev))
        # check if convergence criteria satisfied
        if abs(x - x_prev) < 10 ** (-6):
            file1.close()
            return x
def der2(f,a,h=0.0002):
    return ((f(x + h) - 2*f(x) + f(x - h))/(2*h*h))
def polynomial(x,A = []):
    y = 0
    for i in range(0,len(A)):
        y += A[i]*pow(x,(len(A)-(i+1)))
    return y
def laguerre(coeffs, x0, max_iter = 200):
    n = len(coeffs)
    #define the polynomial function
    p = polynomial(coeffs)
    x = x0
    #check if guess was correct
    if polynomial(x) == 0:
        return x
    for i in range(max_iter):
        #store previous value for comparison
        x_pre = x
        G = der1(p,x)/p(x)
        H = G**2 - der2(p,x)/p(x)
        de1 = G+((n-1)*(n*H - G**2))**0.5
        de2 = G-((n-1)*(n*H - G**2))**0.5
        #compare denominators
        if abs(d2)>abs(de1):
            a = n/de2
        else:
            a = n/de1
        x = x - a
        #check if convergence criteria satisfied
        if abs(x - x_pre) < 10**(-6):
            return x
    return x
def syndiv(coeffs, root):
    n = len(coeffs)
    #initiate list with the same first element
    new_coeffs = []
    new_coeffs.append(coeffs[0])
    for i in range(1, n):
        new_coeffs.append(new_coeffs[i-1]*root+coeffs[i])
    return new_coeffs[:-1]
def polysol(coeffs, x):
    n = len(coeffs)
    roots = []
    for i in range(n-1):
        #find one of the root of polynomial and add to list
        root = laguerre(coeffs, x)
        roots.append(root)
        #reduce the polynomial by synthetic division
        coeffs = syndiv(coeffs, root)
    return roots
# Function in Question 1
def fu1(x):
    return x/(1+x)
# Function in Question 2
def fu2(x):
    return math.e**(-x**2)
# Function in Question 3
def fu3(x):
    k=1+x**2
    return 4/k
# Midpoint method function
def midpoint(a,b,N,f):
    h=abs(b-a)/N
    M=0
    x_0=a
    for i in range(1,N+1):
        x=a+i*h
        m=(x+x_0)/2
        M=M+h*f(m)                        #weight function or w=1
        x_0=x
    return M
# Trapezoid method function
def trapezoid(a,b,N,f):
    h=abs(b-a)/N
    T=h/2*(f(a)+f(b))
    for i in range(1,N):
        x=a+i*h
        T=T+h/2*f(x)*2        #weight  function=2
    return T
# Simpson method function
def simpson(a,b,N,f):
    h=abs(b-a)/N
    S=h/3*(f(a)+f(b))
    for i in range(1,N):
        x=a+i*h
        if i%2==0:
            S=S+h/3*f(x)*2
        else:
            S=S+h/3*f(x)*4
    return S
# Montecarlo method function
def montecarlo(a,b,N,f):
    K=0
    for i in range(1,N+1):
        n = random.random()                #random number generator function
        x=n
        K=K+f(x)
    return K/N
# Forward Euler method
def foeu(f,x0,y0,h,xn):
    n=int((xn-x0)/h)
    print('x0   \ty0   ')                          #printing the data
    for i in range(n+1):
        slope=f(x0,y0)
        y=y0+h*slope
        print('%.5f\t%.5f\t'% (x0,y0))
        y0=y
        x0=x0+h

# Runge-Kutta method
def rk4(f,h,y0,v0,xn,x0):
    n=int((xn-x0)/h)
    dx=h
    #solve for dy/dx=v
    def f1(x,v):
        return v
    for i in range (n):
        k11=h*(f(x0, y0,v0))
        k21=h*(f1(x0, v0))
        k12=h*(f((x0+h/2), (y0+k11/2),v0))
        k22=h*(f1((x0+h/2),v0))
        k13=h*(f((x0+h/2), (y0+k12/2),v0))
        k23=h*(f1((x0+h/2),v0))
        k14=h*(f((x0+h), (y0+k13),v0))
        k24=h*(f1((x0+h),v0))
        vn=v0+(k11+2*k12+2*k13+k14)/6
        yn=y0+(k21+2*k22+2*k23+k24)/6
        print('%.5f\t%.5f\t' % (x0, y0))
        y0=yn
        x0=x0+dx
        v0=vn
    return yn







