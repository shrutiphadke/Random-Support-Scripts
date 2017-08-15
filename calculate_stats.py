import sys
import cv2
import numpy as np
import glob
import os

gtpath = '/home/shruti/virat/gtall/'
predpath = '/home/shruti/sn_pred/'

a1 ='/home/local/KHQ/shruti.phadke/virat/gtall/'
a2 ='/home/local/KHQ/shruti.phadke/virat/imall/'

#f = open('final_lab.txt', 'w')

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
perc = [0.0,0.0,0.0,0.0,0.0,0.0]
#globalacc = 0


for root, directories, files in os.walk(gtpath):
	for filename in sorted(files):
		ng = gtpath + filename
		
	#ni = predpath + str("{0:0=5d}".format(i)) + '.png'
		#f.write(a2 + filename)
		#f.write(' ')
		#f.write(a1 + filename)
		#f.write('\n')
		
		gt = cv2.imread(ng, 0)
	
        	val, ct = np.unique(gt, return_counts= True)
        	print len(val)
                #print np.count_nonzero(gt == 9)
         
        	for j in range(len(val)):
        		cf[val[j]] = cf[val[j]] + ct[j]
        	#print cf	
        
        

md = np.median(cf)
print md
print cf
#f.close()
#print float(cf)/float(40550400)

for k in range(len(cf)):
	weights[k] = float(md)/float(cf[k]) 
	perc[k] = float(cf[k])/ float(sum(cf))

print weights
print perc
