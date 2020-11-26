import pandas as pd
import numpy as np
import pickle
import os


def combine_fourier(data='std'):
    """
    Parameter: Data(type = 'str')
               The data to concatinate and form array
    Return:   Array
              Concatenated Data
    """
    if(data == 'std'):
        all_user_data = os.listdir('./FourierData/UserStdData/')
        ll = []
        for i in all_user_data:
            data = pickle.load(
                open('./FourierData/UserStdData/'+i+'/user_features.pkl', 'rb'))
            ll.append(data)
        return np.concatenate(ll)
    elif(data == 'entropy'):
        all_user_data = os.listdir('./FourierData/UserEntropyData/')
        ll = []
        for i in all_user_data:
            data = pickle.load(
                open('./FourierData/UserEntropyData/'+i+'/user_features.pkl', 'rb'))
            ll.append(data)
        return np.concatenate(ll)


def combine_wavelet(data='std'):
    """
    Parameter: Data(type = 'str')
               The data to concatinate and form array
    Return:   Array
              Concatenated Data
    """
    if(data == 'std'):
        all_user_data = os.listdir('./WaveletData/UserStdData/')
        ll = []
        for i in all_user_data:
            data = pickle.load(
                open('./WaveletData/UserStdData/'+i+'/user_features.pkl', 'rb'))
            ll.append(data)
        return np.concatenate(ll)
    elif(data == 'entropy'):
        all_user_data = os.listdir('./WaveletData/UserEntropyData/')
        ll = []
        for i in all_user_data:
            data = pickle.load(
                open('./WaveletData/UserEntropyData/'+i+'/user_features.pkl', 'rb'))
            ll.append(data)
        return np.concatenate(ll)


def combine_labels():
    all_labels = os.listdir('./UserLabels')
    ll = []
    for i in all_labels:
        data = pickle.load(
            open('./UserLabels/'+i+'/user_labels.pkl', 'rb'))
        ll.append(data)
    return np.concatenate(ll)


pickle.dump(combine_wavelet(data='entropy'), open('./WaveletData.pkl', 'wb'))
pickle.dump(combine_fourier(data='entropy'), open('./FourierData.pkl', 'wb'))
pickle.dump(combine_labels(), open('./UserLabels.pkl', 'wb'))
