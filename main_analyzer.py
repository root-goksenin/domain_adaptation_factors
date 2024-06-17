from src.utils import load_queries, load_corpus
from src.analyzers.type_utils import check_query_type_distribution
from src.analyzers.overlap_utils import get_query_freq, get_corpus_freq
from src.analyzers.analyze_overlap import calculate_overlap
from src.analyzers.analyze_types import calculate_query_type_entropy, calculate_query_type_overlap
import click 


@click.command()
@click.option("--source_query_path", required=True, help="Path to the source query file")
@click.option("--source_corpus_path", required=True, help="Path to the source corpus file")
@click.option("--test_query_path", required=True, help="Path to the test query file")
@click.option("--test_corpus_path", required=True, help="Path to the test corpus file")
@click.option("--generated_query_path", required=True, help="Path to the generated query file")
def main(source_query_path, source_corpus_path, test_query_path, test_corpus_path, generated_query_path):
    gen_q = load_queries(generated_query_path)
    test_q = load_queries(test_query_path)
    source_q = load_queries(source_query_path)
    source_c = load_corpus(source_corpus_path)
    test_c = load_corpus(test_corpus_path)

    # Check types 
    generated_query_types = check_query_type_distribution(gen_q)
    test_query_types = check_query_type_distribution(test_q)
    source_query_types = check_query_type_distribution(source_q)

    # Get vocabularies of corpuses and queries
    freq_gen_q = get_query_freq(gen_q.values())
    test_freq_q = get_query_freq(test_q.values())
    source_freq_q = get_query_freq(source_q.values())
    test_freq_d = get_corpus_freq(test_c.values())
    source_freq_d = get_corpus_freq(source_c.values())
    
    # Calculate overlap between vocabularies
    test_generated_query_overlap = calculate_overlap(freq_gen_q, test_freq_q)
    test_generated_corpus_overlap = calculate_overlap(freq_gen_q, test_freq_d)
    source_generated_query_overlap = calculate_overlap(freq_gen_q, source_freq_q)
    source_generated_corpus_overlap = calculate_overlap(freq_gen_q, source_freq_d)
    
    # Calculate overlap between query types
    generated_query_type_entropy = calculate_query_type_entropy(generated_query_types)
    test_query_type_entropy = calculate_query_type_entropy(test_query_types)
    source_query_type_entropy = calculate_query_type_entropy(source_query_types)

    # Calculate query type entropies
    generated_query_type_to_test_query = calculate_query_type_overlap(generated_query_types,
                                                                      test_query_types)
    generated_query_type_to_source_query = calculate_query_type_overlap(generated_query_types,
                                                                      source_query_types) 
        

if __name__ == "__main__":
    
    main()
