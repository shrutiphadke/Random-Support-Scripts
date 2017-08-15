# Reading QA JASON FIle

import os
import json
from textblob import TextBlob

with open('/home/shruti/Genome/Annot/question_answers.json') as d1:
	data = json.load(d1)


f = open("qa_filt1.txt", 'w')

#print len(data)
#print data[0].keys()
#print (data[0]['id'])
#print type(data[0]['qas'][0])
#print len(data[0]['qas'])
#print data[0]['qas'][0]['question']

ld = len(data)

for i in range(ld):
	for j in range(len(data[i]['qas'])):
		word = data[i]['qas'][j]['question']

		if (word.startswith('Where') or word.startswith('Who')):  
		        wb = TextBlob(word)
			for k in range(len(wb.tags)):
				if wb.tags[k][1] == 'NN' or wb.tags[k][1] == 'JJ':
					f.write(wb.tags[k][0])
				        f.write(" ")
					f.write(data[i]['qas'][j]['answer'])
				        f.write(" ")
					f.write(str(data[i]['id']))
					f.write('\n')

					break

f.close()
