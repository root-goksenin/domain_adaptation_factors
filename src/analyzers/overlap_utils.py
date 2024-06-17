import nltk 
nltk.download('stopwords')
from nltk.corpus import stopwords
from collections import Counter
from src.utils import normalize
from typing import List

stop_words = stopwords.words('english')

def get_query_freq(iter_1: List[str]):
    words = Counter()
    for text in iter_1:
        tokenized = text.split()
        tokenized = [w.lower() for w in tokenized]
        tokenized = [w for w in tokenized if w not in stop_words]
        words.update(tokenized)
    
    common = dict(words.most_common(10000))
    return normalize(common)

def get_corpus_freq(iter_1: List[str]):
    words = Counter()
    for text in iter_1:
        text = text['title'] + " " + text['text']
        tokenized = text.split()
        tokenized = [w.lower() for w in tokenized]
        tokenized = [w for w in tokenized if w not in stop_words]
        words.update(tokenized)
    
    common = dict(words.most_common(10000))
    return normalize(common)


def normalized_jaccard_similarity(vocab_1, vocab_2):
    words = set(vocab_1.keys()).union(set(vocab_2.keys()))
    up = 0
    down = 0
    for k in words:
        word_freq_1, word_freq_2 = vocab_1.get(k, 0), vocab_2.get(k,0)
        up += min(word_freq_1, word_freq_2)
        down += max(word_freq_1, word_freq_2)
    return up/down