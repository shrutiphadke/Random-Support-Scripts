

import numpy as np
import matplotlib.pyplot as plt

conf_arr = [[  15128 ,  9 ,  820 ,  0, 227],
 [  188 ,  31983  , 3233,   139,
    1159],
 [  5   ,292,   15974 ,  0,
    25],
 [  474  , 509 ,  146 ,  53196,
    4301],
 [  111  , 586,   506,   2668,
    30347]]
norm_conf = []
for i in conf_arr:
    a = 0
    tmp_arr = []
    a = sum(i, 0)
    for j in i:
        tmp_arr.append(float(j)/float(a))
    norm_conf.append(tmp_arr)

fig = plt.figure()
plt.clf()
ax = fig.add_subplot(111)
ax.set_aspect(1)
res = ax.imshow(np.array(norm_conf), cmap=plt.cm.ocean, 
                interpolation='nearest')

width  = 5
height = 5

for x in xrange(width):
    for y in xrange(height):
        ax.annotate(str(conf_arr[x][y]), xy=(y, x), 
                    horizontalalignment='center',
                    verticalalignment='center')

cb = fig.colorbar(res)
alphabet = 'Building', 'Trees' , 'Grass', 'Parking', 'Street'
plt.title("Confusion Matrix V1-Frames - SegNet")
plt.xticks(range(width), alphabet[:width])
plt.yticks(range(height), alphabet[:height])
plt.savefig('confusion_matrix1.png', format='png')
