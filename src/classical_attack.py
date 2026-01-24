from .vigenere import decrypt
from .english_score import chi_square


ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def recover_key(ciphertext, key_len):
key = ''
for i in range(key_len):
stream = ciphertext[i::key_len]
best_char, best_score = None, 1e18
for c in ALPHABET:
pt = decrypt(stream, c)
score = chi_square(pt)
if score < best_score:
best_char, best_score = c, score
key += best_char
return key
