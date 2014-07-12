''' This script is designed to plot a single scatter graph, using the 
canopy model data set that has been parsed through GENSTAT REML. 
This data is expected to include S.E and S.E.Ds
'''

import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 
from matplotlib import gridspec

# Inputs data
df = pd.read_csv("C:\\users\\john\\google drive\\thesis\\chapter 2\\chapter 2 data\\2008.csv", na_values=["*"])
df.columns = [str.lower(x) for x in df.columns]
df.index = df["line"]
del df["line"]
col_des = pd.read_csv("C:\\users\\john\\google drive\\thesis\\chapter 2\\chapter 2 data\\col_descriptions_2008.csv")
descriptions_dict = dict(zip(df.columns, col_des["Line"]))

def annotate_maker(x_series, y_series):
	annotate_list = []
	ideotypes = ["SRen76", "SRen61", "SRen103", "SRen104", "SRen4",
	"SRen51", "Ren", "Sav"]
	for i in ideotypes:
		text = i 
		x = x_series.loc[i]
		y = y_series.loc[i]
		temp = [text, x, y]
		annotate_list.append(temp)
	return annotate_list

def scatter(x_series, y_series, descriptions_dict):
	fig = plt.figure()
	ax = fig.add_subplot(111)
	axis_text_size = 8
	#x_series = x_series.dropna()
	#y_series = y_series.dropna()
	x_list = x_series.loc["Ren":"SRen99"]
	y_list = y_series.loc["Ren":"SRen99"]
	x_err = x_series.loc["S.E.D"]
	y_err = y_series.loc["S.E.D"]
	ax.plot(x_list, y_list, color='black', marker='x', linestyle='none',
		markersize=8)
	ax.set_xlabel(descriptions_dict[(x_series.name)])
	ax.set_ylabel(descriptions_dict[y_series.name])
	#ax.set_title(r'%s $\alpha \degree > \beta $' %test)
	ax.xaxis.grid(color='gray', linestyle='--')
	ax.yaxis.grid(color="gray", linestyle='--')
	ax.tick_params(axis='both', which='major', labelsize=axis_text_size)
	annotate_list = annotate_maker(x_series, y_series) 
	for text, x, y in annotate_list:
		ax.annotate(text, xy=(x, y), 
			xytext=(-40, 20), textcoords='offset points', 
			arrowprops=dict(arrowstyle="->", connectionstyle='arc3, rad=0.5',
			color='gray'), fontsize=8)
	#ax.autoscale(enable=True, tight=True, axis=x)
	''' For each graph the location of the error bar may need to change,
	use ax.errorbar to change the location of the errorbar
	'''
	ax.errorbar(x=1555, y=0.007, xerr=x_err, yerr=y_err, color='black')
	ax.set_xlim(1500, 1900)
	#ax.set_ylim(.35, .65)

	plt.show()

# '$\sqrt{x}$'
scatter(df["anth"], df["yield_fill"], descriptions_dict)