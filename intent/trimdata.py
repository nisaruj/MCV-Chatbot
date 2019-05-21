import os
import numpy as np

for i in range(1,6):
    fr = open('raw_data/text' + str(i) + '.txt','r')
    fw = open('trimmed_data/text' + str(i) + '.txt', 'w')
    print('opening: raw_data/text' + str(i) + '.txt')
    a = []
    for line in fr:
        a.append(line)
    np.random.shuffle(a)
    for item in a[:61]:
        fw.write(item)
    print('done')
    fr.close()
    fw.close()