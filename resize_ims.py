import cv2
import numpy as np
import os
import sys

p1 = '/home/shruti/viratseg/imall/'
p2 = '/home/shruti/viratseg/gtall/'

for root, directories, files in os.walk(p2):
	for filename in files:
 
		r1 = p1 + filename
		r2 = p2 + filename
	
		i1 = cv2.imread(r1)
		i2 = cv2.imread(r2,0)
	
		i1 = cv2.resize(i1, (480,360))
	        i2 = cv2.resize(i2, (480,360))
	
		cv2.imwrite(r1, i1)
		cv2.imwrite(r2, i2)
#	        print np.unique(i1)
#		print np.unique(i2)
