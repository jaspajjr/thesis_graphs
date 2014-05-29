''' This script is designed to plot four different graphs, one for each 
gene describing the canopy profile for each allele
'''
import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 
from matplotlib import gridspec

# Input raw data
df = pd.read_csv("C:\\users\\john\\canopy_model\\rfr_allele.csv")

del df["Unnamed: 0"]

tt = [x for x in xrange(0, 3001)]

def graph_one():
	tt = [x for x in xrange(0, 3001)]
	i = 2
	x_list = [x for x in xrange(0, 330)]
	y_list = [(7 + x) for x in xrange(0, 330)]
	fig = plt.figure(figsize=(8, 16))
	pos = df.loc[i]
	neg = df.loc[(i + 1)]	
	ax1 = plt.subplot2grid((2, 2), (0, 0), colspan=2)
	ax1.plot(tt, pos, 'r-')
	ax1.plot(tt, neg, 'r--')
	ax2 = plt.subplot2grid((2, 2), (1, 0), colspan=1)
	ax2.plot(x_list, y_list, color='green', linestyle='-')
	ax3 = plt.subplot2grid((2, 2), (1, 1), colspan=1)
	ax3.plot(x_list, y_list, color='orange', linestyle='-')
	plt.show()

graph_one()	
