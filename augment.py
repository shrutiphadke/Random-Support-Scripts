#dataset augmentation script
import cv2
import numpy as np
import sys 
import os
import math
#Gamma Correction Function
#Credits: http://www.pyimagesearch.com/2015/10/05/opencv-gamma-correction/

def adjust_gamma(image, gamma=1.0):
	# build a lookup table mapping the pixel values [0, 255] to
	# their adjusted gamma values
	invGamma = 1.0 / gamma
	table = np.array([((i / 255.0) ** invGamma) * 255
		for i in np.arange(0, 256)]).astype("uint8")
 
	# apply gamma correction using the lookup table
	return cv2.LUT(image, table) 

#Define global variables and paths
gt_root = '/home/shruti/virat/gtall/'
im_root = '/home/shruti/virat/imall/'
gt_dest = '/home/shruti/virat/gt_aug/'
im_dest = '/home/shruti/virat/im_aug/'

gt_path = gt_root
im_path = im_root
count = 0
augtypes = 15
im_nos = 24


#Read the images
for root, directories, files in os.walk(gt_root):
	for filename in files:
		#im_id_gt = "{0:0=5d}".format(i+1)
		#im_id_im = "{0:0=5d}".format(i+1)
	
		gt_name = gt_root + filename
		im_name = im_root + filename
	
		print gt_name
		print im_name
	
		gt = cv2.imread(gt_name,0)
		im = cv2.imread(im_name)
	
		#gt = cv2.resize(gt, (480, 360))
		#im = cv2.resize(im, (480, 360))
	
		#w = i*augtypes
		
		lf = len(filename)
	
		sv_gt = gt_dest + filename[0:lf-4] + '_0' + filename[lf-4:lf]
		sv_im = im_dest + filename[0:lf-4] + '_0' + filename[lf-4:lf]
	
		cv2.imwrite(sv_gt, gt)
		cv2.imwrite(sv_im, im)
	
		count = count +1
	

		#Horizontal FLip
		h_gt =cv2.flip(gt, 1)
		h_im =cv2.flip(im, 1)
	
		sv_hg = gt_dest + filename[0:lf-4] + '_1' + filename[lf-4:lf]
		sv_hi = im_dest + filename[0:lf-4] + '_1' + filename[lf-4:lf]
	
		cv2.imwrite(sv_hg, h_gt)
		cv2.imwrite(sv_hi, h_im)

		#Vertical FLip
		v_gt =cv2.flip(gt, 0)
		v_im =cv2.flip(im, 0)
	
		#sv_vg = gt_dest + str("{0:0=5d}".format(w+2))+ '.png'
		#sv_vi = im_dest + str("{0:0=5d}".format(w+2))+ '.png'
	
		#cv2.imwrite(sv_vg, v_gt)
		#cv2.imwrite(sv_vi, v_im)
	
		#Power law 1 Gamma =0.5
		gt_pl1 = gt
		im_pl1 = adjust_gamma(im, gamma= 0.5)
	
		sv_g1 = gt_dest + filename[0:lf-4] + '_2' + filename[lf-4:lf]
		sv_i1 = im_dest + filename[0:lf-4] + '_2' + filename[lf-4:lf]
	
		cv2.imwrite(sv_g1, gt_pl1)
		cv2.imwrite(sv_i1, im_pl1)

		#Power law 2 Gamma = 0.8
		gt_pl2 = gt
		im_pl2 = adjust_gamma(im, gamma= 0.8)
	
		sv_g2 = gt_dest + filename[0:lf-4] + '_3' + filename[lf-4:lf]
		sv_i2 = im_dest + filename[0:lf-4] + '_3' + filename[lf-4:lf]
	
		cv2.imwrite(sv_g2, gt_pl2)
		cv2.imwrite(sv_i2, im_pl2)

		#Power law 3 Gamma = 1,5
		gt_pl3 = gt
		im_pl3 = adjust_gamma(im, gamma= 1.5)

		#sv_g3 = gt_dest + str("{0:0=5d}".format(w+5))+ '.png'
		#sv_i3 = im_dest + str("{0:0=5d}".format(w+5))+ '.png'
	
		#cv2.imwrite(sv_g3, gt_pl3)
		#cv2.imwrite(sv_i3, im_pl3)


		#Power law 4 Gamma = 2.0
		gt_pl4 = gt
		im_pl4 = adjust_gamma(im, gamma= 2.0)
	
		#sv_g4 = gt_dest + str("{0:0=5d}".format(w+6))+ '.png'
		#sv_i4 = im_dest + str("{0:0=5d}".format(w+6))+ '.png'
	
		#cv2.imwrite(sv_g4, gt_pl4)
		#cv2.imwrite(sv_i4, im_pl4)

		#Power law 5 Gamma = 2.5
		gt_pl5 = gt
		im_pl5 = adjust_gamma(im, gamma= 2.5)
	
		sv_g5 = gt_dest + filename[0:lf-4] + '_4' + filename[lf-4:lf]
		sv_i5 = im_dest + filename[0:lf-4] + '_4' + filename[lf-4:lf]
	
		cv2.imwrite(sv_g5, gt_pl5)
		cv2.imwrite(sv_i5, im_pl5)

		#Randon noise 1
		m = (15,15,15) 
		s = (15,15,15)
		im_rn1 = im
		im_rn1 = cv2.blur(im_rn1,(5, 5))
	
		gt_rn1 = gt
	
		sv_rng1 = gt_dest + filename[0:lf-4] + '_5' + filename[lf-4:lf]
		sv_rni1 = im_dest + filename[0:lf-4] + '_5' + filename[lf-4:lf]
	
		cv2.imwrite(sv_rng1, gt_rn1)
		cv2.imwrite(sv_rni1, im_rn1)
	
	

		#Random noise 2
		m = (7,7,7) 
		s = (7,7,7)
		im_rn2 = im
		im_rn2 = cv2.blur(im_rn2,(20, 20))
	
		gt_rn2 = gt
	
		#sv_rng2 = gt_dest + str("{0:0=5d}".format(w+9))+ '.png'
		#sv_rni2 = im_dest + str("{0:0=5d}".format(w+9))+ '.png'
	
		#cv2.imwrite(sv_rng2, gt_rn2)
		#cv2.imwrite(sv_rni2, im_rn2)

		#Random crop 1
		r1 = 100.0 / im.shape[1]
		dim = (100, int(im.shape[0] * r1))
	
		r = gt.shape[0]
		c = gt.shape[1]
	
		gt_rc1 = gt[100:r, :]
		im_rc1 = im[100:r, :, :]
	
		gt_rc1 = cv2.resize(gt_rc1, (c,r))
		im_rc1 = cv2.resize(im_rc1, (c,r))
	
		sv_rcg1 = gt_dest + filename[0:lf-4] + '_6' + filename[lf-4:lf]
		sv_rci1 = im_dest + filename[0:lf-4] + '_6' + filename[lf-4:lf]
	
	
		cv2.imwrite(sv_rcg1, gt_rc1)
		cv2.imwrite(sv_rci1, im_rc1)

		#Random crop 2
		gt_rc2 = gt[:, 100:c]
		im_rc2 = im[:, 100:c, :]
	
		gt_rc2 = cv2.resize(gt_rc2, (c,r))
		im_rc2 = cv2.resize(im_rc2, (c,r))
	
		sv_rcg2 = gt_dest + filename[0:lf-4] + '_7' + filename[lf-4:lf]
		sv_rci2 = im_dest + filename[0:lf-4] + '_7' + filename[lf-4:lf]
	
		cv2.imwrite(sv_rcg2, gt_rc2)
		cv2.imwrite(sv_rci2, im_rc2)

		#Random crop 3
		gt_rc3 = gt[100:r, 100:c]
		im_rc3 = im[100:r, 100:c, :]
	
		gt_rc3 = cv2.resize(gt_rc3, (c,r))
		im_rc3 = cv2.resize(im_rc3, (c,r))
	
		sv_rcg3 = gt_dest + filename[0:lf-4] + '_8' + filename[lf-4:lf]
		sv_rci3 = im_dest + filename[0:lf-4] + '_8' + filename[lf-4:lf]
	
		cv2.imwrite(sv_rcg3, gt_rc3)
		cv2.imwrite(sv_rci3, im_rc3)
	
		#Random block 1
		gt_rb1 = gt
		gt_rb1[50:100, 50:100] = 0
		im_rb1 = im
		im_rb1[50:100, 50:100, :] = (0,0,0)
	
		#sv_rbg1 = gt_dest + str("{0:0=5d}".format(w+13))+ '.png'
		#sv_rbi1 = im_dest + str("{0:0=5d}".format(w+13))+ '.png'
	
		#cv2.imwrite(sv_rbg1, gt_rb1)
		#cv2.imwrite(sv_rbi1, im_rb1)
	
		#Random block 2
		gt_rb2 = gt
		gt_rb2[150:200, 150:200] = 0
		im_rb2 = im
		im_rb2[150:200, 150:200, :] = (0,0,0)
	
		#sv_rbg2 = gt_dest + str("{0:0=5d}".format(w+14))+ '.png'
		#sv_rbi2 = im_dest + str("{0:0=5d}".format(w+14))+ '.png'
	
		#cv2.imwrite(sv_rbg2, gt_rb2)
		#cv2.imwrite(sv_rbi2, im_rb2)

