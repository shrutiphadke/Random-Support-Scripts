#visualize annotations in color

import cv2
import numpy as np 
import os
import matplotlib.pyplot as plt
import sys


source = '/home/shruti/virat/gt/'
support = '/home/shruti/virat/im/'

unannotated = [0, 0, 0]
Sky = [0, 255, 255]
Building = [128, 0, 0]
Shadows = [128, 128, 128]
Grass = [0, 255, 0]
Trees = [0, 128, 0]
Parking_Lot = [128, 128, 0]
Street = [192, 192, 192]
Sidewalk = [0, 128, 128]
Crosswalk = [0, 0, 128]
Intersection = [255, 0, 0]
Umbrella = [255, 255, 0]

label_colours = np.array([unannotated,Sky,Building ,Shadows, Grass, Trees, Parking_Lot, Street, Sidewalk,Crosswalk, Intersection, Umbrella ])



for root, directories, files in os.walk(source):
	for filename in files:
		path = source + filename
		
		s_path = support +filename
		print s_path
		org1 = cv2.imread(s_path, 1)
		im = cv2.imread(path,0)
		ind = im
		
		r1 = ind.copy()
		g1 = ind.copy()
		b1 = ind.copy()
		
		for l1 in range(0,11):
		        r1[ind==l1] = label_colours[l1,0]
		        g1[ind==l1] = label_colours[l1,1]
		        b1[ind==l1] = label_colours[l1,2]
		     
		rgb = np.zeros((ind.shape[0], ind.shape[1], 3))
		rgb[:,:,0] = r1/255.0
		rgb[:,:,1] = g1/255.0
		rgb[:,:,2] = b1/255.0
		
		plt.figure()
		plt.imshow(org1, vmin=0, vmax=1)
		plt.figure()
		plt.imshow(rgb,vmin=0, vmax=1)
		plt.show()
		

