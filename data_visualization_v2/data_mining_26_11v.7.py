# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 15:46:54 2019

@author: 15145
"""

import pandas as pd 
df=pd.read_csv(r"C:\Users\15145\Downloads\ToyotaCorolla (1).csv")
tab=df.groupby('Doors').count().iloc[:,0:1]
output_file("C:\\Users\\15145\\Documents\\data_mining\\output.html")
p=figure(plot_width=400,plot_height=400)
p.vbar(x=tab.index,width=.5,left=0,right=tab.Id,color='navy')
show(p)

p=figure(plot_width=400,plot_height=400)
p.hbar(x=tab.index,width=.5,left=0,right=tab.Id,color='navy')
show(p)
