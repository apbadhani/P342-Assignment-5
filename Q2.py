from newlib import*
coeffs = [1, -3, -7, 27, -18]
a = 1.5 #initial guess
#Call the polynomial solving function that returns list of roots
sol=polysol(coeffs, a)
print("The roots of the polynomial are:")
print(sol)