# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 14:48:32 2019

@author: 15145
"""

import pandas as pd
df=pd.read_csv(r"C:\Users\15145\Downloads\ToyotaCorolla (1).csv")
import seaborn

seaborn.lmplot(x='KM',y='Price',data=df)
seaborn.lmplot(x='KM',y='Price',data=df,hue='Automatic')
seaborn.lmplot(x='KM',y='Price',data=df,hue='Doors')
seaborn.lmplot(x='KM',y='Price',data=df,col='Doors')

seaborn.lmplot(x='KM',y='Price',data=df,size=109)

seaborn.lmplot(x='KM',y='Price',data=df,aspect=1.5)

