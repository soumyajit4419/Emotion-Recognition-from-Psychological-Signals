import numpy as np
import pywt

def wavelet_energy(col):
    """
    Parameter:
         col: Channel for which wavelet entropy is calculated
    Output:
        twe: total wavelet entropy of channel
    """
    # Apply wavelet transformation on a channel
    cA5, cD5, cD4, cD3, cD2, cD1 = pywt.wavedec(col, wavelet="db4", level=5)
    all_bands = [cD5, cD4, cD3, cD2, cD1]
    
    # Calculate energy of all bands
    eng_ll = []
    for bands in all_bands:
        s = 0
        for val in bands:
            s += val * val
        eng_ll.append(s)

    # Sum of energy of all bands
    s_eng_ll = sum(eng_ll)

    # Compute relative energy for each band
    pj = []
    
    for engs in eng_ll:
        pj.append(engs/s_eng_ll)
        

    return pj 
