import pandas as pd 
import numpy as np 
import pickle
import os

path = './Dataset/'
all_dataset = os.listdir(path)


def combineData(path):
    ll = []
    all_data = os.listdir(path)
    for user_data in all_data:
        file = os.listdir(path + user_data)
        arr = pickle.load(open(path + user_data + '/'+ file[0],'rb'))
        ll.append(arr)
    return ll


for dataset in all_dataset:
    data_path = path + dataset + '/'
    ll = combineData(data_path)
    arr_data = np.concatenate(ll)
    f_name = dataset + '.pkl'
    pickle.dump(arr_data,open(f_name,'wb'))

