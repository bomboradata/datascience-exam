# --------------------------------------------------------------------
# Based on the fact that Pi is the ratio of a cicle's area to 
# the square of its radius, one way to find pi is as below:
# Suppose we have a uniform random generator, which produces points in
# a range [0,1]. Pi can be computed using the ratio of the random 
#points inside the square to the number of points inside quarter 
# of circle with  radius 1. 
#--------------------------------------------------------------------
# This function finds Pi from a uniform random generator

# import the required libraries
from random import *
from math import sqrt

def find_pi(n):
	inside = 0 # count the number of random points inside the quarter circle
	n = 10000 # number of random points, the larger numbers provide more accurate Pi

	for i in range(0,n):
		x = random()
		y = random()
		if sqrt(x**2+y**2)<=1:
			inside+=1
	pi = 4*inside/n
	return pi

print('Testing for number of points = 1000')
print('Pi = ', find_pi(1000) )
print('------------------------------------')
print('Testing for number of points = 10000')
print('Pi = ', find_pi(10000) )
print('------------------------------------')




