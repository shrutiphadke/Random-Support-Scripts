#visualize annotations in color

import cv2
import numpy as np 
import os
import matplotlib.pyplot as plt
import sys


source = '/home/shruti/camvid/tesannot/'
support = '/home/shruti/camvid/test/'

#unannotated = [0, 0, 0]
#Sky = [0, 255, 255]
#Building = [128, 0, 0]
#Shadows = [128, 128, 128]
#Grass = [0, 255, 0]
#Trees = [0, 128, 0]
#Parking_Lot = [128, 128, 0]
#Street = [192, 192, 192]
#Sidewalk = [0, 128, 128]
#Crosswalk = [0, 0, 128]
#Intersection = [255, 0, 0]
#Umbrella = [255, 255, 0]

#label_colours = np.array([unannotated,Building, Grass, Trees, Parking_Lot, Street])

Sky = [128,128,128]
Building = [128,0,0]
Pole = [192,192,128]
Road_marking = [255,69,0]
Road = [128,64,128]
Pavement = [60,40,222]
Tree = [128,128,0]
SignSymbol = [192,128,128]
Fence = [64,64,128]
Car = [64,0,128]
Pedestrian = [64,64,0]
Bicyclist = [0,128,192]
Unlabelled = [0,0,0]

label_colours = np.array([Sky, Building, Pole, Road, Pavement, Tree, SignSymbol, Fence, Car, Pedestrian, Bicyclist, Unlabelled])

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
		

