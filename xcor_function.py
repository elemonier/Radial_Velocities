#xcor_function.py	
#def xcor(wv_arr, std_flux_arr, obj_flux_arr):
from array import array
import asciitable
import math
import matplotlib.pyplot as plt
import numpy
import pyfits
import pylab
import random
import scipy
from scipy import constants
from scipy import interpolate
import sys

	
def x_cor(wv_arr, std_flux_arr, obj_flux_arr):
#instance variables & overhead---------------
	data_root = '/Users/emilylemonier/Data/Python/MIKE_FIVE_RV/Raw/'
	nLoops = 5000
	rv_array = [None]*nLoops
	inputs = sys.argv
	
	#CORRELATION ---------------------------------------
	#xdata
	i = 0
	num = 0
	for k in range(0, len(wv_arr)-1):
		i += wv_arr[k+1]-wv_arr[k]
		num += 1
		distancePerLag = i/num #computed as avg of distances per lag

		# what youre comparing
		offset = distancePerLag
		#y1 = fx_std_interp
		#y2 = fx_obj_interp

		#compute the cross-correlation between y1 and y2
		ycorr = scipy.correlate(std_flux_arr, obj_flux_arr, mode='same')
		#xcorr = scipy.linspace(0, len(ycorr)-1, num=len(ycorr))

	#TEST PLOT
	plt.figure(1)
	plt.subplot(211)
	plt.plot(ycorr, 'b')
	plt.title('correlation plots of ycorr vs xcorr')
	plt.show()
	#pylab.subplot(211)
	#pylab.plot(wv_std_good, fx_obj_good, 'b')
	#pylab.plot(wv_obj_good, fx_obj_good, 'r')
	#pylab.show()


	# define a gaussian fitting function where
	# p[0] = amplitude
	# p[1] = mean
	# p[2] = sigma.
	fitfunc = lambda p, x: p[0]*scipy.exp(-(x-p[1])**2/(2.0*p[2]**2))
	errfunc = lambda p, x, y: fitfunc(p,x)-y

# guess some fit parameters... + everything after that = cut off!
#END CORRELATION TEST----------------------------------
