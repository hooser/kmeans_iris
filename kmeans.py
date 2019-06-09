from dataproc import *
import random
import math
import numpy as np 

def get_init_centers(df):                      #选取算法开始的三个中心点
	points_num = 0
	dots = []
	centers = []
	while points_num < 3:
		i = random.randint(0,150)
		points_num = points_num + 1
		centers.append(list(df.loc[i][0:4]))
	return centers	

def distance(df,centers):                      #计算每个点到三个中心点的距离
	dist = []                                  
	dist_c = []                                
	for i in range(len(df)):
		for j in range(3):
			d = round(math.pow(df['sepal_length'][i]-centers[j][0],2) + math.pow(df['sepal_width'][i]-centers[j][1],2) + \
			math.pow(df['petal_length'][i]-centers[j][2],2) + math.pow(df['petal_width'][i]-centers[j][3],2) ,4)
			dist_c.append(d)
		dist.append(dist_c)
		dist_c = []
	return dist

def kinds(df,dist):                            #确定每个点的类别
	df['species'] = np.argmin(dist,axis=1)
	return df

def get_rest_centers(df):                      #确定从第二次开始的中心点
	dots_num = [0,0,0]     #记录三类点的数目
	dots_data = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]  #记录三类点的四个属性的值 
	for i in range(len(df)):
		dots_num[df['species'][i]] = dots_num[df['species'][i]] + 1
		dots_data[df['species'][i]][0] = dots_data[df['species'][i]][0] + df['sepal_length'][i]
		dots_data[df['species'][i]][1] = dots_data[df['species'][i]][1] + df['sepal_width'][i]
		dots_data[df['species'][i]][2] = dots_data[df['species'][i]][2] + df['petal_length'][i]
		dots_data[df['species'][i]][3] = dots_data[df['species'][i]][3] + df['petal_width'][i]
	new_centers = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
	for j in range(3):    #3个聚类中心
		for k in range(4):
			new_centers[j][k] = round(dots_data[j][k] / dots_num[j] , 2)
	return new_centers

def disorder(df,times_):                           #df乱序处理,打乱次数为times
	for t in range(times_):
		a = random.randint(0,149)
		b = random.randint(0,149)
		temp = []
		temp = df.iloc[a]
		df.iloc[a] = df.iloc[b]
		df.iloc[b] = temp
	return df

def cal(df2,times_):                # 输入为乱序处理后的df2
	init_centers = get_init_centers(df2)   #初始聚类中心
	dist = distance(df2,init_centers)
	last_centers = init_centers
	temp = kinds(df2,dist)
	new_centers = get_rest_centers(temp)
    
	for _ in range(times_):
		if last_centers == new_centers:
			return temp
		else:
			last_centers = new_centers
			new_centers = get_rest_centers(temp)
			dist = distance(temp,new_centers)
			temp = kinds(temp,dist)
	return temp


if __name__ == '__main__':
	df = pd.read_csv('iris.csv',delimiter=',')    #读取iris.csv到df
	df1 = species_to_num(df)
	#print(df1)
	#print_fig(df1,'original dots')
	cishu = 200000
	df2 = disorder(df1,100)
	df3 = cal(df2,cishu)
	#print(df3)
	print_fig(df3,'classified',cishu)
