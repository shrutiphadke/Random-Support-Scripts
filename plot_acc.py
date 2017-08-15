#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
import argparse

if __name__ == '__main__':
	ap = argparse.ArgumentParser()
	ap.add_argument("-file", "--file", required=True, help="path to the training log file")
	args = vars(ap.parse_args())

	file_path = args["file"]
	print file_path

	fileptr = open(file_path,'r')
	log = fileptr.readlines()
	######################### Plot training error  #########################
	linesWithLoss = [x for x in log if x.find('Wise =') >0]  
	print linesWithLoss
	loss = np.array([float(x.split()[3]) for x  in linesWithLoss])
	filt_size = 20
	smooth_loss = np.convolve(loss, np.ones(filt_size)/filt_size,mode='valid')

	each_step = 2000 #iteration
	iterations = each_step*np.arange(loss.size)

	loss = loss[0:smooth_loss.size]
	iterations = iterations[0:smooth_loss.size]
	########################################################################
	######################### Plot training accuracy #######################
	
	lineswithacc = [y for y in log if y.find('Class =') > 0]
	acc = np.array([float(y.split()[3]) for y  in lineswithacc])
	smooth_acc = np.convolve(acc, np.ones(filt_size)/filt_size, mode = 'valid')
	
	iters = each_step*np.arange(acc.size)
	acc = acc[0: smooth_acc.size]
	iters = iters[0:smooth_acc.size]
	
	##########################################################################

	plt.figure(1)
	plt.plot(iterations,loss, linewidth=5.0, hold=True)
	plt.title("Global Accuracy vs. Iterations", fontsize=18, color='blue')
	#plt.plot(iterations,smooth_loss,hold=True)
	plt.xlabel('Iterations', fontsize=14, color='red')
	plt.ylabel('Global Accuracy', fontsize=14, color='red')
	plt.grid(True)
	plt.show()
	
	
	
	plt.figure(2)
	plt.rc('legend',fontsize=20) # using a size in points
	#plt.rc('legend',fontsize='medium') # using a named size
	plt.plot(iters, acc, linewidth=5.0, hold = True)
	#plt.plot(iters, smooth_acc, hold= True)
	plt.title("Mean Class Accuracy vs. Iterations", fontsize=18, color='blue')
	plt.xlabel('Iterations', fontsize=14, color='red')
	plt.ylabel('Mean Class Accuracy', fontsize=14, color='red')
	plt.grid(True)
	plt.show()
