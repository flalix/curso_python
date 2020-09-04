
# coding: utf-8

# In[1]:


#-- https://python-graph-gallery.com/

import matplotlib.pyplot as plt
import numpy as np

a = np.random.random((16, 16))
plt.imshow(a, cmap='hot', interpolation='nearest')
plt.show()

