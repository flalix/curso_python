#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 29, 2015

@author: flavio
'''
from numpy import sqrt, linspace
from scipy.stats import t
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1)

df = 2.1

alpha = .05
''' Percent point function - inverse of cdf — percentiles '''
tlim = t.ppf(alpha/2, df=df)


mean, var, skew, kurt = t.stats(df, moments='mvsk')

x = linspace(t.ppf(0.01, df), t.ppf(0.99, df), 100)
ax.plot(x, t.pdf(x, df), 'b', lw=3, alpha=0.8, label='t pdf')

plt.axvline(x=tlim, ymin=0, ymax = 0.5, linewidth=2, color='k')
plt.axvline(x=-tlim, ymin=0, ymax = 0.5, linewidth=2, color='k')

plt.show()


piA1 = 0.2590932
piA2 = 0.2739831

sdA1 = 0.01113897
sdA2 = 0.01162302

n1 = 6000 * (1.-.25)
n2 = 6000 * (1.-.25)


s2x1x2 = ((n1-1)*sdA1*sdA1 + (n2-1)*sdA2*sdA2) / (n1+n2-2.)
inv12 = (1./n1 + 1./n2)

tstat = (piA1 - piA2) / sqrt(s2x1x2 * inv12)



print 'piA standard = %f (%f) n = %i' %(piA1, sdA1, n1)
print 'piA covarion = %f (%f) n = %i' %(piA2, sdA2, n2)

print 'tstat = %f'%(tstat)
print 'tlim = %f'%(tlim)

if abs(tstat) > abs(tlim):
    print 'H0 discharged. Ha accepted tstat %f > tlim %f'%(tstat, tlim)
    print 'Probably piA(covarion) distribution is different from piA(standard) distribution'
else:
    print 'H0 cannot be discharged because tstat %f <= tlim %f'%(tstat, tlim)
    print 'Statistically piA(covarion) distribution is not different from piA(standard) distribution'
   

ll_standard = -14767.39

ll_covarion = -14329.99

