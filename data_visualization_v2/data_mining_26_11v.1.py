# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 14:55:46 2019

@author: 15145
"""

## Example 2 (distplot)

import pandas as pd

df=pd.read_csv(r"C:\Users\15145\Downloads\ToyotaCorolla (1).csv")
X = df['Weight']

import seaborn

# Basic distribution plot (X has to be a 1-dimension array, series, or list)
seaborn.distplot(X)
### type your code here ###

# Plot with a normal distribution, without the kernel density estimate plot

from scipy.stats import norm
### type your code here ###
seaborn.distplot(X,fit=norm,kde=False)
# Change the orientation

### type your code here ###
seaborn.distplot(X,vertical=True)
# Change the color
seaborn.distplot(X,color="red")

### type your code here ###