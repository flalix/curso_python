
# coding: utf-8

# In[3]:


# from pylab import plot, show
from numpy import linspace, sin
import matplotlib.pyplot as plt

N = 1000
x = linspace(0,10,N)
y = sin(x)
plt.plot(x,y)
plt.show()


# In[11]:


from numpy import random
mu = 0
sigma = .1
noise = random.normal(mu, sigma, N)

plt.plot(x,(y+noise))
plt.show()


# In[10]:


len(y+noise)

