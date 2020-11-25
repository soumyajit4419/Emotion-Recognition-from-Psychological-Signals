import pandas as pd
import numpy as np
import pywt


def applyWavelet(col):
    """
    Parameter:
         col: Channel for which wavelet is applied
    Output:
        f_bands: list of frequency band from a channel
    """
    f_bands = []
    cA5, cD5, cD4, cD3, cD2, cD1 = pywt.wavedec(
        df[i], wavelet="db4", level=5)
    gamma = np.std(cD1, axis=0)
    beta = np.std(cD2, axis=0)
    alpha = np.std(cD3, axis=0)
    theta = np.std(cD4, axis=0)
    delta = np.std(cD5, axis=0)
    f_bands.append(gamma)
    f_bands.append(beta)
    f_bands.append(alpha)
    f_bands.append(theta)
    f_bands.append(delta)
    return f_bands
