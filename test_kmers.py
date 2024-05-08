from script import find_kmers, process_sequences, find_smallest_unique_k

def test_find_kmers():
    assert find_kmers("ATGC", 2) == {'AT': {'TG'}, 'TG': {'GC'}}

def test_process_sequences():
    sequences = ["ATGC", "GCAT"]
    assert process_sequences(sequences, 2) == {'AT': {'TG'}, 'TG': {'GC'}, 'GC': {'CA'}, 'CA': {'AT'}}

def test_find_smallest_unique_k():
    sequences = ["ATGCGATG", "CATGCGAT"]
    assert find_smallest_unique_k(sequences, 3) == 3
