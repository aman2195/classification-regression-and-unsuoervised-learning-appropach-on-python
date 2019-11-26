# -*- co9ding: utf-8 -*-
"""
Created on Tue Nov 26 15:33:55 2019

@author: 15145
"""

## Example 6 (histogram)

import pandas as pd
### type your code here ###
df=pd.read_csv(r"C:\Users\15145\Downloads\ToyotaCorolla (1).csv")

# create a table for histogram

import numpy
df['Price'].describe()
### type your code here ###
arr_hist=numpy.histogram(df["Price"],bins=int((32500-4350)/1000),range=[4350,32500])
# Put the information in a dataframe
### type your code here ###
price=pd.DataFrame({'arr_price':arr_hist,'left': edges[:-1],'right':edges[1:]})
# Create the blank plot
from bokeh.plotting import figure
### type your code here ###
p=figure(plot_height=600,plot_width=600,title='histogram of prices',x_axis_label='Price',y_axis_label='Inventory')
# Add a quad glyph
### type your code here ###
p.quad(bottom=0,top=prices['arr_prices'],left=prices['left'],right=prices['right'],fill_color='red',line_color='black')
# Show the plot
from bokeh.io import show, output_file
### type your code here ###
output_file("C:\\Users\\15145\\Documents\\data_mining\\output.html")
show(p)