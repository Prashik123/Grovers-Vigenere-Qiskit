from collections import defaultdict
from math import gcd
from functools import reduce

def kasiski_examination(ciphertext, min_len=3, max_len=5):
    repeats = defaultdict(list)

    for size in range(min_len, max_len + 1):
        for i in range(len(ciphertext) - size):
            seq = ciphertext[i:i+size]
            repeats[seq].append(i)

    distances = []
    for positions in repeats.values():
        if len(positions) > 1:
            for i in range(len(positions)-1):
                distances.append(positions[i+1] - positions[i])

    if not distances:
        return []

    return list(set(reduce(gcd, distances)))
