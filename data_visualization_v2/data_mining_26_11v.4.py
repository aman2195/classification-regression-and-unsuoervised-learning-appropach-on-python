# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 15:08:28 2019

@author: 15145
"""

## Example 4 (heatmap)

# heatmap on a 10x12 table

import numpy 
import seaborn
numpy.random.seed(0)
uniform_data = numpy.random.rand(10, 12)
seaborn.heatmap(uniform_data)
### type your code here ###

# heatmap on a built-in pivot table

flights = seaborn.load_dataset("flights")
flights = flights.pivot("month", "year", "passengers")
seaborn.heatmap(flights)
### type your code here ###

# heatmap with a custom table

import pandas as pd
df=pd.read_csv(r"C:\Users\15145\Downloads\ToyotaCorolla (1).csv")

tab = pd.pivot_table(df,index="CC",columns="Doors",values="Price")
seaborn.heatmap(tab)
### type your code here ###

# heatmap with correlation

df = df.iloc[:,2:]
seaborn.heatmap(df.corr())
seaborn.heatmap(df.corr(),annot=True,linewidth=.5)
seaborn.heatmap(df.corr(),annot=True,linewidth=.5,cmap="YlGnBu")

### type your code here ###