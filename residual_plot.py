''' This script is designed to plot a line showing the canopy profile
across the season along with the observed R:FR values and the 
predicted R:FR values.
'''
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

rfr = pd.read_csv("C:\\users\\john\\canopy_model\\rfr.csv", na_values=["NaN", "*"])
rfr.index = rfr[(rfr.columns[0])]
df = pd.read_csv("C:\\users\\john\\google drive\\modelling\\raw.csv")
del rfr[(rfr.columns[0])]

def plot_fig(series_predicted, series_raw, tt):
	fig = plt.figure()
	ax = fig.add_subplot(111)
	x_series = [x for x in xrange(0, 3001)]
	y_series = series_predicted
	axis_text_size = 8
	ax.plot(x_series, y_series, color='black', linestyle='--')
	ax.plot(tt, series_raw, color='black', linestyle='none',
		marker='x', markersize=8)
	ax.set_xlabel("Thermal time")
	ax.set_ylabel("R:FR")
	ax.xaxis.grid(color='gray', linestyle='-')
	ax.yaxis.grid(color='gray', linestyle='-')
	ax.tick_params(axis='both', which='major', labelsize=axis_text_size)
	plt.show()

plot_fig(rfr.loc["Plot2"], df.loc[2], df.loc[0])