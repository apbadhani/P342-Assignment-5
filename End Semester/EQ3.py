import newlib as lib
import math
X=[0.00,0.30,0.60,0.90,1.20,1.50,1.80,2.10,2.40,2.70,3.00,3.30]
Y=[2.20,1.96,1.72,1.53,1.36,1.22,1.10,1.00,0.86,0.75,0.65,0.60]
#PART 1
#This function for linear fitting with W(t)=Wo+Wc*t
Wo,Wc,Rs=lib.LinleastSquare(X,Y)
print("\nPART 1")
print("\nWo = ",Wo)
print("\nWc = ",Wc)
print("\nR(squared) = ",Rs)

#Wo =  2.0291025641025655
#Wc =  -0.4747086247086251
#R(squared) =  0.97053188449053

#PART 2
print("\nPART 2")

#For Fitting data  with exponential function, taking log on both sides makes it linear
#let W=Wo*exp(-Wc*t)
#Equation will be given by log(W(t)) = -Wc*t + log(K)
#Z= log(Y)
Z=[]
for i in range(12):
    Z.append(math.log(Y[i]))
w,x,y=lib.LinleastSquare(X,Z)
print("\nWo = ",math.e**w)
print("\nWc = ",-x)
print("\nR(squared) = ",y)