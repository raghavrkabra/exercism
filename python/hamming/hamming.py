def distance(strand_a, strand_b):
    """Return the hamming distance of given strands of DNA"""

    if len(strand_a) != len(strand_b):
        raise ValueError("Strand length doesn't match")

    return sum(1 for a,b in zip(strand_a, strand_b) if a != b)
