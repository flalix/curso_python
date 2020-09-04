
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


# In[ ]:


#--- Fibonacci --------- http://www-personal.umich.edu/~mejn/computational-physics/
f1,f2 = 1,1
x = [1]
y = [0]
posx = x; posy = y

count = 0

while f2<6:
            
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

print(f1, f2)
plt.plot(x, y)
plt.show()


