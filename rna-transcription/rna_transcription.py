mapping = {"G": "C", "C": "G", "T": "A", "A": "U"}

def to_rna(dna_strand):
    return "".join(map(lambda l: mapping[l], list(dna_strand)))
