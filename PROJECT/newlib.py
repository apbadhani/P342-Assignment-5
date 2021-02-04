import math                                     #for base e
import random                                   #for random function
#function for matrix multiplication
def matrixmultiply(A,B):
    n=len(A)
    prod=[[] for x in range(n)]
    t=0
    for i in range(n):
        for j in range(n):
            for sum in range(n):
                t+=A[i][sum]*B[sum][j]
            prod[i].append(t)
            t=0
        j=0
    return prod
#read from file
def readfile(f1):
    a = f1.read()
    a1 = [item.split(" ") for item in a.split('\n')]
    A = []
    for i in range(len(a1)):
        row = []
        for j in range(len(a1[0])):
            row.append(0)
        A.append(row)
    for i in range(len(a1)):
        for k in range(len(a1[0])):
            A[i][k] = a1[i][k]
    return A
#First derivative
def der1(f,x,h=0.0002):
    return ((f(x + h) - f(x - h))/(2*h))
#Bracketing function
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
#Bisection Function
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
#Regular Falsi method
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
#Newton-Raphson method
def newrap(x,f,N,question,p):
    file = open("newt"+ str(question)+".txt", "w+")
    n = 1
    y = der1(f, x)
    h = f(x)/y
    #print("Iteration  Error")
    while (abs(h) >= p) and n<N:
        #print(n,"        ", abs(h))
        file.writelines([str(n)+"   ",str(abs(h))+"\n"])
        x -= h
        h = f(x)/der1(f, x)
        n+=1
    file.close()
    return(x)
#Second Derivative
def der2(f,a,h=0.0002):
    return ((f(x + h) - 2*f(x) + f(x - h))/(2*h*h))
#Gives Polynomial
def polynomial(x,A = []):
    y = 0
    for i in range(0,len(A)):
        y += A[i]*pow(x,(len(A)-(i+1)))
    return y
#Laguerre method
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
#Synthetic Division
def syndiv(coeffs, root):
    n = len(coeffs)
    #initiate list with the same first element
    new_coeffs = []
    new_coeffs.append(coeffs[0])
    for i in range(1, n):
        new_coeffs.append(new_coeffs[i-1]*root+coeffs[i])
    return new_coeffs[:-1]
#Finding roots
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
        n = random.uniform(a,b)                #random number generator function
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

# Runge-Kutta method order 4
def RK4(x,y,v,h,r,f1,f2):
    #Values stored in arrays
    X=[]
    Y=[]
    #Calculate when x less than range
    while x <= r:
        k1 = h*f1(v)
        l1 = h*f2(x,y,v)

        k2 = h * f1(v+l1/2)
        l2 = h * f2(x+h/2,y+k1/2, v+l1/2)

        k3 = h * f1(v + l2 / 2)
        l3 = h * f2(x + h / 2, y + k2 / 2, v + l2 / 2)

        k4 = h * f1(v + l3)
        l4 = h * f2(x + h, y + k3, v + l3)
        #Calculate for y and v i.e z for next iteration
        y = y + 1/6*(k1+2*k2+2*k3+k4)
        v = v + 1/6*(l1+2*l2+2*l3+l4)
        x = x + h
        X.append(x)
        Y.append(y)
    return X,Y
#Shooting Method
#zl,zh=guesses
def ShootingMethod(fy, fz, x, xlimit, y, yn, zl, zh, h):
    z0 = zl
    for i in range(50):
        y_el, xl = RK4(x, y, z0 ,h,xlimit,fy,fz)
        if abs(y_el - yn) < 10 ** (-6):
            return y_el,z0
        else:
            z0 = zh
            y_eh, xh = RK4(x, y, z0,h,xlimit,fy,fz)
            if abs(y_eh - yn) < 10 ** (-6):
                return y_eh,z0
            elif y_el < yn and yn < y_eh:
                z0 = zl + (zh - zl) * (yn - y_el) / (y_eh - y_el)
            elif y_eh < yn and yn < y_el:
                z0 = zh + (zl - zh) * (yn - y_eh) / (y_el - y_eh)
            else:
                print("choose differnt values of z(%.0f)"%(x))
                return None,None

#Monte Carlo for 3-dimension
#takes input-dimensions of box,function,analytic value
def montecarlo3d(a,b,c,f, N,val):
    X = []                                          #Initiaizing
    Y = []
    Z = []
#volume of the box
    vol_box = 8*a*b*c
    elvol = 0
    count = 0
    for i in range(N):
        x = random.uniform(-a,a)                    #random values from -a to a
        y = random.uniform(-b,b)
        z = random.uniform(-c,c)
#Condition that point lie inside or outside
        if (f(x, y, z) < 1):
            X.append(x)                             #x,y,z values were used for the ellipsoid plot
            Y.append(y)
            Z.append(z)
            count = count + 1
    elvol = vol_box * count/N                      #count/N is a probability function
    fracerr = abs(elvol - val)/val
    return elvol,fracerr*val


#For Plots of part B, extra commands were used but not shown in the main library
#Random Walk function takes two input- no of walks, no of steps
def randwalk1(N, n):
    pi = 3.14
    R = []
    for k in range(N):
        x = 0
        y = 0
        X = []
        Y = []
        i = 0
        while i < n + 1:
            X.append(x)
            Y.append(y)
            angle = random.uniform(0, 2 * pi)
            x = x + math.cos(angle)
            y = y + math.sin(angle)
            i = i + 1
        R.append(((X[n]) ** 2) + ((Y[n]) ** 2))

    Rrms = 0
    sum = 0
    for i in range(N):
        sum = sum + R[i] ** 2
    Rrms = math.sqrt(sum / 100)
    xsum, ysum = 0, 0
    for i in range(N):
        xsum = xsum + X[i]
        ysum = ysum + Y[i]
        r = math.sqrt(X[i] ** 2 + Y[i] ** 2)

    xavg = xsum / N
    yavg = ysum / N
    return Rrms,r,xavg,yavg                         #return rms,radial and x,y avg displacement

#Least Square Fit
def LinleastSquare(X,Y):
    n = len(X)
    x1=0;y1=0;x2=0;xy=0;y2=0
    for i in range(n):
        x1+=X[i]
        y1+=Y[i]
        x2+=pow(X[i],2)
        y2 += pow(Y[i], 2)
        xy+=X[i]*Y[i]
    x1=x1/n
    y1=y1/n
    a = ((y1*x2)-(x1*xy))/(x2-(n*pow(x1,2)))
    b = (xy - n*x1*y1)/(x2-n*pow(x1,2))
    Sxx = x2-n*pow(x1,2)
    Syy = y2-n*pow(y1,2)
    Sxy = xy-n*x1*y1
    sigmax = Sxx/n
    sigmay = Syy/n
    covxy = Sxy/n
    r2 = pow(Sxy,2)/(Sxx*Syy)
    return a,b,r2























