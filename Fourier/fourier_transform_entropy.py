import numpy as np
import pandas as pd

    
def bin_power(chan, bands, Fs):
    
    """To compute the  power in each frequency bin specified by Band from FFT result of
    X. By default, X is a real signal.

    bands:
        a list
        boundary frequencies (in Hz) of bins. They can be unequal bins, e.g.
        [0.5,4,7,12,30] which are delta, theta, alpha and beta respectively.

    chan:
         a list
         Channel on which Spectral Entropy is calculated
    
    Fs
        an integer
        the sampling rate in physical frequency
        
    Returns
    -------
    Power -
        a list-
        spectral power in each frequency bin.
        
    Power_ratio - 
        a list-
        spectral power in each frequency bin normalized by total power in ALL
        frequency bins.
    """

    C = np.fft.fft(chan)
    C = abs(C) ** 2
    Power = np.zeros(len(bands) - 1)
    
    for Freq_Index in range(0, len(bands) - 1):
        
        Freq = float(bands[Freq_Index])
        Next_Freq = float(bands[Freq_Index + 1])
        Power[Freq_Index] = sum(C[int(np.floor(Freq / Fs * len(chan))): int(np.floor(Next_Freq / Fs * len(chan)))])
        
    Power_Ratio = Power / sum(Power)
    return Power, Power_Ratio


def spectral_entropy(chan, bands, Fs, Power_Ratio=None):
    
    """For computing the spectral entropy of a time series from either two cases below:
    
    1. X, the time series (default)
    2. Power_Ratio, a list of normalized signal power in a set of frequency
    bins defined in bands (if Power_Ratio is provided, recommended to speed up)

    bands:
        a list
        boundary frequencies (in Hz) of bins. They can be unequal bins, e.g.
        [0.5,4,7,12,30] which are delta, theta, alpha and beta respectively.

    chan:
         a list
         Channel on which Spectral Entropy is calculated
    
    Fs
        an integer
        the sampling rate in physical frequency
        
  Returns
    -------
   The Spectral Entropy"""

    if Power_Ratio is None:
        Power, Power_Ratio = bin_power(chan, bands, Fs)

    se = 0
    
    for i in range(0, len(Power_Ratio) - 1):
        se += Power_Ratio[i] * np.log(Power_Ratio[i])
    se/= np.log(len(Power_Ratio))
    
    return -1 * se


def entropy(chan):
    
    """
    Parameter:
         chan: Channel on which Spectral Entropy is calculated
    Output:
        tfe: Total Spectral entropy of the input channel
    """
        
    fs = 128
    bands = [1,4,8,13,30]
    
    p,pr= bin_power(chan,bands,fs)
    
    tfe = spectral_entropy(chan,bands,fs,Power_Ratio=pr)
    
#     tfe = [0 if math.isnan(x) else x for x in tfe]
    
    return tfe
