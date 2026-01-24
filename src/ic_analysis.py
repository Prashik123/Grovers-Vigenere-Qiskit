from collections import Counter


def index_of_coincidence(text):
N = len(text)
freqs = Counter(text)
return sum(f*(f-1) for f in freqs.values()) / (N*(N-1))


def estimate_key_length(ciphertext, max_len=8):
scores = {}
for m in range(1, max_len+1):
streams = [''.join(ciphertext[i::m]) for i in range(m)]
scores[m] = sum(index_of_coincidence(s) for s in streams) / m
return max(scores, key=scores.get)
