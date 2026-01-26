import string
from .frequency import score_plaintext

def decrypt(ciphertext, key):
    pt = ""
    for i, c in enumerate(ciphertext):
        shift = ord(key[i % len(key)]) - 65
        pt += chr((ord(c)-65-shift)%26 + 65)
    return pt

def generate_candidate_keys(ciphertext, key_len, threshold=150):
    alphabet = string.ascii_uppercase
    candidates = []

    def dfs(prefix):
        if len(prefix) == key_len:
            pt = decrypt(ciphertext, prefix)
            if score_plaintext(pt) < threshold:
                candidates.append(prefix)
            return
        for c in alphabet:
            dfs(prefix + c)

    dfs("")
    return candidates
