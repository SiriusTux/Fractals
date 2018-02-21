#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import matplotlib.pyplot as plt

def transformation1(point):
	x, y = point
	x_new = 0.
	y_new = 0.16*y
	return x_new, y_new

def transformation2(point):
	x, y = point
	x_new = 0.85*x + 0.04*y
	y_new = -0.04*x + 0.85*y + 1.6
	return x_new, y_new

def transformation3(point):
	x, y = point
	x_new = 0.2*x - 0.26*y
	y_new = 0.23*x + 0.22*y + 1.6
	return x_new, y_new

def transformation4(point):
	x, y = point
	x_new = -0.15*x + 0.28*y
	y_new = 0.26*x + 0.24*y + 0.44
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
	transformations = [transformation1, transformation2, transformation3, transformation4]
	probability = [1/100., 85/100., 7/100., 7/100.]
	tindex = get_index(probability)
	t = transformations[tindex]
	x, y = t(point)
	return x,y

def draw_ferm(n):
	x = [0]
	y = [0]
	x1, y1 = 0, 0
	for i in range(n):
		x1, y1 = transform((x1, y1))
		x.append(x1)
		y.append(y1)
	return x, y


if __name__ == '__main__':
	n = int(input('Enter the number of points in the Barnsley Fern Diagram: '))
	x, y = draw_ferm(n)
	# Plot points
	plt.plot(x, y, 'o', markersize=0.5, color='green')
	plt.title('Barnsley Fern Diagram with {} points'.format(n))
	plt.show()


