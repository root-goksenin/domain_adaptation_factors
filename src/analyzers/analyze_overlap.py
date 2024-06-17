from .overlap_utils import normalized_jaccard_similarity

def calculate_overlap(vocab_1, vocab_2):
    return normalized_jaccard_similarity(vocab_1, vocab_2)
                