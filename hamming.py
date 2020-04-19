def hamming_distance(strand_one, strand_two):
    # Calculate the Hamming Distance between two DNA strands.

    if type(strand_one) is not str or type(strand_two) is not str:
        # raise Exception("Wrong type.")
        return "Wrong type :/"

    # All capitals
    strand_one = strand_one.upper()
    strand_two = strand_two.upper()

    if len(strand_one) != len(strand_two):
        # raise Exception("Length mismatch")
        return "Length mismatch"

    valid_chars = ["C", "A", "G", "T"]

    count = 0
    for i in range(len(strand_one)):
        if strand_one[i] not in valid_chars or strand_two[i] not in valid_chars:
            # raise Exception("Invalid DNA strand")
            return "Invalid DNA strand"
        if strand_one[i] != strand_two[i]:
            count += 1
    return count


# Good input
print(hamming_distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT"))  # 7
print(hamming_distance("GATTACA", "GATTACA"))  # 0
print(hamming_distance("GGG", "CCT"))  # 3

# Bad input
print(hamming_distance(32, 33))  # Wrong type
print(hamming_distance("GGGG", "GGTCC"))  # Length mismatch
print(hamming_distance("not", "dna"))  # Invalid characters

# Edge cases
print(hamming_distance("", ""))  # 0
print(hamming_distance("gattaca", "GATTACA"))  # 0
