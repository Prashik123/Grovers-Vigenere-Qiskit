import string
ALPHABET = string.ascii_uppercase


def char_to_int(c): return ALPHABET.index(c)


def int_to_char(i): return ALPHABET[i % 26]


def decrypt(ciphertext, key):
pt = ''
for i, c in enumerate(ciphertext):
pi = (char_to_int(c) - char_to_int(key[i % len(key)]) + 26) % 26
pt += int_to_char(pi)
return pt
