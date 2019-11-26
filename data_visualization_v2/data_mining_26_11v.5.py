# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 15:22:50 2019

@author: 15145
"""

## Example 5 (scatterplot)

import pandas
df=pd.read_csv(r"C:\Users\15145\Downloads\ToyotaCorolla (1).csv")

# Bokeh Libraries
from bokeh.plotting import figure, show
from bokeh.io import output_file

# Output to file
### type your code here ###
output_file("C:\\Users\\15145\\Documents\\data_mining\\output.html")
# Create the figure
### type your code here ###
fig=figure(plot_height=400,plot_width=600,x_axis_label='KM',y_axis_label='Price',title="KM vs Price of car",toolbar_location='below')
# Add square representing each car
### type your code here ###
fig.square(x='KM',y='Price',source=df,color='royalblue')
# Visualize
### type your code here ###
show(fig)

# Format the tooltip
### type your code here ###

# Add the HoverTool to the figure
### type your code here ###

# Visualize
### type your code here ###