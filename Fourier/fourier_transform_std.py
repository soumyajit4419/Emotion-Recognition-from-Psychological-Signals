import numpy as np
import pandas as pd

def fourier_transform(df):
    
# Parameters :- Dataframe consisting of the rows as time and columns as channels and the values of amplitudes are there in each cell..

# Input-- Dataframe 
# Input Shape= Time duration X 17(no. of channels)

# Output- A list consisting the amplitudes of each frequency band(i.e 5 frequency bands) of each channel
# Output Shape:- 1 X 17*5

    #Length data channel
    L=df.shape[0];
    
      #Sampling frequency
    Fs = 128
    
    final=[]
    
    for i in df.columns:
    
        fft_new=np.fft.fft(df[i]) ## Applying FFT for each column
    
        frequency=abs(fft_new/L)
    
        frequency=frequency[: int(L/2+1)]*2
    
        delta= frequency[int(L*1/Fs-1):int(L*4/Fs)] ## Frequency sorting as per the required range of frequency band.
        delta_std = np.std(list(delta), axis=0) ## Applyitng the standard deviation
        final.append(delta_std)
    
        theta=frequency[int(L*5/Fs-1):int(L*8/Fs)]
        theta_std = np.std(list(theta), axis=0)
        final.append(theta_std)
    
        alpha = frequency[int(L*9/Fs-1): int(L*13/Fs)]
        alpha_std = np.std(list(alpha), axis=0)
        final.append(alpha_std)
    
        beta = frequency[int(L*13/Fs-1): int(L*30/Fs)]
        beta_std=np.std(list(beta), axis=0)
        final.append(beta_std)
    
        gamma = frequency[int(L*30/Fs-1): int(L*50/Fs)]
        gamma_std=np.std(list(gamma),axis=0)
        final.append(gamma_std)
    
    return final