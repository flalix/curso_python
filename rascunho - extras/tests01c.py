
# coding: utf-8

# In[30]:


# from pylab import plot, show
from numpy import linspace, sin
import matplotlib.pyplot as plt

N = 1000
x = linspace(0,10,N)
y = sin(x)
plt.plot(x,y)
plt.show()


# In[9]:





# In[31]:


from numpy import random
mu = 0
sigma = .1
noise = random.normal(mu, sigma, N)

plot(x,y+noise)
show()


# In[40]:


import matplotlib.pyplot as plt
import numpy as np
#-- deltoid curve - pag 98
#-- https://matplotlib.org/users/mathtext.html

N= 1000
theta = np.array( linspace(0,2*np.pi,N) )
# print(type(theta))


x = 2*np.cos(theta) + np.cos(2*theta)
y = 2*np.sin(theta) - np.sin(2*theta)

plt.plot(x,y)
plt.xlabel(r'$2cos(\theta) + cos(2\theta)$')
plt.ylabel(r"$2sin(\theta) - sin(2\theta)$")
plt.title('Deltoid curve')
plt.show()



# In[47]:


import matplotlib.pyplot as plt
import numpy as np
#-- scatter plot

N= 100
mu = 0.1; sigma=3
noise = random.normal(mu, sigma, N)
x = linspace(0,100,N)
y = 2*x + noise

plt.plot(x,y, "k.")
plt.xlabel('x')
plt.ylabel("y")
plt.title('Scatter plot')
plt.show()


# In[49]:


#--- even / odd --------- http://www-personal.umich.edu/~mejn/computational-physics/
print("Enter two integers, one even, one odd.")
m = int(input("Enter the first integer: "))
n = int(input("Enter the second integer: "))
while (m+n)%2==0:
    print("One must be even and the other odd.")
    m = int(input("Enter the first integer: "))
    n = int(input("Enter the second integer: "))
print("The numbers you chose are",m,"and",n)


# In[14]:


#--- Fibonacci --------- http://www-personal.umich.edu/~mejn/computational-physics/
import matplotlib.lines as mlines
import matplotlib.pyplot as plt

# ax = plt.gca()

ax = plt.subplot(111)
#ax.scatter([1, 2], [3, 4])
limit = 30
ax.set_xlim([-limit, limit])
ax.set_ylim([-limit, limit])

f1,f2 = 1,1
x = [1]
y = [0]
posx = x[0]; posy = y[0]

count = 0

xmin = 0
xmax = posx
ymin = 0
ymax = posy

l = mlines.Line2D([xmin,xmax], [ymin,ymax])
ax.add_line(l)
    
while f2<limit:
            
    f1,f2 = f2,f1+f2
    count += 1
    
    if count == 1:
        posy = posy + f2
    elif count == 2:
        posx -= f2
    elif count == 3:
        posy -= f2
    else:
        count = 0
        posx += f2

    x.append(posx)
    y.append(posy)
    
    xmin = xmax
    ymin = ymax
    xmax = posx
    ymax = posy

    l = mlines.Line2D([xmin,xmax], [ymin,ymax])
    ax.add_line(l)

plt.show()


