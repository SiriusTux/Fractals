#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import random
import math

def chooseNextVertex1(vertices, previous_vertex, previous_previous_vertex):
	'''
	Rule = next vertex must be different from previous one
	'''
	vertex = random.choice(list(vertices.keys()))
	while vertex == previous_vertex:
		vertex = random.choice(list(vertices.keys()))
	return vertex

def chooseNextVertex2(vertices, previous_vertex, previous_previous_vertex):
	'''
	Rule = next vertex cannot be 2 places away from the previously chosen vertex
	'''	
	vertex = random.choice(list(vertices.keys()))
	i_ver = list(vertices.keys()).index(vertex)
	i_pre_ver = list(vertices.keys()).index(previous_vertex)
	while abs(i_ver - i_pre_ver) == 2:
		vertex = random.choice(list(vertices.keys()))
		i_ver = list(vertices.keys()).index(vertex)
	return vertex

def chooseNextVertex3(vertices, previous_vertex, previous_previous_vertex):
	'''
	Rule = next vertex cannot be 2 places away from the two previously chosen vertices.
	'''	
	vertex = random.choice(list(vertices.keys()))
	i_ver = list(vertices.keys()).index(vertex)
	i_pre_ver = list(vertices.keys()).index(previous_vertex)
	i_pre_pre_ver = list(vertices.keys()).index(previous_previous_vertex)
	while abs(i_ver - i_pre_ver) == 2 and abs(i_ver - i_pre_pre_ver) == 2:
		vertex = random.choice(list(vertices.keys()))
		i_ver = list(vertices.keys()).index(vertex)
	return vertex

def dist(x1, y1, x2, y2):
	xd = (x1 + x2) / 2.
	yd = (y1 + y2) / 2.
	return xd, yd

def chaos(vertices, iteration, fun):
	x = []
	y = []
	# Random chosen starting point
	start_x = random.uniform(vertices['A'][0], vertices['B'][0])
	start_y = random.uniform(vertices['A'][1], vertices['C'][1])
	x.append(start_x)
	y.append(start_y)
	i = 0
	previous_vertex = 'A'
	previous_previous_vertex = 'A'
	while i <= iteration:
		next_vertex = fun(vertices, previous_vertex, previous_previous_vertex)
		next_vertex_x, next_vertex_y = vertices[next_vertex]
		next_x, next_y = dist(start_x, start_y, next_vertex_x, next_vertex_y)
		x.append(next_x)
		y.append(next_y)
		start_x, start_y = next_x, next_y 
		previous_previous_vertex = previous_vertex
		previous_vertex = next_vertex
		i += 1
	return x, y


if __name__ == '__main__':
	iteration = 100000
	# Vertices of a square
	vertices = {'A':(0.,0.), 'B':(2.,0.), 'C':(2., 2.), 'D':(0., 2.)}
	# Choose a next-vertex rule
	function = [chooseNextVertex1, chooseNextVertex2, chooseNextVertex3]
	print('[1] Next vertex must be different from previously chosen vertex')
	print('[2] Next vertex cannot be 2 places away from the previously chosen vertex')
	print('[3] Next vertex cannot be 2 places away from the two previously chosen vertices.')
	choice = int(input('Enter next vertex rule: '))
	x, y = chaos(vertices, iteration, function[choice-1])
	plt.plot(x, y, 'o', markersize=0.5, color='blue')
	plt.show()





		
