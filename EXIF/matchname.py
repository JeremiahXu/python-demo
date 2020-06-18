#!/usr/bin/python
# -*- coding: utf-8 -*-
    
import os
import exifread
import shutil

total = 0

pathlog = r"C:\Users\xun73\Desktop\云南毕业旅游\r888" 

despath = r"C:\Users\xun73\Desktop\云南毕业旅游\r888" 

def getExif(filename):
    global total
    FIELD = 'EXIF DateTimeOriginal'    
    fd = open(filename, 'rb')    
    tags = exifread.process_file(fd)    
    fd.close()    
    if FIELD in tags:
        print (str(tags[FIELD]) + "Found it! " + filename)
        total = total + 1 
        # shutil.move(filename, despath)
        # "2015-03-26 120001"
        new_name = str(tags[FIELD]).replace(':', '-') + os.path.splitext(filename)[1] 
        new_name2 = new_name.split(" ")[0] + " " + new_name.split(" ")[1].replace('-', '')
        print(new_name2)       
        # tot = 1        
        # while os.path.exists(new_name):            
        #     new_name = str(tags[FIELD]).replace(':', '').replace(' ', '_') + '_' + str(tot) + os.path.splitext(filename)[1]            
        #     tot += 1  

        # new_name2 = new_name.split(".")[0] + '__' +filename        
        # print(new_name2)            
        os.rename(filename, new_name2)    
    # else:        
    #     print('No {} found'.format(FIELD))
    return





files = os.listdir(pathlog)

for f in files:
    path = pathlog + "\\" + str(f)
    if os.path.isfile(path):
        getExif(path)

    
    # if '拍摄时间' in f :
    #     print ("Found it! " + f)
    #     n = n + 1
    #     os.remove(pathlog + "\\" + str(f))
print ("Found it! total: " + str(total) )

