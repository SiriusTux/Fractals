#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
from decorator import timer

def initialyzeplane(n):
	ans = []
	x_vect = np.linspace(-2.5, 1.0, num=n)
	y_vect = np.linspace(-1.0, 1.0, num=n)
	for y in y_vect:
		row = []
		for x in x_vect:
			row.append((x,y))
		ans.append(row)
	return ans

@timer
def mandelbrot(plane):
	max_iteration = 1000
	image = np.zeros((len(plane), len(plane)))
	for i in range(len(plane)):
		for k in range(len(plane[i])):
			x, y = plane[i][k]
			z = complex(0., 0.)
			c = complex(x, y)
			iteration = 0
			while abs(z) < 2 and iteration < max_iteration:
				z = z*z + c
				iteration += 1
			image[i][k] = iteration
	return image

if __name__ == '__main__':
	n = 400
	plane = initialyzeplane(n)
	fig = mandelbrot(plane)
	plt.imshow(fig, extent=(-2.5,1.0,-1.0,1.0),
			cmap=cm.Greys_r, interpolation='nearest')
	plt.title('Mandelbrot Set')
	plt.colorbar()
	plt.show()


