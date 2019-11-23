# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 15:16:13 2019

@author: 15145
"""

import pandas
amtrack_df = pandas.read_csv(r"C:\Users\15145\Downloads\Amtrak.csv")

from matplotlib import pyplot
pyplot.plot(amtrack_df.index,amtrack_df.Ridership)
pyplot.xlabel('Period Index')
pyplot.ylabel('Ridership')
pyplot.title('Amtrack Ridership')

# Using xlim, ylim command (need to run this separately from the plot above)
pyplot.plot(amtrack_df.index,amtrack_df.Ridership)
pyplot.xlabel("Period Index")
pyplot.ylabel("Ridership")
pyplot.title("Amtrack Ridership")
pyplot.xlim([1,12])
pyplot.ylim([1500,2100])


# Using axis command (need to run this separately from the two plots above)
pyplot.plot(amtrack_df.index,amtrack_df.Ridership)
pyplot.xlabel("Period Index")
pyplot.ylabel("Ridership")
pyplot.title("Amtrack Ridership")
pyplot.axis([1,12,1500,2100])