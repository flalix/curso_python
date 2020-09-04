
# coding: utf-8

# In[8]:


from pylab import plot, show
from numpy import linspace, sin

N = 1000
x = linspace(0,10,N)


# In[9]:


y = sin(x)
plot(x,y)
show()


# In[13]:


from numpy import random
mu = 0
sigma = .1
noise = random.normal(mu, sigma, N)

plot(x,y+noise)
show()

