
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



# In[15]:


from math import sin,cos,pi

# Ask the user for the values of r and theta
r = float(input("Enter r: "))
d = float(input("Enter theta in degrees: "))

# Convert the angle to radians
theta = d*pi/180

# Calculate the equivalent Cartesian coordinates
x = r*cos(theta)
y = r*sin(theta)

# Print out the results
print("x = ",x,", y = ",y)


# In[17]:


#--- circular image -------------

from pylab import imshow,show
from numpy import loadtxt

data = loadtxt("C:/python/tests/circular.txt",float)
imshow(data)
show()


# In[19]:


#-- sphere - 
#-- pip install --upgrade https://github.com/vpython/visual/zipball/master

from visual import sphere
L = 5
R = 0.3
for i in range(-L,L+1):
    for j in range(-L,L+1):
        for k in range(-L,L+1):
            sphere(pos=[i,j,k],radius=R)
            
            


# In[20]:


#--- interference

from math import sqrt,sin,pi
from numpy import empty
from pylab import imshow,gray,show

wavelength = 5.0
k = 2*pi/wavelength
xi0 = 1.0
separation = 20.0      # Separation of centers in cm
side = 100.0           # Side of the square in cm
points = 500           # Number of grid points along each side
spacing = side/points  # Spacing of points in cm


# Calculate the positions of the centers of the circles
x1 = side/2 + separation/2
y1 = side/2
x2 = side/2 - separation/2
y2 = side/2

# Make an array to store the heights
xi = empty([points,points],float)

# Calculate the values in the array
for i in range(points):
    y = spacing*i
    for j in range(points):
        x = spacing*j
        r1 = sqrt((x-x1)**2+(y-y1)**2)
        r2 = sqrt((x-x2)**2+(y-y2)**2)
        xi[i,j] = xi0*sin(k*r1) + xi0*sin(k*r2)

# Make the plot
imshow(xi,origin="lower",extent=[0,side,0,side])
gray()
show()

