import sys
import os
import cv2

gt = '/home/shruti/virat/gtall/'
im = '/home/shruti/virat/imall/'

a1 = '/home/local/KHQ/shruti.phadke/virat/gtall/'
a2 = '/home/local/KHQ/shruti.phadke/virat/imall/'

f = open('all.txt', 'w')

for i in range(528):
	g = "{0:0=5d}".format(i+1)
	#gpath = gt + str(g) + '.png'
	#gtim = cv2.imread(gpath)
        
        #gtim = cv2.resize(gtim, (480, 360))
        
        #ipath = im + str(g) + '.png'
        #imim = cv2.imread(ipath)
        #imim = cv2.resize(imim, (480, 360))
        
        #cv2.imwrite(gpath, gtim)
        #cv2.imwrite(ipath, imim)
        
        b1 = a1 +str(g)+ '.png'
        b2 = a2+ str(g)+ '.png'
        
        f.write(b2)
        f.write(" ")
        f.write(b1)
        f.write("\n")
        
        
f.close()
