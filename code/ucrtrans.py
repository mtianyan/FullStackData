# -*- coding: utf-8 -*-
import pandas as pd
import os.path
filepathlist=[]
filenamelist=[]
def processDirectory ( args, dirname, filenames ):
    for filename in filenames:
          file_path=os.path.join(dirname,filename)
          if os.path.isfile(file_path):
            filepathlist.append(file_path)
            filenamelist.append(filename)
os.path.walk(r'C:\Users\mtianyan\Desktop\tudoupuretested', processDirectory, None )
for i in range(len(filepathlist)):
 ucrfile =filepathlist[i]
 csvfile =filenamelist[i]+'_ucrtrans.csv'
 data =pd.read_csv(ucrfile,header =None,index_col=0)
 newdata =map(lambda x:'time'+bytes(x),data.columns)
 data.columns=newdata
 data.to_csv(csvfile,index_label='classlabel')
 




