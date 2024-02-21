""" @author Harikrishna Sappidi (harikrishna.sappidi@gmail.com) """

import glob
import os
Current_Directory = os.getcwd()
DataList = []
for n in glob.glob(Current_Directory+'\\Files\*'):
    f = open(n,'r')
    eachfile = []
    for i in f:
        eachfile.append(int(i.rstrip())) 
    DataList.append(eachfile)
    f.close()
DataList = sorted(DataList, key=len)