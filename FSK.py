
# coding: utf-8

# In[1]:

import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# In[2]:

v = [0,1,1,0,1,1,0,0,1,1,0]


# In[3]:

dim=100
vx = []


# In[6]:

for i in range(1,11):
    f = np.ones(dim)
    x = f*v[i]
    vx = np.concatenate((vx,x))


# In[7]:

plt.subplot(3,1,1)
plt.plot(vx)


# In[8]:

t = np.linspace(0,5,len(vx))
f1 = 2
f2 = 5
w1 = 2*np.pi*f1
w2 = 2*np.pi*f2
y1 = np.cos(w1*t*2)
y2 = np.cos(w2*t*2)
plt.subplot(2,1,1)
plt.plot(t,y1)
plt.subplot(2,1,2)
plt.plot(t,y2)


# In[9]:

mi = []
for i in range(0,len(vx)):
    if vx[i] == 0:
        zero = np.array([y1[i]])
        mi = np.concatenate((mi,zero))
    else:
        one = np.array([y2[i]])
        mi = np.concatenate((mi,one))


# In[11]:

plt.subplot(3,1,1)
plt.plot(t,mi)


# In[ ]:




# In[ ]:



