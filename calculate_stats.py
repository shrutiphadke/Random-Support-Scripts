import sys
import cv2
import numpy as np
import glob
import os

gtpath = '/home/shruti/virat/gtall/'
predpath = '/home/shruti/sn_pred/'


#groundtruths = dir(gtpath)
#skip =2
#preditions= dir(predpath)

#it = 360

#numclass = 11
#unknown_class =12

count = 1 

totalpoints = 0

cf = [0,0,0,0,0,0]
weights = [0.0,0.0,0.0,0.0,0.0,0.0]
#globalacc = 0

for root, directories, files in os.walk(gtpath):
	for filename in files:
		ng = gtpath + filename
	#ni = predpath + str("{0:0=5d}".format(i)) + '.png'
	
		gt = cv2.imread(ng, 0)
	
        	val, ct = np.unique(gt, return_counts= True)
        
                #print np.count_nonzero(gt == 9)
        
        	for j in range(len(val)):
        		cf[val[j]] = cf[val[j]] + ct[j]
        	#print cf	
        
        

md = np.median(cf)


print cf

for k in range(len(cf)):
	weights[k] = float(md)/float(cf[k]) 

print weights
