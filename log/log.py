#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
files = []
for file in os.listdir(path='C://Users//Erdeniz//Desktop//log'):
    if file.endswith('.log') and os.path.isfile(file):
        files.append(file)
out = open('total.log','w')
for file in files:
    filename = file[:-4]
    #print(filename)
    f = open(file,'r') #read
    for line in f:
        if line.find('RncFunction=1,IubLink=Iub_') > 0 and (line.find('DISABLED') > 0 or line.find('ENABLED') > 0):
            out.write(filename+' '+line)
    f.close()
out.close()


# In[ ]:




