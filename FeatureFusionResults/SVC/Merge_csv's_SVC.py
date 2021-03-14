import os
import pandas as pd

dir='./'

files=os.listdir(dir)s

for i in range(1,len(files)-5,1):
    
    csv1=pd.read_csv(files[i])
    csv2=pd.read_csv(files[i+5])
    merged=pd.concat([csv1,csv2],axis=0,ignore_index=False)
    merged=merged.sort_values(by=['user_no'],ascending=True)
#     print(merged)
    merged.to_csv('./'+ 'merged' + str(files[i])[4:], index=False)
    

