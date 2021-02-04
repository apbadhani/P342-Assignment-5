import newlib as lib
import math
import random
print("Radial Distance","     ","Avg x disp","      ","Avg y disp")
print(lib.randwalk1(100,250))
print(lib.randwalk1(100,500))
print(lib.randwalk1(100,1000))
print(lib.randwalk1(100,5000))
print(lib.randwalk1(100,10000))

#Q1 part b
#Graphs are included in the file
#Q1 part c
#Radial Distance    Avg X displacement  Avg Y displacement
#15.582163994868614, 0.31015580303117546, -3.0373968693740414       N=250
#7.828088498785958, -2.3193764581566514, -1.6760883991352302        N=500
#30.321643856075628, -3.08641537649133, -2.6587476535214245         N=1000
#130.63478045988163, 5.51572029511922, 3.3367416699081764           N=5000
#50.54390245809695, -2.063020593450617, 0.09711619835598193         N=10000
