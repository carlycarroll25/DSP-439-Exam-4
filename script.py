import sys

def find_kmers(sequence, k):
    """
    Extracts all k-mers from the given sequence and maps each k-mer to its possible subsequent k-mers.
    """
    kmers = {}
    for i in range(len(sequence) - k):
        kmer = sequence[i:i+k]
        next_kmer = sequence[i+1:i+1+k]
        if kmer not in kmers:
            kmers[kmer] = set()
        kmers[kmer].add(next_kmer)
    return kmers

def process_sequences(sequences, k):
    """
    Aggregates k-mers and their subsequent k-mers from multiple sequences.
    """
    all_kmers = {}
    for sequence in sequences:
        kmers = find_kmers(sequence, k)
        for kmer, next_kmers in kmers.items():
            if kmer not in all_kmers:
                all_kmers[kmer] = set()
            all_kmers[kmer].update(next_kmers)
    return all_kmers

def find_smallest_unique_k(sequences, max_k=10):
    """
    Determines the smallest k such that each k-mer uniquely identifies its subsequent k-mer across all sequences.
    """
    for k in range(1, max_k+1):
        kmers = process_sequences(sequences, k)
        if all(len(next_kmers) == 1 for next_kmers in kmers.values()):
            return k
    return -1

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <sequence1> <sequence2> ...")
        sys.exit(1)
    sequences = sys.argv[1:]
    smallest_k = find_smallest_unique_k(sequences)
    print(f"The smallest k where each k-mer uniquely determines the next k-mer is: {smallest_k}")

if __name__ == "__main__":
    main()
