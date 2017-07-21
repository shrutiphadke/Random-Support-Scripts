#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
import argparse

if __name__ == '__main__':
	ap = argparse.ArgumentParser()
	ap.add_argument("-file", "--file", required=True, help="path to the training log file")
	args = vars(ap.parse_args())

	file_path = args["file"]

	fileptr = open(file_path,'r')
	log = fileptr.readlines()
	######################### Plot training error  #########################
	linesWithLoss = [x for x in log if x.find(': loss =') > 0]
	loss = np.array([float(x.split()[10]) for x  in linesWithLoss])
	filt_size = 20
	smooth_loss = np.convolve(loss, np.ones(filt_size)/filt_size,mode='valid')

	each_step = 20 #iteration
	iterations = each_step*np.arange(loss.size)

	loss = loss[0:smooth_loss.size]
	iterations = iterations[0:smooth_loss.size]
	########################################################################
	######################### Plot training accuracy #######################
	
	lineswithacc = [y for y in log if y.find('#0: accuracy =') > 0]
	acc = np.array([float(y.split()[10]) for y  in lineswithacc])
	smooth_acc = np.convolve(acc, np.ones(filt_size)/filt_size, mode = 'valid')
	
	iters = each_step*np.arange(acc.size)
	acc = acc[0: smooth_acc.size]
	iters = iters[0:smooth_acc.size]
	
	##########################################################################

	plt.figure(1)
	plt.plot(iterations,loss,hold=True)
	plt.plot(iterations,smooth_loss,hold=True)
	plt.xlabel('Iterations')
	plt.ylabel('Training error')
	plt.show()
	
	
	
	plt.figure(2)
	plt.plot(iters, acc, hold = True)
	plt.plot(iters, smooth_acc, hold= True)
	plt.xlabel('Iterations')
	plt.ylabel('Training Accuracy')
	plt.show()
