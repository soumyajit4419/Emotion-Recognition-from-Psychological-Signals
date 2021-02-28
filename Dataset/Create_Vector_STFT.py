import pandas as pd
import numpy as np
import pickle
import os


path = './STFTData/'

all_data= os.listdir(path)

final_data_sfft=[]
final_labels_sfft=[]

for data in all_data:
    with open( path + data , 'rb') as file:
        sub = np.load(file , allow_pickle=True)
        
        for i in range (0,sub.shape[0]):
            final_data_sfft.append(sub[i][0])
            final_labels_sfft.append(sub[i][1])


np.array(final_data_sfft).shape

np.array(final_labels_sfft).shape

np.save(path + 'SFFTFinalData', np.array(final_data_sfft), allow_pickle=True, fix_imports=True)

np.save(path + 'SFFTFinalLabels', np.array(final_labels_sfft), allow_pickle=True, fix_imports=True)