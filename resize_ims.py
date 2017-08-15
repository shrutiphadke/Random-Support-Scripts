import cv2
import numpy as np
import os
import sys

p1 = '/home/shruti/virat/im/'
p2 = '/home/shruti/virat/gt/'

p3 = '/home/shruti/final_test/im/'
p4 = '/home/shruti/final_test/gt/'

for root, directories, files in os.walk(p2):
	for filename in files:
 
		r1 = p1 + filename
		r2 = p2 + filename
		
		r3 = p3 + filename
		r4 = p4 + filename
	
		i1 = cv2.imread(r1)
		i2 = cv2.imread(r2,0)
		
		print i2.shape
	
		i1 = cv2.resize(i1, (1280,720))
	        i2 = cv2.resize(i2, (1280,720))
	
		cv2.imwrite(r3, i1)
		cv2.imwrite(r4, i2)
#	        print np.unique(i1)
#		print np.unique(i2)
