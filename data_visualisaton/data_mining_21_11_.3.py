# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 15:03:36 2019

@author: 15145
"""

## Example 4 (Bar Chart)

label = ['Adventure', 'Action', 'Drama', 'Comedy']
num_movies = [941, 854, 4595, 2125]

import numpy
index = numpy.arange(len(label))

# Vertical bar chart
### type your code here ###
pyplot.bar(index,num_movies)
pyplot.ylabel('number of movies')
pyplot.xticks(index,label)
pyplot.title('number of movies released 1995-2017')


# Horizontla bar chart (need to be run separately from the vertical bar chart)
### type your code here ###
pyplot.bar(index,num_movies)
pyplot.xlabel('number of movies')
pyplot.yticks(index,label)
pyplot.title('number of movies released 1995-2017')


# Two vertical bar chart together (need to be run separately from the two charts above)
### type your code here ###
bar_width=.35
num_movies_china=[300,1021,2345,2004]
pyplot.bar(index,num_movies,bar_width,color='blue',label='USA')
pyplot.bar(index+bar_width,num_movies_china,bar_width,color='red',label='china')
pyplot.xlabel("numebr of movies")
pyplot.ylabel(index+bar_width,label)
pyplot.title('number of movies released from 1995-2017')
