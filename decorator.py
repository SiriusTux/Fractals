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
