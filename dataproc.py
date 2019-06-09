import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np 
import random

def species_to_num(df):                       #对类别进行labelencode
	for i in range(len(df)):
		if df['species'][i] == 'setosa':
			df['species'][i] = 0
		elif df['species'][i] == 'versicolor':
			df['species'][i] = 1
		else:
			df['species'][i] = 2
	return df

def print_fig(df,s,times_):
	x = [[],[],[]]
	y = [[],[],[]]
	for i in range(len(df)):
		if df['species'][i] == 0:        # 第一类点
			x[0].append(df['sepal_length'][i])
			y[0].append(df['sepal_width'][i])
		elif df['species'][i] == 1:        # 第二类点
			x[1].append(df['sepal_length'][i])
			y[1].append(df['sepal_width'][i])
		else:
			x[2].append(df['sepal_length'][i])
			y[2].append(df['sepal_width'][i])
	fig = plt.figure()
	ax1 = fig.add_subplot(111)
	if not times_ == 0:
		ax1.set_title(s+str(times_))
	else:
		ax1.set_title('original dots')
	#print('coount = ',coount)
	plt.xlabel('sepal_length')
	plt.ylabel('sepal_width')
	plt.scatter(x[0],y[0],c=['r'])
	plt.scatter(x[1],y[1],c=['g'])
	plt.scatter(x[2],y[2],c=['b'])
	plt.show()


	
