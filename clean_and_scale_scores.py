import numpy as np

def clean_and_scale_scores(scores, min_score, max_score):
    cleaned_scores = np.clip(scores, min_score, max_score)
    
    scaled_scores = (cleaned_scores - min_score) / (max_score - min_score)
    
    return scaled_scores
