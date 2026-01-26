def index_of_coincidence(text):
    N = len(text)
    freqs = {c: text.count(c) for c in set(text)}
    return sum(f*(f-1) for f in freqs.values()) / (N*(N-1))

def friedman_key_length(ciphertext):
    ic = index_of_coincidence(ciphertext)
    return round((0.027 * len(ciphertext)) /
                 ((len(ciphertext)-1)*ic - 0.038*len(ciphertext) + 0.065))
