# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 15:13:28 2019

@author: 15145
"""

from matplotlib import pyplot
import numpy as np

t = np.arange(0.01, 5.0, 0.01)
s1 = np.sin(2*np.pi*t)
s2 = np.exp(-t)

pyplot.subplot(2,1,1)
pyplot.plot(t,s1,color="red")


pyplot.subplot(2,1,2)
pyplot.plot(t,s2,color="blue")