"""
David Nnaji
4/12/2020
ENGR 501
Project 2


		if names[k]=='Sex':
			vals = df.groupby('Sex').count()['Length'].to_numpy()
			axes1[i,j].plot(['F','I','M'],vals,'+',fillstyle='none',color=colors[k])
			axes1[i,j].set_ylim(0,1750)
		else:

"""

#Libraries
from math import *
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Gather all the data to one place (Source: http://mlr.cs.umass.edu/ml/machine-learning-databases/abalone/abalone.data)
names=[
	"Sex",
	"Length",
	"Diameter",
	"Height",
	"Whole",
	"Shucked",
	"Viscera",
	"Shell",
	"Rings"]
raw_data = pd.read_csv("abalone_data.csv",delimiter=",",names=names)

#Create a safe copy of the raw data to work with.
df = raw_data.copy()

#Remove Stange (Discovered while coding)
df = df[(df.Height<0.3)&(df.Height>0.0)]
df = df.drop(df.index[800:2100])
df = df.reset_index()

#Create Age Column
df['Age'] = df['Rings']+1.5
names.append("Age")

print()

#Get the big picture! Broadly visulaize the data
#Create scatter plots of all the factors
fig1, axes1 = plt.subplots(2, 5, figsize=(17, 6))
fig1.tight_layout(pad=3, w_pad=1, h_pad=3)
colors = 'rgbyrgbymm'
k=0
for i in range(2):
	for j in range(5):
		if names[k]=='Sex':
			axes1[i,j].plot(df[names[k]],'+',fillstyle='none',color=colors[k],markersize=1)
			axes1[i,j].set_title('{} Scatter Plot'.format(names[k]))
		else:
			axes1[i,j].plot(df[names[k]],'+',fillstyle='none',color=colors[k],markersize=1)
			axes1[i,j].set_title('{} Scatter Plot (μ={:.2f}±{:.2f})'.format(names[k],df[names[k]].mean(),df[names[k]].std()))
		k+=1

#Create histograms for all variables
fig2, axes2 = plt.subplots(2, 5, figsize=(17, 6))
fig2.tight_layout(pad=3, w_pad=1, h_pad=3)
k=0
for i in range(2):
	for j in range(5):
		axes2[i,j].hist(df[names[k]],bins=50,color=colors[k])
		axes2[i,j].set_title('{} Histogram'.format(names[k]))
		k+=1



#Explore Relationships!
#Relationship between Sex and Rings
fig3, axes3 = plt.subplots(2, 4, figsize=(14, 6),sharey=True)
fig3.tight_layout(pad=3, w_pad=1, h_pad=3)
k=0
for i in range(2):
	for j in range(4):
		if names[k]=='Sex':
			M_lst = df[df['Sex']=='M']['Age']
			F_lst = df[df['Sex']=='F']['Age']
			I_lst = df[df['Sex']=='I']['Age']
			axes3[i,j].boxplot([M_lst,F_lst,I_lst],labels=["M","F","I"],medianprops=dict(color=colors[k]),showfliers=False)
			axes3[i,j].set_title('{} Boxplot'.format(names[k]))
			axes3[i,j].grid(linestyle='--', linewidth=1,alpha=0.5)
			axes3[i,j].set_ylim(0,25)
		else:
			l_mean = df[df[names[k]]<df[names[k]].mean()]['Age'].to_numpy()
			g_mean = df[df[names[k]]>df[names[k]].mean()]['Age'].to_numpy()
			axes3[i,j].boxplot([l_mean,g_mean],medianprops=dict(color=colors[k]),labels=["<μ",">μ"],showfliers=False)
			axes3[i,j].set_title('{} Binary Boxplot'.format(names[k]))
			axes3[i,j].grid(linestyle='--', linewidth=1,alpha=0.5)
		k+=1
plt.show()
