# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 15:18:01 2019

@author: 15145
"""

from sklearn import datasets

iris = datasets.load_iris()
X = iris.data[:,:2]

from matplotlib import pyplot

pyplot.xlabel("Sepal Length")
pyplot.ylabel("Sepal Width")
pyplot.title("Scatter Plot Of Iris Dataset")

pyplot.scatter(X[0:50,0],X[0:50,1],color="blue",marker="x",label="Iris Sentosa")
pyplot.scatter(X[50:100,0],X[50:100,1],color="red",marker = "o",label="Iris Versicolor")

pyplot.scatter(X[100:150,0],X[100:150,1],color="green",marker = "+",label="Iris Verginica")
pyplot.legend(loc="upper right")

pyplot.show() 