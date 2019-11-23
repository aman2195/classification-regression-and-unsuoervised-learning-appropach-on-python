# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 14:48:41 2019

@author: 15145
"""

## Example 1 (Scatter Plot)

from sklearn import datasets

iris = datasets.load_iris()
X = iris.data[:,:2]

from matplotlib import pyplot

pyplot.xlabel("Sepal Length")

pyplot.ylabel("Sepal Width")

pyplot.title("Scatter Plot of Iris Dataset")
pyplot.scatter(X[0:50,0],X[0:50,1],color="blue",label="Iris Sentosa")
pyplot.scatter(X[50:100,0],X[50:100,1],color="red",label="Iris Versicolor")
pyplot.scatter(X[100:150,0],X[100:150,1],color="green",label="Iris Verginica")
pyplot.legend(loc="upper right")

