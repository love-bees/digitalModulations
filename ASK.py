
#ASK amplitude shift keying
import numpy as np
import matplotlib.pyplot as plt

#sample information that needs to be modulated
v = [0,1,1,0,1,1,0,0,1,1,0]

dim = 100
vx = []

for i in range (1,11):
    f = np.ones(dim)
    x = f*v[i]
    vx = np.concatenate((vx,x))

plt.subplot(3,1,1)
plt.plot(vx)
plt.show()

#carrier of information

plt.subplot(3,1,2)
t = np.linspace(0,2,len(vx))
f = 5
w = 2*np.pi*f
y = np.cos(w*2*t)
plt.plot(t,y)
plt.show()

#modulated information

plt.subplot(3,1,3)
mult = vx*y
plt.plot(t,mult)
plt.show()




