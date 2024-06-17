import json
import numpy as np
from src.utils import entropy, overlap

def calculate_query_type_entropy(data):
    vals = np.fromiter(data.values(), dtype=float)
    return entropy(vals)
    
def calculate_query_type_overlap(data1, data2):
    vals_1 = np.fromiter(data1.values(), dtype=float)
    vals_2 = np.fromiter(data2.values(), dtype=float)
    return  overlap(vals_1, vals_2)
