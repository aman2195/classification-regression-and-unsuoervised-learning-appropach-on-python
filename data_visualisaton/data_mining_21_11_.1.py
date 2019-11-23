# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 14:55:42 2019

@author: 15145
"""

year = [1960, 1970, 1980, 1990, 2000, 2010]
population_pakistan = [44.91, 58.09, 78.07, 107.7, 138.5, 170.6]
population_india = [449.48, 553.57, 696.783, 870.133, 1000.4, 1309.1]

from matplotlib import pyplot
pyplot.plot(year,population_pakistan,color='red',label='Pakistan')
pyplot.plot(year,population_india,color='blue',label='india')
pyplot.xlabel('Year')
pyplot.xlabel('population in million')
pyplot.title("pakistan & india population between 1960-2010")
pyplot.legend(loc='upper right')


