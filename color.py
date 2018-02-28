#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
import random

def color_points():
	x_p = 50
	y_p = 50
	image = np.zeros((x_p, y_p))
	for j in range(y_p):
		for i in range(x_p):
			image[i][j] = random.randint(0,10)
	plt.imshow(	image, origin='lower', extent=(0,5,0,5),
				cmap=cm.nipy_spectral_r, interpolation='nearest')
	plt.colorbar()
	plt.show()

if __name__ == '__main__':
	color_points()