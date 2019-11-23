# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 15:01:14 2019

@author: 15145
"""

from sklearn import datasets

boston = datasets.load_boston()

from matplotlib import pyplot
### type your code here ###
pyplot.hist(boston.target,edgecolor='black')
pyplot.xlabel("price($1000s)")
pyplot.ylabel("count")
pyplot.title('boston housing price')