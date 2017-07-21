import cv2
import json
import numpy as np

labels = ['Unannotated','Sky', 'Building', 'Shadows', 'Grass', 'Ground', 'Trees', 'Parking_Lot', 'Street', 'Sidewalk', 'Crosswalk', 'Intersection', 'Stairs', 'Background', 'Umbrella']

save = '/home/shruti/diva/v1-annotations/0503/static/gt/'

im = cv2.imread('/home/shruti/diva/v1-annotations/0503/static/00001.png', 0)

#X_DIMENSION = 288
#Y_DIMENSION = 382
black = np.zeros((im.shape))*64/255.0
#print black

for j in range(14):
	n = "{0:0=5d}".format(j+1)
	newnm = save+ str(n)+ '.png'
	cv2.imwrite(newnm, black)
	
	

with open('/home/shruti/diva/v1-annotations/0503/static/static.json') as data_file:    
    data = json.load(data_file)


#print len(data["tracks"])

x =[]
y= []
newcoor= []
for i in range(len(data["tracks"])):
#for i in range(1):
	f = len((data["tracks"][i])["frames"])
	#print "\n"
	lab = (data["tracks"][i])["label"]
	for j in range(f):
		#print ((data["tracks"][i])["frames"][j])["frame_id"]
		if ((data["tracks"][i])["frames"][j])["frame_id"]>-1:
			fr_no = ((data["tracks"][i])["frames"][j])["frame_id"]
			coor = (((data["tracks"][i])["frames"][j])["polygon"])
			for k in range(len(coor)):
				#newcoor[k].append((coor[k]["image_x"]))
				#newcoor[k].append((coor[k]["image_y"]))
				
				#newcoor[k[0:1]]= (coor[k]["image_x"] , coor[k]["image_y"])
				newcoor.append((coor[k]["image_x"] , coor[k]["image_y"]))
			#print x , y
			n = "{0:0=5d}".format(fr_no+1)
			newnm = save+ str(n)+ '.png'
			print newnm
			im = cv2.imread(newnm, 0)
			#idx = labels.index(lab)
			##########
			if(lab == 'Unannotated' or lab == 'Background' or lab == 'Stairs'):
				idx = 0
			elif(lab == 'Sky'):
				idx = 1
			elif(lab == 'Building'):
				idx = 2
			elif(lab == 'Shadows'):
				idx = 3
			elif(lab == 'Grass'):
				idx = 4
			elif(lab == 'Trees'):
				idx = 5
			elif(lab == 'Parking_Lot'):
				idx = 6
			elif(lab == 'Street'):
				idx = 7
			elif(lab == 'Sidewalk'):
				idx = 8
			elif(lab == 'Crosswalk'):
				idx = 9
			elif(lab == 'Intersection'):
				idx = 10
			elif(lab == 'Umbrella'):
				idx = 11
			##########
			print "index", idx
			pts = np.array(newcoor, np.int32)
			#print pts.shape
			if(pts.shape[0] >0 and pts.shape[1] >0):
				#pts = pts.reshape((-1,1,2))
				cv2.fillPoly(im, [pts], idx)
				cv2.imwrite(newnm, im)
				newcoor = []
				#newcoor[:]=(x, y)
				#print newcoor
		
				
	


