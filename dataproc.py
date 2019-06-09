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
	num = [0,0,0]
	sum_x = [0,0,0]
	sum_y = [0,0,0]
	for i in range(len(df)):
		if df['species'][i] == 0:        # 第一类点
			x[0].append(df['sepal_length'][i])
			y[0].append(df['sepal_width'][i])
			num[0] = num[0] + 1
			sum_x[0] = sum_x[0] + df['sepal_length'][i]
			sum_y[0] = sum_y[0] + df['sepal_width'][i]
		elif df['species'][i] == 1:        # 第二类点
			x[1].append(df['sepal_length'][i])
			y[1].append(df['sepal_width'][i])
			num[1] = num[1] + 1
			sum_x[1] = sum_x[1] + df['sepal_length'][i]
			sum_y[1] = sum_y[1] + df['sepal_width'][i]
		else:
			x[2].append(df['sepal_length'][i])
			y[2].append(df['sepal_width'][i])
			num[2] = num[2] + 1
			sum_x[2] = sum_x[2] + df['sepal_length'][i]
			sum_y[2] = sum_y[2] + df['sepal_width'][i]

	mean_x_0 = [0,0,0]
	mean_y_0 = [0,0,0]

	for i in range(3):
		mean_x_0[i] = sum_x[i] / num[i]
		mean_y_0[i] = sum_y[i] / num[i]

	max_x = np.argmax(mean_x_0,0) 
	subpos = [0,1,2]
	del subpos[max_x]

	fig = plt.figure()
	ax1 = fig.add_subplot(111)
	plt.xlabel('sepal_length')
	plt.ylabel('sepal_width')
	if not times_ == 0:
		ax1.set_title(s+str(times_))
	else:
		ax1.set_title('original dots')

	if mean_y_0[subpos[0]] > mean_y_0[subpos[1]]:
		plt.scatter(x[subpos[0]],y[subpos[0]],c=['r'])
		plt.scatter(x[subpos[1]],y[subpos[1]],c=['g'])
	else:
		plt.scatter(x[subpos[0]],y[subpos[0]],c=['g'])
		plt.scatter(x[subpos[1]],y[subpos[1]],c=['r'])

	plt.scatter(x[max_x],y[max_x],c=['b'])
	plt.show()


	
