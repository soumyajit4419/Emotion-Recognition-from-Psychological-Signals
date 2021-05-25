import numpy as np
import pandas as pd
import pickle
import os

path = '../../Dataset/EntropyCompleteDataset/'


def getFourierStdData(type='eeg'):
    """
    Input: type(string) the type of data
           options: eeg / ecg / gsr / all

    Output: data(If Exits)
            2D array of data
    """
    data = pickle.load(open(path + 'FourierData.pkl', 'rb'))
    if(type == 'eeg'):
        return data[:, :70].astype(np.float32)
    elif(type == 'ecg'):
        return data[:, 70:80].astype(np.float32)
    elif(type == 'gsr'):
        return data[:, 80:85].astype(np.float32)
    elif(type == 'all'):
        return data[:, :].astype(np.float32)
    else:
        return "Invalid Choice"


def getWaveletStdData(type='eeg'):
    """
    Input: type(string) the type of data
           options: eeg / ecg / gsr / all

    Output: data(If Exits)
            2D array of data
    """
    data = pickle.load(open(path + 'WaveletData.pkl', 'rb'))
    if(type == 'eeg'):
        return data[:, :70].astype(np.float32)
    elif(type == 'ecg'):
        return data[:, 70:80].astype(np.float32)
    elif(type == 'gsr'):
        return data[:, 80:85].astype(np.float32)
    elif(type == 'all'):
        return data.astype(np.float)
    else:
        return "Invalid Choice"


def getLabelData(type='all'):
    """
    Input: type(string) the name of label
           options: arousal / valence / all

    Output: data(If Exits)
            2D array of data
    """
    data = pickle.load(open('../Dataset/UserLabels.pkl', 'rb'))
    if(type == 'arousal'):
        return data[:, :1]
    elif(type == 'valence'):
        return data[:, 1:2]
    elif(type == 'dominance'):
        return data[:, 2:3]
    elif(type == 'liking'):
        return data[:, 3:4]
    elif(type == 'ValAr'):
        return data[:, 0:2]
    elif(type == 'allfour'):
        return data[:, 0:4]
    elif(type == 'all'):
        return data
    else:
        return "Invalid Choice"


def getWaveletEntropyData():
    """
    Input: "

    Output: Wavelet Combined Entropy Data
    """
    data = pickle.load(open(path + 'WaveletData.pkl', 'rb'))
    return data.astype(np.float32)


def getFourierEntropyData():
    """
    Input: "

    Output: Fourier Combined Entropy Data
    """
    data = pickle.load(open(path + 'FourierData.pkl', 'rb'))
    return data.astype(np.float32)
