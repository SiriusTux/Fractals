#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
from color import initialyzeimage

def initialyzeplane(n):
	ans = []
	x_vect = np.linspace(-2., 2., num=n)
	y_vect = np.linspace(-2., 2., num=n)
	for y in y_vect:
		row = []
		for x in x_vect:
			row.append((x,y))
		ans.append(row)
	return ans

def julia(plane, c):
	max_iteration = 1000
	image = initialyzeimage(len(plane), len(plane))
	for i in range(len(plane)):
		for k in range(len(plane[i])):
			x, y = plane[i][k]
			z = complex(x, y)
			iteration = 0
			while abs(z) < 2 and iteration < max_iteration:
				z = z*z + c
				iteration += 1
			image[i][k] = iteration
	return image

if __name__ == '__main__':
	n = 1000
	print('Draw Julia Set iterating f(z) = z^2 + c')
	print('Good values for c are:')
	print('1) c = -0.8 + 0.156i')
	print('2) c = 0.285 + 0.01i')
	print('3) c = -0.4 + 0.6i')
	print('4) c = -0.621')
	real = float(input('Enter real part of c: '))
	imag = float(input('Enter imaginary part of c: '))
	c = complex(real, imag)
	plane = initialyzeplane(n)
	fig = julia(plane, c)
	plt.imshow(fig, extent=(-2.,2.,-2.,2.),
			cmap=cm.nipy_spectral_r, interpolation='nearest')
	plt.title('Julia Set f(z) = z^2 + c with c = {} + {}i'.format(c.real, c.imag))
	plt.colorbar()
	plt.show()
