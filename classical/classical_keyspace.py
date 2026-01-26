from classical.kasiski import kasiski_examination
from classical.friedman import friedman_key_length
from classical.frequency import extract_probable_keys

def reduce_keyspace(ciphertext):
    kasiski_lengths = kasiski_examination(ciphertext)
    friedman_len = friedman_key_length(ciphertext)

    candidate_lengths = set(kasiski_lengths + [friedman_len])
    candidate_keys = []

    for k in candidate_lengths:
        candidate_keys.extend(extract_probable_keys(ciphertext, k, top_n=3))

    return list(set(candidate_keys)), friedman_len
