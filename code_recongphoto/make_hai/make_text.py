import os
import re 

f = open('trainval.txt', 'w')
xmllist = os.listdir('./Anotations/')
for i in xmllist:
    f.write(re.sub('.xml','',str(i)) + '\n')