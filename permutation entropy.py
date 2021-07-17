import numpy as np
from jpype import *
import math
import random
#import matplotlib.pyplot as plt
from math import *
import cmath


with open("sampledata.dat" , 'r') as f:
	y = [line.rstrip('\n') for line in f]
#y = np.linspace(1,100 , 100)
#for z in range(0,100):
#noise = np.random.rand()
#y[z] = math.sin(z)
n=len(y)
ws=512                #window size
r=3                   # step size
nw=(n - ws +1)        #no. of windows
u=ws-r+1           # no. of steps in a window
t=np.zeros(nw+1)
H=np.zeros(nw+1)
Hp=np.zeros(nw+1)
g=open("output.dat" , 'w+')

for k in range(0,nw):
    t[k+1]=(k+ ws)/2.0
    u1=0.0
    u2=0.0
    u3=0.0
    u4=0.0
    for x in range(k,ws+k):
        if(x+1 == ws+k or x+2 == ws+k):
            break
        y[x]=(y[x])
        y[x+1]=(y[x+1])
        y[x+2]=(y[x+2])
        if(y[x]>y[x+1]>y[x+2]):
            u1=u1+1
        elif(y[x]>y[x+1]<y[x+2]):
            u2=u2+1
        elif(y[x]<y[x+1]>y[x+2]):
            u3=u3+1
        elif(y[x]<y[x+1]<y[x+2]):
            u4=u4+1
    if( k==1):
        print u1,u2,u3,u4
    if(u1==0.0):
        d1=0.0
    else:
	d1=-(u1/u)*(math.log(u1/u))
    if(u2==0.0):
	d2=0.0
    else:
        d2=-(u2/u)*(math.log(u2/u))
    if(u3 ==0.0):
        d3=0.0
    else:
        d3=-(u3/u)*(math.log(u3/u))
    if(u4==0.0):
        d4=0.0
    else:
        d4=-(u4/u)*(math.log(u4/u))
        H[k]=d1+d2+d3+d4      
#    H[k] = round(H[k] , 2)
#H[k] =   (u1/u) * (log1p(u1/u)) + (u2/u) * (log1p(u2/u)) + (u3/u) * (log1p(u3/u)) + (u4/u) * (log1p(u4/u))
    Hp[k]=H[k]/(ws-1)
#    Hp[k] = round(Hp[k] , 3)
    g.write(str(t[k+1]))
    g.write("\t")
    g.write(str(H[k]))
    g.write("\t")
    g.write(str(Hp[k]))
    g.write("\n")
g.close()

