import os 
from beir.datasets.data_loader import GenericDataLoader
import json
from scipy import stats 
import numpy as np
from scipy.special import kl_div


def entropy(inp):
    return stats.entropy(inp, base = 2)

def overlap(A,B):
    return np.sum(kl_div(A + 0.001, B + 0.001))

def load_queries(path_to_queries):
    loader = GenericDataLoader(query_file = path_to_queries)
    loader._load_queries()
    return loader.queries

def load_corpus(path_to_corpus):
    loader = GenericDataLoader(corpus_file = path_to_corpus)
    loader._load_corpus
    return loader.corpus

def save_json(title, data):
    with open(title, "w") as file:
        json.dump(data, file)
             
def normalize(counter):
    total_count = sum(counter.values())
    return {key: value / total_count for key, value in counter.items()}    
