''' This script is designed to plot four different graphs, one for each 
gene describing the canopy profile for each allele
'''
import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 
from matplotlib import gridspec

# Input raw data
df = pd.read_csv("C:\\users\\john\\canopy_model\\rfr_allele.csv")
par = pd.read_csv("C:\\users\\john\\google drive\\modelling\\par.csv")
daily_par = pd.read_csv("C:\\users\\john\\canopy_model\\daily_par_allele.csv")
del df["Unnamed: 0"]
del daily_par["Unnamed: 0"]

def graph_one():
	tt = [x for x in xrange(0, 3001)]
	i = 2
	x_list = [x for x in xrange(0, 330)]
	y_list = [(7 + x) for x in xrange(0, 330)]
	# Plot on ax1
	fig = plt.figure(figsize=(8, 16))
	pos = df.loc[i]
	neg = df.loc[(i + 1)]	
	ax1 = plt.subplot2grid((2, 2), (0, 0), colspan=2)
	ax1.plot(tt, pos, 'r-', label="Ppd-D1a")
	ax1.plot(tt, neg, 'r--', label="Ppd-D1b")
	ax1.set_xlabel("Thermal time")
	ax1.set_ylabel("R:FR")
	ax1.legend(loc="upper left")
	ax1.yaxis.grid(color='gray', linestyle='--')
	ax1.xaxis.grid(color='gray', linestyle='--')
	ax1.autoscale(enable=True, tight=True, axis=x)
	# Plot on ax2
	ax2_y = daily_par.loc[i]
	ax2_x = par["tt"][0:len(ax2_y)]
	ax2 = plt.subplot2grid((2, 2), (1, 0), colspan=1)
	ax2.set_xlabel("Thermal time")
	ax2.set_ylabel("PAR interception")
	ax2.bar(ax2_x, ax2_y)
	ax2.autoscale(enable=True, tight=True)
	# Plot on ax3
	ax3_y = daily_par.loc[(i + 1)]
	ax3_x = par["tt"][0:len(ax3_y)]
	ax3 = plt.subplot2grid((2, 2), (1, 1), colspan=1)
	ax3.set_xlabel("Thermal time")
	ax3.set_ylabel("PAR interception")
	ax3.bar(ax3_x, ax3_y)
	ax3.autoscale(enable=True, tight=True)
	plt.show()
	#plt.savefig(fname=("C:\\users\\john\\google drive\\thesis\\chapter 3\\chapter 3 data\\results_ppd_comparison.png")
	#	, dpi=None, facecolor='w', orientation='portrait', transparent=True)


graph_one()	
