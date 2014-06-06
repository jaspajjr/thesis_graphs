''' This script is designed to perform a simple OLS multiple regression
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
''''''''''''''''''''''''''''''''''''''''''''''''
# Start defining the stuff for multiple OLS regression
y = df["sen"].loc["Ren":"SRen99"]
X = pd.DataFrame(index=df.index[0:-7])
X = sm.add_constant(X, prepend=False)
y = y.dropna()
X = X.dropna()
''''''''''''''''''''''''''''''''''''''''''''''''
# Fit the model
model = sm.OLS(y, X)
results = model.fit()
