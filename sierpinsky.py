#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import matplotlib.pyplot as plt

def transformation1(point):
	x, y = point
	x_new = 0.5*x
	y_new = 0.5*y
	return x_new, y_new

def transformation2(point):
	x, y = point
	x_new = 0.5*x + 0.5
	y_new = 0.5*y + 0.5
	return x_new, y_new

def transformation3(point):
	x, y = point
	x_new = 0.5*x + 1
	y_new = 0.5*y
	return x_new, y_new	

def get_index(probability):
	c_probability = 0
	sum_probability = []
	for p in probability:
		c_probability += p
		sum_probability.append(c_probability)
	r = random.random()
	for item, sp in enumerate(sum_probability):
		if r <= sp:
			return item

def transform(point):
	transformations = [transformation1, transformation2, transformation3]
	probability = [1/3., 1/3., 1/3.]
	tindex = get_index(probability)
	t = transformations[tindex]
	x, y = t(point)
	return x,y

def draw_sierpinsky1(n):
	x = [0]
	y = [0]
	x1, y1 = 0, 0
	for i in range(n):
		x1, y1 = transform((x1, y1))
		x.append(x1)
		y.append(y1)
	return x, y


if __name__ == '__main__':
	n = int(input('Enter the number of points in the Sierpinsky Triangle: '))
	x, y = draw_sierpinsky1(n)
	# Plot points
	plt.plot(x, y, 'o', markersize=0.5)
	plt.title('Sierpinsky Triangle with {} points'.format(n))
	plt.show()
