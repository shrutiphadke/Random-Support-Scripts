# Scoring script for sematic segmentation
import os
import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Global Paths

gt_path = '/home/shruti/cross_val/pass1/gt/'
pred_path = '/home/shruti/cross_val/pass1/im/'
or_path = '/home/shruti/cross_val/pass1/or/'

im_nos = 24

class_nos = 6



r = 360
c = 480
ignore= 0
im_sz = r*c
# Read Images
i= 0
acc = 0.0
cl = np.zeros(class_nos, dtype = np.float64)
imcount = np.zeros(class_nos, dtype = np.float64)
pixcount = np.zeros(class_nos, dtype = np.float64)
imcount = imcount + im_nos
ignr = 0
#print os.listdir('/home/shruti/chirag_test/')
for root, directories, files in os.walk(gt_path):
	for filename in files:
 
			
		imp = pred_path + filename
		gtp = gt_path + filename
		orp = or_path + filename
		
		im = cv2.imread(imp, 0)
		gt = cv2.imread(gtp, 0)
                or1 = cv2.imread(orp)
		zi = np.count_nonzero(im == 0)
		zg = np.count_nonzero(gt==0)
		
		# d = min(zi,zg)
		# Convert them into measurable format
	        ignr = ignr + zi

		# Pixel Wise Accuracy
	
		diff = abs(gt - im)
		nz = np.count_nonzero(diff)
	        ignore = ignore + zg
	
		correct = im_sz - nz 
		#correct = nz
		if(correct > im_sz):
			print 'bigger' 
		#print correct
		acc = acc +  (float(correct)) 
		
	

		# Mean class average
		count = 0
		#r = im.shape[0]
		#c = im.shape[1]
		#print gt[200:300 , 100: 350]
		for l in range(class_nos):
			for k in range(c):
				for j in range(r):
					if(im[j, k] == l and gt[j, k]==l):
						count = count +1
			if(np.count_nonzero(gt == l) != 0):
				#print "gt label count" , np.count_nonzero(gt == l)
				#cl[l] = cl[l] + (float(count) /float(np.count_nonzero(gt == l)))
				cl[l] = cl[l] + float(count)
				pixcount[l] = pixcount[l] + np.count_nonzero(gt == l)
		        	#print cl
			else:
				imcount[l] = imcount[l] -1.0
			count = 0		
		print imcount
		
		################################################################################################
		ind = im
		label = gt
		r1 = ind.copy()
		g1 = ind.copy()
		b1 = ind.copy()
		r_gt = label.copy()
		g_gt = label.copy()
		b_gt = label.copy()

		Street = [192, 192, 192]
		Building = [128,0,0]
		Trees = [0, 128, 0]
		Grass = [0, 255, 0]
		Parking_Lot = [128, 128, 0]
		Unlabelled = [0,0,0]

		label_colours = np.array([Unlabelled, Street,Building, Trees, Grass, Parking_Lot])
		for l1 in range(0,5):
		        r1[ind==l1] = label_colours[l1,0]
		        g1[ind==l1] = label_colours[l1,1]
		        b1[ind==l1] = label_colours[l1,2]
		        r_gt[label==l1] = label_colours[l1,0]
		        g_gt[label==l1] = label_colours[l1,1]
		        b_gt[label==l1] = label_colours[l1,2]

		rgb = np.zeros((ind.shape[0], ind.shape[1], 3))
		rgb[:,:,0] = r1/255.0
		rgb[:,:,1] = g1/255.0
		rgb[:,:,2] = b1/255.0
		rgb_gt = np.zeros((ind.shape[0], ind.shape[1], 3))
		rgb_gt[:,:,0] = r_gt/255.0
		rgb_gt[:,:,1] = g_gt/255.0
		rgb_gt[:,:,2] = b_gt/255.0

	        plt.figure()
	        plt.imshow(or1)
		plt.figure()
		plt.imshow(rgb_gt,vmin=0, vmax=1)
		plt.figure()
		plt.imshow(rgb,vmin=0, vmax=1)
		plt.show()

		################################################################################################
		# Weighted Mean Class Average
		
		# Mean IoU

print imcount

#imcount = im_nos - imcount
cl = np.divide(cl, pixcount)
print cl

print "Pixel Wise Accuracy:" , (acc)/float((im_nos*im_sz))
print "Mean Class Accuracy:" , (sum(cl))/(class_nos)

