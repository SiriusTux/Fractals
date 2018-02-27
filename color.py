#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import random
from utilities import initialyzeimage

def color_points():
	x_p = 50
	y_p = 50
	image = initialyzeimage(x_p, y_p)
	for j in range(y_p):
		for i in range(x_p):
			image[i][j] = random.randint(0,10)
	plt.imshow(	image, origin='lower', extent=(0,5,0,5),
				cmap=cm.nipy_spectral_r, interpolation='nearest')
	plt.colorbar()
	plt.show()

if __name__ == '__main__':
	color_points()