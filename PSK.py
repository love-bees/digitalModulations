
# coding: utf-8

# In[1]:

import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# In[2]:

v = [0,1,0,0,1,1,1,0,1,0,1]
np.shape(v)
dim = 100
vx = []


# In[3]:

for i in range(1,11):
    f = np.ones(dim)
    x = f*v[i]
    vx = np.concatenate((x,vx))


# In[16]:

plt.subplot(3,1,1)
plt.plot(vx)


# In[5]:

t = np.linspace(0,5,len(vx))
f = 2
w = 2*np.pi*f
y1 = np.cos(2*w*t)
y2 = -np.cos(2*w*t)


# In[17]:

plt.subplot(3,1,1)
plt.plot(t,y1)
plt.subplot(3,1,2)
plt.plot(t,y2)


# In[7]:

m = []
for i in range(0,len(vx)):
    if vx[i] == 0:
        zero = np.array([y2[i]])
        m = np.concatenate((m,zero))
    else:
        one = np.array([y1[i]])
        m = np.concatenate((m,one))
            


# In[19]:

plt.subplot(3,1,1)
plt.plot(t,m)


# In[ ]:



