import json
from pprint import pprint

save = '/home/shruti/diva/v1-annotations/0100/static/'

with open('/home/shruti/diva/v1-annotations/0100/static/first pass/frames 1-28/static.json') as data_file:    
    data = json.load(data_file)


#print len(data["tracks"])

x =[]
y= []
#for i in range(len(data["tracks"])):
for i in range(1):
	f = len((data["tracks"][i])["frames"])
	#print "\n"
	lab = (data["tracks"][i])["label"]
	for j in range(1):
		#print ((data["tracks"][i])["frames"][j])["frame_id"]
		if ((data["tracks"][i])["frames"][j])["frame_id"]<28:
			fr_no = ((data["tracks"][i])["frames"][j])["frame_id"]
			coor = (((data["tracks"][i])["frames"][j])["polygon"])
			for k in range(len(coor)):
				x.append((coor[k]["image_x"]))
				y.append((coor[k]["image_y"]))
			print x , y
			
				
				
		
		
		
		
		
			
