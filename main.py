"""
David Nnaji
4/12/2020
ENGR 501
Project 2
"""

#Libraries
from math import *
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Gather all the data to one place (Source: http://mlr.cs.umass.edu/ml/machine-learning-databases/abalone/abalone.data)
raw_data = pd.read_csv("abalone_data.csv",delimiter=",",names=[
	"Sex",
	"Length",
	"Diameter",
	"Height","Whole",
	"Shucked",
	"Viscera",
	"Shell",
	"Rings"])

#Create a safe copy of the raw data to work with.
df = raw_data.copy()
df['Age'] = df['Rings']+1.5
for i in range(len(df)):
	if df["Sex"][i] == 'M':
		df['Coded Sex'] = 1
	elif 

print(df)

# PHASE 1: First Steps
#Get familiar with the dataset through visulaization and broad numerical analysis
#Create scatter plots of all the variables

fig1, axes1 = plt.subplots(2, 4, figsize=(6, 6))
fig1.tight_layout(pad=3, w_pad=3, h_pad=3)
