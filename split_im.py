# Breaking up the images
import os
import sys
import cv2
import numpy as np
from math import *
imct = 1

io = '/home/shruti/virat/im/'
go = '/home/shruti/virat/gt/'

di = '/home/shruti/virat/imall/'
dg = '/home/shruti/virat/gtall/'

im_nos = 24

#r = 1080
#c = 1920

#r_iter = int(r/265)
#c_iter = int(c/256)

for i in range(im_nos):
	n1 = "{0:0=5d}".format(i+1)
	ni = io +   str(n1) + '.png'
	ng = go +   str(n1) + '.png'
	im = cv2.imread(ni)
	gt = cv2.imread(ng, 0)
	print np.unique(gt)
	[r,c] = gt.shape
	r_iter = int(r/360)
	c_iter = int(c/480)
	for j in range(r_iter):
		for k in range(c_iter):
			new_im = im[j*(360):(j+1)*360, k*480: (k+1)*480]
			new_gt = gt[j*(360):(j+1)*360, k*480: (k+1)*480]
			n2 = "{0:0=5d}".format(imct)
			new_di = di + str(n2) + '.png'
			new_dg = dg + str(n2) + '.png'
			
			cv2.imwrite(new_di, new_im)
			cv2.imwrite(new_dg, new_gt)
			
			imct = imct + 1
			
			
			
			
			
			
			
			
