# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 14:59:42 2019

@author: 15145
"""

## Example 3 (boxplot)

import pandas as pd

df=pd.read_csv(r"C:\Users\15145\Downloads\ToyotaCorolla (1).csv")

import seaborn

# 1-dimension box plot
seaborn.boxplot(x="Price",data=df)
### type your code here ###
seaborn.boxplot(x="Doors",y="Price",data=df)

# 2-dimension box plot

### type your code here ###

# Changing orientation
seaborn.boxplot(x="Doors",y="Price",orient="h",data=df)

### type your code here ###

# Grouping
seaborn.boxplot(x='Doors',y='Price',data=df,hue='Automatic')
seaborn.boxplot(x='Doors',y='Price',data=df,hue='CC')
#hue----grouping f
### type your code here ###

# Drawing boxplots for all numerical variables in the dataframe
seaborn.boxplot(data=df,orient="h")

### type your code here ###

# Plotting all observations
seaborn.boxplot(x='Doors',y='Price',data=df)

seaborn.boxplot(x='Doors',y='Price',data=df,color=".1")


### type your code here ###
