''' Create a script to draw plots showing all of the ideotype lines,
to see if they have similar attributes
'''
import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 
from matplotlib import gridspec

# Inputs data
df = pd.read_csv("C:\\users\\john\\google drive\\thesis\\chapter 3\\chapter 3 data\\canopy_model.csv", na_values=["*"])
df.columns = [str.lower(x) for x in df.columns]
df.index = df["line"]
del df["line"]
''''''''''''''''''''''''
#line_list = 
''''''''''''''''''''''''
def generic_graph(y_series, ax):
	x_series = [x for x in xrange(0, 3001)]
	ax.plot(x_series, y_series, color='black', linestyle='-')
	ax.set_xlabel(r"Thermal time $\degree$ $C$ days")
	ax.set_ylabel("R:FR")
	ax.yaxis.grid(color='gray', linestyle='--')
	ax.xaxis.grid(color='gray', linestyle='--')
	ax.autoscale(enable=True, tight=True, axis=x)
	return ax

def graph_one():
	# ax1
	fig = plt.figure()
	ax1 = plt.subplot2grid((2, 3), (0, 0), colspan=1)
	y_series = [x for x in xrange(0, 3001)]
	ax1 = generic_graph(y_series, ax1)
	plt.show()

graph_one()
