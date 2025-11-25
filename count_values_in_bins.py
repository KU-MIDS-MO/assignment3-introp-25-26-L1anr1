import numpy as np

def count_values_in_bins(data, bin_edges):
    
    counts, _ = np.histogram(data, bins=bin_edges)
    
    return counts
