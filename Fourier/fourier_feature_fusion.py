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



def power_spectrum(chan):

        
    fs = 128
    bands = [4,8,13,16,30,45] 
    
    p,pr= bin_power(chan,bands,fs)
    
    return pr
