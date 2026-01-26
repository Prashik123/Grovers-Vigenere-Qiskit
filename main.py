from classical.kasiski import kasiski_examination
from classical.friedman import friedman_key_length
from classical.keyspace import generate_candidate_keys
from quantum.oracle import build_verification_oracle
from quantum.grover_search import grover_search
from benchmarks.classical_benchmark import classical_checks
from benchmarks.quantum_benchmark import grover_oracle_calls

# Load ciphertext
with open("data/ciphertext_100_words.txt") as f:
    words = [w.strip() for w in f]
ciphertext = "".join(words)

# Classical analysis
key_lengths = set(kasiski_examination(ciphertext))
key_lengths.add(friedman_key_length(ciphertext))
key_len = min(key_lengths)

candidate_keys = generate_candidate_keys(ciphertext, key_len)

print(f"Candidate keys found: {len(candidate_keys)}")

# Build validity map
validity_map = {i: True for i in range(len(candidate_keys))}

oracle = build_verification_oracle(validity_map)

iterations = 2
counts = grover_search(oracle, oracle.num_qubits, iterations)

print("Grover results:", counts)

# Benchmark
print("\n Quantum Advantage: ")
print("Classical checks:", classical_checks(len(candidate_keys)))
print("Grover oracle calls:", grover_oracle_calls(len(candidate_keys)))
