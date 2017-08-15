# Train/Test/Val Split
# Creating train.txt, test.txt, val.txt

import sys
import glob
import os
import cv2
import numpy as np

impath = '/home/local/KHQ/shruti.phadke/viratseg/test/'
gtpath = '/home/local/KHQ/shruti.phadke/sn_gt/'

imsource = '/home/shruti/virat_input/'
gtsource = '/home/shruti/virat_gt/'

#f = open('test_labels.txt', 'w')

for root, directories, files in os.walk(imsource):
	for filename in files:
		im = imsource + filename
		#gt = gtpath + filename
		m = cv2.imread(im)
		m = cv2.resize(m, (240, 180))
		cv2.imwrite(im, m)
		#f.write(im)
		#f.write(" ")
		#f.write(gt)
		#f.write("\n")
		
#f.close()
		
		
		
		
		
		
		
		
		
