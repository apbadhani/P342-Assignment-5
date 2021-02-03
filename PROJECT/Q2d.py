import newlib as lib
#defining the ellipsoid function
def f(x,y,z):
    return (x/1)**2 + ((y/1.5)**2) + ((z/2)**2)
#calculated value of the volume of ellipsoid
#Loop was used for the data in the graph but not shown here
aval = 12.56637
vol=0
frac=0
N=50000
vol,frac=lib.montecarlo3d(1,1.5,2,f,N,aval)
#printing Volume of ellipsoid and absolute error
print("\nVolume of ellipsoid =",vol)
print("\nFractional Error =",frac)

#Volume of ellipsoid = 12.56544

#Fractional Error = 0.0009299999999985432
