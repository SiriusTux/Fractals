#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from time import time

def timer(func):
	## Time decorator ##
	def f(*arg, **kwargs):
		start = time()
		ans = func(*arg, **kwargs)
		end = time()
		print('Elapsed time: {:.2} sec'.format(end - start))
		return ans
	return f

'''def initialyzeimage(x_p, y_p):
	## Gives back a xp x yp zero matrix 
	image = []
	for j in range(y_p):
		x_colors = []
		for i in range(x_p):
			x_colors.append(0)
		image.append(x_colors)
	return image'''