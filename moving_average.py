import numpy as np

def moving_average(signal, window_size):
    n = len(signal)
    k = (window_size - 1) // 2
    
    result = [np.mean(signal[max(0, i - k) : min(n, i + k + 1)]) for i in range(n)]
    
    return np.array(result, dtype=float)
