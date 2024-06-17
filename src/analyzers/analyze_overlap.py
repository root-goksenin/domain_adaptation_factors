from utils import normalized_jaccard_similarity_without_memo

def calculate_overlap(vocab_1, vocab_2):
    return normalized_jaccard_similarity_without_memo(vocab_1, vocab_2)
                